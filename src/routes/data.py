#route to upload data 
#split the riuters from the logic that should be done 
from fastapi import FastAPI ,APIRouter,Depends ,UploadFile,status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings ,Settings
from controllers import DataController,ProjectController
import aiofiles
from models import ResponseSignal
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
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":result_signal
            }
        )
    
    project_dir_path=ProjectController().get_project_path(project_id=project_id)
    file_path=os.path.join(
        project_dir_path,file.filename
    )

    async with aiofiles.open(file_path,"wb") as f :
        while chuck:=await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chuck)
    return JSONResponse(
        content={
            "signal":ResponseSignal.FILE_UPLOAD_SUCESS.value
        }
    )        
    # return {
    #     "signal":result_signal
    # }

