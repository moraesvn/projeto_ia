import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
token = os.getenv("TINY_API_TOKEN")

url = "https://api.tiny.com.br/api2/pedidos.pesquisa.php"

params = {
    "token": token,
    "formato": "json",
    "dataInicial": "25/06/2025",
    "dataFinal": "25/06/2025",
    "situacao": "cancelado"
}

response = requests.get(url, params=params)

print(response.status_code)
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
