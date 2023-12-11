# booklooker-api-client.UploadApi

All URIs are relative to *https://api.booklooker.de/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_import_post**](UploadApi.md#file_import_post) | **POST** /file_import | Upload von Angebots- oder Bild-Dateien
[**file_status_get**](UploadApi.md#file_status_get) | **GET** /file_status | Abfragen des Status einer hochgeladenen Angebotsdatei
[**import_status_get**](UploadApi.md#import_status_get) | **GET** /import_status | Abfragen der Anzahl unverarbeiteter hochgeladener Angebotsdateien


# **file_import_post**
> AuthenticatePost200Response file_import_post(file_type=file_type, data_type=data_type, media_type=media_type, format_id=format_id, encoding=encoding, body=body)

Upload von Angebots- oder Bild-Dateien

Upload von Angebots- oder Bild-Dateien.

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
    api_instance = booklooker-api-client.UploadApi(api_client)
    file_type = 'article' # str | Dateityp, mögliche Werte: <ul class=\"defaultList\">   <li>pic &middot; Bild-Datei</li>   <li>article &middot; Angebots-Datei</li> </ul>  (optional) (default to 'article')
    data_type = 1 # int | Art des Uploads, mögliche Werte: <ul class=\"defaultList\">   <li>0 &middot; Hinzufügen/ändern/Löschen</li>   <li>1 &middot; Ersetzen</li>   <li>2 &middot; Löschen</li> </ul>  (optional) (default to 1)
    media_type = 0 # int | Medientyp, mögliche Werte: <ul class=\"defaultList\">   <li>0 &middot; Bücher</li>   <li>1 &middot; Filme</li>   <li>2 &middot; Musik</li>   <li>3 &middot; Hörbücher</li>   <li>4 &middot; Spiele</li> </ul>  (optional) (default to 0)
    format_id = n/a (Es wird das Format des letzten Uploads verwendet.) # int | Interne ID des Formats, legt Feld-Reihenfolge und Text-Trenner fest. Für das booklooker-Format verwenden Sie bitte den Wert <q>1</q>, für mehr Informationen wenden Sie sich bitte an daten@booklooker.de  (optional) (default to n/a (Es wird das Format des letzten Uploads verwendet.))
    encoding = 'n/a (Es wird das Encoding des letzten Uploads verwendet.)' # str | Character Encoding der Datei (wenn nicht ISO8859-1 / Latin1), mögliche Werte: <ul class=\"defaultList\">   <li>IBMPC/CR (= CP437)</li>   <li>macintosh (= Mac OS Roman)</li>   <li>UTF-8</li> </ul>  (optional) (default to 'n/a (Es wird das Encoding des letzten Uploads verwendet.)')
    body = None # bytearray | <p>   Die hochzuladende Datei. </p> <p>   Ihre Angebotsdatei können Sie entweder als Textdatei oder als komprimiertes ZIP-Archiv übergeben.   Standardmäßig müssen die Textdateien in der Kodierung <q>ISO 8859-1</q> vorliegen.   Wenn Ihre Daten in einer anderen Kodierung, bspw. <q>UTF-8</q> vorliegen,   verwenden Sie sich bitte den Parameter <q>encoding</q>. </p> <p>   Bild-Dateien müssen als ZIP-Archiv übergeben werden.   Weitere Hinweise finden Sie auf der Seite zum   <a href=\"https://www.booklooker.de/app/priv/upload/upload_pic.php\">manuellen Hochladen</a>.   Die hochgeladenen Dateien werden in der Reihenfolge des Uploads verarbeitet. </p> <p>   Maximale Dateigröße: 80 MB. </p>  (optional)

    try:
        # Upload von Angebots- oder Bild-Dateien
        api_response = api_instance.file_import_post(file_type=file_type, data_type=data_type, media_type=media_type, format_id=format_id, encoding=encoding, body=body)
        print("The response of UploadApi->file_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->file_import_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_type** | **str**| Dateityp, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;pic &amp;middot; Bild-Datei&lt;/li&gt;   &lt;li&gt;article &amp;middot; Angebots-Datei&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to &#39;article&#39;]
 **data_type** | **int**| Art des Uploads, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;0 &amp;middot; Hinzufügen/ändern/Löschen&lt;/li&gt;   &lt;li&gt;1 &amp;middot; Ersetzen&lt;/li&gt;   &lt;li&gt;2 &amp;middot; Löschen&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to 1]
 **media_type** | **int**| Medientyp, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;0 &amp;middot; Bücher&lt;/li&gt;   &lt;li&gt;1 &amp;middot; Filme&lt;/li&gt;   &lt;li&gt;2 &amp;middot; Musik&lt;/li&gt;   &lt;li&gt;3 &amp;middot; Hörbücher&lt;/li&gt;   &lt;li&gt;4 &amp;middot; Spiele&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to 0]
 **format_id** | **int**| Interne ID des Formats, legt Feld-Reihenfolge und Text-Trenner fest. Für das booklooker-Format verwenden Sie bitte den Wert &lt;q&gt;1&lt;/q&gt;, für mehr Informationen wenden Sie sich bitte an daten@booklooker.de  | [optional] [default to n/a (Es wird das Format des letzten Uploads verwendet.)]
 **encoding** | **str**| Character Encoding der Datei (wenn nicht ISO8859-1 / Latin1), mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;IBMPC/CR (&#x3D; CP437)&lt;/li&gt;   &lt;li&gt;macintosh (&#x3D; Mac OS Roman)&lt;/li&gt;   &lt;li&gt;UTF-8&lt;/li&gt; &lt;/ul&gt;  | [optional] [default to &#39;n/a (Es wird das Encoding des letzten Uploads verwendet.)&#39;]
 **body** | **bytearray**| &lt;p&gt;   Die hochzuladende Datei. &lt;/p&gt; &lt;p&gt;   Ihre Angebotsdatei können Sie entweder als Textdatei oder als komprimiertes ZIP-Archiv übergeben.   Standardmäßig müssen die Textdateien in der Kodierung &lt;q&gt;ISO 8859-1&lt;/q&gt; vorliegen.   Wenn Ihre Daten in einer anderen Kodierung, bspw. &lt;q&gt;UTF-8&lt;/q&gt; vorliegen,   verwenden Sie sich bitte den Parameter &lt;q&gt;encoding&lt;/q&gt;. &lt;/p&gt; &lt;p&gt;   Bild-Dateien müssen als ZIP-Archiv übergeben werden.   Weitere Hinweise finden Sie auf der Seite zum   &lt;a href&#x3D;\&quot;https://www.booklooker.de/app/priv/upload/upload_pic.php\&quot;&gt;manuellen Hochladen&lt;/a&gt;.   Die hochgeladenen Dateien werden in der Reihenfolge des Uploads verarbeitet. &lt;/p&gt; &lt;p&gt;   Maximale Dateigröße: 80 MB. &lt;/p&gt;  | [optional] 

### Return type

[**AuthenticatePost200Response**](AuthenticatePost200Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_status_get**
> AuthenticatePost200Response file_status_get(filename)

Abfragen des Status einer hochgeladenen Angebotsdatei

Abfragen des Status einer hochgeladenen Angebotsdatei

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
    api_instance = booklooker-api-client.UploadApi(api_client)
    filename = 'filename_example' # str | Name der hochgeladenen Datei. Existieren mehrere hochgeladene Dateien mit diesem Namen, bezieht sich der zurückgegebene Wert auf die zuletzt hochgeladene Datei. 

    try:
        # Abfragen des Status einer hochgeladenen Angebotsdatei
        api_response = api_instance.file_status_get(filename)
        print("The response of UploadApi->file_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->file_status_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Name der hochgeladenen Datei. Existieren mehrere hochgeladene Dateien mit diesem Namen, bezieht sich der zurückgegebene Wert auf die zuletzt hochgeladene Datei.  | 

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

# **import_status_get**
> AuthenticatePost200Response import_status_get()

Abfragen der Anzahl unverarbeiteter hochgeladener Angebotsdateien

Abfragen der Anzahl unverarbeiteter hochgeladener Angebotsdateien.

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
    api_instance = booklooker-api-client.UploadApi(api_client)

    try:
        # Abfragen der Anzahl unverarbeiteter hochgeladener Angebotsdateien
        api_response = api_instance.import_status_get()
        print("The response of UploadApi->import_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->import_status_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

