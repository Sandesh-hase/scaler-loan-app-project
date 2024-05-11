import pytest
from loan_app import app
import json

@pytest.fixture()
def client():
    return app.test_client()

def test_ping(client):
    result = client.get("/ping")
    assert result.status_code == 200
    # result.data = json.loads
    assert result.json == {"Message": "Pinging the model....!"}

def test_predict(client):
    test_data = {
        "Gender": "Male",
        "Married": "Unmarried",
        "ApplicantIncome": 20000,
        "Credit_History": 1.0,
        "LoanAmount": 500000
    }

    result = client.post("/predict", json=test_data)
    assert result.status_code == 200
    assert result.json == {'Loan approval status:- ': 'Rejected'}
