def string_unazad(string):
    if string == "":
        return  
    else:
        string_unazad(string[1:])  
        print(string[0]) 


unos = input("Unesite string: ")
string_unazad(unos)