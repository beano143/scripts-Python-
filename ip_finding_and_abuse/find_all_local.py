import subprocess
import ipaddress

def get_local():
        # creates local variables for creating a final full list
        list_returned = []
        list_split = []
        try:
                local = subprocess.run(["ip", "addr"], stdout=subprocess.PIPE, text=True, check=True)
                list_local = local.stdout.strip().split('\n') # cleans output 
                for obj in list_local:
                        if "inet" in obj and ":" not in obj and "127.0.0.1" not in obj: # removes anything thats not an ip address
                                list_returned.append(obj)

                for obj in list_returned:
                        ip_addr = obj.split("inet ")
                        ip_addr = ip_addr[1].split("/")
                        list_split.append(ip_addr[0])

                return list_split

        except subprocess.CalledProcessError as e:
                print(f"{e}")


def get_network(base):
        active = []
        network = base.split(".")
        network = f"{network[0]}.{network[1]}." # gets the majority of your network (the main subnet block) 
        for i in range(228, 229):
                for b in range(1, 255):
                        if b != 254:
                                ip = f"{network}{i}.{b}"
                                try:
                                        subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True) # scans with a single ping
                                        active.append(ip)

                                except subprocess.CalledProcessError:
                                        pass
        if active:
                return active
        else:
                active = []
                return active


list_l = get_local()

list_f = []
for i in range(len(list_l)):
        list_f.append(get_network(list_l[i]))
        print(list_f)
