# app/utils/executar_fdb.py

import pandas as pd
from firebird.driver import connect
from app.config import FIREBIRD_DSN, FIREBIRD_USER, FIREBIRD_PASSWORD

def executar_sql(sql: str) -> pd.DataFrame:
    """
    Executa uma query SQL no banco Firebird e retorna um DataFrame com os resultados.
    """
    try:
        dsn = FIREBIRD_DSN.replace  # Garante compatibilidade com Firebird
    except Exception:
        raise ValueError("FIREBIRD_DSN inválido. Use o formato host/porta:caminho_banco")

    conn = connect(
    database=dsn,
    user=FIREBIRD_USER,
    password=FIREBIRD_PASSWORD
)

    cur = conn.cursor()
    cur.execute(sql)

    colunas = [col[0].strip() for col in cur.description]
    dados = cur.fetchall()

    cur.close()
    conn.close()

    return pd.DataFrame(dados, columns=colunas)

if __name__ == "__main__":
    sql = """
    SELECT
      f.nome_fantasia,
      i.codigo,
      p.nome,
      SUM(i.quantidade) AS total_vendido
    FROM item_nota_propria i
    JOIN produto p ON p.id = i.id_produto
    JOIN nota_propria n ON n.id = i.id_nota
    JOIN pessoa f ON f.id = n.id_cliente
    WHERE EXTRACT(YEAR FROM n.data_emissao) = 2024
    GROUP BY f.nome_fantasia, i.codigo, p.nome
    ORDER BY total_vendido DESC
    """
    df = executar_sql(sql)
    print(df.head())
