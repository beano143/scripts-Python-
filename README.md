# Main
- Feel free to use this code for whatever you need it for, this read me file will be written as I update this repository, if you are looking for a specific files instructions ctr-F and search for the file name, once this repo is more fleshed out readmes will be added to their folders, things are still moving so this might not happen for some time.

  -editors note: this is just a tool box mainly for my personl use, so there will be some poor organization

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

## Hydra script blocks
### the hydra file is currently being worked on, it will be done in the next few weeks, I will update as i have code.

## ip finding and abuse
- Note: More will be added
### find all local
- Note: built for linux; if you're running this on a windows system you will need to change the code for a differnt filtering method however the rest will still work
just run the script wait a few seconds and it will return a list of all of the local ip addresses for your subnet (this will however not scan for some sbubnets outside of yours ex: your ip address is '192.168.x.x' while there is a '172.25.x.x' subnet
## minor code 
### minor code is just lighter code that doesnt need a full file suit for it, as to what they all do, an explination will be in comments or the code is self explanitory, this is mainly for anything under 50 lines of code.
