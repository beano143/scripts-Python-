# Main
- Feel free to use this code for whatever you need it for, this read me file will be written as I update this repository, if you are looking for a specific files instructions ctr-F and search for the file name.

# Full_bruteforce.py
## limitations
-in order for this script to run, the target computer will _need_ to have SMB running for this method to work

## basic instructions
- you will need to install 'crackmapexec'

  ```
  apt install crackmapexec
  ```
- to get the 'rockyou.txt' file you will need to run
  ```
  gunzip /usr/share/wordlists/rockyou.txt.gz /.
  ```
- The raw "staff.csv" file is a model for how a user list should be formatted.

just import the code and your username list, you will also need a password list, I would suggest the rockyou database, this comes preinstalled on any kali Linux VM,
  gunzip rockyou to your directory and point the script at the file.