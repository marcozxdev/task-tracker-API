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
        
    def update_user(self):
        pass
        

    def delete_user(self):
        pass
        





class TaskRepo:
    def __int__(self, db: Database):
        self.db = db

    
    def create_task(self, task: TaskCreate):

        try:
            self.db.execute("""
            INSERT INTO tasks
            (titulo, descripcion, estado, user_id)
            VALUES (?, ?, ?, ?);
            """, (task.titulo, task.descripcion, task.estado, task.user_id))
            return True
        except:
            return False

    def list_my_tasks(self, user_id: int):
    
        self.db.execute("""
        SELECT tasks.id, tasks.titulo, tasks.descripcion, tasks.estado FROM tasks
        INNER JOIN users on	tasks.user_id = users.id
        WHERE users.id = ?
        """, (user_id,))
        tasks = self.db.fetchall()
        if tasks:
            return tasks
        return False 
        
            

    def find_task(self, user_id: int, titulo: str | None = None, limit: int=3):
        patron = f"%{titulo}%" 
        self.db.execute("""
        SELECT tasks.id, tasks.titulo, tasks.descripcion, tasks.estado FROM tasks
        INNER JOIN users on tasks.user_id = users.id
        WHERE users.id = ? AND tasks.titulo LIKE ?
        LIMIT ?
            """,(user_id, patron, limit))
        tasks = self.db.rollback()
        if tasks:
            return tasks
        return False
        

    def delete_task(self, user_id: int, task_id: int):
        pass

    def update_task(self, user_id: int, task_id: int):
        pass

    def list_by_state(self, user_id: int, estado: str):
        
        pass
        


    
    

    



