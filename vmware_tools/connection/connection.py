import atexit

from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect

from . import logger
from .configuration import get_vcenter_credentials

def connect_to_vcenter(vcenter_name:str):
    vcenter_connestion_parameters = get_vcenter_credentials(vcenter_name)
    service_instance = connect(*vcenter_connestion_parameters)
    # Get the content object
    content = service_instance.RetrieveContent()
    # Register the disconnect function to be called at exit
    atexit.register(Disconnect, service_instance)
    return content


def connect(vcenter_ip:str, vcenter_user:str, vcenter_password:str):
    try:
        # Connect to the vCenter server
        service_instance = SmartConnect(
            host=vcenter_ip,
            user=vcenter_user,
            pwd=vcenter_password,
            port=443
        )
    except vim.fault.InvalidLogin:
        logger.error("Error: Invalid login credentials")
        return None
    except Exception as e:
        logger.error("Error: Unable to connect to vCenter")
        logger.error(e)
        return None
    return service_instance