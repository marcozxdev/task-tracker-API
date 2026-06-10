from src.database.config_db import Database
from src.schemas.shcemas import *






class UserRepo:
    def  __init__(self, db: Database):
        self.db = db

    def create_user(self, user: UserCreate):
        try:
            self.db.execute("""
            INSERT INTO users (user_name, password, email) VALUES
            (?, ?, ?)""", (user.user_name, user.password, user.email))
            self.db.commit()
            return True 
        except:
            return False
        

    def delete_user(self):
        pass
        





class TaskRepo:
    def __int__(self, db):
        self.db = db

    
    def create_task(self):
        pass

    def list_my_tasks(self):
        pass

    def find_task(self):
        pass

    def delete_task(self):
        pass

    def update_task(self):
        pass

    def list_by_state(self):
        pass
        


    
    

    











