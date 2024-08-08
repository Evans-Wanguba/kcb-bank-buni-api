<?php

use EvansWanguba\KcbBank\BuniApi;

require "vendor/autoload.php";

$buni = new BuniApi();

// BancAssuranceFileService
$params = array();
$buni->postBancAssuranceFileService($params);

// FundsTransferAPIService
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

// MpesaExpressAPIService
$params = array();
$buni->postMpesaExpressAPIService($params);

// MpesaTransactionInfo
$params = array();
$buni->postMpesaTransactionInfo($params);

// QueryCoreTransactionStatus
$params = array();
$buni->postQueryCoreTransactionStatus($params);

// ValidateExternalBill
$params = array();
$buni->postValidateExternalBill($params);

// VendingGatewayApis
$params = array();
$buni->postVendingGatewayApis($params);
