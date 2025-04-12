# avnu_python_client.StarknetApi

All URIs are relative to *https://starknet.api.avnu.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_info**](StarknetApi.md#get_token_info) | **GET** /v1/starknet/tokens/{addressOrSymbol} | 
[**get_tokens**](StarknetApi.md#get_tokens) | **GET** /v1/starknet/tokens | 


# **get_token_info**
> TokenDto get_token_info(address_or_symbol, if_none_match=if_none_match, ask_signature=ask_signature)

### Example


```python
import avnu_python_client
from avnu_python_client.models.token_dto import TokenDto
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
    api_instance = avnu_python_client.StarknetApi(api_client)
    address_or_symbol = 'address_or_symbol_example' # str | Token address or symbol. If symbol is provided, we will only find matching token within the verified token list
    if_none_match = 'if_none_match_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        api_response = api_instance.get_token_info(address_or_symbol, if_none_match=if_none_match, ask_signature=ask_signature)
        print("The response of StarknetApi->get_token_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarknetApi->get_token_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_or_symbol** | **str**| Token address or symbol. If symbol is provided, we will only find matching token within the verified token list | 
 **if_none_match** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**TokenDto**](TokenDto.md)

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

# **get_tokens**
> PageTokenDto get_tokens(pageable, search=search, tag=tag, if_none_match=if_none_match, ask_signature=ask_signature)

### Example


```python
import avnu_python_client
from avnu_python_client.models.page_token_dto import PageTokenDto
from avnu_python_client.models.pageable import Pageable
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
    api_instance = avnu_python_client.StarknetApi(api_client)
    pageable = avnu_python_client.Pageable() # Pageable | 
    search = 'search_example' # str |  (optional)
    tag = ['tag_example'] # List[str] |  (optional)
    if_none_match = 'if_none_match_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        api_response = api_instance.get_tokens(pageable, search=search, tag=tag, if_none_match=if_none_match, ask_signature=ask_signature)
        print("The response of StarknetApi->get_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarknetApi->get_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | [**Pageable**](.md)|  | 
 **search** | **str**|  | [optional] 
 **tag** | [**List[str]**](str.md)|  | [optional] 
 **if_none_match** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**PageTokenDto**](PageTokenDto.md)

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

