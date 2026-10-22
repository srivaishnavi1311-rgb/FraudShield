
import requests

API_URL = "http://127.0.0.1:8000/predict"


def test_response_types():
    print("Testing API response data types...")

    response = requests.post(
        API_URL,
        json={
            "amount": 2000,
            "international": False
        },
        timeout=3
    )

    result = response.json()

    # Check 1: Status code must be an integer
    if isinstance(response.status_code, int):
        print("PASS: Status code is an integer")
    else:
        print("FAIL: Status code is not an integer")

    # Check 2: Prediction must be a string
    prediction = result.get("prediction")

    if isinstance(prediction, str):
        print("PASS: Prediction is text")
        print("Prediction:", prediction)
    else:
        print("FAIL: Prediction is not text")

    # Check 3: Response must be a dictionary
    if isinstance(result, dict):
        print("PASS: API response is a dictionary")
    else:
        print("FAIL: API response is not a dictionary")


test_response_types()
