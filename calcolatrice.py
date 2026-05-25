primo = float(input("Inserisci primo numero: "))
secondo = float(input("Inserisci secondo numero: "))
numRadice = float(input("Inserisci il numero di cui vuoi la radice quadrata: "))
mezzo = 0.5

def somma(primo, secondo):
    return primo+secondo

def sottrazione(primo, secondo):
    return primo-secondo

def moltiplicazione(primo, secondo):
    return primo*secondo

def radice(numRadice, mezzo):
    return numRadice**0.5

#i due print sono uguali, solo che nel secondo caso F fa tipo d'avviso a Python che c'è del codice da eseguire dentro parentesi graffe
#print ("Risultato somma: " + somma(1,2))
print (f"Risultato somma: {somma(primo,secondo)}")
print (f"Risultato sottrazione: {sottrazione(primo,secondo)}")
print (f"Risultato moltiplicazione: {moltiplicazione(primo,secondo)}")
print (f"Risultato radice: {radice(numRadice,mezzo)}")

    