from app.utils.gerar_esquema import obter_esquema_com_descricao

def montar_prompt(pergunta: str) -> str:
    try:
        esquema = obter_esquema_com_descricao()
    except Exception as e:
        esquema = "-- Falha ao carregar esquema: " + str(e)

    prompt_base = f"""
Você é um assistente especializado em análise de vendas. 
Baseie suas respostas no seguinte esquema de banco de dados relacional (Firebird 3.0):

{esquema}

Regras:
- Gere a SQL sempre com base no esquema acima.
- Use sintaxe SQL compatível com Firebird 3.0.
- Não invente nomes de colunas ou tabelas.
- Quando possível, utilize JOINs entre tabelas que tenham relação.
- Se for necessário filtrar por datas, use o campo correto com BETWEEN.
- A resposta deve conter apenas a consulta SQL, sem explicações adicionais.

Pergunta: {pergunta}

SQL:
""".strip()

    return prompt_base
