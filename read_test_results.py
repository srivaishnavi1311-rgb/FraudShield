
import csv

with open("fraudshield_test_results.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Test Number:", row["test_number"])
        print("Amount:", row["amount"])
        print("International:", row["international"])
        print("Prediction:", row["prediction"])
        print("Result:", row["test_result"])
        print("-" * 30)
