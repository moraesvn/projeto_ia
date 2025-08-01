import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Lê a chave da API do .env
api_key = os.getenv("OPENAI_API_KEY")

# Cria o cliente da OpenAI
client = OpenAI(api_key=api_key)

# Faz uma chamada simples usando GPT-4o
response = client.chat.completions.create(
    model="gpt-4o-mini",  # ou "gpt-4-1106-preview"
    messages=[
        {"role": "user", "content": "Qual a capital do brasil?."}
    ]
)

# Exibe a resposta
print(response.choices[0].message.content)