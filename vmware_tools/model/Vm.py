from pyVmomi.vim import VirtualMachine
from pyVmomi import vim

# from .utils import 
from ..utils import wait_for_task

class Vm:
    def __init__(self, vmware_vm:VirtualMachine) -> None:
        self.vmware_object = vmware_vm
        self.summary = vmware_vm.summary
        self._numCpu = self.summary.config.numCpu
        self._mem = self.summary.config.memorySizeMB
        self._name = self.vmware_object.name
        self._host_group = self.vmware_object.runtime.host.parent 

    
    @property
    def numCpu(self):
        return self._cpu


    @numCpu.setter
    def numCpu(self, new_cpu_count:int) -> None:
        spec = vim.vm.ConfigSpec()
        spec.numCPUs = new_cpu_count
        task = self.vmware_object.ReconfigVM_Task(spec)
        wait_for_task(object_name=self.name, task=task)
        # task.wait()


    @property
    def memorySizeMB(self):
        return self._mem


    @memorySizeMB.setter
    def  memorySizeMB(self, memory_size_mb:int) -> None:
        spec = vim.vm.ConfigSpec()
        spec.memoryMB = memory_size_mb
        task = self.vmware_object.Reconfigure(spec)
        wait_for_task(task=task)


    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, new_name:str):
        self.vmware_object.rename(new_name)


    @property
    def host_group(self):
        return self._host_group

    def get_tags(self):
        pass

    def get_custom_attributs(self):
        pass
