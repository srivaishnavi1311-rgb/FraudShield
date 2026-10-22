
import csv


def check_risk(amount, international):
    if amount > 10000 or international == "yes":
        return "SUSPICIOUS"
    else:
        return "LOW RISK"


transactions = []

count = int(input("How many transactions? "))

for i in range(1, count + 1):
    print("\nTransaction", i)

    amount = float(input("Enter amount (Rs.): "))
    international = input(
        "International? (yes/no): "
    ).strip().lower()

    status = check_risk(amount, international)

    transaction = {
        "amount": amount,
        "international": international,
        "status": status
    }

    transactions.append(transaction)


# Save all transactions to a CSV file
with open("transactions.csv", "w", newline="") as file:
    fieldnames = ["amount", "international", "status"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(transactions)


# Display the report
suspicious_count = 0

for transaction in transactions:
    print(transaction)

    if transaction["status"] == "SUSPICIOUS":
        suspicious_count += 1

print("\n===== FraudShield Report =====")
print("Total transactions:", len(transactions))
print("Suspicious transactions:", suspicious_count)
print("Saved records to transactions.csv")
