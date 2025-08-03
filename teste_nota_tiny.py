import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
token = os.getenv("TINY_API_TOKEN")

url_nota = "https://api.tiny.com.br/api2/notas.fiscais.pesquisa.php"

params_nota = {
    "token": token,
    "formato": "json",
    "numeroEcommerce": "2000012077560626" # ex: "258065"
}

resp_nota = requests.get(url_nota, params=params_nota)
dados_nota = resp_nota.json()
print(json.dumps(resp_nota.json(), indent=2, ensure_ascii=False))