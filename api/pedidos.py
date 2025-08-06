import requests

def buscar_pedidos(token, data_inicial, data_final, marcador=None, situacao="cancelado"):
    """
    Busca pedidos cancelados da API do Tiny e retorna uma lista com dados organizados.

    Args:
        token (str): Token da API do Tiny.
        data_inicial (str): Data inicial no formato dd/mm/aaaa.
        data_final (str): Data final no formato dd/mm/aaaa.
        marcador (str, opcional): Marcador da venda (ex: devolucao, zero hora).
        situacao (str): Situação da venda (padrão: "cancelado").

    Returns:
        list: Lista de dicionários com os dados dos pedidos.
    """
    url = "https://api.tiny.com.br/api2/pedidos.pesquisa.php"

    params = {
        "token": token,
        "formato": "json",
        "dataInicial": data_inicial,
        "dataFinal": data_final,
        "situacao": situacao,
    }

    if marcador:
        params["marcador"] = marcador

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Erro na requisição: {response.status_code}")
        return []

    try:
        pedidos_api = response.json()["retorno"]["pedidos"]
    except (KeyError, TypeError):
        print("Nenhum pedido encontrado ou erro na estrutura do retorno.")
        return []

    pedidos_formatados = []

    for item in pedidos_api:
        pedido_raw = item["pedido"]
        pedido = {
            "numero_pedido_tiny": pedido_raw.get("numero"),
            "data_venda": pedido_raw.get("data_pedido"),
            "nome_cliente": pedido_raw.get("nome"),
            "numero_pedido_ecommerce": pedido_raw.get("numero_ecommerce"),
            "valor_total": pedido_raw.get("valor"),
            "status": pedido_raw.get("situacao"),
            "canal_venda": None,  # preencher depois se necessário
            "previsao_entrega": pedido_raw.get("data_prevista") or None,
            "codigo_rastreamento": pedido_raw.get("codigo_rastreamento"),
            "marcadores_venda": marcador,
            "numero_nota_fiscal": None,  # preenchido depois
            "saldo_pedido": None,
            "situacao_devolucao": None,
            "numero_caso_marketplace": None,
            "solucao_agente": None,
            "motivo_observacoes": None,
        }
        pedidos_formatados.append(pedido)

    return pedidos_formatados
