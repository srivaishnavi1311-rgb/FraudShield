
import pandas as pd

# Load the existing API prediction log
df = pd.read_csv("api_prediction_log.csv")

if df.empty:
    print("No transaction predictions available.")

else:
    total = len(df)

    suspicious = (
        df["prediction"] == "SUSPICIOUS"
    ).sum()

    low_risk = (
        df["prediction"] == "LOW RISK"
    ).sum()

    suspicious_percentage = suspicious / total * 100

    highest_amount = df["amount"].max()

    print("\n===== FRAUDSHIELD RISK SUMMARY =====")
    print("Total predictions:", total)
    print("Low-risk predictions:", low_risk)
    print("Suspicious predictions:", suspicious)
    print(f"Suspicious percentage: {suspicious_percentage:.2f}%")
    print(f"Highest transaction amount: Rs. {highest_amount:.2f}")

    # Save the summary into a separate text report
    with open("risk_summary.txt", "w", encoding="utf-8") as file:
        file.write("FRAUDSHIELD RISK SUMMARY\n")
        file.write(f"Total predictions: {total}\n")
        file.write(f"Low-risk predictions: {low_risk}\n")
        file.write(f"Suspicious predictions: {suspicious}\n")
        file.write(
            f"Suspicious percentage: {suspicious_percentage:.2f}%\n"
        )
        file.write(
            f"Highest transaction amount: Rs. {highest_amount:.2f}\n"
        )

    print("\nReport saved to risk_summary.txt")
