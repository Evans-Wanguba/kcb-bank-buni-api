# Sage Evolution Freedom API

This is a PHP package for Sage Evolution Freedom web service integration. The API is a set of generic Accounting functions that 
is designed to cater for a wide-ranging of functions that allows a merchant to have access to the Sage Evolution system.

## Installation

Pull in the package through Composer.
```bash
composer require evanswanguba/kcb-bank-buni-api
```

Create the following variables in your .env file.
```bash
BUNI_API_KEY=ApiKey
BUNI_API_SECRET=ApiSecret
```

## Supported Functions
- AccountInfoDetailsOfVooma
- AccountInfoOfKCBAccounts
- AccountVerificationNon-KCBviaPesaLink
- AgencyCallbackService
- AgentDeposit
- AgentQueryCustomer
- AgentWithdrawal
- Anti-MoneyLaunderingAPI
- Anti-MoneyLaunderingAPIScreening
- APIEncryptionHelperTool

## Usage
To make a create customer request is simple. Just initiate the `BuniApi` and post the transaction:
```php
use EvansWanguba\KcbBank\BuniApi;

require "vendor/autoload.php";

$sage = new BuniApi();
