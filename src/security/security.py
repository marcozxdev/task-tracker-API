from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"] )


def hash_pwd(password):
    """hashea la pasword"""
    return pwd_context.hash(password)



def verify_pwd(plain_pwd,  hashed_pwd):
    """valida la password"""
    return pwd_context.verify(plain_pwd, hashed_pwd)