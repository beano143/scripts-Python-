from string import ascii_letters, digits, punctuation # adds all of the sting types that are human readable 
from itertools import product # adds a function that can scale and generate lists of characters 
import subprocess
maxdex = 2 # sets  to max string size
mindex = 1 # sets the minimum string size 
hashes = []
 
def generate_combinations(size): # for each size scale generate all posible combos
    data = []
    all_characters = ascii_letters + digits + punctuation
    for combo in product(all_characters, repeat=size):
        data.append(combo)
    return data
 
def generate_hash(string): # hashes each string
    data = ""
    for info in string:
        data += info
    cmd = ["echo", "-n", f"'{data}'"] # base command 
    hash_type = ["md5sum"] # sets the hashing type
    run = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) # wrights the data
    (stdout, stderr) = run.communicate()
 
    rerun = subprocess.run(hash_type, input=stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) # converts the data to the hash type
    out = rerun.stdout.split(" ")
    return out[0]
 
collisions = [] # save data for if and when a colision is found
while mindex <= maxdex: # easy to break loop
    use = generate_combinations(mindex)
    for string in use:
        poss_hash = generate_hash(string)
        if poss_hash not in hashes: # if its a new hash add it to the list 
                hashes.append(poss_hash)
        else: # else set it to a found colision
            info = f"collision found with hash#{poss_hash} with {string}"
            collisions.append(info)

    mindex += 1 # increases the size of the srings for each loop

print("all hashes found:") # shows data
print(hashes, "\n")
if collisions:
    print("colisions found:")
    for collision in collisions:
        print(collision)
