import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = '2dff2dc5c949e4e82403650e40970aa9'
header = {'Content-Type' : 'application/json', 'trainer_token': token}
trainer_id = '16834'

# def test_status_code():
#     respose = requests.get(url = f'{url}/pokemons', params = {'trainer_id':trainer_id})
#     assert respose.status_code == 200

# def test_part_of_response():
#     response_get = requests.get(url = f'{url}/pokemons', params = {'trainer_id':trainer_id})
#     assert response_get.json()['data'][0]['name'] == 'Бульбазавр'


# @pytest.mark.parametrize('key, value', [('name','Бульбазавр'), ('trainer_id', trainer_id), ('id', '123296')])
# def test_parametrize(key, value):
#     response_parametrize = requests.get(url = f'{url}/pokemons', params = {'trainer_id':trainer_id})
#     assert response_parametrize.json()['data'][0][key] == value


def test_trainers_status_code():
    respose = requests.get(url = f'{url}/trainers')
    assert respose.status_code == 200

def test_my_trainer_in_response():
    response_get = requests.get(url = f'{url}/trainers', params = {'trainer_id':trainer_id})
    assert response_get.json()['data'][0]['trainer_name'] == 'hjk'