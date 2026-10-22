
import pandas as pd

# 1. Load the transaction dataset
df = pd.read_csv("transactions.csv")

print("Original dataset:")
print(df)

# 2. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 3. Find missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Remove exact duplicate rows
df = df.drop_duplicates()

# 5. Correct the amount column
df["amount"] = pd.to_numeric(
    df["amount"], errors="coerce"
)

# 6. Standardize text values
df["international"] = (
    df["international"].astype("string")
    .str.strip().str.lower()
)

df["status"] = (
    df["status"].astype("string")
    .str.strip().str.upper()
)

# 7. Handle missing amounts using the median
if df["amount"].notna().any():
    df["amount"] = df["amount"].fillna(
        df["amount"].median()
    )

# 8. Standardize international values
df["international"] = df["international"].map({
    "yes": "yes",
    "no": "no"
})

# Fill missing international values with the most common value
if df["international"].notna().any():
    df["international"] = df["international"].fillna(
        df["international"].mode().iloc[0]
    )

# Remove rows without a valid target label
df = df[
    df["status"].isin(["SUSPICIOUS", "LOW RISK"])
].copy()

# 9. Save the cleaned dataset
df.to_csv("clean_transactions.csv", index=False)

print("\nCleaned dataset:")
print(df)

print("\nFinal shape:", df.shape)
print("Saved as clean_transactions.csv")
# Convert international values into numbers
df["international_number"] = df["international"].map({
    "no": 0,
    "yes": 1
})

# Practice target: 1 = suspicious, 0 = low risk
df["target"] = df["status"].map({
    "LOW RISK": 0,
    "SUSPICIOUS": 1
})

# Select input features
X = df[["amount", "international_number"]]

# Select the target
y = df["target"]

print("\nInput features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

print("\nFeature shape:", X.shape)
print("Target shape:", y.shape)