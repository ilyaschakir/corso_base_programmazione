a = 0
e = 0
i = 0
o = 0
u = 0
stringa = input("Inserisci una frase: ")
counter = len(stringa)
c = ""
j = 0
while j < counter:
    c = stringa[j]
    if(c == "a" or c == "A"):
        a = a + 1
    if(c == "e" or c == "E"):
        e = e + 1
    if(c == "i" or c == "I"):
        i = i + 1
    if(c == "o" or c == "O"):
        o = o + 1
    if(c == "u" or c == "U"):
        u = u + 1
    j = j + 1
print("a = ", a)
print("e = ", e)
print("i = ", i)
print("o = ", o)
print("u = ", u)