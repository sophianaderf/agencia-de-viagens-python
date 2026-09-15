import sqlite3
import os

caminho_banco = os.path.join(os.path.dirname(__file__), "agencia.db")

conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

conexao = sqlite3.connect("agencia_viagens.db")

cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


# ==========================================
# TABELA CLIENTE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL UNIQUE,
    data_de_nascimento DATE NOT NULL
)
""")


# ==========================================
# TABELA DESTINO
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS destino (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL
)
""")


# ==========================================
# TABELA HOTEL
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS hotel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    id_destino INTEGER,
    FOREIGN KEY (id_destino) REFERENCES destino(id)
)
""")


# ==========================================
# TABELA PACOTE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS pacote (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_pacote VARCHAR(50) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade_dias NUMERIC NOT NULL,
    id_destino INTEGER,
    FOREIGN KEY (id_destino) REFERENCES destino(id)
)
""")


# ==========================================
# TABELA FUNCIONARIO
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL UNIQUE
)
""")


# ==========================================
# TABELA RESERVA
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS reserva (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_reserva DATE NOT NULL,
    quantidade_pessoas NUMERIC NOT NULL,
    id_cliente INTEGER,
    id_pacote INTEGER,
    id_funcionario INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (id_pacote) REFERENCES pacote(id),
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id)
)
""")


# ==========================================
# TABELA PAGAMENTO
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS pagamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_total DECIMAL(10,2) NOT NULL,
    forma_pagamento VARCHAR(20) NOT NULL,
    quantidade_parcelas NUMERIC NOT NULL,
    valor_parcela DECIMAL(10,2) NOT NULL,
    data_pagamento DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Pendente',
    id_reserva INTEGER,
    FOREIGN KEY (id_reserva) REFERENCES reserva(id)
)
""")


# ==========================================
# INSERT CLIENTES
# ==========================================

cursor.execute("""
INSERT OR IGNORE INTO cliente
(nome, email, telefone, data_de_nascimento)
VALUES
('Ana Souza', 'ana.souza@email.com', '(11) 98888-1001', '1998-03-15'),
('Bruno Oliveira', 'bruno.oliveira@email.com', '(21) 97777-1002', '1995-07-22'),
('Carla Mendes', 'carla.mendes@email.com', '(31) 96666-1003', '2000-01-10'),
('Daniel Santos', 'daniel.santos@email.com', '(41) 95555-1004', '1992-11-05'),
('Eduarda Lima', 'eduarda.lima@email.com', '(51) 94444-1005', '1999-06-18'),
('Felipe Costa', 'felipe.costa@email.com', '(61) 93333-1006', '1994-09-27'),
('Gabriela Alves', 'gabriela.alves@email.com', '(71) 92222-1007', '2001-12-03'),
('Henrique Rocha', 'henrique.rocha@email.com', '(81) 91111-1008', '1997-04-30'),
('Isabela Martins', 'isabela.martins@email.com', '(85) 90000-1009', '1996-08-14'),
('João Pereira', 'joao.pereira@email.com', '(91) 98888-1010', '1993-02-25')
""")


# ==========================================
# INSERT FUNCIONÁRIOS
# ==========================================

cursor.execute("""
INSERT OR IGNORE INTO funcionario
(nome, cargo, email, telefone)
VALUES
('Mariana Ferreira', 'Agente de Viagens', 'mariana.ferreira@agencia.com', '(11) 98888-2001'),
('Lucas Almeida', 'Gerente', 'lucas.almeida@agencia.com', '(21) 97777-2002'),
('Patricia Ribeiro', 'Agente de Viagens', 'patricia.ribeiro@agencia.com', '(31) 96666-2003'),
('Rafael Gomes', 'Consultor de Viagens', 'rafael.gomes@agencia.com', '(41) 95555-2004'),
('Juliana Carvalho', 'Atendente', 'juliana.carvalho@agencia.com', '(51) 94444-2005'),
('Matheus Barbosa', 'Agente de Viagens', 'matheus.barbosa@agencia.com', '(61) 93333-2006'),
('Larissa Nunes', 'Consultora de Viagens', 'larissa.nunes@agencia.com', '(71) 92222-2007'),
('Gustavo Teixeira', 'Atendente', 'gustavo.teixeira@agencia.com', '(81) 91111-2008'),
('Camila Martins', 'Agente de Viagens', 'camila.martins@agencia.com', '(85) 90000-2009'),
('Rodrigo Fernandes', 'Gerente Comercial', 'rodrigo.fernandes@agencia.com', '(91) 98888-2010')
""")


# ==========================================
# INSERT DESTINOS
# ==========================================

cursor.execute("""
INSERT OR IGNORE INTO destino
(id, cidade, estado, pais, descricao)
VALUES
(1, 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil', 'Destino famoso pelas praias, pelo Cristo Redentor e pelo Pao de Acucar.'),
(2, 'Salvador', 'Bahia', 'Brasil', 'Cidade historica conhecida pelas praias, cultura e culinaria baiana.'),
(3, 'Gramado', 'Rio Grande do Sul', 'Brasil', 'Cidade turistica conhecida pelo clima frio, chocolates e arquitetura europeia.'),
(4, 'Foz do Iguacu', 'Parana', 'Brasil', 'Destino conhecido pelas Cataratas do Iguacu e pelo turismo de natureza.'),
(5, 'Florianopolis', 'Santa Catarina', 'Brasil', 'Cidade com belas praias, trilhas e paisagens naturais.'),
(6, 'Natal', 'Rio Grande do Norte', 'Brasil', 'Destino com praias, dunas e passeios de buggy.'),
(7, 'Maceio', 'Alagoas', 'Brasil', 'Cidade conhecida pelas aguas cristalinas e piscinas naturais.'),
(8, 'Recife', 'Pernambuco', 'Brasil', 'Destino com praias, cultura, historia e gastronomia regional.'),
(9, 'Sao Paulo', 'Sao Paulo', 'Brasil', 'Grande centro urbano com atracoes culturais, gastronomia e entretenimento.'),
(10, 'Belo Horizonte', 'Minas Gerais', 'Brasil', 'Cidade conhecida pela gastronomia, cultura e arquitetura.'),
(11, 'Buenos Aires', 'Buenos Aires', 'Argentina', 'Capital argentina conhecida pela arquitetura, tango e gastronomia.'),
(12, 'Santiago', 'Santiago', 'Chile', 'Destino com montanhas, vinicolas e atracoes culturais.'),
(13, 'Lisboa', 'Lisboa', 'Portugal', 'Capital portuguesa conhecida pela historia, cultura e gastronomia.'),
(14, 'Paris', 'Ile-de-France', 'Franca', 'Cidade famosa por seus monumentos, museus e gastronomia.'),
(15, 'Nova York', 'Nova York', 'Estados Unidos', 'Grande cidade conhecida por seus arranha-ceus, parques, museus e entretenimento.')
""")


# ==========================================
# INSERT HOTÉIS
# ==========================================

cursor.execute("""
INSERT OR IGNORE INTO hotel
(id, nome, endereco, telefone, id_destino)
VALUES
(1, 'Hotel Copacabana Palace', 'Avenida Atlantica, 1702 - Copacabana', '(21) 2548-7070', 1),
(2, 'Rio Beach Hotel', 'Rua Barata Ribeiro, 350 - Copacabana', '(21) 2255-1122', 1),
(3, 'Hotel Bahia Palace', 'Rua Chile, 20 - Centro Historico', '(71) 3333-4455', 2),
(4, 'Salvador Praia Hotel', 'Avenida Oceanica, 1500 - Barra', '(71) 3344-5566', 2),
(5, 'Gramado Garden Hotel', 'Rua Borges de Medeiros, 1200 - Centro', '(54) 3286-1122', 3),
(6, 'Hotel Serra Gaucha', 'Avenida das Hortensias, 850 - Centro', '(54) 3286-3344', 3),
(7, 'Hotel Cataratas', 'Avenida das Cataratas, 500 - Parque Nacional', '(45) 3521-7788', 4),
(8, 'Foz Tropical Hotel', 'Rua Brasil, 850 - Centro', '(45) 3574-8899', 4),
(9, 'Floripa Beach Hotel', 'Avenida Beira-Mar Norte, 1200', '(48) 3222-4455', 5),
(10, 'Hotel Ilha Bela', 'Rua das Gaivotas, 450 - Ingleses', '(48) 3234-6677', 5),
(11, 'Natal Dunas Hotel', 'Avenida Roberto Freire, 2000 - Ponta Negra', '(84) 3219-8899', 6),
(12, 'Ponta Negra Resort', 'Rua Erivan Franca, 100 - Ponta Negra', '(84) 3236-7788', 6),
(13, 'Maceio Mar Hotel', 'Avenida Alvaro Otacilio, 5500 - Jatiuca', '(82) 3325-1122', 7),
(14, 'Maceio Beach Resort', 'Rua Engenheiro Mario de Gusmao, 800 - Ponta Verde', '(82) 3344-2233', 7),
(15, 'Recife Praia Hotel', 'Avenida Boa Viagem, 900 - Boa Viagem', '(81) 3084-5566', 8),
(16, 'Mar Recife Hotel', 'Rua dos Navegantes, 1200 - Boa Viagem', '(81) 3344-7788', 8),
(17, 'Paulista Plaza Hotel', 'Avenida Paulista, 1500 - Bela Vista', '(11) 3251-7788', 9),
(18, 'Hotel Sao Paulo Center', 'Rua Augusta, 900 - Consolacao', '(11) 3122-8899', 9),
(19, 'Hotel Minas Gerais', 'Avenida Afonso Pena, 1200 - Centro', '(31) 3222-8899', 10),
(20, 'Belo Horizonte Plaza', 'Rua da Bahia, 800 - Centro', '(31) 3344-5566', 10),
(21, 'Buenos Aires Central Hotel', 'Avenida Corrientes, 850 - Centro', '+54 11 4321-5566', 11),
(22, 'Hotel Puerto Madero', 'Avenida Alicia Moreau, 500 - Puerto Madero', '+54 11 4455-7788', 11),
(23, 'Santiago Andes Hotel', 'Avenida Providencia, 1200 - Providencia', '+56 2 2233-7788', 12),
(24, 'Hotel Santiago Central', 'Rua San Antonio, 450 - Centro', '+56 2 2344-8899', 12),
(25, 'Lisboa Central Hotel', 'Rua Augusta, 150 - Baixa', '+351 21 3222-4455', 13),
(26, 'Hotel Lisboa Palace', 'Avenida da Liberdade, 300 - Lisboa', '+351 21 3344-6677', 13),
(27, 'Paris Eiffel Hotel', 'Rue de Commerce, 80 - Paris', '+33 1 4455-6677', 14),
(28, 'Hotel Paris Central', 'Rue de Rivoli, 250 - Paris', '+33 1 4566-7788', 14),
(29, 'New York Central Hotel', '5th Avenue, 500 - Manhattan', '+1 212-555-1001', 15),
(30, 'Manhattan Grand Hotel', 'Broadway, 800 - Manhattan', '+1 212-555-1002', 15)
""")


# ==========================================
# INSERT PACOTES
# ==========================================

cursor.execute("""
INSERT OR IGNORE INTO pacote
(id, nome_pacote, descricao, preco, quantidade_dias, id_destino)
VALUES
(1, 'Rio de Janeiro Completo', 'Passeio pelo Cristo Redentor, Pao de Acucar e praias do Rio de Janeiro.', 1899.90, 5, 1),
(2, 'Salvador Cultural', 'Conheca o centro historico, praias e os principais pontos turisticos de Salvador.', 1599.90, 5, 2),
(3, 'Gramado Encantador', 'Viagem especial para conhecer Gramado, Canela e os principais pontos da Serra Gaucha.', 2299.90, 6, 3),
(4, 'Aventura em Foz', 'Pacote com visita as Cataratas do Iguacu e principais atracoes da regiao.', 1799.90, 4, 4),
(5, 'Floripa Praias', 'Pacote para aproveitar as principais praias e paisagens de Florianopolis.', 1699.90, 5, 5),
(6, 'Natal e Dunas', 'Passeios pelas praias, dunas e lagoas de Natal.', 1999.90, 5, 6),
(7, 'Maceio Tropical', 'Pacote com praias, piscinas naturais e passeios pelo litoral de Alagoas.', 2099.90, 5, 7),
(8, 'Recife Cultural', 'Conheca Recife, Olinda e as principais praias da regiao.', 1499.90, 4, 8),
(9, 'Sao Paulo Experience', 'Pacote urbano com passeios culturais, gastronomia e entretenimento.', 1299.90, 4, 9),
(10, 'Belo Horizonte Sabores', 'Experiencia pela capital mineira com gastronomia e pontos historicos.', 1199.90, 4, 10),
(11, 'Buenos Aires Tango', 'Conheca os principais pontos turisticos e aproveite uma noite de tango.', 2999.90, 6, 11),
(12, 'Santiago dos Andes', 'Viagem para conhecer Santiago e as paisagens da Cordilheira dos Andes.', 3499.90, 7, 12),
(13, 'Lisboa Historica', 'Explore os principais monumentos e bairros historicos de Lisboa.', 4299.90, 7, 13),
(14, 'Paris Romantica', 'Pacote especial para conhecer os principais pontos turisticos de Paris.', 5999.90, 8, 14),
(15, 'Nova York Completa', 'Experiencia pelos principais pontos turisticos de Nova York.', 6499.90, 8, 15)
""")


# ==========================================
# INSERT RESERVAS
# ==========================================

cursor.execute("""
INSERT OR IGNORE INTO reserva
(id, data_reserva, quantidade_pessoas, id_cliente, id_pacote, id_funcionario)
VALUES
(1, '2026-09-01', 2, 1, 1, 1),
(2, '2026-09-02', 3, 2, 3, 2),
(3, '2026-09-03', 2, 3, 5, 3),
(4, '2026-09-04', 4, 4, 4, 4),
(5, '2026-09-05', 2, 5, 7, 5),
(6, '2026-09-06', 3, 6, 6, 6),
(7, '2026-09-07', 2, 7, 2, 7),
(8, '2026-09-08', 5, 8, 8, 8),
(9, '2026-09-09', 2, 9, 10, 9),
(10, '2026-09-10', 3, 10, 9, 10),
(11, '2026-09-11', 2, 1, 11, 1),
(12, '2026-09-12', 4, 2, 12, 2),
(13, '2026-09-13', 2, 3, 13, 3),
(14, '2026-09-14', 2, 4, 14, 4),
(15, '2026-09-15', 3, 5, 15, 5),
(16, '2026-09-15', 2, 6, 1, 6),
(17, '2026-09-15', 4, 7, 3, 7),
(18, '2026-09-15', 2, 8, 5, 8),
(19, '2026-09-15', 3, 9, 7, 9),
(20, '2026-09-15', 2, 10, 4, 10)
""")


# ==========================================
# INSERT PAGAMENTOS
# ==========================================

cursor.execute("""
INSERT OR IGNORE INTO pagamento
(id, valor_total, forma_pagamento, quantidade_parcelas, valor_parcela, data_pagamento, status, id_reserva)
VALUES
(1, 3799.80, 'Cartao de Credito', 3, 1266.60, '2026-09-01', 'Pago', 1),
(2, 6899.70, 'Pix', 1, 6899.70, '2026-09-02', 'Pago', 2),
(3, 3399.80, 'Cartao de Credito', 2, 1699.90, '2026-09-03', 'Pago', 3),
(4, 7199.60, 'Boleto', 4, 1799.90, '2026-09-04', 'Pendente', 4),
(5, 4199.80, 'Cartao de Debito', 1, 4199.80, '2026-09-05', 'Pago', 5),
(6, 5999.70, 'Pix', 1, 5999.70, '2026-09-06', 'Pago', 6),
(7, 3199.80, 'Cartao de Credito', 2, 1599.90, '2026-09-07', 'Pago', 7),
(8, 7499.50, 'Boleto', 5, 1499.90, '2026-09-08', 'Pendente', 8),
(9, 2399.80, 'Pix', 1, 2399.80, '2026-09-09', 'Pago', 9),
(10, 3899.70, 'Cartao de Credito', 3, 1299.90, '2026-09-10', 'Pago', 10),
(11, 5999.80, 'Cartao de Credito', 4, 1499.95, '2026-09-11', 'Pago', 11),
(12, 13999.60, 'Boleto', 4, 3499.90, '2026-09-12', 'Pendente', 12),
(13, 8599.80, 'Pix', 1, 8599.80, '2026-09-13', 'Pago', 13),
(14, 11999.80, 'Cartao de Credito', 2, 5999.90, '2026-09-14', 'Pago', 14),
(15, 19499.70, 'Cartao de Credito', 3, 6499.90, '2026-09-15', 'Pago', 15),
(16, 3799.80, 'Pix', 1, 3799.80, '2026-09-15', 'Pago', 16),
(17, 9199.60, 'Boleto', 4, 2299.90, '2026-09-15', 'Pendente', 17),
(18, 3399.80, 'Cartao de Debito', 1, 3399.80, '2026-09-15', 'Pago', 18),
(19, 8399.60, 'Cartao de Credito', 4, 2099.90, '2026-09-15', 'Pago', 19),
(20, 3599.80, 'Pix', 1, 3599.80, '2026-09-15', 'Cancelado', 20)
""")


# ==========================================
# SALVAR ALTERAÇÕES
# ==========================================

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")