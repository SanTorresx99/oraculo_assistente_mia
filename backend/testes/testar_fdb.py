from backend.utils.conexao_firebird import criar_conexao
import pandas as pd
from rich import print

def testar_conexao_firebird():
    try:
        conn = criar_conexao()
        query = "SELECT 1 AS TESTE FROM RDB$DATABASE"
        df = pd.read_sql(query, conn)
        conn.close()

        print("\n✅ Conexão bem-sucedida! Resultado da consulta:")
        print(df)

    except Exception as e:
        print(f"\n❌ Erro ao conectar ou consultar o banco Firebird: {e}")

if __name__ == "__main__":
    testar_conexao_firebird()
