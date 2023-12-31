# coding: utf-8

"""
    booklooker REST API

    <p>   Die <strong>Booklooker REST API</strong> ermöglicht die sichere und einfache Kommunikation mit verschiedenen   Booklooker-Schnittstellen. Es besteht die Möglichkeit, Artikel und Aufträge abzufragen, zu ändern, zu stornieren   etc. Auch der automatische Import neuer oder geänderter Artikel ist ohne Weiteres möglich. </p> <p>   Diese API basiert auf REST. Zur Benutzung führen Sie bitte die folgenden Schritte durch: </p> <ol>   <li>     Sie benötigen Ihren persönlichen <strong>API Key</strong>, diesen erhalten Sie im Bereich     <a href=\"https://www.booklooker.de/app/priv/api_key.php\">Persönliche Daten</a>   </li>   <li>     Benutzen Sie anschließend die Schnittstelle     <a href=\"https://www.booklooker.de/pages/api_authenticate.php\">authenticate</a>     via HTTP&nbsp;POST und Sie erhalten einen <strong>Token</strong>,     welcher für alle folgenden Aufrufe benötigt wird.     Sofern Sie 10&nbsp;Minuten keine Schnittstelle aufrufen,     verfällt der Token und Sie müssen sich erneut authentifizieren.   </li>   <li>     Verwenden Sie eine der unten aufgelisteten Schnittstellen.     Die Beschreibung jeder Schnittstelle enthält die benötigten Parameter und die möglichen Rückgabewerte.   </li> </ol> <p>   Zur Kommunikation können verschiedene Programmiersprachen zum Einsatz kommen. Wir stellen Ihnen hier ein   <a href=\"https://www.booklooker.de/pages/rest_api.php?do=download&filename=booklooker_rest_api.php&path=booklooker_rest_api.php\">Beispiel in PHP</a>   zur Verfügung. </p> <p>   Weiterhin bieten wir hier eine <a href=\"https://www.booklooker.de/download/openapi.yaml\">OpenAPI Spezifikation</a> an.  </p> 

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None) -> None:
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None) -> None:
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data.decode('utf-8')
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message

class BadRequestException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(BadRequestException, self).__init__(status, reason, http_resp)

class NotFoundException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(NotFoundException, self).__init__(status, reason, http_resp)


class UnauthorizedException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(UnauthorizedException, self).__init__(status, reason, http_resp)


class ForbiddenException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(ForbiddenException, self).__init__(status, reason, http_resp)


class ServiceException(ApiException):

    def __init__(self, status=None, reason=None, http_resp=None) -> None:
        super(ServiceException, self).__init__(status, reason, http_resp)


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
