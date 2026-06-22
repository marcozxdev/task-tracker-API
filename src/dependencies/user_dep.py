from fastapi import Depends
from src.repos.repo import UserRepo
from src.dependencies.db_dep import get_db
from src.services.user_services import *




def get_user_repo(db = Depends(get_db)):
    return UserRepo(db=db)



def get_create_user(repo: UserRepo = Depends(get_user_repo)):
    return CreateUser(repo=repo)


def get_update_user(repo: UserRepo = Depends(get_user_repo)):
    return UpdateUser(repo=repo)


def get_auth_user(repo: UserRepo = Depends(get_user_repo)):
    return AuthUse(repo=repo)



def get_delete_user(repo: UserRepo = Depends(get_user_repo)):
    return DeleteUser(repo=repo)



def get_user(repo: UserRepo = Depends(get_user_repo)):
    return GetUser(repo=repo)




