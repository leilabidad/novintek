import imp
from fastapi import FastAPI, HTTPException
from .products import *
from .cart import *
from .schemas import *
from app import schemas
app = FastAPI()

sampleProduct = Products()
sampleCart = Cart()

@app.get('/products/', status_code=200)
async def greetings() -> dict:
    """get all products"""
    sampleProduct.getProducts()
    return {"data":sampleProduct.response.text}

@app.get('/products/categories', status_code=200)
async def getCategories() -> dict:
    """get all categories"""
    sampleProduct.getCategories()
    return {"data":sampleProduct.response.text}

@app.get('/products/{product_id}', status_code=200)
async def getProduct(product_id: int) -> dict:
    """get a Product"""
    sampleProduct.getProduct(product_id)
    return {"data":sampleProduct.response.text}

######################### cart
@app.get('/carts/', status_code=200)
async def getAllCart() -> dict:
    """get all carts"""
    sampleCart.getAll()
    return {"data":sampleCart.response.text}

@app.get('/carts/{item_id}', status_code=200)
async def getAllCart(item_id : int) -> dict:
    """get all carts"""
    sampleCart.getSingle(item_id)
    return {"data":sampleCart.response.text}


@app.post('/carts', status_code=200)
async def addToCart(arrayJson : schemas.addToCart) -> dict:
    """add to cart"""
    sampleCart.add(arrayJson)
    return {"data":sampleCart.response.text}

@app.put('/carts/{cart_id}', status_code=200)
async def updateCart(arrayJson : schemas.addToCart, cart_id: int) -> dict:
    """update cart"""
    sampleCart.update(arrayJson, cart_id)
    return {"data":sampleCart.response.text}

@app.delete('/carts/{cart_id}', status_code=200)
async def deleteCart(cart_id: int) -> dict:
    """delete cart"""
    sampleCart.delete(cart_id)
    return {"data":sampleCart.response.text}

######################### end cart
