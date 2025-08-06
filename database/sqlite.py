import sqlite3
from datetime import datetime

def pedido_ja_existe(numero_pedido_tiny: str) -> bool:
    conexao = sqlite3.connect("banco/dados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT 1 FROM pedidos_cancelados WHERE numero_pedido_tiny = ?", (numero_pedido_tiny,))
    resultado = cursor.fetchone()

    conexao.close()
    return resultado is not None

def inserir_pedido(pedido: dict):
    if pedido_ja_existe(pedido.get("numero_pedido_tiny")):
        print(f"⚠️ Pedido {pedido.get('numero_pedido_tiny')} já existe no banco. Ignorando.")
        return

    conexao = sqlite3.connect("banco/dados.db")
    cursor = conexao.cursor()

    atualizado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO pedidos_cancelados (
            empresa,
            numero_pedido_tiny,
            data_venda,
            nome_cliente,
            numero_nfe,
            valor_total,
            numero_pedido_ecommerce,
            marcadores,
            numero_caso_marketplace,
            status_venda,
            canal_venda,
            previsao_entrega,
            saldo_pedido,
            situacao_devolucao,
            codigo_rastreamento,
            solucao_agente,
            observacoes,
            atualizado_em
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        pedido.get("empresa"),
        pedido.get("numero_pedido_tiny"),
        pedido.get("data_venda"),
        pedido.get("nome_cliente"),
        pedido.get("numero_nfe"),
        pedido.get("valor_total"),
        pedido.get("numero_pedido_ecommerce"),
        pedido.get("marcadores"),
        pedido.get("numero_caso_marketplace"),
        pedido.get("status_venda"),
        pedido.get("canal_venda"),
        pedido.get("previsao_entrega"),
        pedido.get("saldo_pedido"),
        pedido.get("situacao_devolucao"),
        pedido.get("codigo_rastreamento"),
        pedido.get("solucao_agente"),
        pedido.get("observacoes"),
        atualizado_em
    ))

    conexao.commit()
    conexao.close()

    print(f"✅ Pedido {pedido.get('numero_pedido_tiny')} inserido no banco.")
