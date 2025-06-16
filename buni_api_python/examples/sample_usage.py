import os
from dotenv import load_dotenv
from buni_api import BuniApi # Assuming buni_api_python is in PYTHONPATH or installed

# Load environment variables from a .env file if it exists
# Create a .env file in the root of the buni_api_python project (or where you run this script from)
# with your BUNI_ACCESS_TOKEN and optionally BUNI_ENV
# Example .env:
# BUNI_ACCESS_TOKEN="your_actual_token_here"
# BUNI_ENV="sandbox"
load_dotenv()

def main():
    try:
        print("Attempting to initialize BuniApi client...")
        buni = BuniApi()
        print("BuniApi client initialized successfully.")
        print(f"Using base URI: {buni.base_uri}")
        print(f"Authorization header set with token: {'******' if buni.access_token else 'Not Set'}")
    except ValueError as e:
        print(f"Error initializing BuniApi client: {e}")
        print("Please ensure BUNI_ACCESS_TOKEN is set in your environment or .env file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred during initialization: {e}")
        return

    print("\n--- BancAssuranceFileService ---")
    # The PHP sample provided an empty array.
    # Depending on the API, this might be valid or might require specific keys.
    # Let's assume it's for fetching all or some default items if params is empty.
    banc_assurance_params = {}
    try:
        response = buni.post_banc_assurance_file_service(banc_assurance_params)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling post_banc_assurance_file_service: {e}")

    print("\n--- FundsTransferAPIService ---")
    funds_transfer_params = {
        "beneficiaryDetails": "JOHN DOE",
        "companyCode": "KE0010001",
        "creditAccountNumber": "1279287799",
        "currency": "KES",
        "debitAccountNumber": "1279258233",
        "debitAmount": 26.0,
        "paymentDetails": "UT Fund withdrawal",
        "transactionReference": "FT1234567890PY", # Added PY to differentiate from PHP sample
        "transactionType": "IF",
        "beneficiaryBankCode": "01"
    }
    try:
        response = buni.post_funds_transfer_api_service(funds_transfer_params)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling post_funds_transfer_api_service: {e}")

    print("\n--- MpesaExpressAPIService ---")
    mpesa_express_params = {
        "phoneNumber": "254700000000",
        "amount": "10",
        "invoiceNumber": "ONETILLNO#YOURPYTHONREF", # Updated ref
        "sharedShortCode": True, # Python boolean
        "orgShortCode": "",
        "orgPassKey": "",
        "callbackUrl": "https://posthere.io/f613-4b7f-b82b", # Using the same callback
        "transactionDescription": "school fee payment python"
    }
    try:
        response = buni.post_mpesa_express_api_service(mpesa_express_params)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling post_mpesa_express_api_service: {e}")

    print("\n--- MpesaTransactionInfo ---")
    # PHP sample used an empty array.
    mpesa_transaction_info_params = {}
    try:
        response = buni.post_mpesa_transaction_info(mpesa_transaction_info_params)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling post_mpesa_transaction_info: {e}")

    print("\n--- QueryCoreTransactionStatus ---")
    query_core_transaction_status_params = {
        "header": {
            "messageID": "some-unique-guid-python", # Placeholder, generate dynamically if needed
            "featureCode": "101",
            "featureName": "FinancialInquiries",
            "serviceCode": "1004",
            "serviceName": "TransactionInfo",
            "serviceSubCategory": "ACCOUNT",
            "minorServiceVersion": "1.0",
            "channelCode": "206",
            "channelName": "ibank",
            "routeCode": "001",
            "timeStamp": "22222", # Consider using dynamic timestamp
            "serviceMode": "sync",
            "subscribeEvents": "1",
            "callBackURL": ""
        },
        "requestPayload": {
            "transactionInfo": {
                "primaryData": {
                    "businessKey": "FT220367DV7J", # Example key
                    "businessKeyType": "FT.REF"
                },
                "additionalDetails": {
                    "companyCode": "KE0010001"
                }
            }
        }
    }
    try:
        response = buni.post_query_core_transaction_status(query_core_transaction_status_params)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling post_query_core_transaction_status: {e}")

    print("\n--- ValidateExternalBill ---")
    validate_external_bill_params = {
        "requestId": "UGC002001PY", # Updated request ID
        "customerReference": "1020220001046912",
        "organizationReference": "572572"
    }
    try:
        response = buni.post_validate_external_bill(validate_external_bill_params)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling post_validate_external_bill: {e}")

    print("\n--- VendingGatewayApis ---")
    # PHP sample used an empty array.
    vending_gateway_params = {}
    try:
        response = buni.post_vending_gateway_apis(vending_gateway_params)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error calling post_vending_gateway_apis: {e}")

if __name__ == "__main__":
    # To run this example:
    # 1. Make sure you have a .env file in the `buni_api_python` directory (or where you execute this from)
    #    with BUNI_ACCESS_TOKEN="your_token" and optionally BUNI_ENV="sandbox" (it defaults to sandbox)
    #    Example .env file content:
    #    BUNI_ACCESS_TOKEN="your_kcb_buni_api_token"
    #    BUNI_ENV="sandbox"
    # 2. Ensure 'python-dotenv' and 'requests' are installed (`pip install python-dotenv requests`)
    # 3. From the `buni_api_python` directory, run: `python examples/sample_usage.py`
    #    Or, if `buni_api_python` is in your PYTHONPATH: `python path/to/buni_api_python/examples/sample_usage.py`
    main()
