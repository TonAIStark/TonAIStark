# avnu_python_client.DCAApi

All URIs are relative to *https://starknet.api.avnu.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_typed_data_cancel_order**](DCAApi.md#build_typed_data_cancel_order) | **POST** /dca/v1/orders/{address}/cancel/build-typed-data | Retrieve typed data to cancel DCA order
[**build_typed_data_create_order**](DCAApi.md#build_typed_data_create_order) | **POST** /dca/v1/orders/build-typed-data | Retrieve typed data to create DCA order
[**cancel_order**](DCAApi.md#cancel_order) | **POST** /dca/v1/orders/{address}/cancel | Retrieve calls to cancel DCA order
[**create_order**](DCAApi.md#create_order) | **POST** /dca/v1/orders | Retrieve calls to create DCA order
[**execute_cancel_order**](DCAApi.md#execute_cancel_order) | **POST** /dca/v1/orders/{address}/cancel/execute | Cancel the order
[**execute_create_order**](DCAApi.md#execute_create_order) | **POST** /dca/v1/orders/execute | Execute the order creation
[**get_orders**](DCAApi.md#get_orders) | **GET** /dca/v1/orders | Find DCA orders


# **build_typed_data_cancel_order**
> TypedData build_typed_data_cancel_order(address, cancel_order_typed_data_request, ask_signature=ask_signature)

Retrieve typed data to cancel DCA order

Call this endpoint if you want to the paymaster to cancel a DCA order.

### Example


```python
import avnu_python_client
from avnu_python_client.models.cancel_order_typed_data_request import CancelOrderTypedDataRequest
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
    api_instance = avnu_python_client.DCAApi(api_client)
    address = 'address_example' # str | 
    cancel_order_typed_data_request = avnu_python_client.CancelOrderTypedDataRequest() # CancelOrderTypedDataRequest | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Retrieve typed data to cancel DCA order
        api_response = api_instance.build_typed_data_cancel_order(address, cancel_order_typed_data_request, ask_signature=ask_signature)
        print("The response of DCAApi->build_typed_data_cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCAApi->build_typed_data_cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **cancel_order_typed_data_request** | [**CancelOrderTypedDataRequest**](CancelOrderTypedDataRequest.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**TypedData**](TypedData.md)

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

# **build_typed_data_create_order**
> TypedData build_typed_data_create_order(create_order_typed_data_request, ask_signature=ask_signature)

Retrieve typed data to create DCA order

Call this endpoint if you want to the paymaster to create a DCA order.

### Example


```python
import avnu_python_client
from avnu_python_client.models.create_order_typed_data_request import CreateOrderTypedDataRequest
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
    api_instance = avnu_python_client.DCAApi(api_client)
    create_order_typed_data_request = avnu_python_client.CreateOrderTypedDataRequest() # CreateOrderTypedDataRequest | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Retrieve typed data to create DCA order
        api_response = api_instance.build_typed_data_create_order(create_order_typed_data_request, ask_signature=ask_signature)
        print("The response of DCAApi->build_typed_data_create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCAApi->build_typed_data_create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_typed_data_request** | [**CreateOrderTypedDataRequest**](CreateOrderTypedDataRequest.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**TypedData**](TypedData.md)

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

# **cancel_order**
> List[CallDto] cancel_order(address, ask_signature=ask_signature)

Retrieve calls to cancel DCA order

Call this endpoint if you want to execute the transaction that will cancel the DCA order.

### Example


```python
import avnu_python_client
from avnu_python_client.models.call_dto import CallDto
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
    api_instance = avnu_python_client.DCAApi(api_client)
    address = 'address_example' # str | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Retrieve calls to cancel DCA order
        api_response = api_instance.cancel_order(address, ask_signature=ask_signature)
        print("The response of DCAApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCAApi->cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**List[CallDto]**](CallDto.md)

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

# **create_order**
> List[CallDto] create_order(create_order_request_dto, ask_signature=ask_signature)

Retrieve calls to create DCA order

Call this endpoint if you want to execute the transaction that will create a DCA order.

### Example


```python
import avnu_python_client
from avnu_python_client.models.call_dto import CallDto
from avnu_python_client.models.create_order_request_dto import CreateOrderRequestDto
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
    api_instance = avnu_python_client.DCAApi(api_client)
    create_order_request_dto = avnu_python_client.CreateOrderRequestDto() # CreateOrderRequestDto | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Retrieve calls to create DCA order
        api_response = api_instance.create_order(create_order_request_dto, ask_signature=ask_signature)
        print("The response of DCAApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCAApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_request_dto** | [**CreateOrderRequestDto**](CreateOrderRequestDto.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**List[CallDto]**](CallDto.md)

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

# **execute_cancel_order**
> ExecuteResponse execute_cancel_order(address, execute_request, ask_signature=ask_signature)

Cancel the order

Call after calling the /build-typed-data endpoint and signing the typed data.

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
    api_instance = avnu_python_client.DCAApi(api_client)
    address = 'address_example' # str | 
    execute_request = avnu_python_client.ExecuteRequest() # ExecuteRequest | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Cancel the order
        api_response = api_instance.execute_cancel_order(address, execute_request, ask_signature=ask_signature)
        print("The response of DCAApi->execute_cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCAApi->execute_cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **execute_request** | [**ExecuteRequest**](ExecuteRequest.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

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

# **execute_create_order**
> ExecuteResponse execute_create_order(execute_request, ask_signature=ask_signature)

Execute the order creation

Call after calling the /build-typed-data endpoint and signing the typed data.

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
    api_instance = avnu_python_client.DCAApi(api_client)
    execute_request = avnu_python_client.ExecuteRequest() # ExecuteRequest | 
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Execute the order creation
        api_response = api_instance.execute_create_order(execute_request, ask_signature=ask_signature)
        print("The response of DCAApi->execute_create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCAApi->execute_create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_request** | [**ExecuteRequest**](ExecuteRequest.md)|  | 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

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

# **get_orders**
> OrderPage get_orders(trader_address, status=status, page=page, size=size, sort=sort, ask_signature=ask_signature)

Find DCA orders

This endpoint returns all the trader's orders.

### Example


```python
import avnu_python_client
from avnu_python_client.models.order_page import OrderPage
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
    api_instance = avnu_python_client.DCAApi(api_client)
    trader_address = '0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7' # str | The trader address (hex format)
    status = 'ACTIVE' # str | Filter orders by status. ACTIVE will return all the open orders (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Find DCA orders
        api_response = api_instance.get_orders(trader_address, status=status, page=page, size=size, sort=sort, ask_signature=ask_signature)
        print("The response of DCAApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DCAApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trader_address** | **str**| The trader address (hex format) | 
 **status** | **str**| Filter orders by status. ACTIVE will return all the open orders | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**OrderPage**](OrderPage.md)

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

