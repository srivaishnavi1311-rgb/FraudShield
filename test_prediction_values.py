
import requests

API_URL = "http://127.0.0.1:8000/predict"

ALLOWED_PREDICTIONS = ["LOW RISK", "SUSPICIOUS"]


def test_prediction_values():
    print("Testing prediction values...")

    response = requests.post(
        API_URL,
        json={
            "amount": 2000,
            "international": False
        },
        timeout=3
    )

    if response.status_code != 200:
        print("FAIL: API request was unsuccessful")
        print("HTTP Status:", response.status_code)
        return

    result = response.json()
    prediction = result.get("prediction")

    if prediction in ALLOWED_PREDICTIONS:
        print("PASS: Prediction value is valid")
        print("Prediction:", prediction)
    else:
        print("FAIL: Unexpected prediction value")
        print("Received:", prediction)


test_prediction_values()
