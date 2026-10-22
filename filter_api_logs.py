
import pandas as pd

# Load the prediction log
df = pd.read_csv("api_prediction_log.csv")

# Convert timestamp text into date/time values
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Display available dates
print("\n--- Available Dates ---")
print(df["timestamp"].dt.date.unique())

# Ask the user which date to analyze
date_input = input(
    "\nEnter a date (YYYY-MM-DD): "
).strip()

try:
    selected_date = pd.to_datetime(
        date_input, format="%Y-%m-%d", errors="raise"
    ).date()

    # Filter transactions for the selected date
    filtered_df = df[
        df["timestamp"].dt.date == selected_date
    ]

    print(f"\n--- Predictions for {selected_date} ---")

    if filtered_df.empty:
        print("No predictions found for this date.")
    else:
        print(filtered_df.to_string(index=False))
        print("\nTotal predictions:", len(filtered_df))
        print("\nPrediction summary:")
        print(filtered_df["prediction"].value_counts())

except ValueError:
    print("Invalid date. Use YYYY-MM-DD format.")
