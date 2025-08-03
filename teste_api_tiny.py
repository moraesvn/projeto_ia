import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TINY_API_TOKEN")

url = "https://api.tiny.com.br/api2/pedidos.pesquisa.php"

params = {
    "token": token,
    "formato": "json"
}

response = requests.get(url, params=params)

print("Status:", response.status_code)
print("Resposta:")
print(response.json())
