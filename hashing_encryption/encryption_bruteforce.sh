#!/bin/bash

# Define variables
wordlist="wordlist.txt"
input_file="layer_2_encryption.enc"

# Loop through passwords from the wordlist file
while IFS= read -r pass; do
    # Loop through first layer encryption algorithms
    for algorithm1 in $(openssl enc -list | awk '{print $1}' | tail +2); do
        decrypted_layer1="Decrypt_${algorithm1}-${pass}-layer1.enc"

        # Decrypt the first layer using the selected algorithm and password
        openssl "${algorithm1:1}" -d -pbkdf2 -in "$input_file" -out "$decrypted_layer1" -k "$pass"

        # Loop through second layer encryption algorithms
        for algorithm2 in $(openssl enc -list | awk '{print $1}' | tail +2); do
            decrypted_final="Decrypt_${algorithm1}-${algorithm2}-${pass}.txt"

            # Decrypt the second layer using a different algorithm and the result from the first layer
            openssl "${algorithm2:1}" -d -pbkdf2 -in "$decrypted_layer1" -out "$decrypted_final" -k "$pass"
        done
    done
done < "$wordlist"
