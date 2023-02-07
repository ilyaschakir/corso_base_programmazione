i=0
nani=["Brontolo", "Eolo", "Dotto", "Pisolo", "Mammolo", "Gongolo", "Cucciolo"]
while True:
    input_utente=input("Inserisci il nome di un nano: ")
    if(input_utente in nani):
        i=i+1
        nani.remove(input_utente)
        print("Giusto!")
    else:
        print("Hai sbagliato, o lo hai già messo. Riprova")
    if(i==7):
        print("Biancaneve")
        break