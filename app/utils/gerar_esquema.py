from firebird.driver import connect
from app.config import FIREBIRD_DSN, FIREBIRD_USER, FIREBIRD_PASSWORD

def obter_esquema_com_descricao() -> str:
    # Extrai host, porta e caminho do DSN
    host_port, database_path = FIREBIRD_DSN.split(":", 1)
    host, port = host_port.split("/")

    # ✅ CORRETO (compatível com firebird-driver atual)
    conn = connect(
    database=FIREBIRD_DSN.replace("\\", "/"),
    user=FIREBIRD_USER,
    password=FIREBIRD_PASSWORD
)


    cur = conn.cursor()

    cur.execute("""
        SELECT rdb$relation_name
        FROM rdb$relations
        WHERE rdb$system_flag = 0 AND rdb$view_blr IS NULL
    """)
    tabelas = [linha[0].strip() for linha in cur.fetchall()]

    esquema = ""

    for tabela in sorted(tabelas):
        esquema += f"\n📌 {tabela.lower()}:\n"
        cur.execute(f"""
            SELECT
                rf.rdb$field_name,
                f.rdb$field_type,
                COALESCE(rf.rdb$description, f.rdb$description)
            FROM rdb$relation_fields rf
            JOIN rdb$fields f ON rf.rdb$field_source = f.rdb$field_name
            WHERE rf.rdb$relation_name = '{tabela}'
        """)
        for nome, tipo, descricao in cur.fetchall():
            nome = nome.strip().lower()
            tipo_str = tipo_nome(tipo)
            desc = descricao.strip() if descricao else gerar_descricao_auto(nome)
            esquema += f"- {nome} ({tipo_str}): {desc}\n"

    cur.close()
    conn.close()
    return esquema

def tipo_nome(tipo_id):
    tipos = {
        7: "SMALLINT", 8: "INTEGER", 10: "FLOAT", 12: "DATE", 13: "TIME",
        14: "CHAR", 16: "BIGINT/NUMERIC", 27: "DOUBLE", 35: "TIMESTAMP", 
        37: "VARCHAR", 261: "BLOB"
    }
    return tipos.get(tipo_id, f"UNKNOWN_TYPE_{tipo_id}")

def gerar_descricao_auto(nome):
    if "id" in nome:
        return "identificador relacionado"
    elif "data" in nome:
        return "data do evento"
    elif "nome" in nome:
        return "nome do item"
    elif "valor" in nome or "preco" in nome:
        return "valor monetário"
    elif "quant" in nome:
        return "quantidade numérica"
    return "informação relacionada"
