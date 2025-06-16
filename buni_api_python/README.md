# KCB Buni API Python Client

A Python client library for interacting with the KCB Buni API. This library is a Python conversion of the original PHP library.

## Features

*   Provides methods for all documented KCB Buni API services:
    *   BancAssuranceFileService
    *   FundsTransferAPIService
    *   MpesaExpressAPIService
    *   MpesaTransactionInfo
    *   QueryCoreTransactionStatus
    *   ValidateExternalBill
    *   VendingGatewayApis
*   Handles authentication using Bearer Token.
*   Configurable for sandbox and production environments via environment variables.
*   Uses the `requests` library for HTTP communication.

## Prerequisites

*   Python 3.7+
*   An active KCB Buni API account with an Access Token.

## Installation

1.  **Clone the repository (if not already done):**
    ```bash
    git clone <repository_url>
    cd buni_api_python
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file (or it will be provided) with the following content:
    ```
    requests
    python-dotenv
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```
    Alternatively, if a `setup.py` is provided and you want to install the package itself:
    ```bash
    pip install .
    ```

## Configuration

The client requires the following environment variables to be set:

*   `BUNI_ACCESS_TOKEN`: Your KCB Buni API access token.
*   `BUNI_ENV`: (Optional) The API environment to use. Can be `sandbox` (default) or `production`.

You can set these environment variables directly in your system, or by creating a `.env` file in the root of your project (`buni_api_python` directory if running examples directly).

**Example `.env` file:**

```
BUNI_ACCESS_TOKEN="your_actual_api_access_token_here"
BUNI_ENV="sandbox"
```

## Usage

First, ensure the library is installed and environment variables are set.

```python
from buni_api import BuniApi
from dotenv import load_dotenv

# Load environment variables from .env file in the current directory
load_dotenv()

try:
    client = BuniApi()
except ValueError as e:
    print(f"Error: {e}")
    print("Please ensure BUNI_ACCESS_TOKEN is set in your environment or .env file.")
    exit()

# Example: Funds Transfer
funds_transfer_payload = {
    "beneficiaryDetails": "JANE DOE",
    "companyCode": "KE0010001",
    "creditAccountNumber": "1234567890",
    "currency": "KES",
    "debitAccountNumber": "0987654321",
    "debitAmount": 50.0,
    "paymentDetails": "Test payment",
    "transactionReference": "PYTEST001",
    "transactionType": "IF",
    "beneficiaryBankCode": "01"
}

try:
    response = client.post_funds_transfer_api_service(funds_transfer_payload)
    print("Funds Transfer Response:")
    print(response)
except Exception as e:
    print(f"An error occurred during Funds Transfer: {e}")

# Example: Mpesa Express STK Push
mpesa_express_payload = {
    "phoneNumber": "254712345678",
    "amount": "100",
    "invoiceNumber": "INV2023001",
    "sharedShortCode": True,
    "orgShortCode": "", # Required if sharedShortCode is False
    "orgPassKey": "",   # Required if sharedShortCode is False
    "callbackUrl": "https://yourdomain.com/callbacks/mpesa_express",
    "transactionDescription": "Payment for order INV2023001"
}

try:
    response = client.post_mpesa_express_api_service(mpesa_express_payload)
    print("\nMpesa Express Response:")
    print(response)
except Exception as e:
    print(f"An error occurred during Mpesa Express: {e}")

# ... call other methods similarly ...

```

See the `examples/sample_usage.py` file for more detailed examples of how to call each API method.

## Error Handling

The client's methods will return a dictionary with an "error" key if a request fails at the HTTP level (e.g., connection error, 4xx/5xx status codes before getting a JSON response from the API). If the API returns a JSON error, that JSON is typically returned.

Successful API calls return a dictionary parsed from the API's JSON response.

## Development

(Optional: Add details about running tests if you implement them)

```bash
# Example: Run tests using pytest
# pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
```
