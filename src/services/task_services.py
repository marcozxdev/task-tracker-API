# from src.utils import *
from src.repos.repo import TaskRepo
from src.schemas.shcemas import *




class CreateTask:
    def __init__(self , repo: TaskRepo):
        self.repo = repo

    async def create_task(self, task: TaskCreate):
        return await self.repo.create_task(task=task)





class ListTask:
    def __init__(self, repo: TaskRepo ):
        self.repo = repo


    async def list_tasks(self, user_id: int, limit: int):
        tasks_db = await self.repo.list_my_tasks(user_id=user_id, limit=limit)

        if tasks_db:
            
            tasks: list = []
            for task in tasks_db:
                tasks.append(task)
            return tasks
        return False

        


    async def list_by_state(self, user_id: int, state: str):
        tasks_db = await self.repo.list_by_state(user_id=user_id, estado=state)
        if tasks_db:
            tasks: list = []
            for task in tasks_db:
                tasks.append(task)
            return tasks
        return False







class UpdateTask:
    def __init__(self, repo: TaskRepo):
        self.repo = repo

    async def update_state(self,estado: str, user_id: int, task_id: int ):

        return await self.repo.update_state(estado=estado, user_id=user_id, task_id=task_id)

        

    




class DeleteTask:
    def __init__(self, repo: TaskRepo):
        self.repo = repo

    
    async def delete_task_by_id(self,id_task: int, id_user: int):
        
        return await self.repo.delete_task(user_id=id_user, task_id=id_task)











class FindTask:
    def __init__(self, repo: TaskRepo):
        self.repo  = repo


    
    async def find_task_by_title(self, user_id: int, title: str, limit: int  = 1):
        tasks_db = await self.repo.find_task(user_id=user_id, titulo=title, limit=limit)
        if tasks_db:
            tasks: list = []
            for task in tasks_db:
                tasks.append(task)
            return tasks
        return None




