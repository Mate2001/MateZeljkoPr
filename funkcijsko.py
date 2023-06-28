"""
Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
"""
def pozdrav_Ime(ime):
    return f"Pozdrav {ime}"

dobrodosao_ime=lambda ime:f"Dobrodošao {ime}!"

def pozovi_funkciju(funkcija,ime):
    return funkcija(ime)

ime="Mate"

prvi_rezultat=pozovi_funkciju (pozdrav_Ime, ime)
drugi_rezultat=pozovi_funkciju(dobrodosao_ime,ime)

print(prvi_rezultat)
print(drugi_rezultat)
