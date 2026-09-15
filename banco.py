import sqlite3
import os


def conectar():
    caminho_banco = os.path.join(
        os.path.dirname(__file__),
        "banco-de-dados",
        "agencia_viagens.db"
    )

    return sqlite3.connect(caminho_banco)