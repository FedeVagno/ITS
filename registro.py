#In python gli array sono chiamate LISTE
#è più flessibile rispetto a cpp, si usano le [] , il conteggio parte da 0 
#e se vuoi aggiungere un elemento metti .append()
#ciclo for si mette prodotti["pane","latte","uova"] for p in prodotti: print("...")

voti=[6,7,8,9]
voti.append(5) #aggiunge alla fine
voti.insert(0, 3) #aggiunge (posizione, valore)

for p in voti:
    print("Voto registrato: ")
    print(p) #dentro al ciclo
