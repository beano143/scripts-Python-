from string import ascii_letters, digits, punctuation
from itertools import product
import subprocess

maxdex = 2 # end size 
mindex = 1 # start size 

def generate_combinations(size):
    data = []
    all_characters = ascii_letters + digits + punctuation + " " # all human readable characters 
    for combo in product(all_characters, repeat=size): # generates the combinations 
        data.append(combo) # writes them down for later use
    return data

def generate_hash(string):
    data = "".join(string)
    hash_type = ["md5sum"] # change for whatever hash alg your wanting to generate 
    run = subprocess.run(hash_type, input=data.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = run.stdout.decode().split(" ")
    return out[0]

collisions = []

try:
    while mindex <= maxdex: # generates untill string legnth is reached
        with open("hashes.txt", "a") as file:
            use = generate_combinations(mindex)
            for string in use: # runs for each returned string
                poss_hash = generate_hash(string) # generates a hash
                with open("hashes.txt", "r") as reading:
                    if poss_hash not in reading: # makes sure the hash isnt in the table already
                        data = f"{poss_hash}\n"
                        file.write(data)
                    else: # otherwise it markes it down as a collision
                        info = f"Collision found with hash#{poss_hash} with {string}"
                        collisions.append(info)
        mindex += 1

except KeyboardInterrupt as e: # the terminal will nolonger yell at you for ending the program
    print(f"\nProgram ended early.\nHash string index at end: {mindex}")


print("All hashes found.\nHashes can be found in 'hashes.txt'")
if collisions:
    print("Colisions found:")
    for collision in collisions:
        print(collision)
