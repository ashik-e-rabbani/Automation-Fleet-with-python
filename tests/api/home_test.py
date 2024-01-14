import pytest
import requests

# Define the base URL for your API
BASE_URL = "http://10.9.0.77:6060/np-payment-gateway/"

def test_get_request():
    # Send a GET request to the API endpoint
    response = requests.get(BASE_URL + "api/admin/reconcile-dbbl/12-12-2023 10:02:15/11-11-2024 10:02:15")

    # Assert the response status code
    assert response.status_code == 201

    # Add more assertions based on your API response

# You can add more test functions as needed
