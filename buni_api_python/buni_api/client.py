import os
import requests
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

class BuniApi:
    def __init__(self):
        buni_env = os.getenv('BUNI_ENV', 'sandbox').lower()
        self.access_token = os.getenv('BUNI_ACCESS_TOKEN')

        if not self.access_token:
            raise ValueError("BUNI_ACCESS_TOKEN environment variable not set.")

        if buni_env == 'sandbox':
            self.base_uri = 'https://uat.buni.kcbgroup.com/'
        elif buni_env == 'production':
            self.base_uri = 'https://buni.kcbgroup.com/'
        else:
            raise ValueError(f"Invalid BUNI_ENV: {buni_env}. Must be 'sandbox' or 'production'.")

        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json', # Added Content-Type as it's good practice for POST
        })

    def _make_request(self, endpoint, params):
        url = f"{self.base_uri}{endpoint}"
        try:
            response = self.session.post(url, json=params)
            response.raise_for_status() # Raises HTTPError for bad responses (4XX or 5XX)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # You might want to log the error or handle specific status codes
            print(f"HTTP error occurred: {http_err} - {response.text}") # Or raise a custom exception
            # For now, re-raising the original error or returning a processed error message
            # Based on PHP code, it returned error message, let's try to mimic that for now
            # but ideally we'd raise a more specific error.
            error_content = response.json() if response.content else {}
            return {"error": str(http_err), "details": error_content, "status_code": response.status_code}
        except requests.exceptions.RequestException as req_err:
            # For other request errors (e.g., connection issues)
            print(f"Request exception occurred: {req_err}")
            return {"error": str(req_err)} # Mimicking PHP's return of error message

    def post_banc_assurance_file_service(self, params: dict):
        """Initiate a BancAssuranceFileService request."""
        return self._make_request('bancassurance/files/readbyid/1.0.0', params)

    def post_funds_transfer_api_service(self, params: dict):
        """Initiate a FundsTransferAPIService request."""
        return self._make_request('fundstransfer/1.0.0/api/v1/transfer', params)

    def post_mpesa_express_api_service(self, params: dict):
        """Initiate a MpesaExpressAPIService request."""
        return self._make_request('mm/api/request/1.0.0/stkpush', params)

    def post_mpesa_transaction_info(self, params: dict):
        """Initiate a MpesaTransactionInfo request."""
        return self._make_request('mpesa/transactioninfo/1.0.0', params)

    def post_query_core_transaction_status(self, params: dict):
        """Initiate a QueryCoreTransactionStatus request."""
        return self._make_request('v1/core/t24/querytransaction/1.0.0/api/transactioninfo', params)

    def post_validate_external_bill(self, params: dict):
        """Initiate a ValidateExternalBill request."""
        return self._make_request('kcb/vpi/api/v1/validate-external-bill/1.0.0/execute', params)

    def post_vending_gateway_apis(self, params: dict):
        """Initiate a VendingGatewayApis request."""
        return self._make_request('kcb/vendingGateway/v1/1.0.0', params)

if __name__ == '__main__':
    # A simple test to ensure class can be instantiated
    # This requires BUNI_ACCESS_TOKEN to be set in your environment or a .env file
    try:
        api = BuniApi()
        print("BuniApi client instantiated successfully.")
        # Example of a call (will fail if endpoint expects specific params or if token is invalid)
        # print(api.post_banc_assurance_file_service({}))
    except ValueError as e:
        print(f"Error instantiating BuniApi: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
