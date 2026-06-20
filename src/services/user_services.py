from security.security import verify_pwd, hash_pwd
from src.repos.repo import UserRepo, UserResponse
from src.schemas.shcemas import *





class AuthUse:
    def __init__(self, repo: UserRepo):
        self.repo = repo


    async def validate_user(self, user: UserValidation):
        user_db = await self.repo.get_user(user.email)
        if user_db:
            is_user = verify_pwd(user.password, user_db["password"])
            if is_user:
                return UserResponse(**user_db)
            else:
                return False
            
        return False
    





class CreateUser:
    def __init__(self, repo: UserRepo):
        self.repo = repo


    
    async def create_user(self, user: UserCreate):
        user.password = hash_pwd(user.password)
        return await self.repo.create_user(user=user)
    



class GetUser:
    def __init__( self, repo: UserRepo):
        self.repo = repo


    async def get_user(self, email):
        data = await self.repo.get_user(email=email)
        if data:
            return UserResponse(**data)
        return None
    


class UpdateUser:
    def __init__(self,  repo: UserRepo):
        self.repo  = repo

    async def update_user(self, user: UserCreate, id: int):
        if id is not None:
            return await self.repo.update_user(user=user, user_id=id)
        return None



class DeleteUser:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    
    async def delet_user(self, id: int):
        return await self.repo.delete_user(user_id=id)







    

    
    

    

    

