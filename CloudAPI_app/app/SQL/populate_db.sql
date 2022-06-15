USE mercado;

-- CARRINHO
INSERT INTO carrinho VALUES (1, 1);
INSERT INTO carrinho VALUES (2, 1);
INSERT INTO carrinho VALUES (3, 2);
INSERT INTO carrinho VALUES (4, 3);

-- PRODUTO
INSERT INTO produto VALUES (1, "creme de avelã", "30.0", "doces", 0.0, "Nutella", "pote com 650g");
INSERT INTO produto VALUES (2, "macarrão", "2.0", "massas", 0.0, "Aurora", "pacote com 500g");
INSERT INTO produto VALUES (3, "refrigerante", "10.0", "bebidas", 0.0, "Coca-Cola", "garrafa pet de 2L");

-- PRODUTO CARRINHO
INSERT INTO carrinho_produto VALUES (1, 1, 1);
INSERT INTO carrinho_produto VALUES (1, 2, 5);
INSERT INTO carrinho_produto VALUES (1, 3, 2);
INSERT INTO carrinho_produto VALUES (2, 1, 2);
INSERT INTO carrinho_produto VALUES (3, 1, 1);
INSERT INTO carrinho_produto VALUES (4, 2, 4);
