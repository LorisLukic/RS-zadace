tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

tekst_lower = tekst.lower()
riječi = tekst_lower.split()  
counter = {}

def prebrojavanje(tekst):
    for riječ in riječi:
        if riječ in counter:
            counter[riječ] += 1
        else:
            counter[riječ] = 1

    return counter

rezultat = prebrojavanje(tekst)
print("Broj pojavljivanja svake riječi je: ", rezultat)