from pydantic import BaseModel
from typing import Optional
class ProcessRequest(BaseModel):
    file_id:str
    chunck_size: Optional[int]=100 #this is optional the user not necessary to add by the user
    overlap_size: Optional[int]=20
    #if u have anything releated to the same file and i need to reset all the saving and start from scratch

    do_reset :Optional[int]=0
    
