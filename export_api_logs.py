
import pandas as pd

# Read the original prediction log
df = pd.read_csv("api_prediction_log.csv")

# Convert timestamps into datetime values
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Ask the user for a date
date_input = input("Enter date (YYYY-MM-DD): ").strip()

try:
    selected_date = pd.to_datetime(
        date_input, format="%Y-%m-%d", errors="raise"
    ).date()

    # Filter records for the selected date
    filtered_df = df[
        df["timestamp"].dt.date == selected_date
    ]

    if filtered_df.empty:
        print("No predictions found for this date.")
    else:
        # Save results into a separate CSV
        output_file = f"predictions_{selected_date}.csv"
        filtered_df.to_csv(output_file, index=False)

        print("\nExport successful!")
        print("Records exported:", len(filtered_df))
        print("Saved file:", output_file)

except ValueError:
    print("Invalid date. Please use YYYY-MM-DD.")
