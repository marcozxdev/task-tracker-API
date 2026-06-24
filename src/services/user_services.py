from src.security.security import verify_pwd, hash_pwd
from src.repos.repo import UserRepo, UserResponse
from src.schemas.shcemas import *





class AuthUse:
    def __init__(self, repo: UserRepo):
        self.repo = repo


    async def validate_user(self, user: UserValidation):
        user_db = await self.repo.get_user_by_email(user.email)
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


    async def get_user_by_id(self, id):
        data = await self.repo.get_user(id=id)
        if data:
            return UserResponse(**data)
        return None
    


class UpdateUser:
    def __init__(self,  repo: UserRepo):
        self.repo  = repo

    async def update_user(self, user: UserCreate, id: int):
        
        user.password = hash_pwd(user.password)
        return await self.repo.update_user(user=user, user_id=id)
        



class DeleteUser:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    
    async def delete_user(self, id: int):
        is_user = await GetUser(repo=self.repo).get_user_by_id(id=id)
        if not is_user:
            return False 
        return await self.repo.delete_user(user_id=id)







    

    
    

    

    

