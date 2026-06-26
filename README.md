
# TASK-TRACKER-API

**Task Tracker API** es una API para gestionar usuarios y tareas con autenticación JWT.
Esta versión está construida con FastAPI y tiene rutas de usuario y tareas separadas.

---

##  Requisitos

- Python 3.11+ (recomendado)
- `git`

---

## 🚀 Instalación

```bash
git clone https://github.com/marcozxdev/task-tracker-API
cd task-tracker-API
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> No es necesario usar `pip install -e .` para este proyecto.

---

## Ejecutar la aplicación

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La API quedará disponible en `http://127.0.0.1:8000`.

---

##  Rutas principales

La aplicación registra los routers en `main.py` con estos prefijos:

- `users` → rutas de usuario
- `users/tasks` → rutas de tareas

---

## Rutas de usuario

### Registrar usuario

- Método: `POST`
- Ruta: `/users/register/`
- Body JSON:
  ```json
  {
    "user_name": "mi_usuario",
    "email": "correo@ejemplo.com",
    "password": "contraseña123"
  }
  ```

### Login y obtención de token

- Método: `POST`
- Ruta: `/users/login`
- Datos de formulario:
  - `username`: correo del usuario
  - `password`: contraseña

Respuesta esperada:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

### Obtener datos del usuario autenticado

- Método: `GET`
- Ruta: `/users/me/`
- Header: `Authorization: Bearer <token>`

### Actualizar usuario

- Método: `PUT`
- Ruta: `/users/update/`
- Header: `Authorization: Bearer <token>`
- Body JSON igual que en registro

### Eliminar usuario

- Método: `DELETE`
- Ruta: `/users/del/{id}`
- Header: `Authorization: Bearer <token>`

---

##  Rutas de tareas

### Crear nueva tarea

- Método: `POST`
- Ruta: `/users/tasks/new_task/`
- Header: `Authorization: Bearer <token>`
- Body JSON:
  ```json
  {
    "titulo": "Mi tarea",
    "descripcion": "Descripción de la tarea"
  }
  ```

> El estado de la tarea se crea automáticamente como `EN-PROGRESO`.

### Listar tareas del usuario

- Método: `GET`
- Ruta: `/users/tasks/list/`
- Header: `Authorization: Bearer <token>`
- Query params opcionales:
  - `limit` (por defecto 5)
  - `state` (`HECHA`, `EN-PROGRESO`, `OLVIDADA`)

Ejemplo:

```bash
curl "http://127.0.0.1:8000/users/tasks/list/?limit=10&state=EN-PROGRESO" \
  -H "Authorization: Bearer <token>"
```

### Buscar tarea por título

- Método: `GET`
- Ruta: `/users/tasks/find/`
- Header: `Authorization: Bearer <token>`
- Query params:
  - `s`: texto a buscar en el título
  - `limit`: cantidad máxima de resultados

Ejemplo:

```bash
curl "http://127.0.0.1:8000/users/tasks/find/?s=mi%20tarea&limit=1" \
  -H "Authorization: Bearer <token>"
```

### Actualizar estado de una tarea

- Método: `PATCH`
- Ruta: `/users/tasks/state/{id_task}`
- Header: `Authorization: Bearer <token>`
- Query param:
  - `state`: `HECHA`, `EN-PROGRESO` o `OLVIDADA`

Ejemplo:

```bash
curl -X PATCH "http://127.0.0.1:8000/users/tasks/state/5?state=HECHA" \
  -H "Authorization: Bearer <token>"
```

### Eliminar tarea

- Método: `DELETE`
- Ruta: `/users/tasks/del/{id_task}`
- Header: `Authorization: Bearer <token>`

Ejemplo:

```bash
curl -X DELETE "http://127.0.0.1:8000/users/tasks/del/5" \
  -H "Authorization: Bearer <token>"
```

---

##  Notas

- La autenticación usa JWT con `Authorization: Bearer <token>`.
- Las rutas de tareas dependen de un usuario autenticado.
- Si necesitas ver la documentación automática de OpenAPI, visita:
  - `http://127.0.0.1:8000/docs`
  - `http://127.0.0.1:8000/redoc`

