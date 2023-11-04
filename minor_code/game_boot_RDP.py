import os
import subprocess
from pydrop import RDPClient 

def boot_game():
    # Replace the path with your Steam installation path if it's different
    steam_path = "C:/Program Files (x86)/Steam"  # Example path for Windows, change it for your system if needed

    # Replace the app ID with the appropriate ID for VRChat on Steam
    vrchat_app_id = "438100"  # Example app ID for VRChat on Steam

    # Construct the command to launch VRChat through Steam
    command = f'"{steam_path}/Steam.exe" -applaunch {vrchat_app_id}'

    # Launch VRChat through Steam
    os.system(command)

def find_from_mac(mac):
    cmd = ["ping", mac, "-c", "1"]
    ip_out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ip_out = ip_out.strip().split("\n")
    # gets thee reply lines 
    for line in ip_out:
        output = line if "from" in line

    # seperates out the ip addr from the output
    output = output.strip().split("from")
    output = output[-1].split(": ")
    print(f"ip from mac addr: {output[0]}")
    return output[0]


def connect(ip_addr, user, passwd):
    from pyrdp import RDPClient

    # Set up the RDP client
    client = RDPClient(ip_addr, username=user, password=passwd)

    # Connect to the remote desktop
    client.connect()
    # Perform actions on the remote desktop
    boot_game()

# defines username pass mac addr
mac_addr = ""
user_name = ""
pass_word = ""

# calls for the functions 
ip = find_ip_from_mac(mac_addr)
connect(ip, user_name, pass_word)
