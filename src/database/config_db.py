from pathlib import Path
import sqlite3



def get_db_path():
    app_dir = Path.home() / ".tasks"
    app_dir.mkdir(exist_ok=True)
    return app_dir / "tasks.db"




DB_PATH = get_db_path()


class Database:

    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

        self.conn = sqlite3.connect(self.db_path)


        self.cursor = self.conn.cursor()

    # -------------------------
    # Métodos básicos
    # -------------------------

    def execute(self, query, params=None):
        """Ejecuta una consulta SQL con o sin parámetros."""
        if params is None:
            params = ()

        self.cursor.execute(query, params)

    def fetchone(self):
        """Recupera la siguiente fila de un resultado de consulta."""
        return self.cursor.fetchone()

    def fetchall(self):
        """Recupera todas las filas restantes de un resultado de consulta."""
        return self.cursor.fetchall()

    def commit(self):
        """Guarda permanentemente los cambios de la transacción actual en el disco."""
        self.conn.commit()

    def rollback(self):
        """Revierte los cambios de la transacción actual en caso de error."""
        self.conn.rollback()

    def close(self):
        """Cierra la conexión con el archivo de la base de datos."""
        self.conn.close()






# estructura de la base de datos
def estructure_db(database: Database):
    """
    Crea la tabla 'libros' y sus respectivos índices de búsqueda rápida
    si no existen previamente en la base de datos.
    """
    cursor = database.cursor

    
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""
    CREATE TABLE IF NOT EXIST users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_name TEXT NOT NULL,
                   password TEXT NOT NULL,
                   email TEX NOT NULL UNIQUE
                   );
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   descripcion TEX NOT NULL,
                   estado TEXT,
                   user_id INTEGER,
                   FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
    );
    """)

    # Confirma la creación de las tablas e índices
    database.commit()




def init_db():

    if not DB_PATH.exists():
        DB_PATH.touch()

    db = Database(DB_PATH)
    estructure_db(db)

    return db




### instancia de la db
db = init_db()