import configparser

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
    config = configparser.ConfigParser()
    config.read('config.ini')
    vcenter_ip = config['vcenter']['ip']
    vcenter_user = config['vcenter']['user']
    vcenter_password = config['vcenter']['password']
    return vcenter_ip, vcenter_user, vcenter_password
