import requests
import json
import pandas as pd

pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

ditto = json.dumps(pokemon.json()["abilities"])

print(ditto)

df = pd.read_json(ditto)
print(df)