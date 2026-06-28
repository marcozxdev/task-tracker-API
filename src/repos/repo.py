from src.database.config_db import Database
from src.schemas.shcemas import *






class UserRepo:
    def  __init__(self, db: Database):
        self.db = db

    

    async def get_user_by_email(self ,email: str):
        self.db.execute("""
        SELECT * FROM users
        WHERE email = ?
        """, (email,))
        user = self.db.fetchone()
        if user:
            return user
        return False


    async def get_user(self, id: int):
        self.db.execute("""
        SELECT * FROM users
        WHERE  id = ?
        """,( id,))
        data = self.db.fetchone()
        if data:
            return data
        return False

    async def create_user(self, user: UserCreate):
        """crea nuevo usario """
        try:
            self.db.execute("""
            INSERT INTO users (user_name, password, email) VALUES
            (?, ?, ?)""", (user.user_name, user.password, user.email))
            self.db.commit()
            return True 
        except:
            return False
        
    async def update_user(self, user: UserCreate, user_id: int):
        """actualiza toda la fila por id"""
        try:
            self.db.execute("""
            UPDATE users
            SET user_name = ?, password = ?, email = ?
            WHERE id = ?
            """, (user.user_name, user.password, user.email, user_id))
            self.db.commit()
            return True
        except:
            return False

    async def delete_user(self, user_id):
        """borra usuario por id"""
        try:
            self.db.execute("""
            DELETE FROM users
            WHERE id = ?
            """, (user_id,))
            self.db.commit()
            return True
        except:
            return False
        





class TaskRepo:
    def __init__(self, db: Database):
        self.db = db

    
    async def create_task(self, task: TaskCreate):
        """crea una nueva tarea"""

        try:
            self.db.execute("""
            INSERT INTO tasks
            (titulo, descripcion, estado, user_id)
            VALUES (?, ?, ?, ?);
            """, (task.titulo, task.descripcion, task.estado, task.user_id))
            self.db.commit()
            return True
        except:
            return False

    async def list_my_tasks(self, user_id: int, limit: int = 3):
        """lista las tareas de un usario desde la mas reciente con limite """
    
        self.db.execute("""
        SELECT tasks.id, tasks.titulo, tasks.descripcion, tasks.estado FROM tasks
        INNER JOIN users on	tasks.user_id = users.id
        WHERE users.id = ?
        ORDER BY tasks.id DESC
        LIMIT ?
        """, (user_id, limit))
        tasks = self.db.fetchall()
        if tasks:
            return tasks
        return False 
        
            

    async def find_task(self, user_id: int, titulo: str | None = None, limit: int=1):
        """busca tarea por titulo """
        patron = f"%{titulo}%" 
        self.db.execute("""
        SELECT tasks.id, tasks.titulo, tasks.descripcion, tasks.estado FROM tasks
        INNER JOIN users on tasks.user_id = users.id
        WHERE users.id = ? AND tasks.titulo LIKE ?
        LIMIT ?
            """,(user_id, patron, limit))
        tasks = self.db.fetchall()
        if tasks:
            return tasks
        return False
        

    async def delete_task(self, user_id: int, task_id: int):
        """borra tarea por  id  """
        try:
            self.db.execute("""
            DELETE FROM tasks
            WHERE id = ? AND user_id = ?
            """, (task_id, user_id))
            self.db.commit()
            return True
        except:
            return False

    async def update_state(self,estado: str, user_id: int, task_id: int):
        """actualiza el estado de una tarea"""
        try:
            self.db.execute("""
            UPDATE tasks
            SET estado = ?
            WHERE id = ? AND user_id = ?
        """,(estado, task_id, user_id))
            self.db.commit()
            return True
        except:
            return False

    async def list_by_state(self, user_id: int, estado: str):
        """lista tarea por estado"""
        self.db.execute("""
        SELECT tasks.id, titulo, descripcion, estado FROM tasks
        INNER JOIN users on tasks.user_id = users.id
        WHERE estado = ? AND tasks.user_id = ?
        """, (estado, user_id))
        data = self.db.fetchall()
        if data:
            return data
        return False

        


    
    

    



