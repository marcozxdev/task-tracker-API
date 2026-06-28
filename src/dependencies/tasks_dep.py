from fastapi import Depends

from src.repos.repo import TaskRepo
from src.services.task_services import *
from src.dependencies.db_dep import get_db




def get_task_repo(db = Depends(get_db)):
    return TaskRepo(db=db)



def get_list_task(repo: TaskRepo = Depends(get_task_repo)):
    return ListTask(repo=repo)




def get_create_task(repo: TaskRepo = Depends(get_task_repo)):
    return CreateTask(repo=repo)


def get_find_task(repo: TaskRepo = Depends(get_task_repo)):
    return FindTask(repo=repo)


def get_update_task(repo: TaskRepo = Depends(get_task_repo)):
    return UpdateTask(repo=repo)



def get_delete_task(repo: TaskRepo = Depends(get_task_repo)):
    return DeleteTask(repo=repo)