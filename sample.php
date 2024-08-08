<?php

use EvansWanguba\KcbBank\BuniApi;

require "vendor/autoload.php";

$buni = new BuniApi();

/*
* BancAssuranceFileService
*/
$params = array();
$buni->postBancAssuranceFileService($params);


/*
* FundsTransferAPIService
*/
$fundsTransferParams = [
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
];
$buni->postFundsTransferAPIService($fundsTransferParams);


/*
* MpesaExpressAPIService
*/
$mpesaExpressParams = [
    "phoneNumber"               => "254700000000",
    "amount"                    => "10",
    "invoiceNumber"             => "ONETILLNO#YOURREF",
    "sharedShortCode"           => true,
    "orgShortCode"              => "",
    "orgPassKey"                => "",
    "callbackUrl"               => "https://posthere.io/f613-4b7f-b82b",
    "transactionDescription"    => "school fee payment"
];
$buni->postMpesaExpressAPIService($mpesaExpressParams);


/*
* MpesaTransactionInfo
*/
$params = array();
$buni->postMpesaTransactionInfo($params);


/*
* QueryCoreTransactionStatus
*/
$queryCoreTransactionStatusParams = [
    "header" => [
        "messageID"             => "{{$guid}}",
        "featureCode"           => "101",
        "featureName"           => "FinancialInquiries",
        "serviceCode"           => "1004",
        "serviceName"           => "TransactionInfo",
        "serviceSubCategory"    => "ACCOUNT",
        "minorServiceVersion"   => "1.0",
        "channelCode"           => "206",
        "channelName"           => "ibank",
        "routeCode"             => "001",
        "timeStamp"             => "22222",
        "serviceMode"           => "sync",
        "subscribeEvents"       => "1",
        "callBackURL"           => ""  
    ],
    "requestPayload" => [
        "transactionInfo" => [
            "primaryData" => [
                "businessKey"       => "FT220367DV7J",
                "businessKeyType"   => "FT.REF"
            ],
            "additionalDetails" => [
                "companyCode"       => "KE0010001"
            ]
        ]
    ]
];
$buni->postQueryCoreTransactionStatus($queryCoreTransactionStatusParams);


/*
* ValidateExternalBill
*/
$validateExternalBillParams = [
    "requestId"                 => "UGC002001",
    "customerReference"         => "1020220001046912",
    "organizationReference"     => "572572"
];
$buni->postValidateExternalBill($validateExternalBillParams);


/*
* VendingGatewayApis
*/
$params = array();
$buni->postVendingGatewayApis($params);
