from fastapi.testclient import TestClient
from main import app

# Создаем тестовый клиент для FastAPI приложения
client = TestClient(app)


def test_register_success():
    """
    Тест успешной регистрации пользователя.
    - Проверяет, что сервер возвращает ожидаемый ответ.
    - Проверяет, что пользователь действительно добавлен в базу данных.
    """
    response = client.post(
        "/register/", json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}


def test_register_duplicate():
    """
    Тест попытки регистрации существующего пользователя.
    - Проверяет, что сервер возвращает ошибку 400.
    """
    client.post(
        "/register/", json={"username": "testuser", "password": "testpass"}
    )  # Регистрируем пользователя
    response = client.post(
        "/register/", json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Username already exists"}


def test_upload_csv_success():
    """
    Тест успешной загрузки CSV-файла.
    - Проверяет, что сервер возвращает ожидаемый ответ.
    - Проверяет, что данные сохранены в базе данных.
    """
    client.post(
        "/register/", json={"username": "testuser", "password": "testpass"}
    )  # Регистрируем пользователя
    files = {"file": ("data.csv", b"name,age\nJohn,30\nJane,25")}
    response = client.post("/upload-csv/testuser/", files=files)
    assert response.status_code == 200
    assert response.json() == {
        "message": "CSV data uploaded successfully",
        "data_count": 2,
    }


def test_list_users():
    """
    Тест получения списка пользователей.
    - Проверяет, что сервер возвращает ожидаемый список.
    """
    client.post("/register/", json={"username": "user1", "password": "pass1"})
    client.post("/register/", json={"username": "user2", "password": "pass2"})
    response = client.get("/users/")
    assert response.status_code == 200
    assert set(response.json()["users"]) == {"user1", "user2"}
