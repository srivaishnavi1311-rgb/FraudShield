from sklearn.tree import export_text
import pandas as pd
import joblib

# Load the trained FraudShield model
model = joblib.load("fraudshield_model.joblib")

# Test transactions with challenging amounts
test_cases = [
    {"amount": 49999, "international": "No"},
    {"amount": 50000, "international": "No"},
    {"amount": 50001, "international": "No"},
    {"amount": 2000, "international": "Yes"},
    {"amount": 80000, "international": "No"},
    {"amount": 1000, "international": "No"}
]

print("===== FraudShield Lesson 18 =====")

passed = 0

for case in test_cases:
    amount = case["amount"]
    international = case["international"]

    # Convert input into model features
    international_number = 1 if international == "Yes" else 0

    features = pd.DataFrame({
        "amount": [amount],
        "international_number": [international_number]
    })

    # Ask the trained model for its prediction
    prediction = int(model.predict(features)[0])

    if prediction == 1:
        predicted_status = "SUSPICIOUS"
    else:
        predicted_status = "LOW RISK"

    # Expected result from our synthetic training rule
    if amount > 50000 or international == "Yes":
        expected_status = "SUSPICIOUS"
    else:
        expected_status = "LOW RISK"

    # Compare prediction with expected result
    if predicted_status == expected_status:
        result = "PASS"
        passed += 1
    else:
        result = "CHECK"

    print("\nAmount: Rs.", amount)
    print("International:", international)
    print("Predicted:", predicted_status)
    print("Expected:", expected_status)
    print("Result:", result)

print("\n===== Final Report =====")
print("Total test cases:", len(test_cases))
print("Passed:", passed)
print("Needs checking:", len(test_cases) - passed)
print("\n===== Model Inspection =====")

print("Model type:", type(model).__name__)
print("Maximum tree depth:", model.get_depth())
print("Number of leaves:", model.get_n_leaves())

print("\nFeature importances:")
for feature, importance in zip(
    ["amount", "international_number"],
    model.feature_importances_
):
    print(feature, ":", round(importance, 3))
    print("\n===== Learned Decision Rules =====")

    print(
        export_text(
            model,
            feature_names=["amount", "international_number"]
        )
    )