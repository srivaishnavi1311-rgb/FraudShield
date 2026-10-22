
import pandas as pd

# Load the dataset
df = pd.read_csv("synthetic_transactions.csv")

print("===== FraudShield Data Inspection =====")

# 1. Dataset size
print("\nDataset shape:")
print(df.shape)

# 2. Column details
print("\nColumn names:")
print(df.columns.tolist())

# 3. Missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Duplicate records
print("\nDuplicate records:", df.duplicated().sum())

# 5. Number of transactions in each class
print("\nTransaction class counts:")
print(df["status"].value_counts().sort_index())

# 6. Fraud percentage
fraud_percentage = (df["status"] == 1).mean() * 100
print(f"\nSuspicious label percentage: {fraud_percentage:.2f}%")

# 7. Amount statistics by label
print("\nAmount statistics by status:")
print(df.groupby("status")["amount"].describe())


# 8. Display duplicate records
print("\nDuplicate records:")
duplicates = df[df.duplicated(keep=False)]
print(duplicates.sort_values(by=list(df.columns)).to_string(index=False))

print("\nInspection completed!")
