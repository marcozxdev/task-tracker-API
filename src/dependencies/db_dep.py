from fastapi import dependencies

from src.database.config_db import db




def get_db():
    return db

