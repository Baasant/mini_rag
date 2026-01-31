from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunck
from .enums.DataBaseEnum import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne

class ChunkModel(BaseDataModel):
    def __init__(self,db_client:object):
        super().__init__(db_client=db_client)
        self.collenction =self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value] #to get table that we have 
    async def create_chunck(self,chunk:DataChunck):
        result=await self.collenction.insert_one(chunk.dict(by_alias=True,exclude_unset=True))
        chunk._id=result.inserted_id
        return chunk
    
    async def get_chunk(self,chunk_id:str):
        result=await self.collection.find_one({

            "_id":ObjectId(chunk_id)
        })
        if result is None:
            return None
        
        return DataChunck(**result)
    
    async def insert_many_chunks(self,chunks:list,batch_size:int=100):
        for i in range(0,len(chunks),batch_size):
            batch=chunks[i:i+batch_size]

            operations=[InsertOne(chunk.dict(by_alias=True,exclude_unset=True))
                        for chunk in batch
                        
                        ]
            await self.collenction.bulk_write(operations)
        return len(chunks)
