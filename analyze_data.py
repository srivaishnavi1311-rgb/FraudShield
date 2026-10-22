
import pandas as pd

# 1. Read the CSV file
df = pd.read_csv("transactions.csv")

# 2. Display the first five records
print("\n--- First 5 Transactions ---")
print(df.head())

# 3. Check the dataset size
print("\n--- Dataset Shape ---")
print(df.shape)

# 4. Check column names and data types
print("\n--- Dataset Information ---")
df.info()

# 5. Calculate basic statistics
print("\n--- Amount Statistics ---")
print(df["amount"].describe())

# 6. Count each risk status
print("\n--- Risk Status Counts ---")
print(df["status"].value_counts())

# 7. Display suspicious transactions
print("\n--- Suspicious Transactions ---")
suspicious = df[df["status"] == "SUSPICIOUS"]
print(suspicious)

# 8. Calculate the suspicious transaction count
print("\nTotal suspicious:", len(suspicious))
