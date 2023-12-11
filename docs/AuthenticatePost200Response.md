# AuthenticatePost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**return_value** | [**AuthenticatePost200ResponseReturnValue**](AuthenticatePost200ResponseReturnValue.md) |  | [optional] 

## Example

```python
from booklooker-api-client.models.authenticate_post200_response import AuthenticatePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatePost200Response from a JSON string
authenticate_post200_response_instance = AuthenticatePost200Response.from_json(json)
# print the JSON string representation of the object
print AuthenticatePost200Response.to_json()

# convert the object into a dict
authenticate_post200_response_dict = authenticate_post200_response_instance.to_dict()
# create an instance of AuthenticatePost200Response from a dict
authenticate_post200_response_form_dict = authenticate_post200_response.from_dict(authenticate_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


