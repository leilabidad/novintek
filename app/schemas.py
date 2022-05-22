from pydantic import BaseModel
from typing import Optional
from typing import List


class addToCart(BaseModel):

    userId : int 
    date : str
    products : List[dict]

    class Config:
        orm_mode = True
