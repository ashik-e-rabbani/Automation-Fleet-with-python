import pytest
import requests

# Define the base URL for your API
BASE_URL = "https://demoqa.com/"

def test_get_request():
    # Send a GET request to the API endpoint
    response = requests.get(BASE_URL + "books")

    # Assert the response status code
    assert response.status_code == 200

    # Add more assertions based on your API response

# You can add more test functions as needed
