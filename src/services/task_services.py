# from src.utils import *
from src.repos.repo import TaskRepo
from schemas.shcemas import *




class CreateTask:
    def __init__(self, task: TaskCreate, repo: TaskRepo):
        self.task = task
        self.repo = repo

    async def create_task(self):
        return await self.repo.create_task()






class UpdateTask:
    def __init__(self, task: TaskResponse, repo: TaskRepo):
        self.task = task
        self.repo = repo

    async def update_state(self):
        return await self.repo.update_state(user_id=self.task.user_id, task_id=self.task.id)
    




class DeleteTask:
    def __init__(self, task: TaskResponse, repo: TaskRepo):
        self.task = task 
        self.repo = repo

    
    async def delete_task(self):
        return await self.repo.delete_task(user_id=self.task.user_id, task_id=self.task.id)
    




class ListTask:
    def __init__(self, repo: TaskRepo ):
        self.repo = repo


    async def list_tasks(self, user_id: int, limit: int):
        tasks_db = await self.repo.list_my_tasks(user_id=user_id, limit=limit)

        if tasks_db:
        
            tasks: list[TaskResponse] = []
            for task in tasks_db:
                tasks.append(TaskResponse(**task))
            return tasks
        return False

        


    async def list_by_state(self, user_id, state):
        tasks_db = await self.repo.list_by_state(user_id=user_id, estado=state)
        if tasks_db:
            tasks: list[TaskResponse] = []
            for task in tasks_db:
                tasks.append(TaskResponse(**task))
            return tasks
        return False







