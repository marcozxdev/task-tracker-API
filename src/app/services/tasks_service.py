#service

# importamos algunas funciones de el modulo repository y unas constantes tienen la direccion a los json

from app.repository.task_repository import (load, FILE_TASKS, save)
from app.models.tasks_model import Task

# varibles donde se cargan las tareas
tasks = load(FILE_TASKS) # vamos cargando los datos por si las moscas y medio tipandolos para fastapi



### funciones de listado
def ls(data=tasks) -> list[dict] | None: # lista todas las tareas
    if not data:
        return 


def list_done(data=tasks) -> list[dict] | None : # lista solo las tareas hechas
    pass


def list_progrres(data=tasks) -> list[dict] | None: # lista las tareas en progreso
    pass


def save_all(): # guarda todo para que no se pierda nada
    save(FILE_TASKS, tasks)




### funciones para añadir tareas
def add_task(task: Task):
    if not task:
        return "faltan argumentos en addtask"   # solo se guardan las tareas en tasks_progress
        
    
    # falta la logica de ver si una tarea se repite
    for i in tasks:
        if i["id"] == task.id:
            return 

    tasks.append(task.to_dict()) #es para añadir la tarea
    save_all()
    
    return

add_task(Task(len(tasks) + 1, "terminar la api", "implementar las routes de fastapi", "done"))



### funciones para marcar tareas
def mark_done(id: int):

    for task in tasks:
        if task["status"] == "progress" and task["ID"] == id:
            task["status"] = "done"
            save_all()


