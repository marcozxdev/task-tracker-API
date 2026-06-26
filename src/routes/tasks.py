from fastapi import APIRouter, HTTPException, Depends
from src.schemas.shcemas import *
from src.dependencies.tasks_dep import *
from src.routes.user import get_current_user




router = APIRouter()


estados = ["HECHA", "EN-PROGRESO", "OLVIDADA"]

def rules_of_task(task: TaskCreate):



    if not task.estado in estados:
        raise HTTPException(400, headers="estado de tarea invalido")


    if not (len(task.titulo) >= 5 and len(task.descripcion) >= 5):
        raise HTTPException(400, headers="tamaño del titulo min 5 y descripcion min 5")
    
    return task



@router.post("/new_task/", status_code=201)
async def new_task(task: TaskReq, current_user: UserResponse = Depends(get_current_user), service: CreateTask = Depends(get_create_task)):



    task_m = TaskCreate(titulo=task.titulo, descripcion=task.descripcion, estado=estados[1], user_id=current_user.id)

    valide_rules = rules_of_task(task_m)
    if valide_rules:
        
        await service.create_task(task_m)
        return {"message": "task crated"}






@router.get("/list/")
async def  my_tasks(limit: int = 5, state: str = None ,current_user: UserResponse = Depends(get_current_user), service: ListTask = Depends(get_list_task)):

    user_id = current_user.id
    
    if state is None:
        tasks = await service.list_tasks(user_id=user_id, limit=limit)
        if not tasks:
            raise HTTPException(404)
        return tasks
    

    if state in estados:
        tasks = await service.list_by_state(user_id=user_id, state=state)
        if not tasks:
            raise HTTPException(404)
        return tasks
    
    raise HTTPException(400, detail="state invalide")




@router.get("/find/", status_code=200)
async def find_task(s: str, limit: int = 1,current_user: UserResponse = Depends(get_current_user), service: FindTask = Depends(get_find_task)):
                    
    user_id = current_user.id
    
    tasks = await service.find_task_by_title(user_id=user_id, title=s, limit=limit)
    if not tasks:
        raise HTTPException(404, detail="not task")

    return tasks




@router.patch("/state/{id_task}", status_code=200)
async def update_state(state: str, id_task: int, current_user: UserResponse = Depends(get_create_task), service: UpdateTask = Depends(get_update_task)):
    

    if not (state in estados):
        raise HTTPException(400, detail="state invalide")
    
    user_id = current_user.id

    update = await service.update_state(estado=state, user_id=user_id, task_id=id_task)
    if not update:
        raise HTTPException(404)
    






@router.delete("/del/{id_task}", status_code=204)
async def delete_task(id_task: int, current_user: UserResponse = Depends(get_current_user), service: DeleteTask = Depends(get_delete_task) ):


    user_id = current_user.id
    
    task_del = await service.delete_task_by_id(id_task=id_task, id_user=user_id)
    if not task_del:
        raise HTTPException(404, detail="task not delete")
    

    





    

