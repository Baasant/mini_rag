from .BaseDataModel import BaseDataModel
from .db_schemes import Project
from .enums.DataBaseEnum import DataBaseEnum
class ProjectModel(BaseDataModel):
    #need project schema
    def __init__(self,db_client:object):
        super().__init__(db_client=db_client)
        self.collenction =self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value] #to get table that we have 

    #functions to make ssome operation onthe data

    async def create_project(self,project:Project):
        result=await self.collenction.insert_one(project.dict()) #to wait till it connect the data
        project._id=result.inserted_id
        return project
    
    async def get_project_or_create_one(self,project_id:str):
        record=await self.collenction.find_one({
            "project_id":project_id
        })
        if record is None:
            #create new project
            project= Project(project_id=project_id)
            project =await self.create_project(project=project
            )
            return project
        return Project(**record)
    
    async def get_all_projects(self, page: int=1, page_size: int=10):
         # count total number of documents
        total_documents = await self.collection.count_documents({})
        total_pages = total_documents // page_size
        if total_documents % page_size > 0:
            total_pages += 1

        cursor=self.collenction.find().skip( (page-1) * page_size).limit(page_size)
        projects=[]
        async for documnt in cursor:
            projects.append(
                Project(**documnt)
            )
        return projects,total_pages





    
    



    