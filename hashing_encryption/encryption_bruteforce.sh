# this is just a simple shell script to runn passwords against encrypted files 

for pass in $(cat wordlist.txt); # password list 
do
    for i in $( openssl enc -list | tail +2); # removes null lines
        # add for each level of encryption
        do $(openssl ${i:1} -d -pbkdf2 -in Level_2_Challenge.enc -out Decrypt_$i-$pass.txt -k $pass);
        # remove hashes on following lines for multi layer
        #for pass2 in $(cat wordlist.txt); # password list 
        #do
        #    for i in $( openssl enc -list | tail +2);
        #        do $(openssl ${i:1} -d -pbkdf2 -in Level_2_Challenge.enc -out Decrypt_$i-$pass.txt -k $pass2)
        #done;
    done;
done;
