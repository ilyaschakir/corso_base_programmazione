stringa = input("Inserisci una stringa: ")
carattere = input("Scegli il carattere della stringa: ")
counter = len(stringa)
c = ""
i = 0
tot = 0
while i < counter:
    c = stringa[i]
    if(c == carattere):
        tot = tot + 1
    i = i + 1
print(tot)