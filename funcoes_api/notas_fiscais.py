import requests

def buscar_nota_por_pedido(numero_ecommerce, token):
    """
    Consulta a nota fiscal de um pedido pelo número do e-commerce.

    Args:
        numero_ecommerce (str): Número do pedido no e-commerce.
        token (str): Token da API do Tiny.

    Returns:
        str | None: Número da nota fiscal, ou None se não encontrar.
    """
    url = "https://api.tiny.com.br/api2/notas.fiscais.pesquisa.php"

    params = {
        "token": token,
        "formato": "json",
        "numeroEcommerce": numero_ecommerce
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"[Erro] Código {response.status_code} ao buscar nota para {numero_ecommerce}")
        return None

    try:
        notas = response.json()["retorno"]["notas_fiscais"]
    except (KeyError, TypeError):
        print(f"[Info] Nenhuma nota encontrada para o pedido {numero_ecommerce}")
        return None

    if not notas:
        return None

    nota_raw = notas[0]["nota_fiscal"]
    return nota_raw.get("numero")
