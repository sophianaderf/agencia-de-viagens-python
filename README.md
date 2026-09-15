# Documento de requisitos do projeto

Nome do projeto: Agência de Viagens

Equipe de desenvolvimento: Laura Beatriz, Mayara Caetano, Sophia Nader

## Visão Geral do Sistema (Escopo)

O objetivo do projeto é desenvolver um sistema para gerenciamento de uma agência de viagens, permitindo o cadastro e a organização de informações sobre clientes, funcionários, destinos, hotéis, pacotes de viagens, reservas e pagamentos, proporcionando uma forma simples e eficiente de administrar os dados da agência.

## Requisitos Funcionais (RF)

RF01 Cadastro de clientes - O sistema deve permitir o cadastro de clientes, contendo as seguintes informações:

Nome;
E-mail;
Telefone;
Data de nascimento.

RF02 Cadastro de funcionários - O sistema deve permitir o cadastro de funcionários, contendo as seguintes informações:

Nome;
Cargo;
E-mail;
Telefone.

RF03 Cadastro de destinos - O sistema deve permitir o cadastro de destinos turísticos, contendo as seguintes informações:

Cidade;
Estado;
País;
Descrição.

RF04 Cadastro de hotéis - O sistema deve permitir o cadastro de hotéis relacionados aos destinos, contendo as seguintes informações:

Nome do hotel;
Endereço;
Telefone;
Destino.

RF05 Cadastro de pacotes - O sistema deve permitir o cadastro de pacotes de viagem, contendo as seguintes informações:

Nome do pacote;
Descrição;
Preço;
Quantidade de dias;
Destino.

RF06 Cadastro de reservas - O sistema deve permitir o registro de reservas, relacionando clientes, pacotes e funcionários, contendo as seguintes informações:

Cliente;
Pacote;
Funcionário;
Data da reserva;
Quantidade de pessoas.

RF07 Registro de pagamentos - O sistema deve permitir o registro dos pagamentos relacionados às reservas, contendo as seguintes informações:

Reserva;
Valor;
Quantidade de parcelas;
Valor da parcela;
Forma de pagamento;
Data do pagamento;
Status do pagamento.

RF08 Visualização dos dados - O sistema deve permitir que o usuário visualize os registros cadastrados de clientes, funcionários, destinos, hotéis, pacotes, reservas e pagamentos.

RF09 Menu de navegação - O sistema deve disponibilizar um menu principal para facilitar o acesso às funcionalidades de cadastro e visualização dos dados.

## Requisitos Não Funcionais (RNF)

RNF01 Gerenciamento de dados - O sistema deve armazenar e organizar as informações cadastradas de forma adequada, garantindo a integridade dos dados.

RNF02 Tempo de carregamento - O sistema deve apresentar um tempo de resposta adequado durante a utilização de suas funcionalidades.

RNF03 Usabilidade - O sistema deve possuir uma interface simples e organizada, facilitando a utilização pelo usuário.

RNF04 Organização do código - O sistema deve utilizar funções e módulos para manter o código organizado e facilitar sua manutenção.

## Restrições do Projeto

RT01 Linguagem de programação - O sistema deve ser desenvolvido utilizando obrigatoriamente a linguagem de programação Python.

RT02 Banco de dados - O sistema deve utilizar obrigatoriamente o SQLite como banco de dados para armazenamento persistente das informações.

RT03 Bibliotecas e tecnologias - A implementação do sistema deve utilizar os recursos disponíveis na linguagem Python e sua biblioteca para integração com o SQLite.