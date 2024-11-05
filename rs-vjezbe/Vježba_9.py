lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def ukloni_duplikate(lista):
    nova_lista = []
    for element in lista:
        if element not in nova_lista:
            nova_lista.append(element)
    return nova_lista


lista_bez_duplikata = ukloni_duplikate(lista)
print(lista_bez_duplikata)