import fdb
import pandas as pd
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

FIREBIRD_DSN = os.getenv("FIREBIRD_DSN")
FIREBIRD_USER = os.getenv("FIREBIRD_USER")
FIREBIRD_PASSWORD = os.getenv("FIREBIRD_PASSWORD")

def criar_conexao():
    """Cria uma conexão com o banco de dados Firebird."""
    return fdb.connect(
        dsn=FIREBIRD_DSN,
        user=FIREBIRD_USER,
        password=FIREBIRD_PASSWORD
    )

def executar_sql_com_dataframe(sql: str) -> pd.DataFrame:
    """Executa uma consulta SQL e retorna o resultado como DataFrame."""
    conn = criar_conexao()
    try:
        df = pd.read_sql(sql, conn)
        return df
    finally:
        conn.close()
