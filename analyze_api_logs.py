
import pandas as pd

# Read the API prediction log
df = pd.read_csv("api_prediction_log.csv")

# Display all recorded predictions
print("\n--- Transaction Prediction Log ---")
print(df.to_string(index=False))

# Count the total successful predictions
total = len(df)
print("\nTotal predictions:", total)

# Count each prediction category
print("\n--- Prediction Summary ---")
print(df["prediction"].value_counts().to_string())

# Calculate the percentage marked suspicious
if total > 0:
    suspicious_count = (df["prediction"] == "SUSPICIOUS").sum()
    suspicious_percentage = (suspicious_count / total) * 100

    print("\nSuspicious predictions:", suspicious_count)
    print(f"Suspicious percentage: {suspicious_percentage:.2f}%")
else:
    print("No predictions found.")
