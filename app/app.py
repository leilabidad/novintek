import imp
from fastapi import FastAPI, HTTPException
from .products import *
from .cart import *
from .schemas import *
from app import schemas
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


##############

app = FastAPI()

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "stanleyjobson")
    correct_password = secrets.compare_digest(credentials.password, "swordfish")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}



###############3


sampleProduct = Products()
sampleCart = Cart()

@app.get('/products/', status_code=200)
async def greetings(username: str = Depends(get_current_username)) -> dict:
    """get all products"""
    sampleProduct.getProducts()
    return {"data":sampleProduct.response.text}

@app.get('/products/categories', status_code=200)
async def getCategories(username: str = Depends(get_current_username)) -> dict:
    """get all categories"""
    sampleProduct.getCategories()
    return {"data":sampleProduct.response.text}

@app.get('/products/{product_id}', status_code=200)
async def getProduct(product_id: int, username: str = Depends(get_current_username)) -> dict:
    """get a Product"""
    sampleProduct.getProduct(product_id)
    return {"data":sampleProduct.response.text}

######################### cart
@app.get('/carts/', status_code=200)
async def getAllCart(username: str = Depends(get_current_username)) -> dict:
    """get all carts"""
    sampleCart.getAll()
    return {"data":sampleCart.response.text}

@app.get('/carts/{item_id}', status_code=200)
async def getAllCart(item_id : int, username: str = Depends(get_current_username)) -> dict:
    """get all carts"""
    sampleCart.getSingle(item_id)
    return {"data":sampleCart.response.text}


@app.post('/carts', status_code=200)
async def addToCart(arrayJson : schemas.addToCart, username: str = Depends(get_current_username)) -> dict:
    """add to cart"""
    sampleCart.add(arrayJson)
    return {"data":sampleCart.response.text}

@app.put('/carts/{cart_id}', status_code=200)
async def updateCart(arrayJson : schemas.addToCart, cart_id: int, username: str = Depends(get_current_username)) -> dict:
    """update cart"""
    sampleCart.update(arrayJson, cart_id)
    return {"data":sampleCart.response.text}

@app.delete('/carts/{cart_id}', status_code=200)
async def deleteCart(cart_id: int, username: str = Depends(get_current_username)) -> dict:
    """delete cart"""
    sampleCart.delete(cart_id)
    return {"data":sampleCart.response.text}

######################### end cart
