# avnu_python_client.PaymasterApi

All URIs are relative to *https://starknet.api.avnu.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_typed_data1**](PaymasterApi.md#build_typed_data1) | **POST** /paymaster/v1/build-typed-data | Build the typed data
[**deploy_account1**](PaymasterApi.md#deploy_account1) | **POST** /paymaster/v1/deploy-account | Deploy an account
[**execute1**](PaymasterApi.md#execute1) | **POST** /paymaster/v1/execute | Execute the calls
[**get_gas_token_prices**](PaymasterApi.md#get_gas_token_prices) | **GET** /paymaster/v1/gas-token-prices | Get the supported gas tokens and their prices in ETH and USD
[**get_rewards1**](PaymasterApi.md#get_rewards1) | **GET** /paymaster/v1/accounts/{address}/rewards | Retrieve account&#39;s rewards
[**get_sponsor**](PaymasterApi.md#get_sponsor) | **GET** /paymaster/v1/sponsor-activity | 
[**is_compatible1**](PaymasterApi.md#is_compatible1) | **GET** /paymaster/v1/accounts/{address}/compatible | Check if the account is compatible with the gasless service
[**register_reward1**](PaymasterApi.md#register_reward1) | **POST** /paymaster/v1/accounts/{address}/rewards | Add a reward to an account
[**status**](PaymasterApi.md#status) | **GET** /paymaster/v1/status | Get the current gasless service status


# **build_typed_data1**
> TypedData build_typed_data1(build_typed_data_request, api_key=api_key, ask_signature=ask_signature)

Build the typed data

This endpoint enables dapps or users to build the typed data from a list of calls. Once signed by the user, the typed data's calls will be executed by the API using the POST /execute endpoint

### Example


```python
import avnu_python_client
from avnu_python_client.models.build_typed_data_request import BuildTypedDataRequest
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    build_typed_data_request = avnu_python_client.BuildTypedDataRequest() # BuildTypedDataRequest | 
    api_key = 'api_key_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Build the typed data
        api_response = api_instance.build_typed_data1(build_typed_data_request, api_key=api_key, ask_signature=ask_signature)
        print("The response of PaymasterApi->build_typed_data1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->build_typed_data1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_typed_data_request** | [**BuildTypedDataRequest**](BuildTypedDataRequest.md)|  | 
 **api_key** | **str**|  | [optional] 
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

# **deploy_account1**
> ExecuteResponse deploy_account1(deploy_account_request_dto, api_key=api_key, ask_signature=ask_signature)

Deploy an account

This endpoint just deploys an account. It doesn't execute any call

### Example


```python
import avnu_python_client
from avnu_python_client.models.deploy_account_request_dto import DeployAccountRequestDto
from avnu_python_client.models.execute_response import ExecuteResponse
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    deploy_account_request_dto = avnu_python_client.DeployAccountRequestDto() # DeployAccountRequestDto | 
    api_key = 'api_key_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Deploy an account
        api_response = api_instance.deploy_account1(deploy_account_request_dto, api_key=api_key, ask_signature=ask_signature)
        print("The response of PaymasterApi->deploy_account1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->deploy_account1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_account_request_dto** | [**DeployAccountRequestDto**](DeployAccountRequestDto.md)|  | 
 **api_key** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

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

# **execute1**
> ExecuteResponse execute1(execute_request, api_key=api_key, ask_signature=ask_signature)

Execute the calls

This endpoint enables dapps or users to execute calls using the gasless service

### Example


```python
import avnu_python_client
from avnu_python_client.models.execute_request import ExecuteRequest
from avnu_python_client.models.execute_response import ExecuteResponse
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    execute_request = avnu_python_client.ExecuteRequest() # ExecuteRequest | 
    api_key = 'api_key_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Execute the calls
        api_response = api_instance.execute1(execute_request, api_key=api_key, ask_signature=ask_signature)
        print("The response of PaymasterApi->execute1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->execute1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_request** | [**ExecuteRequest**](ExecuteRequest.md)|  | 
 **api_key** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

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

# **get_gas_token_prices**
> GaslessStatus get_gas_token_prices(ask_signature=ask_signature)

Get the supported gas tokens and their prices in ETH and USD

### Example


```python
import avnu_python_client
from avnu_python_client.models.gasless_status import GaslessStatus
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Get the supported gas tokens and their prices in ETH and USD
        api_response = api_instance.get_gas_token_prices(ask_signature=ask_signature)
        print("The response of PaymasterApi->get_gas_token_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->get_gas_token_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**GaslessStatus**](GaslessStatus.md)

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

# **get_rewards1**
> List[Reward] get_rewards1(address, sponsor=sponsor, campaign=campaign, protocol=protocol, ask_signature=ask_signature)

Retrieve account's rewards

Rewards are registered by a sponsor. This sponsor will pay account's gas fees.

### Example


```python
import avnu_python_client
from avnu_python_client.models.reward import Reward
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    address = 'address_example' # str | 
    sponsor = 'sponsor_example' # str |  (optional)
    campaign = 'campaign_example' # str |  (optional)
    protocol = 'protocol_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Retrieve account's rewards
        api_response = api_instance.get_rewards1(address, sponsor=sponsor, campaign=campaign, protocol=protocol, ask_signature=ask_signature)
        print("The response of PaymasterApi->get_rewards1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->get_rewards1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **sponsor** | **str**|  | [optional] 
 **campaign** | **str**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**List[Reward]**](Reward.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sponsor**
> SponsorActivity get_sponsor(api_key, start_date=start_date, end_date=end_date, ask_signature=ask_signature)

### Example


```python
import avnu_python_client
from avnu_python_client.models.sponsor_activity import SponsorActivity
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    api_key = 'api_key_example' # str | 
    start_date = '2024-02-04T14:08:38.511Z' # datetime | Default value 7 days ago (optional)
    end_date = '2024-02-04T15:08:38.511Z' # datetime | Default value is now (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        api_response = api_instance.get_sponsor(api_key, start_date=start_date, end_date=end_date, ask_signature=ask_signature)
        print("The response of PaymasterApi->get_sponsor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->get_sponsor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **start_date** | **datetime**| Default value 7 days ago | [optional] 
 **end_date** | **datetime**| Default value is now | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**SponsorActivity**](SponsorActivity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_compatible1**
> GaslessStatus is_compatible1(address, ask_signature=ask_signature)

Check if the account is compatible with the gasless service

This endpoint indicates if the accounts is compatible with the gasless service and if so, what is the validation's gas consumed overhead. When simulating a transaction, the returned gas cost doesn't include the validation's gas consumed

### Example


```python
import avnu_python_client
from avnu_python_client.models.gasless_status import GaslessStatus
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    address = '0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7' # str | The account's address
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Check if the account is compatible with the gasless service
        api_response = api_instance.is_compatible1(address, ask_signature=ask_signature)
        print("The response of PaymasterApi->is_compatible1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->is_compatible1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The account&#39;s address | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**GaslessStatus**](GaslessStatus.md)

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

# **register_reward1**
> Reward register_reward1(address, api_key, register_reward, ask_signature=ask_signature)

Add a reward to an account

You can decide to pay the gas fees of an address. To do so, you simply have to add a reward

### Example


```python
import avnu_python_client
from avnu_python_client.models.register_reward import RegisterReward
from avnu_python_client.models.reward import Reward
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    address = 'address_example' # str | 
    api_key = 'api_key_example' # str | 
    register_reward = avnu_python_client.RegisterReward() # RegisterReward | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Add a reward to an account
        api_response = api_instance.register_reward1(address, api_key, register_reward, ask_signature=ask_signature)
        print("The response of PaymasterApi->register_reward1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->register_reward1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **api_key** | **str**|  | 
 **register_reward** | [**RegisterReward**](RegisterReward.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**Reward**](Reward.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**200** | OK |  * signature - The response body signature. Only returned when &#39;ask-signature&#39; has been provided. To validate the signature, you need first to encode the body using keccak and to compute the hash with the encoded value. Then your can verify the signature using the public key, the hash and the signature. You can find an example here: https://github.com/419Labs/avnu-sdk/blob/main/src/services.ts#L23 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> GaslessStatus status(ask_signature=ask_signature)

Get the current gasless service status

### Example


```python
import avnu_python_client
from avnu_python_client.models.gasless_status import GaslessStatus
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
    api_instance = avnu_python_client.PaymasterApi(api_client)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Get the current gasless service status
        api_response = api_instance.status(ask_signature=ask_signature)
        print("The response of PaymasterApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymasterApi->status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**GaslessStatus**](GaslessStatus.md)

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

