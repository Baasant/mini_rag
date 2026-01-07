from pydantic import BaseModel,Field, validator
from typing import Optional
from bson import ObjectId


class DataChunck(BaseModel):
    _id : Optional[ObjectId]
    chunck_test: str=Field(...,min_length=1)
    chunck_metadata:dict
    chunk_order:int =Field(...,gt=0)
    chunk_project_if :ObjectId

    class Config:
        arbitrary_types_allowed = True
    