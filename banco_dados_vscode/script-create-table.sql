-- Active: 1788283801116@@127.0.0.1@5432@agencia_viagens
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL UNIQUE,
    data_de_nascimento DATE NOT NULL
);
CREATE TABLE destino (
    id SERIAL PRIMARY KEY,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL
);
CREATE TABLE hotel (
    ID SERIAL PRIMARY KEY, 
    nome VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    id_destino INTEGER REFERENCES destino(id)
);
CREATE TABLE pacote (
    id SERIAL PRIMARY KEY,
    nome_pacote VARCHAR(50) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade_dias NUMERIC NOT NULL,
    id_destino INTEGER REFERENCES destino(id)
);
CREATE TABLE funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo  VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL UNIQUE
);
CREATE TABLE reserva (
    id SERIAL PRIMARY KEY,
    data_reserva DATE NOT NULL,
    quantidade_pessoas NUMERIC NOT NULL,
    id_cliente INTEGER REFERENCES cliente(id),
    id_pacote INTEGER REFERENCES pacote(id),
    id_funcionario INTEGER REFERENCES funcionario(id)
);
CREATE TYPE status_pedido_enum AS ENUM ('Pendente', 'Pago', 'Cancelado');
CREATE TABLE pagamento (
    id SERIAL PRIMARY KEY,
    valor_total DECIMAL(10,2) NOT NULL,
    forma_pagamento VARCHAR(20) NOT NULL,
    quantidade_parcelas NUMERIC NOT NULL,
    valor_parcela DECIMAL(10,2) NOT NULL,
    data_pagamento DATE NOT NULL,
    status status_pedido_enum DEFAULT 'Pendente',
    id_reserva INTEGER REFERENCES reserva(id)
);