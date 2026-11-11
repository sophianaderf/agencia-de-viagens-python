import sqlite3
from pathlib import Path


CAMINHO_BANCO = Path(__file__).resolve().parent / "banco-de-dados" / "agencia_viagens.db"


def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao
