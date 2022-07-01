<?php

namespace EvansWanguba\Sage;

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
    private $baseUri = 'http://YourIp:5000/freedom.core/DatabaseName/SDK/Rest/';

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
            'auth' => [
                env('BUNI_API_KEY'), 
                env('BUNI_API_SECRET')
            ]
        ]);
    }

    /**
     * Initiate a get request and send the information to Sage.
     *
     * @return string
     */
    public function getTransaction($initiateEndpoint)
    {
        try {
            $response = $this->client->request('GET', $initiateEndpoint);

            $statuscode = $response->getStatusCode();

            return $response->getBody()->getContents();
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }

    /**
     * Initiate a post request and send the information to Sage.
     *
     * @return string
     */
    public function postTransaction($initiateEndpoint, $params)
    {
        try {
            $response = $this->client->request('POST', $initiateEndpoint, [
                'json' => $params
            ]);

            $statuscode = $response->getStatusCode();

            return json_decode($response->getBody()->getContents());
        } catch (\Exception $exception) {
            return $exception->getMessage();
        }
    }
}
