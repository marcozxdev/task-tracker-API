




# modelado de datos para guardar los datos de las tareas

class Task:
    def __init__(self, id: int, name_task: str, description: str, status: str): # un constructor para modelar los datos
        self.id = id                # para acomodar los datos
        self.name_task = name_task
        self.description = description
        self.status = status

    def to_dict(self) -> dict: # funcion que retorna un dict ya acomodado para integrar
        return {"id": self.id, "name_task": self.name_task, "description": self.description, "status": self.status}
