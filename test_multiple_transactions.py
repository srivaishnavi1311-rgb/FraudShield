
import requests

API_URL = "http://127.0.0.1:8000/predict"

transactions = [
    {"amount": 2000, "international": False},
    {"amount": 2000, "international": True},
    {"amount": 60000, "international": False},
    {"amount": 1000, "international": False},
]

allowed_predictions = ["LOW RISK", "SUSPICIOUS"]

print("Testing multiple transactions...\n")

for number, transaction in enumerate(transactions, start=1):
    try:
        response = requests.post(
            API_URL,
            json=transaction,
            timeout=3
        )

        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction")

            if prediction in allowed_predictions:
                print(f"Transaction {number}: PASS")
                print("Prediction:", prediction)
            else:
                print(f"Transaction {number}: FAIL")
                print("Unexpected prediction:", prediction)

        else:
            print(f"Transaction {number}: HTTP {response.status_code}")

    except requests.exceptions.RequestException as error:
        print(f"Transaction {number}: Request failed - {error}")

    print("-" * 30)
