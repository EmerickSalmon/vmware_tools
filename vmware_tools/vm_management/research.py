"""
Search VM 
"""

from typing import Union
from pyVmomi import vim
from pyVmomi.vim import ClusterComputeResource, Datacenter, VirtualMachine


def search_by_dns(vm_dns_name:str, search_in_entity: Union(ClusterComputeResource, Datacenter, None)) -> VirtualMachine:
    #TODO: Replace None by searchIndex
    if not vm_dns_name:
        raise Exception(f"vm_dns_name is None")
    if vm_dns_name is not str:
        raise Exception(f"Parameter vm_dns_name is not str")
    
    # Search the VM in entity
    try:
        vm = search_in_entity.FindByDnsName(vm_dns_name, True)
        return vm
    except vim.fault.NotFound:
        raise(f"Vm {vm_dns_name} not found")






