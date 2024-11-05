vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

samoglasnici = list(vowels)
suglasnici = list (consonants)


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def prebrojavanje(tekst):
    preb_sam = 0
    preb_sug = 0
    for i in tekst:
        if i in samoglasnici:
            preb_sam = preb_sam + 1
        elif i in suglasnici:
            preb_sug = preb_sug + 1
    print("vowels: ", preb_sam, "consonants: ", preb_sug)

prebrojavanje(tekst)