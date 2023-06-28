import re

regex = r"^[K][a-zA-Z]*[0-5].*[Razmak][a-zA-Z]*[S]$"
string = "Kristijan Sliskovic"

if re.match(regex, string):
    print("Podudaranje pronađeno!")
else:
    print("Podudaranje nije pronađeno.")