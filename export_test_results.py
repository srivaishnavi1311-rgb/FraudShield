
import requests
import csv
from datetime import datetime

API_URL = "http://127.0.0.1:8000/predict"

transactions = [
    {"amount": 2000, "international": False},
    {"amount": 2000, "international": True},
    {"amount": 60000, "international": False},
    {"amount": 1000, "international": False},
]

allowed_predictions = ["LOW RISK", "SUSPICIOUS"]
results = []

for number, transaction in enumerate(transactions, start=1):
    try:
        response = requests.post(
            API_URL,
            json=transaction,
            timeout=3
        )

        prediction = ""

        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction", "")

            if prediction in allowed_predictions:
                test_result = "PASS"
            else:
                test_result = "FAIL"
        else:
            test_result = f"HTTP {response.status_code}"

    except requests.exceptions.RequestException:
        prediction = ""
        test_result = "REQUEST ERROR"

    results.append({
        "test_number": number,
        "amount": transaction["amount"],
        "international": transaction["international"],
        "prediction": prediction,
        "test_result": test_result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

with open("fraudshield_test_results.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "test_number",
        "amount",
        "international",
        "prediction",
        "test_result",
        "timestamp"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("CSV report saved: fraudshield_test_results.csv")
print("Total test records:", len(results))

for result in results:
    print(
        f"Test {result['test_number']}: "
        f"{result['test_result']} - {result['prediction']}"
    )
