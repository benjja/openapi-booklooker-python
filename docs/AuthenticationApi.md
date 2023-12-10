# openapi_client.AuthenticationApi

All URIs are relative to *https://api.booklooker.de/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_post**](AuthenticationApi.md#authenticate_post) | **POST** /authenticate | Authentifizierung via API Key


# **authenticate_post**
> AuthenticatePost200Response authenticate_post(api_key)

Authentifizierung via API Key

Authentifizierung via API Key. Ihren persönlichen API Key erhalten Sie <a href=\"https://www.booklooker.de/app/priv/api_key.php\">hier</a>. 

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.authenticate_post200_response import AuthenticatePost200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.booklooker.de/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.booklooker.de/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)
    api_key = 'api_key_example' # str | Ihr persönlicher API Key

    try:
        # Authentifizierung via API Key
        api_response = api_instance.authenticate_post(api_key)
        print("The response of AuthenticationApi->authenticate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Ihr persönlicher API Key | 

### Return type

[**AuthenticatePost200Response**](AuthenticatePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

