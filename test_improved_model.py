
import pandas as pd
import joblib

# Load the new practice model
model = joblib.load("fraudshield_improved_model.joblib")

test_cases = [
    {"amount": 49999, "international": "No"},
    {"amount": 50000, "international": "No"},
    {"amount": 50001, "international": "No"},
    {"amount": 2000, "international": "Yes"},
    {"amount": 80000, "international": "No"},
    {"amount": 1000, "international": "No"}
]

passed = 0

print("===== Improved Model Test =====")

for case in test_cases:
    amount = case["amount"]
    international = case["international"]

    international_number = 1 if international == "Yes" else 0

    features = pd.DataFrame({
        "amount": [amount],
        "international_number": [international_number]
    })

    prediction = int(model.predict(features)[0])

    predicted_status = (
        "SUSPICIOUS" if prediction == 1 else "LOW RISK"
    )

    if amount > 50000 or international == "Yes":
        expected_status = "SUSPICIOUS"
    else:
        expected_status = "LOW RISK"

    result = "PASS" if predicted_status == expected_status else "CHECK"

    if result == "PASS":
        passed += 1

    print(
        f"Rs.{amount} | International: {international} "
        f"| Predicted: {predicted_status} "
        f"| Expected: {expected_status} | {result}"
    )

print("\nTotal tests:", len(test_cases))
print("Passed:", passed)
print("Needs checking:", len(test_cases) - passed)
