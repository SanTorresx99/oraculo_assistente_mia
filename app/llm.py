from app.oraculos import vendas
from app.config import LLM_API  # ou TOGETHER_API_KEY se for alternar

def gerar_sql(pergunta: str, via: str = "ollama", modelo: str = None) -> str:
    prompt = vendas.montar_prompt(pergunta)
    return gerar_resposta(prompt, via=via, modelo=modelo)

def gerar_resposta(prompt: str, via: str = "ollama", modelo: str = None) -> str:
    # Aqui futuramente terá o roteamento entre LLMs (ollama, together etc.)
    # Por enquanto, simulação:
    print(f"[DEBUG] Enviando prompt para {via.upper()}")
    return f"-- SQL simulado baseado no prompt:\n-- {prompt.strip()[:60]}..."
