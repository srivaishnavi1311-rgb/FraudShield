
import csv

failed_count = 0

with open("fraudshield_test_results.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["test_result"] != "PASS":
            print("Failed Test:", row["test_number"])
            print("Amount:", row["amount"])
            print("Prediction:", row["prediction"])
            print("Result:", row["test_result"])
            print("-" * 30)
            failed_count += 1

if failed_count == 0:
    print("Great! No failed tests found.")

print("Total failed tests:", failed_count)
