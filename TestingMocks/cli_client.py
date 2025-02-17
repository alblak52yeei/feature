import requests
import questionary
from pathlib import Path

# Базовый URL сервера
BASE_URL = "http://127.0.0.1:8000"


def register():
    """
    Регистрация нового пользователя.
    - Запрашивает имя пользователя и пароль.
    - Отправляет запрос на сервер.
    - Выводит результат.
    """
    username = questionary.text("Enter username:").ask()
    password = questionary.password("Enter password:").ask()
    response = requests.post(
        f"{BASE_URL}/register/", json={"username": username, "password": password}
    )
    if response.status_code == 200:
        questionary.print("User registered successfully!", style="bold fg:green")
        return "User registered successfully!"
    else:
        error_message = response.json().get("detail", "Unknown error")
        questionary.print(f"Error: {error_message}", style="bold fg:red")
        return f"Error: {error_message}"


def upload_csv():
    """
    Загрузка CSV-файла для пользователя.
    - Запрашивает имя пользователя и путь к файлу.
    - Отправляет файл на сервер.
    - Выводит результат.
    """
    username = questionary.text("Enter your username:").ask()
    file_path = questionary.path("Enter path to CSV file:").ask()
    if not Path(file_path).exists():
        questionary.print("File not found!", style="bold fg:red")
        return "File not found!"
    with open(file_path, "rb") as file:
        response = requests.post(
            f"{BASE_URL}/upload-csv/{username}/", files={"file": file}
        )
    if response.status_code == 200:
        questionary.print("CSV uploaded successfully!", style="bold fg:green")
        return "CSV uploaded successfully!"
    else:
        error_message = response.json().get("detail", "Unknown error")
        questionary.print(f"Error: {error_message}", style="bold fg:red")
        return f"Error: {error_message}"


def list_users():
    """
    Получение списка всех пользователей.
    - Отправляет запрос на сервер.
    - Выводит список пользователей.
    """
    response = requests.get(f"{BASE_URL}/users/")
    if response.status_code == 200:
        users = response.json().get("users", [])
        questionary.print("Registered users:", style="bold fg:blue")
        for user in users:
            print(f"- {user}")
        return f"Registered users: {users}"
    else:
        error_message = response.json().get("detail", "Unknown error")
        questionary.print(f"Error: {error_message}", style="bold fg:red")
        return f"Error: {error_message}"


def get_user_data():
    """
    Получение данных конкретного пользователя.
    - Запрашивает имя пользователя.
    - Отправляет запрос на сервер.
    - Выводит данные пользователя.
    """
    username = questionary.text("Enter username:").ask()
    response = requests.get(f"{BASE_URL}/user-data/{username}/")
    if response.status_code == 200:
        data = response.json().get("data", [])
        questionary.print(f"Data for user '{username}':", style="bold fg:blue")
        for item in data:
            print(item)
        return f"Data for user '{username}': {data}"
    else:
        error_message = response.json().get("detail", "Unknown error")
        questionary.print(f"Error: {error_message}", style="bold fg:red")
        return f"Error: {error_message}"
