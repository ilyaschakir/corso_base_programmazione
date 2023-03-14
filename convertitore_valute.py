TASSO_CAMBIO_EURO = {
"USD": 1.07,
"JPY": 143.96,
"GBP": 0.88,
"CHF": 0.98,
"CAD": 1.47,
"AUD": 1.61
}
TASSO_CAMBIO_USD = {
"EUR": 0.93,
"JPY": 134.10,
"GBP": 0.82,
"CHF": 0.91,
"CAD": 1.37,
"AUD": 1.50
}
TASSO_CAMBIO_GBP = {
"EUR": 1.13,
"USD": 1.22,
"CHF": 1.11,
"JPY": 163.29,
"CAD": 1.67,
"AUD": 1.82
}
TASSO_CAMBIO_CHF = {
"EUR": 1.02,
"USD": 1.1,
"GBP": 0.90,
"JPY": 146.94,
"CAD": 1.50,
"AUD": 1.64
}
TASSO_CAMBIO_JPY = {
"EUR": 0.0069,
"USD": 0.0075,
"GBP": 0.0061,
"CHF": 0.0068,
"CAD": 0.010,
"AUD": 0.011
}
TASSO_CAMBIO_AUD = {
"EUR": 0.62,
"USD": 0.67,
"GBP": 0.55,
"CHF": 0.61,
"JPY": 89.68,
"CAD": 0.91
}
TASSO_CAMBIO_CAD = {
"EUR": 0.68,
"USD": 0.73,
"GBP": 0.6,
"CHF": 0.67,
"JPY": 98.13,
"AUD": 1.09
}
valute = {
"euro": {"simbolo": "EUR", "tassi": TASSO_CAMBIO_EURO},
"dollaro": {"simbolo": "USD", "tassi": TASSO_CAMBIO_USD},
"sterlina": {"simbolo": "GBP", "tassi": TASSO_CAMBIO_GBP},
"franco svizzero": {"simbolo": "CHF", "tassi": TASSO_CAMBIO_CHF},
"yen": {"simbolo": "JPY", "tassi": TASSO_CAMBIO_JPY},
"dollaro australiano": {"simbolo": "AUD", "tassi": TASSO_CAMBIO_AUD},
"dollaro canadese": {"simbolo": "CAD", "tassi": TASSO_CAMBIO_CAD}
}
valute_disponibili=["euro", "dollaro", "sterlina", "franco svizzero", "yen", "dollaro australiano" , "dollaro canadese"]
visualizza_valute=input("Desideri visualizzare le valute disponibili? (s/n): " .lower())
if visualizza_valute=="s":
    print("Le valute disponibili sono: "+str(valute_disponibili))
conversioni_effettuate = []
while True:
    quantita = float(input("Inserisci la quantità di valuta di origine: "))
    valuta_origine = input("Inserisci la valuta di origine (es. Euro): ").lower()
    if valuta_origine not in valute:
        print("Valuta di origine non supportata, riprova.")
        continue
    valuta_destinazione = input("Inserisci la valuta di destinazione (es. Dollaro): ").lower()
    if valuta_destinazione not in valute:
        print("Valuta di destinazione non supportata, riprova.")
        continue
    if valuta_origine == valuta_destinazione:
        print("Non puoi inserire la stessa valuta 2 volte! Riprova.")
    if valuta_destinazione.lower() not in valute[valuta_origine]["tassi"] and valuta_destinazione.lower() == valuta_origine:
        print("Tasso di cambio non disponibile per la valuta di destinazione, riprova.")
        continue
    simbolo_valuta=valute[valuta_destinazione]["simbolo"]
    tasso_cambio = valute[valuta_origine]["tassi"][simbolo_valuta]
    importo_convertito = quantita * tasso_cambio
    conversione = str(quantita) + " " + valute[valuta_origine]["simbolo"] + " corrispondono a " + str(importo_convertito) + " " + valute[valuta_destinazione]["simbolo"]
    print(conversione)
    conversioni_effettuate.append(conversione)
    risposta = input("Vuoi fare un'altra conversione? (s/n): ").lower()
    if risposta == "s":
        continue
    visualizza_conversioni = input("Vuoi visualizzare le conversioni effettuate? (s/n): " ).lower()
    if visualizza_conversioni == "s":
        print("Conversioni effettuate:" +str(conversioni_effettuate)) 
        break
    if(risposta!="s" and visualizza_conversioni != "s"):
        break
print("Grazie per aver usato il mio programma per convertire le valute, spero che ti sia stato di aiuto. Buon proseguimento di giornata.")