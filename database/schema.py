from database.connection import get_connection

def criar_tabela_pedidos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos_cancelados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_pedido_tiny TEXT,
            data_venda TEXT,
            nome_cliente TEXT,
            numero_nfe TEXT,
            valor_total REAL,
            numero_pedido_ecommerce TEXT,
            marcadores TEXT,
            numero_caso_marketplace TEXT,
            status_venda TEXT,
            canal_venda TEXT,
            previsao_entrega TEXT,
            saldo_pedido REAL,
            situacao_devolucao TEXT,
            codigo_rastreamento TEXT,
            solucao_agente TEXT,
            observacoes TEXT,
            atualizado_em TEXT
        )
    """)

    conn.commit()
    conn.close()