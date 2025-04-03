import pandas as pd
import firebird.driver
import os
from dotenv import load_dotenv

load_dotenv()

FIREBIRD_DSN = os.getenv("FIREBIRD_DSN").replace("\\", "/")
FIREBIRD_USER = os.getenv("FIREBIRD_USER")
FIREBIRD_PASSWORD = os.getenv("FIREBIRD_PASSWORD")

def executar_sql(sql: str) -> pd.DataFrame:
    try:
        conn = firebird.driver.connect(
            database=FIREBIRD_DSN,
            user=FIREBIRD_USER,
            password=FIREBIRD_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute(sql)

        colunas = [col[0] for col in cursor.description] if cursor.description else []
        dados = cursor.fetchall()

        df = pd.DataFrame(dados, columns=colunas)
        cursor.close()
        conn.close()
        return df

    except Exception as e:
        try:
            print("[ERRO] Erro ao executar SQL:", str(e).encode("ascii", errors="ignore").decode())
        except:
            print("[ERRO] Erro ao executar SQL: erro ao tratar string de erro")
        raise