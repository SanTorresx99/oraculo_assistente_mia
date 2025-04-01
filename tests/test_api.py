# tests/test_api.py

import requests

# Testa o endpoint /ping
def testar_ping():
    response = requests.get("http://127.0.0.1:8000/ping")
    print("/ping =>", response.json())

# Testa o endpoint /sql
def testar_sql():
    pergunta = "Quais os 5 produtos mais vendidos em janeiro de 2024?"
    response = requests.post(f"http://127.0.0.1:8000/sql", params={"pergunta": pergunta})
    print("/sql =>", response.json())

# Testa o endpoint /perguntar
def testar_perguntar():
    payload = {
        "pergunta": "Quais os 5 produtos mais vendidos em janeiro de 2024?",
        "via": "ollama",  # ou "together"
        }
    response = requests.post("http://127.0.0.1:8000/perguntar", json=payload)
    print("/perguntar =>", response.json())

# Executa todos os testes
if __name__ == "__main__":
    testar_ping()
    testar_sql()
    testar_perguntar()
