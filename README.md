# Main
- Feel free to use this code for whatever you need it for, this read me file will be written as I update this repository, if you are looking for a specific files instructions ctr-F and search for the file name.

# games
- This is for any of the games that i upload, feel free to play them; and if you find any errors please let me know

# Actual code

## Full_bruteforce.py
### limitations
-in order for this script to run, the target computer will _need_ to have SMB running for this method to work

### Basic Instructions
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


## Cookie_bruteforce
### Limitations
- I don't fully know if this will even work on most things, however, i will be keeping it here just in case i need it for later

### Basic Instructions
- you will need a word list, you can find many of the [here](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content)
#### To Run the Script
- find the ip of the target site and add the directory in the format as instrusted in the code
  finding the ip address can be done like this
  ```
  ping <domain>
  ```
  the ip will be embedded after the domain name
