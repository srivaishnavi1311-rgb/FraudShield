
import pandas as pd

# Load the original dataset
df = pd.read_csv("synthetic_transactions.csv")

print("Original rows:", len(df))

# Remove rows that are identical in every column
clean_df = df.drop_duplicates().copy()

print("Rows after removing duplicates:", len(clean_df))
print("Rows removed:", len(df) - len(clean_df))

# Save to a new file; original remains unchanged
clean_df.to_csv("synthetic_transactions_deduplicated.csv", index=False)

print("\nClass counts after deduplication:")
print(clean_df["status"].value_counts().sort_index())

print("\nCleaned dataset saved successfully!")
