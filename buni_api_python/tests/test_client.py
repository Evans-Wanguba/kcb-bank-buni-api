import pytest
import requests
import os
from buni_api import BuniApi # Assuming buni_api_python is in PYTHONPATH

# Set dummy environment variables for testing if not already set
# In a real CI/CD, these would be set in the environment.
# For local testing, a .env file in the root (buni_api_python) is still good.
if not os.getenv("BUNI_ACCESS_TOKEN"):
    os.environ["BUNI_ACCESS_TOKEN"] = "test_token"
if not os.getenv("BUNI_ENV"):
    os.environ["BUNI_ENV"] = "sandbox"


@pytest.fixture
def client():
    """Pytest fixture to create a BuniApi client."""
    return BuniApi()

@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("BUNI_ACCESS_TOKEN", "test_token_from_fixture")
    monkeypatch.setenv("BUNI_ENV", "sandbox")

def test_buni_api_client_instantiation(mock_env_vars):
    """Test that the BuniApi client can be instantiated."""
    client = BuniApi()
    assert client is not None
    assert client.base_uri == 'https://uat.buni.kcbgroup.com/'
    assert client.access_token == "test_token_from_fixture"
    assert client.session.headers['Authorization'] == 'Bearer test_token_from_fixture'

def test_buni_api_client_instantiation_production(monkeypatch):
    """Test client instantiation for production environment."""
    monkeypatch.setenv("BUNI_ACCESS_TOKEN", "prod_token")
    monkeypatch.setenv("BUNI_ENV", "production")
    client = BuniApi()
    assert client.base_uri == 'https://buni.kcbgroup.com/'
    assert client.access_token == "prod_token"

def test_buni_api_client_missing_token(monkeypatch):
    """Test client instantiation fails if token is missing."""
    monkeypatch.delenv("BUNI_ACCESS_TOKEN", raising=False)
    with pytest.raises(ValueError, match="BUNI_ACCESS_TOKEN environment variable not set"):
        BuniApi()

def test_buni_api_client_invalid_env(monkeypatch):
    """Test client instantiation fails for invalid BUNI_ENV."""
    monkeypatch.setenv("BUNI_ACCESS_TOKEN", "any_token")
    monkeypatch.setenv("BUNI_ENV", "invalid_env")
    with pytest.raises(ValueError, match="Invalid BUNI_ENV: invalid_env"):
        BuniApi()

def test_post_banc_assurance_file_service_success(client, requests_mock):
    """Test a successful call to post_banc_assurance_file_service."""
    endpoint = 'bancassurance/files/readbyid/1.0.0'
    full_url = f"{client.base_uri}{endpoint}"
    mock_payload = {"param1": "value1"}
    mock_response_data = {"status": "success", "data": "some data"}

    requests_mock.post(full_url, json=mock_response_data, status_code=200)

    response = client.post_banc_assurance_file_service(mock_payload)

    assert response == mock_response_data
    history = requests_mock.request_history
    assert len(history) == 1
    assert history[0].method == "POST"
    assert history[0].json() == mock_payload
    assert history[0].headers["Authorization"] == f"Bearer {client.access_token}"

def test_post_funds_transfer_api_service_http_error(client, requests_mock):
    """Test an HTTP error during a call to post_funds_transfer_api_service."""
    endpoint = 'fundstransfer/1.0.0/api/v1/transfer'
    full_url = f"{client.base_uri}{endpoint}"
    mock_payload = {"debitAmount": 100}
    error_response_data = {"errorCode": "E001", "errorMessage": "Insufficient funds"}

    requests_mock.post(full_url, json=error_response_data, status_code=400)

    response = client.post_funds_transfer_api_service(mock_payload)

    assert response is not None
    assert response["error"] is not None # Check structure from _make_request error handling
    assert "400 Client Error" in response["error"]
    assert response["status_code"] == 400
    assert response["details"] == error_response_data

def test_all_service_methods_exist(client):
    """Check if all expected service methods are present."""
    methods = [
        "post_banc_assurance_file_service",
        "post_funds_transfer_api_service",
        "post_mpesa_express_api_service",
        "post_mpesa_transaction_info",
        "post_query_core_transaction_status",
        "post_validate_external_bill",
        "post_vending_gateway_apis",
    ]
    for method_name in methods:
        assert hasattr(client, method_name)
        assert callable(getattr(client, method_name))

# Add more tests for other methods and error scenarios (e.g., network errors)

# Example for a network error (e.g. ConnectionTimeout)
def test_network_error(client, requests_mock):
    endpoint = 'bancassurance/files/readbyid/1.0.0'
    full_url = f"{client.base_uri}{endpoint}"
    requests_mock.post(full_url, exc=requests.exceptions.ConnectTimeout)

    response = client.post_banc_assurance_file_service({})
    assert "error" in response
    assert "ConnectTimeout" in response["error"]
