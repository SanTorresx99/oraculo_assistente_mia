# 🤖 Oráculo Assistente MIA

Sistema inteligente que utiliza LLMs da plataforma [Together.ai](https://www.together.ai/) para interpretar perguntas em linguagem natural e gerar comandos SQL para Firebird 3.0.

## 🔧 Tecnologias utilizadas

- Python 3.10+
- Firebird 3.0
- [fdb](https://pypi.org/project/fdb/) (driver Firebird)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
- Modelos LLM da [Together.ai](https://www.together.ai/)

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/SanTorresx99/oraculo_assistente_mia.git
   cd oraculo_assistente_mia

2. Crie e ative o amiente virtual:
   ```bash
   python3 -m venv venv
   source venv/Scripts/activate

3. Instale as dependencias:
  ```bash
  pip install -r requirements.txt

4.Crie o arquivo .env no projeto raiz com suas variáveis:
  ```bash
  #Conexões com modelos IA via together.ai:
  TOGETHER_API_KEY=sua_chave_aqui
  TOGETHER_MODELS=mistralai/Mistral-7B-Instruct-v0.2,meta-llama/Llama-3-8b-chat-hf,...
  #Conexão com seu database, no caso Firebird:
  FIREBIRD_DSN=localhost
  FIREBIRD_USER=usuario
  FIREBIRD_PASSWORD=senha

5.Execuções:

  #Para executar o teste das LLMs:
  ```bash
  python -m backend.testes.testar_modelo_llama3

  #Para executar SQL com base em perguntas em linguagem natural:
  ```bash
  python -m backend.testes.testar_ia_com_dados

6. Exemplos de uso:
  "Qual foi a última venda do cliente João?"
  "Quantas notas fiscais foram emitidas este mês?"

7.Estrutura do projeto (tree):

```bash
  backend/
  ├── core/
  │   └── corretor.py            # Aplica correções e refinamentos em instruções SQL geradas
  │
  ├── llms/
  │   └── orquestrador.py        # Gerencia a escolha e consulta de modelos LLM da Together.ai
  │
  ├── testes/
  │   └── testar_fdb.py          # Testa a conexão com o banco Firebird e executa uma query simples
  │   └── testar_modelo_llama3.py  # Executa e imprime respostas dos modelos LLM configurados via Together
  │
  ├── utils/
  │   └── conexao_firebird.py    # Realiza a conexão ao banco Firebird usando variáveis de ambiente
  │   └── prompts.py              # Armazena e organiza prompts utilizados nas requisições aos modelos
  |
  .env                                # Armazena chaves de API e credenciais sensíveis do banco Firebird
  |
  venv/ #repositório criado automáticamente com a criação do ambiente virtual