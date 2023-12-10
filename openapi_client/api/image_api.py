# coding: utf-8

"""
    booklooker REST API

    <p>   Die <strong>Booklooker REST API</strong> ermöglicht die sichere und einfache Kommunikation mit verschiedenen   Booklooker-Schnittstellen. Es besteht die Möglichkeit, Artikel und Aufträge abzufragen, zu ändern, zu stornieren   etc. Auch der automatische Import neuer oder geänderter Artikel ist ohne Weiteres möglich. </p> <p>   Diese API basiert auf REST. Zur Benutzung führen Sie bitte die folgenden Schritte durch: </p> <ol>   <li>     Sie benötigen Ihren persönlichen <strong>API Key</strong>, diesen erhalten Sie im Bereich     <a href=\"https://www.booklooker.de/app/priv/api_key.php\">Persönliche Daten</a>   </li>   <li>     Benutzen Sie anschließend die Schnittstelle     <a href=\"https://www.booklooker.de/pages/api_authenticate.php\">authenticate</a>     via HTTP&nbsp;POST und Sie erhalten einen <strong>Token</strong>,     welcher für alle folgenden Aufrufe benötigt wird.     Sofern Sie 10&nbsp;Minuten keine Schnittstelle aufrufen,     verfällt der Token und Sie müssen sich erneut authentifizieren.   </li>   <li>     Verwenden Sie eine der unten aufgelisteten Schnittstellen.     Die Beschreibung jeder Schnittstelle enthält die benötigten Parameter und die möglichen Rückgabewerte.   </li> </ol> <p>   Zur Kommunikation können verschiedene Programmiersprachen zum Einsatz kommen. Wir stellen Ihnen hier ein   <a href=\"https://www.booklooker.de/pages/rest_api.php?do=download&filename=booklooker_rest_api.php&path=booklooker_rest_api.php\">Beispiel in PHP</a>   zur Verfügung. </p> <p>   Weiterhin bieten wir hier eine <a href=\"https://www.booklooker.de/download/openapi.yaml\">OpenAPI Spezifikation</a> an.  </p> 

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictInt

from typing import Any, Optional

from openapi_client.models.authenticate_post200_response import AuthenticatePost200Response

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class ImageApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def image_delete(
        self,
        order_no: Annotated[Any, Field(description="Ihre Bestell-Nummer")],
        position: Annotated[Optional[StrictInt], Field(description="<p>   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. </p> <p>   <strong>Achtung:</strong> Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position <q>2</q> gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. </p> ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AuthenticatePost200Response:
        """Einzelne oder alle Bilder eines Artikels löschen

        Einzelne oder alle Bilder eines Artikels löschen.

        :param order_no: Ihre Bestell-Nummer (required)
        :type order_no: object
        :param position: <p>   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. </p> <p>   <strong>Achtung:</strong> Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position <q>2</q> gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. </p> 
        :type position: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._image_delete_serialize(
            order_no=order_no,
            position=position,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuthenticatePost200Response"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def image_delete_with_http_info(
        self,
        order_no: Annotated[Any, Field(description="Ihre Bestell-Nummer")],
        position: Annotated[Optional[StrictInt], Field(description="<p>   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. </p> <p>   <strong>Achtung:</strong> Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position <q>2</q> gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. </p> ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AuthenticatePost200Response]:
        """Einzelne oder alle Bilder eines Artikels löschen

        Einzelne oder alle Bilder eines Artikels löschen.

        :param order_no: Ihre Bestell-Nummer (required)
        :type order_no: object
        :param position: <p>   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. </p> <p>   <strong>Achtung:</strong> Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position <q>2</q> gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. </p> 
        :type position: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._image_delete_serialize(
            order_no=order_no,
            position=position,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuthenticatePost200Response"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def image_delete_without_preload_content(
        self,
        order_no: Annotated[Any, Field(description="Ihre Bestell-Nummer")],
        position: Annotated[Optional[StrictInt], Field(description="<p>   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. </p> <p>   <strong>Achtung:</strong> Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position <q>2</q> gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. </p> ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Einzelne oder alle Bilder eines Artikels löschen

        Einzelne oder alle Bilder eines Artikels löschen.

        :param order_no: Ihre Bestell-Nummer (required)
        :type order_no: object
        :param position: <p>   Position des Bildes, falls nicht vorhanden werden alle (!) Bilder des Artikels gelöscht. </p> <p>   <strong>Achtung:</strong> Beim Löschen mehrerer (aber nicht aller) Bilder eines Artikels muss   berücksichtigt werden, dass sich beim Aufruf dieser Schnittstelle die Position der nachfolgenden Bilder   ändert: Wenn ein Artikel z.B. 5 Bilder hat und das Bild an Position <q>2</q> gelöscht wird,   ändert sich die Position der Bilder 3, 4, 5 in 2, 3, 4. </p> 
        :type position: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._image_delete_serialize(
            order_no=order_no,
            position=position,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuthenticatePost200Response"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _image_delete_serialize(
        self,
        order_no,
        position,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if order_no is not None:
            
            _query_params.append(('orderNo', order_no))
            
        if position is not None:
            
            _query_params.append(('position', position))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'tokenAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/image',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


