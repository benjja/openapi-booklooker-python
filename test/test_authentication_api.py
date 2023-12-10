# coding: utf-8

"""
    booklooker REST API

    <p>   Die <strong>Booklooker REST API</strong> ermöglicht die sichere und einfache Kommunikation mit verschiedenen   Booklooker-Schnittstellen. Es besteht die Möglichkeit, Artikel und Aufträge abzufragen, zu ändern, zu stornieren   etc. Auch der automatische Import neuer oder geänderter Artikel ist ohne Weiteres möglich. </p> <p>   Diese API basiert auf REST. Zur Benutzung führen Sie bitte die folgenden Schritte durch: </p> <ol>   <li>     Sie benötigen Ihren persönlichen <strong>API Key</strong>, diesen erhalten Sie im Bereich     <a href=\"https://www.booklooker.de/app/priv/api_key.php\">Persönliche Daten</a>   </li>   <li>     Benutzen Sie anschließend die Schnittstelle     <a href=\"https://www.booklooker.de/pages/api_authenticate.php\">authenticate</a>     via HTTP&nbsp;POST und Sie erhalten einen <strong>Token</strong>,     welcher für alle folgenden Aufrufe benötigt wird.     Sofern Sie 10&nbsp;Minuten keine Schnittstelle aufrufen,     verfällt der Token und Sie müssen sich erneut authentifizieren.   </li>   <li>     Verwenden Sie eine der unten aufgelisteten Schnittstellen.     Die Beschreibung jeder Schnittstelle enthält die benötigten Parameter und die möglichen Rückgabewerte.   </li> </ol> <p>   Zur Kommunikation können verschiedene Programmiersprachen zum Einsatz kommen. Wir stellen Ihnen hier ein   <a href=\"https://www.booklooker.de/pages/rest_api.php?do=download&filename=booklooker_rest_api.php&path=booklooker_rest_api.php\">Beispiel in PHP</a>   zur Verfügung. </p> <p>   Weiterhin bieten wir hier eine <a href=\"https://www.booklooker.de/download/openapi.yaml\">OpenAPI Spezifikation</a> an.  </p> 

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_authenticate_post(self) -> None:
        """Test case for authenticate_post

        Authentifizierung via API Key
        """
        pass


if __name__ == '__main__':
    unittest.main()
