import psycopg

def conectar():
    return psycopg.connect(
        dbname="agencia_viagens",
        user="postgres",            # O seu utilizador do PostgreSQL
        password="1234",  # <-- Substitua pela sua palavra-passe real do PostgreSQL
        host="localhost",
        port="5432"
    )