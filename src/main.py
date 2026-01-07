from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")
from  routes import base ,data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

app = FastAPI()

#with each event make action 
@app.on_event("startup")
async def startup_db_client():
    #get seeting to get the seeting of the application 
    settings=get_settings()

    app.mongo_conn=AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client=app.mongo_conn[settings.MONGODB_DATABASE]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()



app.include_router(base.base_router)
app.include_router(data.data_router)
 


# @app.get("/welcome")
# def welcome():
#     return {
#         "message": "Hello World!"
#     }