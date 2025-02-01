import requests
import random

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '271253f723e6760ac74fd4b16bf278d1'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
bodyCreatePokemon = {
    "name": "generate",
    "photo_id": random.randint(0, 1008)
}

responseCreatePokemon = requests.post(url = f'{URL}/pokemons', headers=HEADER , json = bodyCreatePokemon)
print(responseCreatePokemon.text)

pokemonID = responseCreatePokemon.json()['id']

bodyAddInPokeball = {"pokemon_id": pokemonID}
bodyRenamePokemon = {
    "pokemon_id": pokemonID,
    "name": "generate",
    "photo_id": random.randint(0, 1008)
}

responseAddInPokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER ,json = bodyAddInPokeball)
print(responseAddInPokeball.text)

responseRenamePokemon = requests.put(url = f'{URL}/pokemons', headers=HEADER ,json = bodyRenamePokemon)
print(responseRenamePokemon.text)

