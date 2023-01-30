i = 0
contatore = 0
stringa1 = input("inserisci la prima stringa: ")
stringa2 = input("inserisci la seconda stringa: ")
l_stringa1 = len(stringa1)
l_stringa2 = len(stringa2)
while i < l_stringa1:
    carattere1 = stringa1[i]
    if(carattere1 in stringa2):
        contatore = contatore + 1
    i = i + 1
if(contatore == l_stringa2):
    print("True")
else:
    print("False")