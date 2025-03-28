# 🤖 Oráculo Assistente MIA

Sistema inteligente que utiliza LLMs da plataforma [Together.ai](https://www.together.ai/) para interpretar perguntas em linguagem natural e gerar comandos SQL para Firebird 3.0.

---

## 🔧 Tecnologias utilizadas

- Python 3.10+
- Firebird 3.0
- [fdb](https://pypi.org/project/fdb/) – driver Firebird
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
- Modelos LLM da [Together.ai](https://www.together.ai/)

---

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SanTorresx99/oraculo_assistente_mia.git
   cd oraculo_assistente_mia

2. **Crie e ative o ambiente virtual:**

bash
python -m venv venv
source venv/Scripts/activate  # ou venv/bin/activate no Linux/macOS

**Instale as dependências:**
bash
pip install -r requirements.txt
Crie o arquivo .env na raiz do projeto com suas variáveis de ambiente:

ini
# Conexão com a Together.ai
TOGETHER_API_KEY=sua_chave_aqui
TOGETHER_MODELS=mistralai/Mistral-7B-Instruct-v0.2,meta-llama/Llama-3-8b-chat-hf,...

# Conexão com banco Firebird
FIREBIRD_DSN=localhost
FIREBIRD_USER=usuario
FIREBIRD_PASSWORD=senha

**▶️ Execução**
Para testar os modelos LLMs:
bash
python -m backend.testes.testar_modelo_llama3
Para gerar SQL com base em perguntas em linguagem natural:

```bash
python -m backend.testes.testar_ia_com_dados

**💡 Exemplos de uso**
"Qual foi a última venda do cliente João?"

"Quantas notas fiscais foram emitidas este mês?"

"Liste os produtos mais vendidos no último trimestre."

**🧩 Estrutura do projeto**
```bash
backend/
├── core/
│   └── corretor.py              # Aplica correções e refinamentos em instruções SQL geradas
│
├── llms/
│   └── orquestrador.py          # Gerencia a escolha e consulta de modelos LLM da Together.ai
│
├── testes/
│   ├── testar_fdb.py            # Testa a conexão com o banco Firebird
│   └── testar_modelo_llama3.py  # Testa execução e respostas dos modelos LLM
│
├── utils/
│   ├── conexao_firebird.py      # Realiza conexão ao banco Firebird usando .env
│   └── prompts.py               # Organiza prompts usados nas requisições

.env                              # Armazena variáveis sensíveis (NÃO subir ao GitHub)
venv/                             # Ambiente virtual Python (ignorado pelo Git)
