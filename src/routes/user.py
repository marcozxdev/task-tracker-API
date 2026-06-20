from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from src.schemas.shcemas import *
from src.security.jwt_handler import *
from typing import Annotated




router = APIRouter()
oauth_schema = OAuth2PasswordBearer(tokenUrl="token")





async def get_current_user(token: Annotated[str,  oauth_schema]):
    user = decode_access_token(token=token)
    return user




@router.get("/users/me")
async def me_user(current_user: Annotated[str,  Depends(get_current_user)]):
    return current_user






