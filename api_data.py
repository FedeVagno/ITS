import json
raw_data = '{"server": "Amazon", "config":{"port":80,"active":true}}' #è una stringa

data = json.loads(raw_data) #trasformo la stringa in un dizionario

#voglio stampare 80

print(data["config"]["port"]) #richiamo il dizionario e poi quello che mi serve
