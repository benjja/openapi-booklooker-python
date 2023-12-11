# booklooker-api-client.ImageApi

All URIs are relative to *https://api.booklooker.de/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_delete**](ImageApi.md#image_delete) | **DELETE** /image | Einzelne oder alle Bilder eines Artikels löschen


# **image_delete**
> AuthenticatePost200Response image_delete(order_no, position=position)

Einzelne oder alle Bilder eines Artikels löschen

Einzelne oder alle Bilder eines Artikels löschen.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import booklooker-api-client
from booklooker-api-client.models.authenticate_post200_response import AuthenticatePost200Response
from booklooker-api-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.booklooker.de/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = booklooker-api-client.Configuration(
    host = "https://api.booklooker.de/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with booklooker-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = booklooker-api-client.ImageApi(api_client)
    order_no = None # object | Ihre Bestell-Nummer
    position = n/a # int | <p>   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. </p> <p>   <strong>Achtung:</strong> Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position <q>2</q> gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. </p>  (optional) (default to n/a)

    try:
        # Einzelne oder alle Bilder eines Artikels löschen
        api_response = api_instance.image_delete(order_no, position=position)
        print("The response of ImageApi->image_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageApi->image_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_no** | [**object**](.md)| Ihre Bestell-Nummer | 
 **position** | **int**| &lt;p&gt;   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. &lt;/p&gt; &lt;p&gt;   &lt;strong&gt;Achtung:&lt;/strong&gt; Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position &lt;q&gt;2&lt;/q&gt; gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. &lt;/p&gt;  | [optional] [default to n/a]

### Return type

[**AuthenticatePost200Response**](AuthenticatePost200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

