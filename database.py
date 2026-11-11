import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def criar_conexao():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("Configure a variável de ambiente DATABASE_URL.")

    return psycopg.connect(database_url, connect_timeout=10)
