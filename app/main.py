from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from app.llm import gerar_resposta, gerar_sql
from app.utils.executar_fdb import executar_sql
from app.oraculos.vendas import montar_prompt
import pandas as pd
import unicodedata
import re

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
    print("✅ Recebida requisição no endpoint /executar-sql")
    try:
        print("[DEBUG] Enviando prompt para", payload.via.upper())

        prompt = montar_prompt(payload.pergunta)
        prompt_ascii = unicodedata.normalize('NFKD', prompt).encode('ascii', 'ignore').decode('ascii')
        prompt_ascii = re.sub(r'[^\x00-\x7F]+', '', prompt_ascii)
        print("[DEBUG] Prompt utilizado para gerar SQL:\n", prompt_ascii)

        sql_raw = gerar_sql(prompt_ascii)
        sql_ascii = unicodedata.normalize('NFKD', sql_raw).encode('ascii', 'ignore').decode('ascii')
        sql_ascii = re.sub(r'[^\x00-\x7F]+', '', sql_ascii)
        print("[DEBUG] SQL gerada:\n", sql_ascii)

        df: pd.DataFrame = executar_sql(sql_ascii)
        print("[DEBUG] DataFrame com", len(df), "linhas.")

        return {
            "sql_gerado": sql_ascii,
            "linhas": len(df),
            "dados": df.to_dict(orient="records")
        }
    except Exception as e:
        try:
            print("[ERRO] Falha ao executar SQL:", str(e).encode("ascii", errors="ignore").decode())
        except:
            print("[ERRO] Falha ao executar SQL: erro ao tratar string de erro")
        raise HTTPException(status_code=500, detail=f"Erro ao executar SQL: {str(e)}")

print("✅ main.py carregado até o fim.")
