import requests
import json
import hashlib

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN"
urlPOST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN"
json_data = requests.get(url).json()

with open('answer.json', 'w') as w:
  w.write(repr(json_data))

json_casas = json_data["numero_casas"]
json_token = json_data["token"]
json_cifrado = json_data["cifrado"].lower()

alfabeto = "abcdefghijklmnopqrstuvwxyz"

json_decifrado = ""
for letra in json_cifrado:
  if letra in alfabeto:
    letra_index = alfabeto.index(letra)
    json_decifrado += alfabeto[(letra_index - json_casas) % len(alfabeto)]
  else:
    json_decifrado += letra
print(json_decifrado)
#if the programmers like each other, they play a game called pair programming. and if not then the game is called peer review. anna nachesa

json_data["decifrado"] = json_decifrado
print(json_data)
#{'numero_casas': 10, 'token': 'SEU_TOKEN', 'cifrado': 'sp dro zbyqbkwwobc vsuo okmr ydrob, droi zvki k qkwo mkvvon zksb zbyqbkwwsxq. kxn sp xyd drox dro qkwo sc mkvvon zoob bofsog. kxxk xkmrock', 'decifrado': 'if the programmers like each other, they play a game called pair programming. and if not then the game is called peer review. anna nachesa', 'resumo_criptografico': 'fb4d65533f538348ff11079580b3cc61ce3c3d17'}

with open('answer.json', 'w') as f:
  f.write(repr(json_data))

json_resumo_criptografico = hashlib.sha1(json_decifrado.encode()).hexdigest()
json_data["resumo_criptografico"] = json_resumo_criptografico

with open('answer.json', 'w') as f:
  f.write(repr(json_data))
  print(json_data)
  #{'numero_casas': 10, 'token': 'SEU_TOKEN', 'cifrado': 'sp dro zbyqbkwwobc vsuo okmr ydrob, droi zvki k qkwo mkvvon zksb zbyqbkwwsxq. kxn sp xyd drox dro qkwo sc mkvvon zoob bofsog. kxxk xkmrock', 'decifrado': 'if the programmers like each other, they play a game called pair programming. and if not then the game is called peer review. anna nachesa', 'resumo_criptografico': 'fb4d65533f538348ff11079580b3cc61ce3c3d17'}

file = open("answer.json", "r")
file = {"answer": ("answer.json", file.read(), "multipart/form-data")}
resposta = requests.post(urlPOST, files=file)
print(resposta.text)
#{"score":100}