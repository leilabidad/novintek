import requests
from .interfaces import Shop
from .schemas import *
from app import schemas

class Cart(Shop):
    Shop.prefix = "carts"
    def getAll(self):
        self.response = requests.request("GET", self.url+"/"+Shop.prefix, headers=self.headers, data=self.payload)

    def getSingle(self, item_id:int):
        self.response = requests.request("GET", self.url+"/"+Shop.prefix+"/"+str(item_id), headers=self.headers, data=self.payload)

    def getLimit(self, limit:int):
        self.response = requests.request("GET", self.url+Shop.prefix+"?limit="+str(limit), headers=self.headers, data=self.payload)

    def getSort(self, sort:str):
        self.response = requests.request("GET", self.url+Shop.prefix+"?sort="+sort, headers=self.headers, data=self.payload)

    def add(self,arrayJson:schemas.addToCart):
        self.response = requests.request("POST", self.url+Shop.prefix, headers=self.headers, data=self.payload)

    def update(self, arrayJson:schemas.addToCart, cart_id:int):
        self.response = requests.request("PUT", self.url+Shop.prefix+"/"+str(cart_id), headers=self.headers, data=self.payload)

    def delete(self, cart_id:int):
        self.response = requests.request("DELETE", self.url+Shop.prefix+"/"+str(cart_id), headers=self.headers, data=self.payload)
