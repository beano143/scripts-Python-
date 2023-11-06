import paramiko
import time

# Define the IP address, username, and password for the routers
router_ip = '192.168.1.1'  # Replace with the actual IP address
username = 'your_username'  # Replace with the actual username
password = 'your_password'  # Replace with the actual password

# Define the command to reset the router to factory default settings
reset_command = 'write erase\n'

# Establish an SSH connection to the router
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(router_ip, username=username, password=password, allow_agent=False, look_for_keys=False)

# Send the reset command and wait for the process to complete
ssh_shell = ssh_client.invoke_shell()
ssh_shell.send(reset_command)
time.sleep(5)  # Adjust the delay as needed

# Confirm the reset by sending 'y' or any confirmation input
ssh_shell.send('y\n')  # Modify if the confirmation input is different
time.sleep(5)  # Adjust the delay as needed

# Close the SSH connection
ssh_client.close()

print("Router reset to factory default settings.")
