import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '271253f723e6760ac74fd4b16bf278d1'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 18380

def test_getTrainers200():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_getTrainersID():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()['data'][0]['id'] == '18380'

@pytest.mark.parametrize('key, value', [('id', '18380')])
def test_parametrize(key, value):
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()['data'][0][key] == value