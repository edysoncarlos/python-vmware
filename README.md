**VMware vCenter Management with pyVim**

This repository demonstrates a Python script that retrieves information about a virtual machine (VM) from a VMware vCenter server using the pyVim library.

**Prerequisites:**

- Python: Ensure you have Python installed on your system.
- pyVim Library: Install the library using pip:

pip install pyVmomi

VMware vCenter Credentials: Obtain the hostname/IP address, username, and password for your vCenter server.

**How to Use:**

**Update Credentials:**

Replace <VC-HOST> with the hostname or IP address of your vCenter server.
Replace <VC-USER> with your vCenter username.
Replace <VC-PASSWORD> with your vCenter password.
Update <VC-NAME> with the name of the virtual machine you want to query.

**Run the Script: Execute the Python script:**

python vcenter_vm_info.py

**Script Functionality:**

- Connects to vCenter: Establishes a secure connection to the vCenter server using the provided credentials.

- Retrieves VM: Locates the virtual machine by name within the vCenter inventory.

- Prints VM Details: If the VM is found, the script displays information such as:

VM name
Power state (on, off, suspended)
Guest operating system
CPU count
Memory size
Attached disks and their sizes
Network adapters and their MAC addresses

- Disconnects: Closes the connection to vCenter server after execution.

**Security Note:**

Store credentials securely: Avoid storing sensitive credentials like passwords directly in the script. Consider environment variables or configuration files for a more secure approach.
