import sqlite3

conexao = sqlite3.connect("agencia_viagens.db")

print("Banco conectado com sucesso!")

conexao.close()