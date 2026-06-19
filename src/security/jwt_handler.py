from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError 

# payload = {
#     "sub": "marco@gmail.com",
#     "id": 1,
#     "exp": datetime.now(timezone.utc)
#     + timedelta(minutes=30)
# }

# token = jwt.encode(
#     payload,
#     "mi_clave_secreta",
#     algorithm="HS256"
# )






# data = jwt.decode(
#     token,
#     "mi_clave_secreta",
#     algorithms=["HS256"]
# )

# print(data, token)




# basado en el ejemplo de arriba voy a construir lo que necesito




ALGORITHM = "HS256"
SECRET_KEY = "JAVASCRIPT_WEB_TOKEN1234EDSW" # MI EJEMPLO DE CLAVE
EXPIRE = 30


def create_access_token(user_id: int, email: str, user_name: str):
    payload = {
        "sub": user_id,
        "username": user_name,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=EXPIRE)
        }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=[ALGORITHM])

    return token


def decode_access_token(token):
    try:
        data = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return data
    except JWTError:
        return None
    
    


