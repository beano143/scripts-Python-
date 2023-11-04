import os

def boot_game():
    # Replace the path with your Steam installation path if it's different
    steam_path = "C:/Program Files (x86)/Steam"  # Example path for Windows, change it for your system if needed

    # Replace the app ID with the appropriate ID for VRChat on Steam
    vrchat_app_id = "438100"  # Example app ID for VRChat on Steam

    # Construct the command to launch VRChat through Steam
    command = f'"{steam_path}/Steam.exe" -applaunch {vrchat_app_id}'

    # Launch VRChat through Steam
    os.system(command)

def connect():
    from pyrdp import RDPClient

    # Set up the RDP client
    client = RDPClient("hostname_or_ip", username="your_username", password="your_password")

    # Connect to the remote desktop
    client.connect()

    # Perform actions on the remote desktop
    # ...

    # Disconnect from the remote desktop
    client.disconnect()

# Call the functions
boot_game()
connect()
