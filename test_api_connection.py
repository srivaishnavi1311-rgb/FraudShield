
import requests

API_URL = "http://127.0.0.1:8000/predict"


def test_api_connection():
    print("Checking FraudShield API connection...")

    try:
        response = requests.post(
            API_URL,
            json={
                "amount": 2000,
                "international": False
            },
            timeout=3
        )

        print("HTTP Status:", response.status_code)

        if response.status_code == 200:
            print("Connection test: PASS")
            print("Prediction:", response.json().get("prediction"))
        else:
            print("Connection reached, but request failed.")
            print("Response:", response.text)

    except requests.exceptions.Timeout:
        print("Connection test: FAIL")
        print("Reason: The API took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("Connection test: FAIL")
        print("Reason: Cannot connect to the API server.")

    except requests.exceptions.RequestException as error:
        print("Connection test: FAIL")
        print("Reason:", error)


test_api_connection()
