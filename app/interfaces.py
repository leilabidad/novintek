from abc import ABCMeta, abstractmethod

class Shop(metaclass = ABCMeta):
    def __init__(self):
        self.url = "https://fakestoreapi.com/"

        self.payload={}
        self.headers = {}
        self.response = {}
        self.products = {}

    @abstractmethod
    def add(self,arrayJson):
        pass

    def update(self,arrayJson):
        pass

    def delete(self,arrayJson):
        pass


