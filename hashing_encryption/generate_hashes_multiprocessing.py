  GNU nano 6.3                                                                                         multi.py                                                                                                   
from string import ascii_letters, digits, punctuation
from itertools import product
import subprocess
from multiprocessing import Pool

maxdex = 2  # end size
mindex = 1  # start size
hashes = []

def generate_combinations(size):
    data = []
    all_characters = ascii_letters + digits + punctuation + " "  # all human-readable characters
    for combo in product(all_characters, repeat=size):  # generates the combinations
        data.append(combo)  # writes them down for later use
    return data

def generate_hash(string):
    data = "".join(string)
    hash_type = ["md5sum"]  # change for whatever hash alg you're wanting to generate
    run = subprocess.run(hash_type, input=data.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = run.stdout.decode().split(" ")
    return out[0]

def return_data(size):
    collisions = []
    try:
        with open("hashes.txt", "a") as file: # adds data to the file instead of replacing it
            use = generate_combinations(size)
            for string in use:
                poss_hash = generate_hash(string)
                with open("hashes.txt", "r") as reading:
                    if poss_hash not in reading.read(): # checks for collisions; if none add it to the file
                        data = f"{poss_hash}\n"
                        file.write(data)
                    else: # mark it down as a collision
                        info = f"Collision found with hash#{poss_hash} with {string}"
                        collisions.append(info)
    except KeyboardInterrupt as e:
        print(f"\nProgram ended early.\nHash string index at end: {size}")
    return collisions

if __name__ == '__main__':
    try:
        with Pool() as pool:
            sizes = range(mindex, maxdex + 1)
            collisions = pool.map(return_data, sizes)
            collisions = [item for sublist in collisions for item in sublist]

        print("All hashes found.\nHashes can be found in 'hashes.txt'")

        if collisions:
            print("Collisions found:")
            for collision in collisions:
                print(collision)

    except KeyboardInterrupt as e:
        print(f"\nProgram ended early.\nHash string index at end: {mindex}")
