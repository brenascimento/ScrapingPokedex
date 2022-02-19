from bs4 import BeautifulSoup
import pandas as pd
# import requests

# to save html file and don't make much requests
# req = requests.get('https://pokemondb.net/pokedex/all')
# 
# with open('pokedex.html', 'w') as file:
#   file.write(req.text)

with open('pokedex.html') as f:
  soup = BeautifulSoup(f, 'html.parser')

pokedex_table = soup.find(id="pokedex").find("tbody")
# for poke in pokedex_table.find_all("tr")[0:5]:
#   print(poke.select_one(".cell-name small"))

def pokemon_stat(pokedex):
  pokemons = []
  for tr in pokedex.find_all("tr"):
    p_id = tr.select_one("td .infocard-cell-data").string
    if tr.select_one(".cell-name small"):
      name = tr.select_one(".cell-name small").string
    else:
      name = tr.select_one(".cell-name a").string
    types = [i.string for i in tr.select(".cell-icon a")]
    total = tr.select_one('.cell-total').string
    hp, attack, defense, special_attack, special_defense, speed =\
      map(lambda x: x.string, tr.select('.cell-total~.cell-num'))


    pokemon = {"p_id": int(p_id),
      "name":name,
      "p_type":types, 
      "total_attr":total,
      "hp":hp,
      "attack":attack,
      "defense":defense,
      "special_attack":special_attack,
      "special_defense":special_defense,
      "speed":speed}
    pokemons.append(pokemon)
  return pokemons

df = pd.DataFrame(pokemon_stat(pokedex_table))
print(df.head(10))
df.to_csv('pokedex.csv', index=False)

poke = pd.read_csv('pokedex.csv')
print(poke.head())


