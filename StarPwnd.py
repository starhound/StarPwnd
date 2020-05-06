# Written and developed by Wesley Reid (http://starhound.com) (http://lostsouls.org)

import requests
import hashlib

password = input("Please enter your password: ")

result = hashlib.sha1(password.encode('utf-8'))

print("SHA1 Hash: ")
print(result.hexdigest())
print("\n\n")
print("Password API Results\n")

hashedChars = result.hexdigest()[:5]
resp = requests.get('https://api.pwnedpasswords.com/range/' + hashedChars)
content = resp.text
lines = content.splitlines()
passwordList = []

for line in lines:
    head, sep, tail = line.partition(':')
    returnedPass = hashedChars.upper() + head.upper()
    passwordList.append(returnedPass)
    print(returnedPass + " " + sep + tail)

hashedPass = result.hexdigest().upper()
foundPass = 0

for password in passwordList:
    if password == hashedPass:
        foundPass = password
        break

if foundPass:
    print("Password Found: " + foundPass)
else:
    print("Password not found.")
