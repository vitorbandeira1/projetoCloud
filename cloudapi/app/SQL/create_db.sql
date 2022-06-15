-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS mercado ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS mercado;
USE mercado ;

-- -----------------------------------------------------
-- Table mercado.carrinho
-- -----------------------------------------------------
DROP TABLE IF EXISTS mercado.carrinho ;

CREATE TABLE IF NOT EXISTS mercado.carrinho (
  id_carrinho INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  PRIMARY KEY (id_carrinho));

-- -----------------------------------------------------
-- Table mercado.produto
-- -----------------------------------------------------
DROP TABLE IF EXISTS mercado.produto ;

CREATE TABLE IF NOT EXISTS mercado.produto (
  id_produto INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  preco FLOAT NOT NULL,
  categoria VARCHAR(45) NOT NULL,
  desconto FLOAT NOT NULL,
  marca VARCHAR(45) NULL,
  descricao VARCHAR(100) NULL,
  PRIMARY KEY (id_produto));

-- -----------------------------------------------------
-- Table mercado.carrinho_produto
-- -----------------------------------------------------
DROP TABLE IF EXISTS mercado.carrinho_produto ;

CREATE TABLE IF NOT EXISTS mercado.carrinho_produto (
  id_carrinho INT NOT NULL,
  id_produto INT NOT NULL,
  quantidade INT NOT NULL,
  PRIMARY KEY (id_carrinho, id_produto),
  INDEX fk_id_produto_idx (id_produto ASC) VISIBLE,
  CONSTRAINT fk_id_carrinho
    FOREIGN KEY (id_carrinho)
    REFERENCES mercado.carrinho (id_carrinho)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_id_produto
    FOREIGN KEY (id_produto)
    REFERENCES mercado.produto (id_produto)
    ON DELETE CASCADE
    ON UPDATE CASCADE);