import os

def get_vcenter_credentials(vcenter_name:str) -> tuple[str, str, str]:
    """
    Import vcenter IP user and password from config file.

    !! This is not recommend for production use !!
    Create your own fonction to replace this one
    TODO: Add exemple in configuration

    Example of vcenter config file
    [vcenter]
    ip = 192.168.1.100
    user = admin
    password = admin

    """
    try:
        vcenter_ip = os.environ["MY_VCENTER_ADDRESS"]
        vcenter_user = os.environ["MY_VCENTER_USERNAME"]
        vcenter_password = os.environ["MY_VCENTER_PASSWORD"]
        return vcenter_ip, vcenter_user, vcenter_password
    except KeyError as e:
        raise ValueError(f"Missing environment variable: {e}")
