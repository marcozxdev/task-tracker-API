from security.security import verify_pwd, hash_pwd
from src.repos.repo import UserRepo, UserResponse
from src.schemas.shcemas import *





class AuthUse:
    def __init__(self, user: UserValidation, repo: UserRepo):
        self.user = user
        self.repo = repo


    async def validate_user(self):
        user_db = await self.repo.get_user(self.user.email)
        if user_db:
            is_user = verify_pwd(self.user.password, user_db["password"])
            if is_user:
                return UserResponse(**user_db)
            else:
                return False
            
        return False
    





class CreateUser:
    def __init__(self, user: UserCreate, repo: UserRepo):
        self.user = user
        self.repo = repo

    
    async def create_user(self):
        return await self.repo.create_user(user=self.user)
    



class GetUser:
    def __init__(self, email: str, repo: UserRepo):
        self.email = email
        self.repo = repo


    async def get_user(self):
        data = await self.repo.get_user(email=self.email)
        return UserResponse(**data)
    


class UpdateUser:
    def __init__(self, user: UserCreate, repo: UserRepo, id: int | None = None):
        self.user = user
        self.repo  = repo
        self.id = id

    async def update_user(self):
        if self.id :
            return await self.repo.update_user(user=self.user, user_id=self.id)
        return None



class DeleteUser:
    def __init__(self, id: int, repo: UserRepo):
        self.id = id
        self.repo = repo

    
    async def delet_user(self):
        return self.repo.delete_user(user_id=self.id)






class UserService:
    def __init__(self, auth_user: UserResponse, repo: UserRepo):
        self.user = auth_user
        self.repo   = repo
    
    

    

    
    

    

    

