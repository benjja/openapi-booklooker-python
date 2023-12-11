# booklooker-api-client.ArticleApi

All URIs are relative to *https://api.booklooker.de/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**article_delete**](ArticleApi.md#article_delete) | **DELETE** /article | Einzelnen Artikel zum Löschen vormerken
[**article_list_get**](ArticleApi.md#article_list_get) | **GET** /article_list | Download aller aktiven Artikelnummern
[**article_status_get**](ArticleApi.md#article_status_get) | **GET** /article_status | Abfragen des Status eines Artikels


# **article_delete**
> AuthenticatePost200Response article_delete(order_no)

Einzelnen Artikel zum Löschen vormerken

Einzelnen Artikel zum Löschen vormerken. Der Artikel wird innerhalb der nächsten 2 Stunden gelöscht.

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
    api_instance = booklooker-api-client.ArticleApi(api_client)
    order_no = None # object | Ihre Bestell-Nummer

    try:
        # Einzelnen Artikel zum Löschen vormerken
        api_response = api_instance.article_delete(order_no)
        print("The response of ArticleApi->article_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_no** | [**object**](.md)| Ihre Bestell-Nummer | 

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

# **article_list_get**
> AuthenticatePost200Response article_list_get(field=field, show_price=show_price, show_stock=show_stock, media_type=media_type)

Download aller aktiven Artikelnummern

Download aller aktiven Artikelnummern.

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
    api_instance = booklooker-api-client.ArticleApi(api_client)
    field = 'orderNo' # str | Rückgabefeld, mögliche Werte: <ul class=\"defaultList\">   <li>orderNo &middot; Bestell-Nummer</li>   <li>isbn &middot; ISBN</li>   <li>ean &middot; EAN</li> </ul>  (optional) (default to 'orderNo')
    show_price = 0 # int | Übermittlung des Preises, mögliche Werte: <ul class=\"defaultList\">   <li>0 &middot; nein</li>   <li>1 &middot; ja</li> </ul>  (optional) (default to 0)
    show_stock = 0 # int | Übermittlung des Bestands, mögliche Werte: <ul class=\"defaultList\">   <li>0 &middot; nein</li>   <li>1 &middot; ja</li> </ul>  (optional) (default to 0)
    media_type = n/a # int | Einschränkung nach Medientyp, mögliche Werte: <ul class=\"defaultList\">   <li>0 &middot; Bücher</li>   <li>1 &middot; Filme</li>   <li>2 &middot; Musik</li>   <li>3 &middot; Hörbücher</li>   <li>4 &middot; Spiele</li> </ul>  (optional) (default to n/a)

    try:
        # Download aller aktiven Artikelnummern
        api_response = api_instance.article_list_get(field=field, show_price=show_price, show_stock=show_stock, media_type=media_type)
        print("The response of ArticleApi->article_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_list_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Rückgabefeld, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;orderNo &amp;middot; Bestell-Nummer&lt;/li&gt;   &lt;li&gt;isbn &amp;middot; ISBN&lt;/li&gt;   &lt;li&gt;ean &amp;middot; EAN&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to &#39;orderNo&#39;]
 **show_price** | **int**| Übermittlung des Preises, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;0 &amp;middot; nein&lt;/li&gt;   &lt;li&gt;1 &amp;middot; ja&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to 0]
 **show_stock** | **int**| Übermittlung des Bestands, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;0 &amp;middot; nein&lt;/li&gt;   &lt;li&gt;1 &amp;middot; ja&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to 0]
 **media_type** | **int**| Einschränkung nach Medientyp, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;0 &amp;middot; Bücher&lt;/li&gt;   &lt;li&gt;1 &amp;middot; Filme&lt;/li&gt;   &lt;li&gt;2 &amp;middot; Musik&lt;/li&gt;   &lt;li&gt;3 &amp;middot; Hörbücher&lt;/li&gt;   &lt;li&gt;4 &amp;middot; Spiele&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to n/a]

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

# **article_status_get**
> AuthenticatePost200Response article_status_get(order_no)

Abfragen des Status eines Artikels

Abfragen des Status eines Artikels.

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
    api_instance = booklooker-api-client.ArticleApi(api_client)
    order_no = None # object | Ihre Bestell-Nummer

    try:
        # Abfragen des Status eines Artikels
        api_response = api_instance.article_status_get(order_no)
        print("The response of ArticleApi->article_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_status_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_no** | [**object**](.md)| Ihre Bestell-Nummer | 

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

