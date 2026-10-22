
import os
from datetime import datetime

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraudshield_improved_model.joblib")

st.set_page_config(
    page_title="FraudShield Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FraudShield")
st.subheader("AI-Based Transaction Risk Dashboard")
st.info("Educational demo using synthetic practice data.")

# Transaction input section
st.header("🔍 Check a Transaction")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=0.0,
        value=2000.0,
        step=500.0
    )

with col2:
    international = st.selectbox(
        "International Transaction?",
        ["No", "Yes"]
    )

if st.button("Check Transaction", type="primary"):
    international_number = 1 if international == "Yes" else 0

    transaction = pd.DataFrame({
        "amount": [amount],
        "international_number": [international_number]
    })

    prediction = int(model.predict(transaction)[0])
    status = "SUSPICIOUS" if prediction == 1 else "LOW RISK"

    if prediction == 1:
        st.error("⚠️ Prediction: SUSPICIOUS")
    else:
        st.success("✅ Prediction: LOW RISK")

    new_record = pd.DataFrame([{
        "Date and Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Amount (₹)": amount,
        "International": international,
        "Prediction": status
    }])

    file_name = "transaction_history.csv"
    file_exists = os.path.exists(file_name)

    new_record.to_csv(
        file_name,
        mode="a",
        header=not file_exists,
        index=False,
        encoding="utf-8-sig"
    )

    st.success("Transaction saved successfully!")

# Dashboard section
st.divider()
st.header("📊 Transaction Analytics")

file_name = "transaction_history.csv"

if os.path.exists(file_name):
    history_df = pd.read_csv(file_name, encoding="utf-8-sig")

    if not history_df.empty:
        # Summary metrics
        total = len(history_df)
        suspicious = int(
            (history_df["Prediction"] == "SUSPICIOUS").sum()
        )
        low_risk = int(
            (history_df["Prediction"] == "LOW RISK").sum()
        )

        metric1, metric2, metric3 = st.columns(3)

        metric1.metric("Total Transactions", total)
        metric2.metric("Suspicious Predictions", suspicious)
        metric3.metric("Low-Risk Predictions", low_risk)

        # Filter transaction history
        st.subheader("🔎 Filter Transactions")

        selected_status = st.selectbox(
            "Choose prediction status",
            ["All", "SUSPICIOUS", "LOW RISK"]
        )

        if selected_status == "All":
            filtered_df = history_df
        else:
            filtered_df = history_df[
                history_df["Prediction"] == selected_status
            ]

        st.dataframe(filtered_df, use_container_width=True)

        # Chart data
        st.subheader("📈 Risk Distribution")

        chart_data = pd.DataFrame({
            "Prediction": ["LOW RISK", "SUSPICIOUS"],
            "Count": [low_risk, suspicious]
        })

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.write("**Bar Chart**")
            st.bar_chart(
                chart_data.set_index("Prediction")
            )

        with chart_col2:
            st.write("**Pie Chart**")
            pie_data = chart_data.set_index("Prediction")
            st.write("Share of predictions")
            st.vega_lite_chart(
                pie_data.reset_index(),
                {
                    "mark": {"type": "arc", "tooltip": True},
                    "encoding": {
                        "theta": {
                            "field": "Count",
                            "type": "quantitative"
                        },
                        "color": {
                            "field": "Prediction",
                            "type": "nominal"
                        }
                    },
                    "view": {"stroke": None}
                },
                use_container_width=True
            )

        # Download history
        st.subheader("📥 Export Records")

        st.download_button(
            "Download Transaction History CSV",
            data=history_df.to_csv(index=False).encode("utf-8-sig"),
            file_name="transaction_history.csv",
            mime="text/csv"
        )

    else:
        st.info("No transactions available yet.")
else:
    st.info("Check your first transaction to start the dashboard.")

st.caption(
    "Educational project only. Predictions use synthetic practice data "
    "and are not suitable for real financial decisions."
)
