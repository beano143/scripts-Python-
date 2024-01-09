import subprocess

base = "631aada47deaf488bb72eee0873a20472c8f43ff960f2188f66cc41eb3f35428"
hash_type = ["sha256sum"]
word_path = "combined_words.txt"

with open(word_path, "r") as file:
    for line in file:
        line = line.strip()
        cmd = ["echo", "-n", line]
        echo_run = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        rerun = subprocess.run(hash_type, input=echo_run.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out = rerun.stdout.strip().split(" ")

        if base in out:
            print(line)
