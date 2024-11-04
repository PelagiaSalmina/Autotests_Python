import requests

url = 'https://api.pokemonbattle.ru/v2'
token = '90d4511a2ef7e4faab002f6bf0d3b76c'
header = {'Content-Type' : 'application/json', 'trainer_token': token}

# body_registration = {
#     "trainer_token": token,
#     "email": "cool.mgdeva@mail.ru",
#     "password": "Iloveqa111"
# }

# body_confirmation = {
#     "trainer_token": "90d4511a2ef7e4faab002f6bf0d3b76c"
# }

body_createpok = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_changenamepok = {
     "pokemon_id": "123309",
    "name": "NewName"
}
body_catchpok = {
    "pokemon_id": "123309"
}

# response_registration = requests.post(url = f'{url}/trainers/reg', headers = header, json = body_registration)
# print(response_registration.text)


# response_confirmation = requests.post(url = f'{url}/trainers/confirm_email',headers = header, json = body_confirmation)
# print(response_confirmation.text)


response_createpok = requests.post(url = f'{url}/pokemons',headers = header, json = body_createpok)
print(response_createpok.text)


response_changenamepok = requests.patch(url = f'{url}/pokemons',headers = header, json = body_changenamepok)
print(response_changenamepok.text)


response_catchpok = requests.post(url = f'{url}/trainers/add_pokeball',headers = header, json = body_catchpok)
print(response_catchpok.text)