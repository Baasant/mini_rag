#route to upload data 
#split the riuters from the logic that should be done 
from fastapi import FastAPI ,APIRouter,Depends ,UploadFile
import os
from helpers.config import get_settings ,Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    # tag name 
    tags=["api_v1","data"]
)
#end points
#when upload i will give it a value to add files under it 
@data_router.post("/upload/{project_id}")
#function o the end point 
# defin project as string becouse there no mathmaticla operation will be done
async def upload_data(project_id :str ,file :UploadFile ,app_settings :Settings =Depends(get_settings)):
    #make some validation for the uploaded files before accept it 
    #max size of the files 
    #accepted types of the types
    #split the riuters from the logic that should be done thats why the logic will be written in another file

    is_valid ,result_signal=DataController().validate_uploaded_file(file=file)
    # return is_valid
    return {
        "signal":result_signal
    }
