# FraudShield — AI-Based Transaction Risk Checker

## About the Project

FraudShield is a beginner-friendly AI project that predicts whether a financial transaction is **LOW RISK** or **SUSPICIOUS** based on the transaction amount and international transaction status.

This project uses synthetic transaction data for learning and demonstration.

## Features

- Transaction data cleaning and preprocessing
- Machine learning model training and comparison
- Transaction risk prediction
- Interactive Streamlit dashboard
- FastAPI prediction endpoint
- Input validation and error handling
- Automated API testing
- Test reports in TXT and CSV formats
- Transaction prediction logging

## Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- Streamlit
- Joblib
- Requests
- CSV

## How to Run

### 1. Open the Project Folder

Open the FraudShield folder in VS Code and open the terminal.

### 2. Run the Streamlit Dashboard

```powershell
python -m streamlit run streamlit_app.py
```

### 3. Run the FastAPI Server

Open another terminal and run:

```powershell
python -m uvicorn fraud_api:app --reload --port 8000
```

API documentation: http://127.0.0.1:8000/docs

### 4. Run the Tests

```powershell
python test_multiple_transactions.py
python export_test_results.py
python read_test_results.py
python filter_failed_tests.py
```

If a test script requires the API server, keep the server running in another terminal.

## Example Predictions

| Transaction Amount | International | Expected Prediction |
|---:|---|---|
| ₹2,000 | No | LOW RISK |
| ₹2,000 | Yes | SUSPICIOUS |
| ₹60,000 | No | SUSPICIOUS |

These are example outputs from the current practice model.

## Limitations

- The model uses synthetic data, not a representative real-world banking dataset.
- Predictions are not guaranteed to identify actual fraud.
- This project is for educational purposes only and must not be used to make real financial decisions.

## Future Improvements

- Train and evaluate using responsibly sourced real-world data.
- Improve model generalization and fraud detection metrics.
- Add visual analytics and monitoring.
- Strengthen API security and authentication.

## Author

**Sri Vaishnavi**

B.Tech Artificial Intelligence and Data Science
