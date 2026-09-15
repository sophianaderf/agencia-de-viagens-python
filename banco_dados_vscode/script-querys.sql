-- Ver tabelas com as informações completas 
SELECT * FROM cliente;
SELECT * FROM destino;
SELECT * FROM hotel;
SELECT * FROM pacote;
SELECT * FROM funcionario;
SELECT * FROM reserva;
SELECT * FROM pagamento;
-- Ver informações específicas
SELECT nome, email, telefone
FROM cliente;
-- Mostrar preços acima de R$ 3.000
SELECT nome_pacote, preco, quantidade_dias FROM pacote
WHERE preco > 3000;
-- Atualizar cargo de funcionarios
UPDATE funcionario SET cargo = 'Gerente de Vendas'
WHERE id = 1;
-- Deletar pagamento
DELETE FROM pagamento
WHERE id = 8;