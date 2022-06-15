import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, insert, delete, update, and_
from dotenv import load_dotenv

load_dotenv()

# Cria Engine
""" engine = create_engine(
    f'mysql+pymysql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@localhost/mercado') """

engine = create_engine(f'sqlite:///./app/SQL/mercado.db')


def query2object(query_records):
    result_object = []
    for row in query_records:
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))
        result_object.append(d)

    return result_object


def commit_changes(stmt):
    with engine.connect() as conn:
        result = conn.execute(stmt)

    return result


class CrudProducts():
    def __init__(self):
        # Cria Base praparada a refletir o que já existe no banco de dados
        Base = automap_base()
        Base.prepare(engine, reflect=True)

        self.session = Session(engine)

        # Obtem tabelas do banco de dados
        self.Product = Base.classes.produto
        # self.CartProduct = Base.classes.carrinho_produto

    def create(self, creation_object):
        stmt = (
            insert(self.Product).
            values(nome=creation_object["nome"],
                   preco=creation_object["preco"],
                   categoria=creation_object["categoria"],
                   marca=creation_object["marca"],
                   descricao=creation_object["descricao"],
                   desconto=creation_object["desconto"])
        )

        return commit_changes(stmt)

    def get_all(self):
        records = self.session.query(self.Product).all()
        return query2object(records)

    def get_by_id(self, id_produto):
        record = self.session.query(
            self.Product).filter_by(id_produto=id_produto)

        return query2object(record)[0]

    def update_by_id(self, id_produto, update_object):
        record = self.get_by_id(id_produto)

        for key, value in update_object.items():
            if value != None:
                record[key] = value

        stmt = (
            update(self.Product).
            where(self.Product.id_produto == id_produto).
            values(nome=record["nome"],
                   preco=record["preco"],
                   categoria=record["categoria"],
                   marca=record["marca"],
                   descricao=record["descricao"],
                   esconto=record["desconto"])
        )

        return commit_changes(stmt)

    def delete_by_id(self, id_produto):
        stmt = (
            delete(self.Product).
            where(self.Product.id_produto == id_produto)
        )

        return commit_changes(stmt)


class CrudCarts():
    def __init__(self):
        # Cria Base praparada a refletir o que já existe no banco de dados
        Base = automap_base()
        Base.prepare(engine, reflect=True)

        self.session = Session(engine)

        # Obtem tabelas do banco de dados
        self.Cart = Base.classes.carrinho

    def create(self, creation_object):
        stmt = (
            insert(self.Cart).
            values(id_usuario=creation_object["id_usuario"])
        )

        return commit_changes(stmt)

    def get_all(self):
        records = self.session.query(self.Cart).all()
        return query2object(records)

    def get_by_id(self, id_carrinho):
        record = self.session.query(
            self.Cart).filter_by(id_carrinho=id_carrinho)
        return query2object(record)[0]

    def delete_by_id(self, id_carrinho):
        stmt = (
            delete(self.Cart).
            where(self.Cart.id_carrinho == id_carrinho)
        )

        return commit_changes(stmt)


class CrudCartsProducts():
    def __init__(self):
        # Cria Base praparada a refletir o que já existe no banco de dados
        Base = automap_base()
        Base.prepare(engine, reflect=True)

        self.session = Session(engine)

        # Obtem tabelas do banco de dados
        self.CartProduct = Base.classes.carrinho_produto

    def create(self, creation_object):
        stmt = (
            insert(self.CartProduct).
            values(id_carrinho=creation_object["id_carrinho"],
                   id_produto=creation_object["id_produto"],
                   quantidade=creation_object["quantidade"])
        )

        return commit_changes(stmt)

    def get_all(self):
        records = self.session.query(self.CartProduct).all()
        return query2object(records)

    def get_by_id(self, id_carrinho):
        record = self.session.query(
            self.CartProduct).filter_by(id_carrinho=id_carrinho)
        return query2object(record)

    def update_by_id(self, id_carrinho, id_produto, quantidade):

        stmt = (
            update(self.CartProduct).
            where((and_(self.CartProduct.id_carrinho == id_carrinho,
                        self.CartProduct.id_produto == id_produto))).
            values(quantidade=quantidade)
        )

        return commit_changes(stmt)

    def delete_by_id(self, id_carrinho, id_produto):
        stmt = (
            delete(self.CartProduct).
            where((and_(self.CartProduct.id_carrinho == id_carrinho,
                        self.CartProduct.id_produto == id_produto)))
        )

        return commit_changes(stmt)
