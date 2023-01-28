import unittest
import os

from unittest.mock import Mock
from .connection import connect_to_vcenter



def mock_smart_connect():
    mock_connection = Mock()
    mock_connection.content.__str__ = Mock(return_value="Mocked vCenter Content")
    return mock_connection

class TestConnectToVcenter(unittest.TestCase):
    address = "1.2.3.4"
    username = "vcenter_username"
    password = "vcenter_password"

    def __init__(self, *args, **kwargs):
        super(TestConnectToVcenter, self).__init__(*args, **kwargs)
        os.environ["MY_VCENTER_ADDRESS"] = self.address 
        os.environ["MY_VCENTER_USERNAME"] = self.username
        os.environ["MY_VCENTER_PASSWORD"] = self.password        

    def test_connect_to_vcenter(self):
        with unittest.mock.patch('vmware_tools.connection.connection.connect', return_value=mock_smart_connect()) as mock_connect:
            _ = connect_to_vcenter('my_vcenter')
            mock_connect.assert_called_with(self.address, self.username, self.password)


if __name__ == '__main__':
    unittest.main()