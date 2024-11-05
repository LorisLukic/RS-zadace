Lozinka = input("Upišite lozinku: ")

ima_veliko_slovo = any(char.isupper() for char in Lozinka)
ima_broj = any(char.isdigit() for char in Lozinka)
lozinka_lower = Lozinka.lower()

def provjera_lozinke(Lozinka):

    if 15 < len(Lozinka) & len(Lozinka) < 8:
        print("Lozinka mora imati između 8 i 15 znamenaka")

    elif ima_veliko_slovo==False & ima_broj==False:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    
    elif "password" in lozinka_lower or "lozinka" in lozinka_lower:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")

    else: 
        print("Lozinka je jaka")

    
    
provjera_lozinke(Lozinka)