
import requests

API_URL = "http://127.0.0.1:8000/predict"


def test_required_fields():
    print("Testing required API response fields...")

    response = requests.post(
        API_URL,
        json={
            "amount": 2000,
            "international": False
        },
        timeout=3
    )

    result = response.json()

    if response.status_code == 200 and isinstance(result, dict):
        print("PASS: Valid API response received")
    else:
        print("FAIL: Invalid API response")
        return

    required_fields = ["prediction"]

    for field in required_fields:
        if field in result:
            print(f"PASS: '{field}' field exists")
        else:
            print(f"FAIL: '{field}' field is missing")

    print("Complete response:", result)


test_required_fields()
