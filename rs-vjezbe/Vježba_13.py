lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(lista1):
    zadnji_broj = -1
    for i in lista1:
        zadnji_broj += 1
    print("Prvi broj je:", lista1[0], ", a zadnji broj je:", lista1[zadnji_broj])

prvi_i_zadnji(lista1)

lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def max_i_min(lista2):
    minimum = lista2[0]
    maximum = 0
    for i in lista2:
        if minimum > i:
            minimum = i
        elif maximum < i:
            maximum = i
    print("Najmanji broj je:", minimum, ", a najveći je:", maximum)

max_i_min(lista2)