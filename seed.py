import sqlite3
import os
from faker import Faker
import random

# Inicializa o Faker configurado para Português do Brasil
fake = Faker('pt_BR')

def popular_banco():
    caminho_banco = os.path.join(os.path.dirname(__file__), "banco-de-dados", "agencia_viagens.db")
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    print("Iniciando a geração de dados com Faker...")

    # 1. Gerar Clientes
    for _ in range(15):
        nome = fake.name()
        email = fake.unique.email()
        telefone = fake.unique.cellphone_number()
        data_nasc = fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d')
        cursor.execute(
            "INSERT INTO cliente (nome, email, telefone, data_de_nascimento) VALUES (?, ?, ?, ?)",
            (nome, email, telefone, data_nasc)
        )

    # 2. Gerar Funcionários
    cargos = ['Agente de Viagens', 'Gerente', 'Consultor de Viagens', 'Atendente']
    for _ in range(8):
        nome = fake.name()
        cargo = random.choice(cargos)
        email = fake.unique.company_email()
        telefone = fake.unique.cellphone_number()
        cursor.execute(
            "INSERT INTO funcionario (nome, cargo, email, telefone) VALUES (?, ?, ?, ?)",
            (nome, cargo, email, telefone)
        )

    # 3. Gerar Reservas e Pagamentos vinculados aos dados gerados
    cursor.execute("SELECT id FROM cliente")
    clientes_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT id FROM funcionario")
    func_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT id, preco FROM pacote")
    pacotes = cursor.fetchall()

    formas_pagamento = ['Pix', 'Cartao de Credito', 'Cartao de Debito', 'Boleto']
    status_list = ['Pago', 'Pendente', 'Cancelado']

    if clientes_ids and func_ids and pacotes:
        for _ in range(10):
            cliente_id = random.choice(clientes_ids)
            func_id = random.choice(func_ids)
            pacote_id, preco_pacote = random.choice(pacotes)
            qtd_pessoas = random.randint(1, 4)
            data_reserva = fake.date_between(start_date='-6m', end_date='today').strftime('%Y-%m-%d')

            cursor.execute(
                "INSERT INTO reserva (data_reserva, quantidade_pessoas, id_cliente, id_pacote, id_funcionario) VALUES (?, ?, ?, ?, ?)",
                (data_reserva, qtd_pessoas, cliente_id, pacote_id, func_id)
            )
            reserva_id = cursor.lastrowid

            # Pagamento da reserva
            valor_total = float(preco_pacote) * qtd_pessoas
            forma = random.choice(formas_pagamento)
            parcelas = 1 if forma in ['Pix', 'Cartao de Debito'] else random.randint(1, 6)
            valor_parcela = round(valor_total / parcelas, 2)
            status = random.choice(status_list)

            cursor.execute(
                "INSERT INTO pagamento (valor_total, forma_pagamento, quantidade_parcelas, valor_parcela, data_pagamento, status, id_reserva) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (valor_total, forma, parcelas, valor_parcela, data_reserva, status, reserva_id)
            )

    conexao.commit()
    conexao.close()
    print("Banco de dados populado com sucesso via Faker!")

if __name__ == '__main__':
    popular_banco()