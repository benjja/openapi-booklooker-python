# coding: utf-8

"""
    booklooker REST API

    <p>   Die <strong>Booklooker REST API</strong> ermöglicht die sichere und einfache Kommunikation mit verschiedenen   Booklooker-Schnittstellen. Es besteht die Möglichkeit, Artikel und Aufträge abzufragen, zu ändern, zu stornieren   etc. Auch der automatische Import neuer oder geänderter Artikel ist ohne Weiteres möglich. </p> <p>   Diese API basiert auf REST. Zur Benutzung führen Sie bitte die folgenden Schritte durch: </p> <ol>   <li>     Sie benötigen Ihren persönlichen <strong>API Key</strong>, diesen erhalten Sie im Bereich     <a href=\"https://www.booklooker.de/app/priv/api_key.php\">Persönliche Daten</a>   </li>   <li>     Benutzen Sie anschließend die Schnittstelle     <a href=\"https://www.booklooker.de/pages/api_authenticate.php\">authenticate</a>     via HTTP&nbsp;POST und Sie erhalten einen <strong>Token</strong>,     welcher für alle folgenden Aufrufe benötigt wird.     Sofern Sie 10&nbsp;Minuten keine Schnittstelle aufrufen,     verfällt der Token und Sie müssen sich erneut authentifizieren.   </li>   <li>     Verwenden Sie eine der unten aufgelisteten Schnittstellen.     Die Beschreibung jeder Schnittstelle enthält die benötigten Parameter und die möglichen Rückgabewerte.   </li> </ol> <p>   Zur Kommunikation können verschiedene Programmiersprachen zum Einsatz kommen. Wir stellen Ihnen hier ein   <a href=\"https://www.booklooker.de/pages/rest_api.php?do=download&filename=booklooker_rest_api.php&path=booklooker_rest_api.php\">Beispiel in PHP</a>   zur Verfügung. </p> <p>   Weiterhin bieten wir hier eine <a href=\"https://www.booklooker.de/download/openapi.yaml\">OpenAPI Spezifikation</a> an.  </p> 

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, ValidationError, field_validator
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

AUTHENTICATEPOST200RESPONSERETURNVALUE_ANY_OF_SCHEMAS = ["int", "str"]

class AuthenticatePost200ResponseReturnValue(BaseModel):
    """
    AuthenticatePost200ResponseReturnValue
    """

    # data type: str
    anyof_schema_1_validator: Optional[StrictStr] = None
    # data type: int
    anyof_schema_2_validator: Optional[StrictInt] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[int, str]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Literal[AUTHENTICATEPOST200RESPONSERETURNVALUE_ANY_OF_SCHEMAS]

    model_config = {
        "validate_assignment": True
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        if v is None:
            return v

        instance = AuthenticatePost200ResponseReturnValue.model_construct()
        error_messages = []
        # validate data type: str
        try:
            instance.anyof_schema_1_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: int
        try:
            instance.anyof_schema_2_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in AuthenticatePost200ResponseReturnValue with anyOf schemas: int, str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        # deserialize data into str
        try:
            # validation
            instance.anyof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_1_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into int
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AuthenticatePost200ResponseReturnValue with anyOf schemas: int, str. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


