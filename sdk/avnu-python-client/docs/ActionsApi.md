# avnu_python_client.ActionsApi

All URIs are relative to *https://starknet.api.avnu.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile**](ActionsApi.md#get_profile) | **GET** /v1/actions/{address} | Retrieve user&#39;s actions


# **get_profile**
> PageActionDto get_profile(address, pageable, type=type, integrator_name=integrator_name, ask_signature=ask_signature)

Retrieve user's actions

### Example


```python
import avnu_python_client
from avnu_python_client.models.page_action_dto import PageActionDto
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
    api_instance = avnu_python_client.ActionsApi(api_client)
    address = 'address_example' # str | 
    pageable = avnu_python_client.Pageable() # Pageable | 
    type = ['type_example'] # List[str] |  (optional)
    integrator_name = 'integrator_name_example' # str |  (optional)
    ask_signature = 'ask_signature_example' # str | When the given value is provided with the value 'true', the response header 'signature' will be returned. (optional)

    try:
        # Retrieve user's actions
        api_response = api_instance.get_profile(address, pageable, type=type, integrator_name=integrator_name, ask_signature=ask_signature)
        print("The response of ActionsApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **pageable** | [**Pageable**](.md)|  | 
 **type** | [**List[str]**](str.md)|  | [optional] 
 **integrator_name** | **str**|  | [optional] 
 **ask_signature** | **str**| When the given value is provided with the value &#39;true&#39;, the response header &#39;signature&#39; will be returned. | [optional] 

### Return type

[**PageActionDto**](PageActionDto.md)

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

