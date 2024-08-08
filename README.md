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
BUNI_ENV=sandbox
```

## Supported API Services
- BancAssuranceFileService
- FundsTransferAPIService
- MpesaExpressAPIService
- MpesaTransactionInfo
- QueryCoreTransactionStatus
- ValidateExternalBill
- VendingGatewayApis

## Usage
To make a fund transfer request is simple. Just initiate the `BuniApi` and post the transaction:
```php
use EvansWanguba\KcbBank\BuniApi;

// FundsTransferAPIService
$buni = new BuniApi();
$fundsTransferParams = array(
    "beneficiaryDetails"    => "JOHN DOE",
    "companyCode"           => "KE0010001",
    "creditAccountNumber"   => "1279287799",
    "currency"              => "KES",
    "debitAccountNumber"    => "1279258233",
    "debitAmount"           => 26.0,
    "paymentDetails"        => "UT Fund withdrawal",
    "transactionReference"  => "FT1234567890",
    "transactionType"       => "IF",
    "beneficiaryBankCode"   => "01"
);
$buni->postFundsTransferAPIService($fundsTransferParams);
```

see `sample.php` for more examples.
Or email me at `ewanguba@gmail.com`
