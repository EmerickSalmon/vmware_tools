import unittest
import os

from unittest.mock import Mock
from unittest.mock import MagicMock
from .connection import connect_to_vcenter


def mock_smart_connect(username, password, host):
    # Création d'un objet mock pour simuler une connexion réussie
    mock_connection = MagicMock()
    mock_connection.content.sessionManager.currentSession.name = username
    return mock_connection

class TestConnectToVcenter(unittest.TestCase):
    address = "1.2.3.4"
    username = "vcenter_username"
    password = "vcenter_password"

    def __init__(self):
        os.environ["MY_VCENTER_ADDRESS"] = self.address
        os.environ["MY_VCENTER_USERNAME"] = self.username
        os.environ["MY_VCENTER_PASSWORD"] = self.password        

    def test_connect_to_vcenter(self):
        # patch the `connect` function to return the mock object
        connexion_mock = mock_smart_connect()
        with unittest.mock.patch('pyVim.connect.SmartConnect', return_value=connexion_mock) as mock_connect:
            content = connect_to_vcenter()
            mock_connect.assert_called_once()
            assert content.sessionManager.currentSession.name == self.username

            self.assertEqual(content, "Mocked vCenter Content")

if __name__ == '__main__':
    unittest.main()