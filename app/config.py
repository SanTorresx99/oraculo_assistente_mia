import os
from dotenv import load_dotenv

# Carrega o arquivo .env
load_dotenv()

# Configurações do banco de dados Firebird
FIREBIRD_DSN = os.getenv("FIREBIRD_DSN")
FIREBIRD_USER = os.getenv("FIREBIRD_USER")
FIREBIRD_PASSWORD = os.getenv("FIREBIRD_PASSWORD")

# API key da Together (se estiver usando modelo remoto)
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_MODELS = os.getenv("TOGETHER_MODELS")

# Endpoint local para LLM via Ollama (pode adicionar ao .env futuramente)
LLM_API = os.getenv("LLM_API", "http://localhost:11434/api/generate")
