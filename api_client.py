
import csv
import json
import os
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

API_URL = "http://127.0.0.1:8000/predict"
LOG_FILE = "api_prediction_log.csv"


def save_prediction(amount, international, prediction):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Add column headings only when creating the file
        if not file_exists:
            writer.writerow([
                "timestamp",
                "amount",
                "international",
                "prediction"
            ])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            amount,
            international,
            prediction
        ])

    print("Prediction saved to:", LOG_FILE)


def check_transaction(amount, international):
    transaction = {
        "amount": amount,
        "international": international
    }

    data = json.dumps(transaction).encode("utf-8")

    request = Request(
        API_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(request, timeout=5) as response:
            result = json.loads(
                response.read().decode("utf-8")
            )

            print("HTTP Status:", response.status)
            print("API Response:", result)

            save_prediction(
                result["amount"],
                result["international"],
                result["prediction"]
            )

    except HTTPError as error:
        print("HTTP Status:", error.code)
        print("Error Response:", error.read().decode("utf-8"))
        print("No prediction saved because the request failed.")

    except URLError as error:
        print("Connection failed:", error.reason)
        print("Check whether the API server is running.")


print("\n--- Test 1: Domestic ---")
check_transaction(2000, False)

print("\n--- Test 2: International ---")
check_transaction(2000, True)

print("\n--- Test 3: Invalid Amount ---")
check_transaction(-500, False)
