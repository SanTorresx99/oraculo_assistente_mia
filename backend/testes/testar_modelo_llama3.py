import requests
from dotenv import load_dotenv
import os
from rich import print

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

MODELOS = [
    "mistralai/Mistral-7B-Instruct-v0.2",
    "meta-llama/Llama-3-8b-chat-hf",
    "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    "meta-llama/Llama-Vision-Free"
]

prompt = "Quem foi Aristóteles?"

for modelo in MODELOS:
    print(f"\n🔍 Modelo: [bold yellow]{modelo}[/bold yellow]")

    payload = {
        "model": modelo,
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7,
        "top_p": 0.7
    }

    try:
        response = requests.post("https://api.together.xyz/inference", headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()

        # Tenta primeiro via "output", depois fallback para "choices" direto (caso Vision-Free)
        choices = data.get("output", {}).get("choices")
        if not choices:
            choices = data.get("choices")

        if choices and isinstance(choices[0], dict):
            resposta = choices[0].get("text", "").strip()
        else:
            resposta = "[Resposta não formatada como texto]"

        print(f"🧠 Resposta: [green]{resposta}[/green]")

    except Exception as e:
        print(f"❌ Erro ao consultar modelo {modelo}: [red]{e}[/red]")
