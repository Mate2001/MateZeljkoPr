def par_nepar_brojevi(n):
    for broj in range(n):
        if broj % 2 == 0:
            yield broj, "paran"
        else:
            yield broj, "neparan"

n = int(input("Unesi max vrijednost: "))
numbers = par_nepar_brojevi(n)

for number, parity in numbers:
    print(number, "je", parity)
