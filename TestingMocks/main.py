from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

# Создаем экземпляр FastAPI приложения
app = FastAPI()

# Временное хранилище данных (в реальном приложении это будет база данных)
users_db: Dict[str, str] = {}  # Хранилище пользователей (имя: пароль)
user_data_db: Dict[str, List[Dict]] = {}  # Хранилище данных пользователей


# Модель данных для регистрации
class User(BaseModel):
    username: str
    password: str


# Модель данных для CSV
class CSVData(BaseModel):
    name: str
    age: int


# Эндпоинт для регистрации нового пользователя
@app.post("/register/")
def register(user: User):
    """
    Регистрация нового пользователя.
    - Проверяет, что имя пользователя уникально.
    - Сохраняет пользователя в базе данных.
    """
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = user.password
    return {"message": "User registered successfully"}


# Эндпоинт для загрузки CSV-файла
@app.post("/upload-csv/{username}/")
async def upload_csv(username: str, file: bytes):
    """
    Загрузка CSV-файла для пользователя.
    - Проверяет, что пользователь существует.
    - Парсит CSV-файл и сохраняет данные в базу данных.
    """
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    # Парсим CSV-файл (упрощенная реализация)
    try:
        content = file.decode("utf-8")
        lines = content.strip().split("\n")
        header = lines[0].split(",")
        data = [dict(zip(header, line.split(","))) for line in lines[1:]]
        user_data_db[username] = data
        return {"message": "CSV data uploaded successfully", "data_count": len(data)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV format: {str(e)}")


# Эндпоинт для получения списка пользователей
@app.get("/users/")
def list_users():
    """
    Возвращает список всех зарегистрированных пользователей.
    """
    return {"users": list(users_db.keys())}


# Эндпоинт для получения данных конкретного пользователя
@app.get("/user-data/{username}/")
def get_user_data(username: str):
    """
    Возвращает данные, связанные с пользователем.
    - Если данных нет, возвращает пустой список.
    """
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"data": user_data_db.get(username, [])}
