
import pandas as pd
import matplotlib.pyplot as plt

# Load the API prediction log
df = pd.read_csv("api_prediction_log.csv")

if df.empty:
    print("No predictions available to visualize.")

else:
    # Count each prediction category
    counts = df["prediction"].value_counts()

    print("\nPrediction counts:")
    print(counts)

    # Create a bar chart
    counts.plot(kind="bar")

    plt.title("FraudShield Prediction Summary")
    plt.xlabel("Prediction")
    plt.ylabel("Number of Transactions")
    plt.xticks(rotation=0)
    plt.tight_layout()

    # Save the chart
    plt.savefig("prediction_summary.png", dpi=150)

    print("\nChart saved to prediction_summary.png")

    # Display the chart
    plt.show()
