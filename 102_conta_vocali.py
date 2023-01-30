stringa = input("Inserisci una frase: ")
counter = len(stringa)
c = ""
i = 0
vocali = 0
while i < counter:
    c = stringa[i]
    if((c == "a" or c == "A" or c == "e" or c == "E" or c == "i" or c == "I" or c == "o" or c == "O" or c == "u" or c == "U")):
        vocali = vocali + 1
    i = i + 1
print("Le vocali sono: "+str(vocali))