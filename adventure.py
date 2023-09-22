#you are an adventurer
#find treasure
#beat monster

def torpeKerdez(mit, helyesValasz):
#input: két string, output: bool
#ha a user által begépelt bálasz ugyanaz, mint a helyes válasz, akkor True, ha nem, akkor False
   #todo: több helyes válasz
    print(mit)
    valasz = input()
    if valasz==helyesValasz:
        return True
    else:
        return False
    
#can be repurposed to do the spoder
#todo: random műveletet kódolni a póknak