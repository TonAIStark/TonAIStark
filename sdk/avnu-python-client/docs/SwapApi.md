# avnu_python_client.SwapApi

All URIs are relative to *https://starknet.api.avnu.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build**](SwapApi.md#build) | **POST** /swap/v2/build | Build swap calldata
[**build1**](SwapApi.md#build1) | **POST** /swap/v1/build | Build swap calldata
[**build_typed_data2**](SwapApi.md#build_typed_data2) | **POST** /swap/v2/build-typed-data | 
[**execute2**](SwapApi.md#execute2) | **POST** /swap/v2/execute | Execute swap
[**get_prices**](SwapApi.md#get_prices) | **GET** /swap/v2/prices | Find the prices of DEX applications
[**get_prices1**](SwapApi.md#get_prices1) | **GET** /swap/v1/prices | Find the prices of DEX applications
[**get_quotes**](SwapApi.md#get_quotes) | **GET** /swap/v2/quotes | Find the best quotes
[**get_quotes1**](SwapApi.md#get_quotes1) | **GET** /swap/v1/quotes | Find the best quotes
[**get_sources**](SwapApi.md#get_sources) | **GET** /swap/v2/sources | Fetch the list of supported sources
[**get_sources1**](SwapApi.md#get_sources1) | **GET** /swap/v1/sources | Fetch the list of supported sources
[**get_tokens1**](SwapApi.md#get_tokens1) | **GET** /swap/v2/tokens | Fetch supported tokens
[**get_tokens2**](SwapApi.md#get_tokens2) | **GET** /swap/v1/tokens | Fetch supported tokens


# **build**
> BuildSwapResponse build(build_swap_request_dto_v2, ask_signature=ask_signature)

Build swap calldata

The build endpoint enables traders to construct swap calldata, which can be used to execute the transaction independently. Prior to targeting the build endpoint, traders should have already chosen a quote from the GET /quotes endpoint.

### Example


```python
import avnu_python_client
from avnu_python_client.models.build_swap_request_dto_v2 import BuildSwapRequestDtoV2
from avnu_python_client.models.build_swap_response import BuildSwapResponse
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    build_swap_request_dto_v2 = avnu_python_client.BuildSwapRequestDtoV2() # BuildSwapRequestDtoV2 | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Build swap calldata
        api_response = api_instance.build(build_swap_request_dto_v2, ask_signature=ask_signature)
        print("The response of SwapApi->build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_swap_request_dto_v2** | [**BuildSwapRequestDtoV2**](BuildSwapRequestDtoV2.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**BuildSwapResponse**](BuildSwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build1**
> BuildSwapResponse build1(build_swap_request, ask_signature=ask_signature)

Build swap calldata

The build endpoint enables traders to construct swap calldata, which can be used to execute the transaction independently. Prior to targeting the build endpoint, traders should have already chosen a quote from the GET /quotes endpoint.

### Example


```python
import avnu_python_client
from avnu_python_client.models.build_swap_request import BuildSwapRequest
from avnu_python_client.models.build_swap_response import BuildSwapResponse
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    build_swap_request = avnu_python_client.BuildSwapRequest() # BuildSwapRequest | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Build swap calldata
        api_response = api_instance.build1(build_swap_request, ask_signature=ask_signature)
        print("The response of SwapApi->build1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->build1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_swap_request** | [**BuildSwapRequest**](BuildSwapRequest.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**BuildSwapResponse**](BuildSwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_typed_data2**
> TypedData build_typed_data2(build_swap_typed_data_request, ask_signature=ask_signature)

### Example


```python
import avnu_python_client
from avnu_python_client.models.build_swap_typed_data_request import BuildSwapTypedDataRequest
from avnu_python_client.models.typed_data import TypedData
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    build_swap_typed_data_request = avnu_python_client.BuildSwapTypedDataRequest() # BuildSwapTypedDataRequest | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        api_response = api_instance.build_typed_data2(build_swap_typed_data_request, ask_signature=ask_signature)
        print("The response of SwapApi->build_typed_data2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->build_typed_data2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_swap_typed_data_request** | [**BuildSwapTypedDataRequest**](BuildSwapTypedDataRequest.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**TypedData**](TypedData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute2**
> ExecuteSwapResponse execute2(execute_swap_request, ask_signature=ask_signature)

Execute swap

This endpoint allows trader to execute swap transaction

### Example


```python
import avnu_python_client
from avnu_python_client.models.execute_swap_request import ExecuteSwapRequest
from avnu_python_client.models.execute_swap_response import ExecuteSwapResponse
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    execute_swap_request = avnu_python_client.ExecuteSwapRequest() # ExecuteSwapRequest | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Execute swap
        api_response = api_instance.execute2(execute_swap_request, ask_signature=ask_signature)
        print("The response of SwapApi->execute2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->execute2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_swap_request** | [**ExecuteSwapRequest**](ExecuteSwapRequest.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteSwapResponse**](ExecuteSwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prices**
> Quote get_prices(sell_token_address, buy_token_address, sell_amount, ask_signature=ask_signature)

Find the prices of DEX applications

This endpoint returns the prices of AMM without any path optimization. It allows to measure the performance of the results from the getQuotes endpoints. The prices will be returned and are sorted (best first).

### Example


```python
import avnu_python_client
from avnu_python_client.models.quote import Quote
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    sell_token_address = '0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7' # str | The token address user wants to sell
    buy_token_address = '0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d' # str | The token address user wants to buy
    sell_amount = '0x038d7ea4c68000' # str | The Amount of token user wants to sell
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Find the prices of DEX applications
        api_response = api_instance.get_prices(sell_token_address, buy_token_address, sell_amount, ask_signature=ask_signature)
        print("The response of SwapApi->get_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sell_token_address** | **str**| The token address user wants to sell | 
 **buy_token_address** | **str**| The token address user wants to buy | 
 **sell_amount** | **str**| The Amount of token user wants to sell | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prices1**
> Quote get_prices1(sell_token_address, buy_token_address, sell_amount, ask_signature=ask_signature)

Find the prices of DEX applications

This endpoint returns the prices of AMM without any path optimization. It allows to measure the performance of the results from the getQuotes endpoints. The prices will be returned and are sorted (best first).

### Example


```python
import avnu_python_client
from avnu_python_client.models.quote import Quote
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    sell_token_address = '0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7' # str | The token address user wants to sell
    buy_token_address = '0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d' # str | The token address user wants to buy
    sell_amount = '0x038d7ea4c68000' # str | The Amount of token user wants to sell
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Find the prices of DEX applications
        api_response = api_instance.get_prices1(sell_token_address, buy_token_address, sell_amount, ask_signature=ask_signature)
        print("The response of SwapApi->get_prices1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_prices1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sell_token_address** | **str**| The token address user wants to sell | 
 **buy_token_address** | **str**| The token address user wants to buy | 
 **sell_amount** | **str**| The Amount of token user wants to sell | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes**
> Quote get_quotes(sell_token_address, buy_token_address, sell_amount=sell_amount, buy_amount=buy_amount, taker_address=taker_address, exclude_sources=exclude_sources, size=size, integrator_fees=integrator_fees, integrator_fee_recipient=integrator_fee_recipient, integrator_name=integrator_name, only_direct=only_direct, pulsar_money_fee_recipient_value=pulsar_money_fee_recipient_value, origin=origin, user_agent=user_agent, ask_signature=ask_signature)

Find the best quotes

This endpoint permits you to receive the best quotes for performing a swap. The endpoint provides default quotes that are sorted in descending order (best first). Each quote is assigned a unique quoteId, which you will use when making calls to the /swap/v2/build or /swap/v2/execute endpoints to initiate the actual swap process.

### Example


```python
import avnu_python_client
from avnu_python_client.models.quote import Quote
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    sell_token_address = '0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7' # str | The token address user wants to sell
    buy_token_address = '0xda114221cb83fa859dbdb4c44beeaa0bb37c7537ad5ae66fe5e0efd20e6eb3' # str | The token address user wants to buy
    sell_amount = '0x38d7ea4c68000' # str | The amount of token user wants to sell. It must be defined if buyAmount is not defined. (optional)
    buy_amount = '0x38d7ea4c68000' # str | The exact amount of token user wants to buy. It must be defined if sellAmount is not defined. (optional)
    taker_address = '0x052D8E9778D026588a51595E30B0F45609B4F771EecF0E335CdeFeD1d84a9D89' # str | The address which will fill the quote (optional)
    exclude_sources = ['10KSwap'] # List[str] | The sources that the user wants to exclude (optional)
    size = 1 # int | The maximum number of returned quotes (optional)
    integrator_fees = '0x3' # str | Fee amount in bps, 30 is 0.3% (optional)
    integrator_fee_recipient = '0x01238E9778D026588a51595E30B0F45609B4F771EecF0E335CdeFeD1d84a9D89' # str | Required when `integratorFees` is defined. You need to provide the address of your fee collector. (optional)
    integrator_name = 'Swagger UI' # str | The name of your application (optional)
    only_direct = True # bool |  (optional)
    pulsar_money_fee_recipient_value = 56 # int |  (optional)
    origin = 'origin_example' # str |  (optional)
    user_agent = 'user_agent_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Find the best quotes
        api_response = api_instance.get_quotes(sell_token_address, buy_token_address, sell_amount=sell_amount, buy_amount=buy_amount, taker_address=taker_address, exclude_sources=exclude_sources, size=size, integrator_fees=integrator_fees, integrator_fee_recipient=integrator_fee_recipient, integrator_name=integrator_name, only_direct=only_direct, pulsar_money_fee_recipient_value=pulsar_money_fee_recipient_value, origin=origin, user_agent=user_agent, ask_signature=ask_signature)
        print("The response of SwapApi->get_quotes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_quotes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sell_token_address** | **str**| The token address user wants to sell | 
 **buy_token_address** | **str**| The token address user wants to buy | 
 **sell_amount** | **str**| The amount of token user wants to sell. It must be defined if buyAmount is not defined. | [optional] 
 **buy_amount** | **str**| The exact amount of token user wants to buy. It must be defined if sellAmount is not defined. | [optional] 
 **taker_address** | **str**| The address which will fill the quote | [optional] 
 **exclude_sources** | [**List[str]**](str.md)| The sources that the user wants to exclude | [optional] 
 **size** | **int**| The maximum number of returned quotes | [optional] 
 **integrator_fees** | **str**| Fee amount in bps, 30 is 0.3% | [optional] 
 **integrator_fee_recipient** | **str**| Required when &#x60;integratorFees&#x60; is defined. You need to provide the address of your fee collector. | [optional] 
 **integrator_name** | **str**| The name of your application | [optional] 
 **only_direct** | **bool**|  | [optional] 
 **pulsar_money_fee_recipient_value** | **int**|  | [optional] 
 **origin** | **str**|  | [optional] 
 **user_agent** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes1**
> Quote get_quotes1(sell_token_address, buy_token_address, sell_amount=sell_amount, buy_amount=buy_amount, taker_address=taker_address, exclude_sources=exclude_sources, size=size, integrator_fees=integrator_fees, integrator_fee_recipient=integrator_fee_recipient, integrator_name=integrator_name, only_direct=only_direct, pulsar_money_fee_recipient_value=pulsar_money_fee_recipient_value, origin=origin, user_agent=user_agent, ask_signature=ask_signature)

Find the best quotes

This endpoint permits you to receive the best quotes for performing a swap. The endpoint provides default quotes that are sorted in descending order (best first). Each quote is assigned a unique quoteId, which you will use when making calls to the /swap/v1/build or /swap/v1/execute endpoints to initiate the actual swap process.

### Example


```python
import avnu_python_client
from avnu_python_client.models.quote import Quote
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    sell_token_address = '0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7' # str | The token address user wants to sell
    buy_token_address = '0xda114221cb83fa859dbdb4c44beeaa0bb37c7537ad5ae66fe5e0efd20e6eb3' # str | The token address user wants to buy
    sell_amount = '0x38d7ea4c68000' # str | The amount of token user wants to sell. It must be defined if buyAmount is not defined. (optional)
    buy_amount = '0x38d7ea4c68000' # str | The exact amount of token user wants to buy. It must be defined if sellAmount is not defined. (optional)
    taker_address = '0x052D8E9778D026588a51595E30B0F45609B4F771EecF0E335CdeFeD1d84a9D89' # str | The address which will fill the quote (optional)
    exclude_sources = ['10KSwap'] # List[str] | The sources that the user wants to exclude (optional)
    size = 1 # int | The maximum number of returned quotes (optional)
    integrator_fees = '0x3' # str | Fee amount in bps, 30 is 0.3% (optional)
    integrator_fee_recipient = '0x01238E9778D026588a51595E30B0F45609B4F771EecF0E335CdeFeD1d84a9D89' # str | Required when `integratorFees` is defined. You need to provide the address of your fee collector. (optional)
    integrator_name = 'Swagger UI' # str | The name of your application (optional)
    only_direct = True # bool |  (optional)
    pulsar_money_fee_recipient_value = 56 # int |  (optional)
    origin = 'origin_example' # str |  (optional)
    user_agent = 'user_agent_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Find the best quotes
        api_response = api_instance.get_quotes1(sell_token_address, buy_token_address, sell_amount=sell_amount, buy_amount=buy_amount, taker_address=taker_address, exclude_sources=exclude_sources, size=size, integrator_fees=integrator_fees, integrator_fee_recipient=integrator_fee_recipient, integrator_name=integrator_name, only_direct=only_direct, pulsar_money_fee_recipient_value=pulsar_money_fee_recipient_value, origin=origin, user_agent=user_agent, ask_signature=ask_signature)
        print("The response of SwapApi->get_quotes1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_quotes1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sell_token_address** | **str**| The token address user wants to sell | 
 **buy_token_address** | **str**| The token address user wants to buy | 
 **sell_amount** | **str**| The amount of token user wants to sell. It must be defined if buyAmount is not defined. | [optional] 
 **buy_amount** | **str**| The exact amount of token user wants to buy. It must be defined if sellAmount is not defined. | [optional] 
 **taker_address** | **str**| The address which will fill the quote | [optional] 
 **exclude_sources** | [**List[str]**](str.md)| The sources that the user wants to exclude | [optional] 
 **size** | **int**| The maximum number of returned quotes | [optional] 
 **integrator_fees** | **str**| Fee amount in bps, 30 is 0.3% | [optional] 
 **integrator_fee_recipient** | **str**| Required when &#x60;integratorFees&#x60; is defined. You need to provide the address of your fee collector. | [optional] 
 **integrator_name** | **str**| The name of your application | [optional] 
 **only_direct** | **bool**|  | [optional] 
 **pulsar_money_fee_recipient_value** | **int**|  | [optional] 
 **origin** | **str**|  | [optional] 
 **user_agent** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sources**
> ExecuteSwapResponse get_sources(page=page, size=size, sort=sort, ask_signature=ask_signature)

Fetch the list of supported sources

This endpoint allows to return the list of all supported sources

### Example


```python
import avnu_python_client
from avnu_python_client.models.execute_swap_response import ExecuteSwapResponse
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Fetch the list of supported sources
        api_response = api_instance.get_sources(page=page, size=size, sort=sort, ask_signature=ask_signature)
        print("The response of SwapApi->get_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteSwapResponse**](ExecuteSwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sources1**
> ExecuteSwapResponse get_sources1(page=page, size=size, sort=sort, ask_signature=ask_signature)

Fetch the list of supported sources

This endpoint allows to return the list of all supported sources

### Example


```python
import avnu_python_client
from avnu_python_client.models.execute_swap_response import ExecuteSwapResponse
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Fetch the list of supported sources
        api_response = api_instance.get_sources1(page=page, size=size, sort=sort, ask_signature=ask_signature)
        print("The response of SwapApi->get_sources1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_sources1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteSwapResponse**](ExecuteSwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens1**
> ExecuteSwapResponse get_tokens1(page=page, size=size, sort=sort, ask_signature=ask_signature)

Fetch supported tokens

This endpoint allows to fetch the list of all officially supported tokens

### Example


```python
import avnu_python_client
from avnu_python_client.models.execute_swap_response import ExecuteSwapResponse
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Fetch supported tokens
        api_response = api_instance.get_tokens1(page=page, size=size, sort=sort, ask_signature=ask_signature)
        print("The response of SwapApi->get_tokens1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_tokens1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteSwapResponse**](ExecuteSwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens2**
> ExecuteSwapResponse get_tokens2(page=page, size=size, sort=sort, ask_signature=ask_signature)

Fetch supported tokens

This endpoint allows to fetch the list of all officially supported tokens

### Example


```python
import avnu_python_client
from avnu_python_client.models.execute_swap_response import ExecuteSwapResponse
from avnu_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://starknet.api.avnu.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = avnu_python_client.Configuration(
    host = "https://starknet.api.avnu.fi"
)


# Enter a context with an instance of the API client
with avnu_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = avnu_python_client.SwapApi(api_client)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Fetch supported tokens
        api_response = api_instance.get_tokens2(page=page, size=size, sort=sort, ask_signature=ask_signature)
        print("The response of SwapApi->get_tokens2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapApi->get_tokens2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteSwapResponse**](ExecuteSwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

