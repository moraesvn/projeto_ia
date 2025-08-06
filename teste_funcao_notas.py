from api.notas_fiscais import buscar_nota_por_pedido
from dotenv import load_dotenv
import os
import json

# Carrega a variável de ambiente
load_dotenv()
token = os.getenv("TINY_API_TOKEN_SP")

# Parâmetros de teste
numero_ecommerce = "377007"

# Executa a função
pedidos = buscar_nota_por_pedido(numero_ecommerce, token)

# Exibe o resultado formatado
#print(f"Total de pedidos encontrados: {len(pedidos)}")
print(json.dumps(pedidos, indent=2, ensure_ascii=False))
