import re

regex = r"^[M][a-zA-Z]*[0-5].*[Razmak][a-zA-Z]*[Z]$"
string=input("unesi string: ")

if re.match(regex, string):
    print("Podudaranje pronađeno!")
else:
    print("Podudaranje nije pronađeno.")