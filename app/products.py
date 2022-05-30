import requests

class Products(object):
    def __init__(self):

        self.url = "https://fakestoreapi.com/products/"

        self.payload={}
        self.headers = {}
        self.response = {}
        self.products = {}

    def getProducts(self):

        self.response = requests.request("GET", self.url, headers=self.headers, data=self.payload)

    def getProduct(self, product_id):

        self.response = requests.request("GET",self.url+str(product_id), headers=self.headers, data=self.payload)


    def getCategories(self):

        self.response = requests.request("GET",self.url+"categories", headers=self.headers, data=self.payload)

