from typing import Union

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import VirtualMachine
from pyVmomi import vim


class CLuster:
    def __init__(self, vmware_object:ClusterComputeResource):
        self.vmware_object = vmware_object
        self._drs_groups = vmware_object.configurationEx.group


    @property
    def drs_groups(self):
        return self._drs_groups

    
    def add_drs_group(self, vmware_obect:VirtualMachine): 
        # TODO: Add ESX managemnt
        spec = self.vmware_object.ConfigSpecEx()
        