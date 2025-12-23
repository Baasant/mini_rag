#class 
from .BaseController import BaseController
from fastapi import UploadFile
class DataController(BaseController):

    def __init__(self):
        #to wakeup the paerent class
        super().__init__()
        #convert MB to bytes 1024*1024
        self.size_scale=1048576
    
    def validate_uploaded_file(self,file :UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        if file.size > self.app_settings.FIle_MAX_SIZE*self.size_scale:
            return False
        return True



    
