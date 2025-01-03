from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import atexit

def get_vm_by_name(content, vm_name):
    """
    Retrieve a virtual machine by name.
    """
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            vm_folder = child.vmFolder
            vm_list = vm_folder.childEntity
            for vm in vm_list:
                if vm.name == vm_name:
                    return vm
    return None

def print_vm_details(vm):
    """
    Print details of the virtual machine.
    """
    print(f"VM Name: {vm.name}")
    print(f"Power State: {vm.runtime.powerState}")
    print(f"Guest OS: {vm.config.guestFullName}")
    print(f"CPU Count: {vm.config.hardware.numCPU}")
    print(f"Memory Size (MB): {vm.config.hardware.memoryMB}")
    print("Disks:")
    for device in vm.config.hardware.device:
        if isinstance(device, vim.vm.device.VirtualDisk):
            print(f"  - {device.deviceInfo.label}: {device.capacityInKB // 1024} MB")
    print("Network Adapters:")
    for device in vm.config.hardware.device:
        if isinstance(device, vim.vm.device.VirtualEthernetCard):
            print(f"  - {device.deviceInfo.label}: {device.macAddress}")

def main():
    # Replace these variables with your vCenter details
    vc_host = "VC-HOST"
    vc_user = "<VC-USER>"
    vc_password = "<VC-PASSWORD>"
    vm_name = "<VC-NAME>"

    # Connect to vCenter
    print("Connecting to vCenter...")
    si = SmartConnect(host=vc_host, user=vc_user, pwd=vc_password, sslContext=context)
    atexit.register(Disconnect, si)

    content = si.RetrieveContent()

    # Get VM
    vm = get_vm_by_name(content, vm_name)
    if not vm:
        print(f"VM {vm_name} not found.")
        return

    # Print VM details
    print_vm_details(vm)

if __name__ == "__main__":
    main()
