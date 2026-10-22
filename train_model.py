
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Load the cleaned dataset
df = pd.read_csv("clean_transactions.csv")

# 2. Prepare the input features
df["international_number"] = df["international"].map({
    "no": 0,
    "yes": 1
})

X = df[["amount", "international_number"]]

# 3. Prepare the target labels
y = df["status"].map({
    "LOW RISK": 0,
    "SUSPICIOUS": 1
})

# 4. Create the machine-learning model
model = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)

# 5. Train the model
model.fit(X, y)

print("FraudShield ML model trained successfully!")

# 6. Test with a sample transaction
new_transaction = pd.DataFrame({
    "amount": [8000],
    "international_number": [0]
})

prediction = model.predict(new_transaction)[0]

if prediction == 1:
    print("Predicted status: SUSPICIOUS")
else:
    print("Predicted status: LOW RISK")
