# booklooker-api-client.OrderApi

All URIs are relative to *https://api.booklooker.de/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_cancel_put**](OrderApi.md#order_cancel_put) | **PUT** /order_cancel | Stornieren einer kompletten Bestellung
[**order_get**](OrderApi.md#order_get) | **GET** /order | Download aller Bestellungen eines bestimmten Tages
[**order_item_cancel_put**](OrderApi.md#order_item_cancel_put) | **PUT** /order_item_cancel | Stornieren der Bestellung eines Einzelartikels
[**order_message_put**](OrderApi.md#order_message_put) | **PUT** /order_message | Versand einer Nachricht an den Kunden
[**order_status_put**](OrderApi.md#order_status_put) | **PUT** /order_status | Setzen des Status einer Bestellung


# **order_cancel_put**
> AuthenticatePost200Response order_cancel_put(order_id)

Stornieren einer kompletten Bestellung

Stornieren einer kompletten Bestellung

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
    api_instance = booklooker-api-client.OrderApi(api_client)
    order_id = None # object | Interne booklooker orderId der Bestellung, wird von der Schnittstelle <q>order</q> zurückgeliefert. 

    try:
        # Stornieren einer kompletten Bestellung
        api_response = api_instance.order_cancel_put(order_id)
        print("The response of OrderApi->order_cancel_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_cancel_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**object**](.md)| Interne booklooker orderId der Bestellung, wird von der Schnittstelle &lt;q&gt;order&lt;/q&gt; zurückgeliefert.  | 

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

# **order_get**
> AuthenticatePost200Response order_get(order_id, var_date=var_date, date_from=date_from, date_to=date_to)

Download aller Bestellungen eines bestimmten Tages

Download aller Bestellungen eines bestimmten Tages bzw. Zeitintervalls.

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
    api_instance = booklooker-api-client.OrderApi(api_client)
    order_id = 56 # int | Interne booklooker orderId der Bestellung, wird von der Schnittstelle <q>order</q> zurückgeliefert. 
    var_date = 'var_date_example' # str | Datum, zu dem Bestellungen angefordert werden, im Format YYYY-MM-DD. Wenn übergeben, hat dieser Parameter Vorrang vor dateFrom und dateTo  (optional)
    date_from = 'date_from_example' # str | Start-Datum, zu dem Bestellungen angefordert werden, im Format YYYY-MM-DD (optional)
    date_to = 'date_to_example' # str | End-Datum, zu dem Bestellungen angefordert werden, im Format YYYY-MM-DD (optional)

    try:
        # Download aller Bestellungen eines bestimmten Tages
        api_response = api_instance.order_get(order_id, var_date=var_date, date_from=date_from, date_to=date_to)
        print("The response of OrderApi->order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Interne booklooker orderId der Bestellung, wird von der Schnittstelle &lt;q&gt;order&lt;/q&gt; zurückgeliefert.  | 
 **var_date** | **str**| Datum, zu dem Bestellungen angefordert werden, im Format YYYY-MM-DD. Wenn übergeben, hat dieser Parameter Vorrang vor dateFrom und dateTo  | [optional] 
 **date_from** | **str**| Start-Datum, zu dem Bestellungen angefordert werden, im Format YYYY-MM-DD | [optional] 
 **date_to** | **str**| End-Datum, zu dem Bestellungen angefordert werden, im Format YYYY-MM-DD | [optional] 

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

# **order_item_cancel_put**
> AuthenticatePost200Response order_item_cancel_put(order_id, media_type)

Stornieren der Bestellung eines Einzelartikels

Stornieren der Bestellung eines Einzelartikels

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
    api_instance = booklooker-api-client.OrderApi(api_client)
    order_id = None # object | Interne booklooker orderId der Bestellung, wird von der Schnittstelle <q>order</q> zurückgeliefert. 
    media_type = 56 # int | Medientyp, mögliche Werte, mögliche Werte: <ul class=\"defaultList\">   <li>0 &middot; Bücher</li>   <li>1 &middot; Filme</li>   <li>2 &middot; Musik</li>   <li>3 &middot; Hörbücher</li>   <li>4 &middot; Spiele</li> </ul> 

    try:
        # Stornieren der Bestellung eines Einzelartikels
        api_response = api_instance.order_item_cancel_put(order_id, media_type)
        print("The response of OrderApi->order_item_cancel_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_item_cancel_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**object**](.md)| Interne booklooker orderId der Bestellung, wird von der Schnittstelle &lt;q&gt;order&lt;/q&gt; zurückgeliefert.  | 
 **media_type** | **int**| Medientyp, mögliche Werte, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;0 &amp;middot; Bücher&lt;/li&gt;   &lt;li&gt;1 &amp;middot; Filme&lt;/li&gt;   &lt;li&gt;2 &amp;middot; Musik&lt;/li&gt;   &lt;li&gt;3 &amp;middot; Hörbücher&lt;/li&gt;   &lt;li&gt;4 &amp;middot; Spiele&lt;/li&gt; &lt;/ul&gt;  | 

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

# **order_message_put**
> AuthenticatePost200Response order_message_put(order_id, message_type, additional_text=additional_text)

Versand einer Nachricht an den Kunden

Versand einer Nachricht an den Kunden.

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
    api_instance = booklooker-api-client.OrderApi(api_client)
    order_id = None # object | Interne booklooker orderId der Bestellung, wird von der Schnittstelle <q>order</q> zurückgeliefert. 
    message_type = 'message_type_example' # str | Typ der Nachricht, mögliche Werte: <ul class=\"defaultList\">   <li>PAYMENT_INFORMATION &middot; Zahlungsinformationen senden</li>   <li>PAYMENT_REMINDER &middot; Zahlungserinnerung senden</li>   <li>SHIPPING_NOTICE &middot; Versandmitteilung senden</li> </ul> 
    additional_text = 'additional_text_example' # str | Zusätzlicher Text, der in der Nachricht aufgenommen wird (optional)

    try:
        # Versand einer Nachricht an den Kunden
        api_response = api_instance.order_message_put(order_id, message_type, additional_text=additional_text)
        print("The response of OrderApi->order_message_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_message_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**object**](.md)| Interne booklooker orderId der Bestellung, wird von der Schnittstelle &lt;q&gt;order&lt;/q&gt; zurückgeliefert.  | 
 **message_type** | **str**| Typ der Nachricht, mögliche Werte: &lt;ul class&#x3D;\&quot;defaultList\&quot;&gt;   &lt;li&gt;PAYMENT_INFORMATION &amp;middot; Zahlungsinformationen senden&lt;/li&gt;   &lt;li&gt;PAYMENT_REMINDER &amp;middot; Zahlungserinnerung senden&lt;/li&gt;   &lt;li&gt;SHIPPING_NOTICE &amp;middot; Versandmitteilung senden&lt;/li&gt; &lt;/ul&gt;  | 
 **additional_text** | **str**| Zusätzlicher Text, der in der Nachricht aufgenommen wird | [optional] 

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

# **order_status_put**
> AuthenticatePost200Response order_status_put(order_id, status)

Setzen des Status einer Bestellung

Setzen des Status einer Bestellung.

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
    api_instance = booklooker-api-client.OrderApi(api_client)
    order_id = None # object | Interne booklooker orderId der Bestellung, wird von der Schnittstelle <q>order</q> zurückgeliefert. 
    status = 'status_example' # str | <p>Neuer Status der Bestellung, mögliche Werte:</p>  <h4>Bei Verkäufen sind die folgenden Status möglich:</h4>  <table class=\"table-padding-5 grid\">   <tr><th>Rückgabewert</th><th>Bedeutung</th></tr>   <tr><td>WAITING_FOR_PAYMENT</td><td>Zahlung offen</td></tr>   <tr><td>READY_FOR_SHIPMENT</td><td>fertig zum Versand</td></tr>   <tr><td>SHIPPED_WAITING_FOR_PAYMENT</td><td>versendet, warte auf Zahlung</td></tr>   <tr><td>SHIPPED_AND_PAID</td><td>versendet &amp; bezahlt</td></tr>   <tr><td>BUYER_NO_REACTION</td><td>Kunde reagiert nicht</td></tr>   <tr><td>CANCELED</td><td>storniert</td></tr> </table>              <p>   <strong>Achtung:</strong> Das Setzen des Status <strong>CANCELED</strong>   ist nicht gleichbedeutend mit dem Aufruf der Funktion   <q>order_item_cancel</q>. Der Status <strong>CANCELED</strong> dient lediglich der   Eigenorganisation des Verkäufers. Um eine Bestellung so zu   stornieren, dass keine Provision anfällt, *muss*   <q>order_item_cancel</q> aufgerufen werden. </p>  <h4>Bei Käufen sind die folgenden Status möglich:</h4>  <table class=\"table-padding-5 grid\">   <tr><th>Rückgabewert</th><th>Bedeutung</th></tr>   <tr><td>TO_BE_PAID</td><td>Zahlung offen</td></tr>   <tr><td>WAITING_FOR_SHIPMENT</td><td>warte auf Lieferung</td></tr>   <tr><td>PAID_WAITING_FOR_SHIPMENT</td><td>bezahlt, warte auf Lieferung</td></tr>   <tr><td>RECEIVED_AND_PAID</td><td>erhalten &amp; bezahlt </td></tr>   <tr><td>VENDOR_NO_REACTION</td><td>Verkäufer reagiert nicht</td></tr>   <tr><td>CANCELED</td><td>storniert</td></tr> </table> 

    try:
        # Setzen des Status einer Bestellung
        api_response = api_instance.order_status_put(order_id, status)
        print("The response of OrderApi->order_status_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_status_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**object**](.md)| Interne booklooker orderId der Bestellung, wird von der Schnittstelle &lt;q&gt;order&lt;/q&gt; zurückgeliefert.  | 
 **status** | **str**| &lt;p&gt;Neuer Status der Bestellung, mögliche Werte:&lt;/p&gt;  &lt;h4&gt;Bei Verkäufen sind die folgenden Status möglich:&lt;/h4&gt;  &lt;table class&#x3D;\&quot;table-padding-5 grid\&quot;&gt;   &lt;tr&gt;&lt;th&gt;Rückgabewert&lt;/th&gt;&lt;th&gt;Bedeutung&lt;/th&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;WAITING_FOR_PAYMENT&lt;/td&gt;&lt;td&gt;Zahlung offen&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;READY_FOR_SHIPMENT&lt;/td&gt;&lt;td&gt;fertig zum Versand&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;SHIPPED_WAITING_FOR_PAYMENT&lt;/td&gt;&lt;td&gt;versendet, warte auf Zahlung&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;SHIPPED_AND_PAID&lt;/td&gt;&lt;td&gt;versendet &amp;amp; bezahlt&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;BUYER_NO_REACTION&lt;/td&gt;&lt;td&gt;Kunde reagiert nicht&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;CANCELED&lt;/td&gt;&lt;td&gt;storniert&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt;              &lt;p&gt;   &lt;strong&gt;Achtung:&lt;/strong&gt; Das Setzen des Status &lt;strong&gt;CANCELED&lt;/strong&gt;   ist nicht gleichbedeutend mit dem Aufruf der Funktion   &lt;q&gt;order_item_cancel&lt;/q&gt;. Der Status &lt;strong&gt;CANCELED&lt;/strong&gt; dient lediglich der   Eigenorganisation des Verkäufers. Um eine Bestellung so zu   stornieren, dass keine Provision anfällt, *muss*   &lt;q&gt;order_item_cancel&lt;/q&gt; aufgerufen werden. &lt;/p&gt;  &lt;h4&gt;Bei Käufen sind die folgenden Status möglich:&lt;/h4&gt;  &lt;table class&#x3D;\&quot;table-padding-5 grid\&quot;&gt;   &lt;tr&gt;&lt;th&gt;Rückgabewert&lt;/th&gt;&lt;th&gt;Bedeutung&lt;/th&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;TO_BE_PAID&lt;/td&gt;&lt;td&gt;Zahlung offen&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;WAITING_FOR_SHIPMENT&lt;/td&gt;&lt;td&gt;warte auf Lieferung&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;PAID_WAITING_FOR_SHIPMENT&lt;/td&gt;&lt;td&gt;bezahlt, warte auf Lieferung&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;RECEIVED_AND_PAID&lt;/td&gt;&lt;td&gt;erhalten &amp;amp; bezahlt &lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;VENDOR_NO_REACTION&lt;/td&gt;&lt;td&gt;Verkäufer reagiert nicht&lt;/td&gt;&lt;/tr&gt;   &lt;tr&gt;&lt;td&gt;CANCELED&lt;/td&gt;&lt;td&gt;storniert&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt;  | 

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

