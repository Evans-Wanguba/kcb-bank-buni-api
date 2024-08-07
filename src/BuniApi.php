<?php

namespace EvansWanguba\KcbBank;

use GuzzleHttp\Client;
use GuzzleHttp\Promise;

/**
 * Class BuniApi.
 *
 * @category PHP
 * @author   Evans Wanguba <ewanguba@gmail.com>
 */
class BuniApi
{
    /**
     * The base URI to be called.
     *
     * @var string
     */
    private $baseUri = 'https://sandbox.buni.kcbgroup.com/devportal/apis/';

    /**
     * The Guzzle HTTP Client.
     *
     * @var Client
     */
    private $client;

    /**
     * BuniApi constructor.
     */
    public function __construct()
    {
        $this->client = new Client([
            'base_uri' => $this->baseUri,
            'headers' => [
                'Authorization' => 'Bearer ' . env('BUNI_ACCESS_TOKEN'),
                'Accept'        => 'application/json',
            ]
        ]);
    }

    /**
     * Initiate a FundsTransferAPIService request.
     *
     * @return string
     */
    public function postFundsTransferAPIService($params)
    {
        try {
            $response = $this->client->request('POST', 'fundstransfer', [
                'json' => $params
            ]);

            $statuscode = $response->getStatusCode();

            return json_decode($response->getBody()->getContents());
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }

    /**
     * Initiate a MpesaExpressAPIService request.
     *
     * @return string
     */
    public function postMpesaExpressAPIService($params)
    {
        try {
            $response = $this->client->request('POST', 'mm/api/request', [
                'json' => $params
            ]);

            $statuscode = $response->getStatusCode();

            return json_decode($response->getBody()->getContents());
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }

    /**
     * Initiate a MpesaTransactionInfo request.
     *
     * @return string
     */
    public function postMpesaTransactionInfo($params)
    {
        try {
            $response = $this->client->request('POST', 'mpesa/transactioninfo', [
                'json' => $params
            ]);

            $statuscode = $response->getStatusCode();

            return json_decode($response->getBody()->getContents());
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }

    /**
     * Initiate a QueryCoreTransactionStatus request.
     *
     * @return string
     */
    public function postQueryCoreTransactionStatus($params)
    {
        try {
            $response = $this->client->request('POST', 'v1/core/t24/querytransaction', [
                'json' => $params
            ]);

            $statuscode = $response->getStatusCode();

            return json_decode($response->getBody()->getContents());
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }

    /**
     * Initiate a ValidateExternalBill request.
     *
     * @return string
     */
    public function postValidateExternalBill($params)
    {
        try {
            $response = $this->client->request('POST', 'kcb/vpi/api/v1/validate-external-bill', [
                'json' => $params
            ]);

            $statuscode = $response->getStatusCode();

            return json_decode($response->getBody()->getContents());
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }

    /**
     * Initiate a VendingGatewayApis request.
     *
     * @return string
     */
    public function postVendingGatewayApis($params)
    {
        try {
            $response = $this->client->request('POST', 'kcb/vendingGateway/v1', [
                'json' => $params
            ]);

            $statuscode = $response->getStatusCode();

            return json_decode($response->getBody()->getContents());
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }
}
