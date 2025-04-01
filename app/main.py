from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from app.llm import gerar_resposta, gerar_sql
from app.utils.executar_fdb import executar_sql
import pandas as pd

app = FastAPI(
    title="Oráculo Assistente MIA",
    description="API para consultas em linguagem natural com LLM local ou em nuvem (Together.ai)",
    version="0.1.0"
)

class PerguntaRequest(BaseModel):
    pergunta: str
    via: str = "ollama"
    modelo: str = None

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Oráculo rodando!"}

@app.get("/sql")
def gerar_sql_endpoint(pergunta: str = Query(..., description="Pergunta em linguagem natural")):
    try:
        resposta = gerar_sql(pergunta)
        return {"sql_gerado": resposta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.post("/perguntar")
def perguntar(payload: PerguntaRequest):
    try:
        resposta = gerar_resposta(
            prompt=payload.pergunta,
            via=payload.via,
            modelo=payload.modelo
        )
        return {"resposta": resposta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

# 🚀 Novo endpoint: executa a SQL no Firebird e retorna os dados
@app.post("/executar-sql")
def executar_sql_endpoint(payload: PerguntaRequest):
    print("✅ Endpoint /executar-sql registrado.")  # Debug
    try:
        sql = gerar_sql(payload.pergunta)
        df: pd.DataFrame = executar_sql(sql)

        return {
            "sql_gerado": sql,
            "linhas": len(df),
            "dados": df.to_dict(orient="records")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao executar SQL: {str(e)}")

print("✅ main.py carregado até o fim.")  # Debug global
