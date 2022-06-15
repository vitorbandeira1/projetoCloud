from traceback import print_tb
from fastapi import FastAPI, Query, Path, Body, Header, HTTPException
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl
from fastapi.encoders import jsonable_encoder
from uuid import UUID

from sqlalchemy import except_

from .crud import *
crud_projects = CrudProducts()
crud_carts = CrudCarts()
crud_carts_products = CrudCartsProducts()

app = FastAPI()


# *********************************************************************************#
##################################### Produtos #####################################
# *********************************************************************************#
class ProductsIn(BaseModel):
    nome: str = Field(..., max_length=45)
    preco: float
    categoria: str = Field(..., max_length=45)
    desconto: float = Field(None, ge=0, le=1)
    marca: Optional[str] = Field(None, max_length=45)
    descricao: Optional[str] = Field(None, max_length=150)


class ProductsInOptional(BaseModel):
    nome: Optional[str] = Field(None, max_length=45)
    preco: Optional[float]
    categoria: Optional[str] = Field(None, max_length=45)
    desconto: Optional[float] = Field(None, ge=0, le=1)
    marca: Optional[str] = Field(None, max_length=45)
    descricao: Optional[str] = Field(None, max_length=150)


@app.get("/products/", tags=["Produto"])
async def get_all_products():
    data = crud_projects.get_all()
    return {"produtos": data}


@app.get("/products/{id_produto}", tags=["Produto"])
async def get_product(
    *,
    id_produto: int = Path(..., title="The ID of the product to get", ge=1)
):
    try:
        data = crud_projects.get_by_id(id_produto)
        return {"produto": data}
    except:
        raise HTTPException(status_code=404, detail="Product not found")

# Create itens


@app.post("/products/", tags=["Produto"])
async def create_product(
    product: ProductsIn = Body(
        ...,
        examples={
            "normal": {
                "summary": "Normal example",
                "description": "A **normal** request to create a product.",
                "value": {
                    "nome": "string",
                    "preco": 10.50,
                    "categoria": "string",
                    "desconto": 0.2,
                    "marca": "string",
                    "descricao": "string",
                },
            },
            "mandatory": {
                "summary": "Mandatory example",
                "description": "A **mandatory** request to create a product has to set these parameters.",
                "value": {
                    "nome": "string",
                    "preco": 10.50,
                    "categoria": "string",
                    "desconto": 0.0
                },
            }
        })
):
    json_produto = jsonable_encoder(product)

    try:
        crud_projects.create(json_produto)
        return {"message": "success"}
    except:
        raise HTTPException(status_code=400, detail="Wrong parameters.")


# Replace itens
@app.patch("/products/{id_produto}", tags=["Produto"])
async def replace_product(
    *,
    id_produto: int = Path(..., title="The ID of the product to get", ge=1),
    product: ProductsInOptional = Body(
        ...,
        examples={
            "normal": {
                "summary": "A complete example",
                "description": "A **complete** request to update, when you want to replace all fields of the product.",
                "value": {
                    "nome": "string",
                    "marca": "string",
                    "preco": 10.50,
                    "categoria": "string",
                    "descricao": "string",
                    "desconto": 0.2,
                },
            },
            "Choise": {
                "summary": "Choice of fields",
                "description": "Product will update only the values passed in the request.",
                "value": {
                    "preco": 20.50
                },
            }
        })
):

    try:
        json_produto_update = jsonable_encoder(product)
        crud_projects.update_by_id(id_produto, json_produto_update)

        return {"message": "success"}

    except:
        raise HTTPException(status_code=404, detail="Product not found")


# Delete data
@app.delete("/products/{id_produto}", tags=["Produto"])
async def delete_product(
    *,
    id_produto: int = Path(..., title="The ID of the product to get", ge=1),
):

    try:
        crud_projects.delete_by_id(id_produto)
        return {"message": "success"}
    except:
        raise HTTPException(status_code=404, detail="Product not found")


# *********************************************************************************#
##################################### Carrinho #####################################
# *********************************************************************************#
class CartIn(BaseModel):
    id_usuario: Optional[int] = Field(None, ge=1)


# Puxa lista de todos os carrinhos e seus donos
@app.get("/cart/", tags=["Carrinho"])
async def get_all_carts():
    data = crud_carts.get_all()
    return {"carrinho": data}


@app.get("/cart/{id_carrinho}", tags=["Carrinho"])
async def get_product(
    *,
    id_carrinho: int = Path(..., title="The ID of the cart to get", ge=1)
):
    try:
        data = crud_carts.get_by_id(id_carrinho)
        return {"carrinho": data}
    except:
        raise HTTPException(status_code=404, detail="Cart not found")


@app.post("/cart/", tags=["Carrinho"])
async def create_cart(
    cart: CartIn = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "To create a cart, you only need to pass the id of the user.",
                "value": {
                    "id_usuario": 1,
                },
            },
        }
    )
):
    json_carrinho = jsonable_encoder(cart)

    try:
        crud_carts.create(json_carrinho)
        return {"message": "success"}
    except:
        raise HTTPException(status_code=400, detail="Wrong parameters.")


@app.delete("/cart/{id_carrinho}", tags=["Carrinho"])
async def delete_cart(
    *,
    id_carrinho: int = Path(..., title="The ID of the cart to get", ge=1)
):

    try:
        crud_carts.delete(id_carrinho)
        return {"message": "success"}
    except:
        raise HTTPException(status_code=404, detail="Cart not found")

# *********************************************************************************#
################################ Produto Carrinho ##################################
# *********************************************************************************#
class CartProductIn(BaseModel):
    id_carrinho: int = Field(None, ge=1)
    id_produto: int = Field(None, ge=1)
    quantidade: int = Field(..., ge=1)


class Quantity(BaseModel):
    quantidade: int = Field(..., ge=1)


# Puxa lista de todos os carrinhos, produtos e quantidades
@app.get("/cart_product/", tags=["Carrinho Produto"])
async def get_all_carts():
    data = crud_carts_products.get_all()
    return {"carrinho_produto": data}


@app.get("/cart_product/{id_carrinho}", tags=["Carrinho Produto"])
async def get_cart_products(
    *,
    id_carrinho: int = Path(..., title="The ID of the cart to get", ge=1)
):
    try:
        data = crud_carts_products.get_by_id(id_carrinho)
        return {"carrinho_produto": data}
    except:
        raise HTTPException(status_code=404, detail="Cart not found")


@app.post("/cart_product/", tags=["Carrinho Produto"])
async def create_cart(
    cart_product: CartProductIn = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** example to create insert a product into a cart.",
                "value": {
                    "id_carrinho": 1,
                    "id_produto": 1,
                    "quantidade": 3
                },
            },
        }
    )
):
    json_cart_product = jsonable_encoder(cart_product)

    try:
        crud_carts_products.create(json_cart_product)
        return {"message": "success"}
    except:
        raise HTTPException(status_code=400, detail="Wrong parameters.")


@app.patch("/cart/{id_carrinho}/{id_produto}", tags=["Carrinho Produto"])
async def update_cart_product(
    *,
    id_carrinho: int = Path(..., title="The ID of the cart to get", ge=1),
    id_produto: int = Path(..., title="The ID of the product to get", ge=1),
    quantidade: Quantity = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** request to update a quantity of a product in a cart.",
                "value": {
                    "quantidade": 5
                },
            }
        })
):

    try:
        qtd = jsonable_encoder(quantidade)["quantidade"]
        crud_carts_products.update_by_id(id_carrinho, id_produto, qtd)
        return {"message": "success"}
    except:
        raise HTTPException(
            status_code=404, detail="Cart and Product association not found")


@app.delete("/cart/{id_carrinho}/{id_produto}", tags=["Carrinho Produto"])
async def delete_cart_product(
    *,
    id_carrinho: int = Path(..., title="The ID of the cart to get", ge=1),
    id_produto: int = Path(..., title="The ID of the product to get", ge=1)

):
    try:
        crud_carts_products.delete_by_id(id_carrinho, id_produto)
        return {"message": "success"}
    except:
        raise HTTPException(
            status_code=404, detail="Cart and Product association not found")
