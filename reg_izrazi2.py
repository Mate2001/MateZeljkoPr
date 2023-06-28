import re

regex=r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
email=input("Unesite e-mail: ")

if re.match(regex, email):
    print("E-mail vrijedi.")
else:
    print("E-mail ne vrijed.")   

regex2=r"^[a-zA-Z]+[a-zA-Z]+\d*@sum\.ba$"
edu_id=input("Unesite eduId: ")
if re.match(regex2, edu_id):
    print("eduId vrijedi.")
else:
    print("eduId ne vrijedi.")