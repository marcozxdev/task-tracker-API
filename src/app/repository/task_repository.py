
import json #sqlite3 # librerias para acceder a la base de datos en este primera version se usara json
from pathlib import Path




BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent # sube cuatro niveles para que encuentre el archivo
DATA_DIR = BASE_DIR / "data" # da el path de la carpeta

FILE_TASKS  = DATA_DIR / "tasks.json"   # para mas eficasia y hacer menos trabajo creare un json mientras tanto



# print(FILE_TASKS_DONE)
# print(BASE_DIR)
# print(DATA_DIR)


def load(path: Path) -> list[dict]: # carga los datos, o crea el archivo en caso de que no exista
    if not path.exists():
        with path.open("w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
            return   []   # lo voy a dejar que retorne none mientras escalo mas 
        
    with open(path, "r") as f:
        return json.load(f)


def save(path: Path, data): # guarda los datos en el archivo json
    if not data or not path:
        print("\n faltan argumentos path y data")

    with open(path, "w") as f: # 
        json.dump(data, f, indent=4)
        return
        
