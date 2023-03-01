TASSO_CAMBIO_EURO = {
"USD": 1.22,
"JPY": 129.03,
"GBP": 0.88,
"CHF": 1.11,
"CAD": 1.48,
"AUD": 1.56
}

TASSO_CAMBIO_USD = {
"EUR": 0.82,
"JPY": 105.62,
"GBP": 0.72,
"CHF": 0.91,
"CAD": 1.21,
"AUD": 1.28
}

TASSO_CAMBIO_GBP = {
"EUR": 1.14,
"USD": 1.39,
"CHF": 1.26,
"JPY": 146.25,
"CAD": 1.67,
"AUD": 1.76
}

TASSO_CAMBIO_CHF = {
"EUR": 0.9,
"USD": 1.1,
"GBP": 0.79,
"JPY": 116.14,
"CAD": 1.32,
"AUD": 1.4
}

TASSO_CAMBIO_JPY = {
"EUR": 0.0077,
"USD": 0.0095,
"GBP": 0.0068,
"CHF": 0.0086,
"CAD": 0.0098,
"AUD": 0.0104
}

TASSO_CAMBIO_AUD = {
"EUR": 0.64,
"USD": 0.78,
"GBP": 0.57,
"CHF": 0.71,
"JPY": 96.46,
"CAD": 0.95
}

TASSO_CAMBIO_CAD = {
"EUR": 0.67,
"USD": 0.82,
"GBP": 0.6,
"CHF": 0.75,
"JPY": 102.63,
"AUD": 1.06
}

valute = {
"euro": {"simbolo": "EUR", "tassi": TASSO_CAMBIO_EURO},
"dollaro": {"simbolo": "USD", "tassi": TASSO_CAMBIO_USD},
"sterlina": {"simbolo": "GBP", "tassi": TASSO_CAMBIO_GBP},
"franco": {"simbolo": "CHF", "tassi": TASSO_CAMBIO_CHF},
"yen": {"simbolo": "JPY", "tassi": TASSO_CAMBIO_JPY},
"dollaro australiano": {"simbolo": "AUD", "tassi": TASSO_CAMBIO_AUD},
"dollaro canadese": {"simbolo": "CAD", "tassi": TASSO_CAMBIO_CAD}
}

conversioni_effettuate = []

while True:
    
    quantita = float(input("Inserisci la quantità di valuta di origine: "))
    valuta_origine = input("Inserisci la valuta di origine (es. Euro): ").lower()
    if valuta_origine not in valute:
        print("Valuta di origine non supportata, riprova.")
        continue
    valuta_destinazione = input("Inserisci la valuta di destinazione (es. Dollaro): ").lower()
    if valuta_destinazione.lower() not in valute[valuta_origine]["tassi"] and valuta_destinazione.lower() == valuta_origine:
        print("Tasso di cambio non disponibile per la valuta di destinazione, riprova.")
        continue
    tasso_cambio = valute[valuta_origine]["tassi"][valuta_destinazione]
    importo_convertito = quantita * tasso_cambio
    conversione = str(quantita) + " " + valute[valuta_origine]["simbolo"] + " corrispondono a " + str(importo_convertito) + " " + valute[valuta_destinazione]["simbolo"]
    print(conversione)
    conversioni_effettuate.append(conversione)
    risposta = input("Vuoi fare un'altra conversione? (s/n)").lower()
    if risposta != "s":
        break
    visualizza_conversioni = input("Vuoi visualizzare le conversioni effettuate? (s/n)").lower()
    if visualizza_conversioni == "s":
        print("Conversioni effettuate:")
for conversione in conversioni_effettuate:
    print(conversione)