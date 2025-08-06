from funcoes_api.pedidos import buscar_pedidos       # sua função para buscar pedidos da API
from funcoes_api.notas_fiscais import buscar_nota_por_pedido     # sua função para buscar nota fiscal pela API
from database.sqlite import inserir_pedido               # função para inserir no banco

def processar_pedidos(token, data_inicial, data_final, marcador, empresa):
    pedidos = buscar_pedidos(token, data_inicial, data_final, marcador, situacao="cancelado")
    
    for pedido_raw in pedidos:
        # Extrai info do pedido da resposta da API
        numero_ecommerce = pedido_raw.get("numero_ecommerce")
        numero_pedido_tiny = pedido_raw.get("numero")
        data_venda = pedido_raw.get("data_pedido")
        nome_cliente = pedido_raw.get("nome", "N/A")
        valor_total = pedido_raw.get("valor", 0.0)
        marcadores = marcador  # ou outra lógica para marcadores

        # Buscar dados da nota fiscal com o número do pedido ecommerce
        nota = buscar_nota_por_pedido(token, numero_ecommerce)

        # Montar o dicionário completo para o banco
        pedido_para_bd = {
            "empresa": empresa,
            "numero_pedido_tiny": numero_pedido_tiny,
            "data_venda": data_venda,
            "nome_cliente": nome_cliente,
            "numero_nfe": nota.get("numero_nfe", None),
            "valor_total": valor_total,
            "numero_pedido_ecommerce": numero_ecommerce,
            "marcadores": marcadores,
            # Aqui você pode preencher outros campos conforme disponível
            "numero_caso_marketplace": None,
            "status_venda": "Cancelado",
            "canal_venda": None,
            "previsao_entrega": None,
            "saldo_pedido": None,
            "situacao_devolucao": None,
            "codigo_rastreamento": None,
            "solucao_agente": None,
            "observacoes": None
        }

        # Inserir no banco (com validação de duplicidade)
        inserir_pedido(pedido_para_bd)

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()
    token = os.getenv("TINY_API_TOKEN_SP")

    # Parâmetros para teste, ajuste datas e marcadores conforme necessário
    data_inicial = "01/01/2022"
    data_final = "05/01/2022"
    marcador = "cancelamento"
    empresa = "GP SP"

    processar_pedidos(token, data_inicial, data_final, marcador, empresa)













#Coordena o fluxo entre API e banco de dados, puxa as funcoes criadas na pasta api, pega os pedidos e salva no banco de dados







