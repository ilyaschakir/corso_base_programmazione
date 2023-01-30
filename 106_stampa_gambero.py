stringa = str(input("Inserisci una frase: "))
i = 0
counter = len(stringa)
while True:
    i = i - 1
    print(stringa[i])
    if(i == -counter):
        break 