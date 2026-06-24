
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.schemas.shcemas import *
from src.security.jwt_handler import *
from typing import Annotated
from src.dependencies.user_dep import *



router = APIRouter()
oauth_schema = OAuth2PasswordBearer(tokenUrl="login")





async def get_current_user(token: Annotated[str, Depends(oauth_schema) ], service: GetUser = Depends(get_user)):
    payload = decode_access_token(token=token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Not authenticated", headers={"WWW-Authenticate": "Bearer"})



    id = payload.get("id")

    
    user = await service.get_user_by_id(id=id)

    if not user:
        raise HTTPException(404, detail="User not found")

    return UserResponse(user_name=user.user_name, email=user.email, id=user.id)









@router.post("/login", status_code=201)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], service: AuthUse = Depends(get_auth_user)):

    user: UserResponse = await service.validate_user(UserValidation(email=form_data.username, password=form_data.password))

    if not user:
        raise HTTPException(401, detail="incorrect username or password")
    

    token = create_access_token(id=user.id, email=user.email)

    return {
        "access_token": token,
        "token_type": "bearer"
    }



async def user_data_rules(user: UserCreate):
    if not (len(user.user_name) > 3 and "@" in user.email and len(user.password) >= 8):
        return False
    return UserCreate(user_name=user.user_name, email=user.email, password=user.password)








@router.post("/register/", status_code=201)
async def register(user: UserCreate, service: CreateUser = Depends(get_create_user)):
    
    user_validation = await user_data_rules(user=user)
    if not user_validation:
        raise HTTPException(400)


    await service.create_user(UserCreate(user_name=user_validation.user_name, email=user.email, password=user_validation.password))
    return {"message": "user created"}










@router.get("/me/",status_code=200)
async def me_user(current_user: UserResponse  = Depends(get_current_user)):
    return   current_user



@router.put("/update/", status_code=201)
async def update_user(user: UserCreate , current_user: UserResponse = Depends(get_current_user), service: UpdateUser = Depends(get_update_user)):
    
    user_validation = await user_data_rules(user=user)
    

    if not  user_validation:
        return HTTPException(400)

    new_update_user = await service.update_user(user, id=current_user.id)
    if not new_update_user:
        HTTPException(400)


    return {"message": "user update"}










@router.delete("/del/{id}", status_code=204)
async def delete_user_id(id: int, current_user: UserResponse = Depends(get_current_user), service: DeleteUser = Depends(get_delete_user)):

    if not id == current_user.id:
        raise HTTPException(status_code=404)

    await service.delete_user(current_user.id)
    







