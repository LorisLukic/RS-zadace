lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parna_lista = []
neparna_lista = []
for i in lista:
    if i % 2 == 0:
        parna_lista.append(i)
    else:
        neparna_lista.append(i)

print("Parni ", parna_lista, ", Neparni: ", neparna_lista)
