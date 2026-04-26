# Controlador do banco de dados do bestiário

import sqlite3

print("Iniciando o Banco de dados do Bestiário")

# 1. Conectando ao banco de dados do bestiário
connect = sqlite3.connect("bestiary_data.db")
cursor = connect.cursor()

# 2. Cria a tabela 'monsters' e cria os valores
cursor.execute("""
    CREATE TABLE IF NOT EXISTS monsters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        _type TEXT,
        hp INTEGER
    )
""")

# 3. Cria a tabela 'suggests' e seus valores
cursor.execute("""
    CREATE TABLE IF NOT EXISTS suggests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        _type TEXT,
        hp INTEGER,
        suggested TEXT
    )
""")

connect.commit()
connect.close()