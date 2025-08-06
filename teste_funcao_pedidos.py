from api.pedidos import buscar_pedidos
from dotenv import load_dotenv
import os
import json

# Carrega a variável de ambiente
load_dotenv()
token = os.getenv("TINY_API_TOKEN_SP")

# Parâmetros de teste
data_inicial = "01/01/2022"
data_final = "05/01/2022"
marcador = "cancelamento"  # ou outro que você queira testar

# Executa a função
pedidos = buscar_pedidos(token, data_inicial, data_final, marcador)

# Exibe o resultado formatado
print(f"Total de pedidos encontrados: {len(pedidos)}")
print(json.dumps(pedidos, indent=2, ensure_ascii=False))
