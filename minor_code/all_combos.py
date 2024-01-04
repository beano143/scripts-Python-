import string
from itertools import product

def generate_combinations(size):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    with open(f'words_longform_{size}.txt', 'a') as file:
        for combo in product(all_characters, repeat=size):
            file.write(''.join(combo) + '\n')

# Adjust the size parameter to control the character size
generate_combinations(size=6)  # Change the size as needed
