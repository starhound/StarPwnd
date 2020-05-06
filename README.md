# StarPwnd
Simple python script that utilizes the "Have I Been Pwned" API

DEPENDENCIES: Hashlib, Requests 

StarPwnd is a python script file that will prompt the user for their password (any password will do), the script will then hash the input password with SHA1 and use it to query the "Have I Been Pwned" API (https://haveibeenpwned.com/).

The script impliments k-Anonymity as described from the API (https://haveibeenpwned.com/API/v2#PwnedPasswords), meaning it only sends them the first five characters of your hashed password, gets a list of matches, and will then filter through those matches to find an exact match.

I'm sure this script could be improved upon significantly as I'm not a python master but I'm quite pleased with how compact this tool is. 

You may utilize source code from or redistribute this script as desired as long as you credit the creator in some form. I am not liable for any damages or loss caused from usage of this script. 
