import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from jose import JWTError, jwt

load_dotenv()

# La clave se lee del entorno: hardcodearla en el repositorio publica la
# firma de los tokens, y cualquiera con el codigo podria falsificar sesiones.
# Para gerar una clave real:
#   python -c "import secrets; print(secrets.token_urlsafe(64))"
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
EXPIRE = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))

if not SECRET_KEY:
    raise RuntimeError(
        "JWT_SECRET_KEY no esta definida. Copia .env.example a .env y define "
        "una clave, por ejemplo: "
        'python -c "import secrets; print(secrets.token_urlsafe(64))"'
    )


def create_access_token(email: str, id: int):
    payload = {
        "id": id,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=EXPIRE)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def decode_access_token(token):
    try:
        data = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return data
    except JWTError:
        return None
