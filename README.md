# KCB Bank Buni API

This is a PHP package for KCB Bank Buni web service integration. Buni is designed for the modern innovator. Developers can now leverage on the KCB API to offer their customers a seamless digital experience on their platforms. Buni helps you integrate a unified payment system onto your website or app, allowing customers to easily pay for your product or service.
For more information, check out [KCB Buni API](https://sandbox.buni.kcbgroup.com/devportal/apis) Guide.

## Installation

Pull in the package through Composer.
```bash
composer require evanswanguba/kcb-bank-buni-api
```

Create the following variables in your .env file.
```bash
BUNI_ACCESS_TOKEN=AccessToken
```

## Supported Functions
- FundsTransferAPIService
- MpesaExpressAPIService
- MpesaTransactionInfo
- QueryCoreTransactionStatus
- ValidateExternalBill
- VendingGatewayApis

## Usage
To make a create customer request is simple. Just initiate the `BuniApi` and post the transaction:
```php
use EvansWanguba\KcbBank\BuniApi;

require "vendor/autoload.php";

$buni = new BuniApi();
