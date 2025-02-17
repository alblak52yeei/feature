from unittest.mock import patch
import responses
from cli_client import register, upload_csv, list_users, get_user_data

# Базовый URL сервера (должен совпадать с адресом, на котором запущен сервер)
BASE_URL = "http://127.0.0.1:8000"


@responses.activate
@patch("questionary.text")  # Мокаем функцию questionary.text для ввода текста
@patch("questionary.print")  # Мокаем функцию questionary.print для вывода сообщений
@patch("questionary.password")  # Мокаем функцию questionary.password для ввода пароля
def test_register_success(mock_print, mock_text, mock_password):
    """
    Тест успешной регистрации пользователя.
    Проверяет, что:
    - Пользователь может зарегистрироваться.
    - Сервер возвращает ожидаемый ответ.
    - Выводится сообщение об успешной регистрации.
    """
    # Мокаем ввод имени пользователя и пароля
    mock_text.return_value.ask.return_value = "mockuser"  # Имя пользователя
    mock_password.return_value.ask.return_value = "mockpass"  # Пароль

    # Мокаем ответ сервера на запрос регистрации
    responses.add(
        responses.POST,
        f"{BASE_URL}/register/",  # URL для регистрации
        json={"message": "User registered successfully"},  # Ожидаемый ответ сервера
        status=200,  # Код статуса HTTP
    )

    # Вызываем функцию регистрации
    result = register()

    # Проверяем, что результат содержит сообщение об успешной регистрации
    assert "User registered successfully!" in result

    # Проверяем, что questionary.print был вызван с правильным сообщением
    mock_print.assert_called_with(
        "User registered successfully!", style="bold fg:green"
    )


@responses.activate
@patch("questionary.text")  # Мокаем функцию questionary.text для ввода текста
@patch("questionary.print")  # Мокаем функцию questionary.print для вывода сообщений
@patch("questionary.path")  # Мокаем функцию questionary.path для ввода пути к файлу
def test_upload_csv_success(mock_print, mock_text, mock_path, tmp_path):
    """
    Тест успешной загрузки CSV-файла.
    Проверяет, что:
    - Пользователь может загрузить CSV-файл.
    - Сервер возвращает ожидаемый ответ.
    - Выводится сообщение об успешной загрузке.
    """
    # Мокаем ввод имени пользователя
    mock_text.return_value.ask.side_effect = ["mockuser"]

    # Создаем временный CSV-файл
    csv_content = "name,age\nJohn,30\nJane,25"  # Содержимое CSV-файла
    file_path = tmp_path / "data.csv"  # Путь к временному файлу
    file_path.write_text(csv_content)  # Записываем содержимое в файл

    # Мокаем ввод пути к файлу
    mock_path.return_value.ask.return_value = str(file_path)

    # Мокаем ответ сервера на запрос загрузки CSV
    responses.add(
        responses.POST,
        f"{BASE_URL}/upload-csv/mockuser/",  # URL для загрузки CSV
        json={
            "message": "CSV data uploaded successfully",
            "data_count": 2,
        },  # Ожидаемый ответ сервера
        status=200,  # Код статуса HTTP
    )

    # Вызываем функцию загрузки CSV
    result = upload_csv()

    # Проверяем, что результат содержит сообщение об успешной загрузке
    assert "CSV uploaded successfully!" in result

    # Проверяем, что questionary.print был вызван с правильным сообщением
    mock_print.assert_called_with("CSV uploaded successfully!", style="bold fg:green")


@responses.activate
@patch("questionary.print")  # Мокаем функцию questionary.print для вывода сообщений
def test_list_users(mock_print):
    """
    Тест получения списка пользователей.
    Проверяет, что:
    - Сервер возвращает список пользователей.
    - Выводится список пользователей.
    """
    # Мокаем ответ сервера на запрос списка пользователей
    responses.add(
        responses.GET,
        f"{BASE_URL}/users/",  # URL для получения списка пользователей
        json={"users": ["user1", "user2"]},  # Ожидаемый ответ сервера
        status=200,  # Код статуса HTTP
    )

    # Вызываем функцию получения списка пользователей
    result = list_users()

    # Проверяем, что результат содержит сообщение о зарегистрированных пользователях
    assert "Registered users:" in result

    # Проверяем, что questionary.print был вызван с правильным сообщением
    mock_print.assert_called_with("Registered users:", style="bold fg:blue")


@responses.activate
@patch("questionary.text")  # Мокаем функцию questionary.text для ввода текста
@patch("questionary.print")  # Мокаем функцию questionary.print для вывода сообщений
def test_get_user_data(mock_print, mock_text):
    """
    Тест получения данных пользователя.
    Проверяет, что:
    - Пользователь может получить свои данные.
    - Сервер возвращает ожидаемые данные.
    - Выводятся данные пользователя.
    """
    # Мокаем ввод имени пользователя
    mock_text.return_value.ask.return_value = "mockuser"

    # Мокаем ответ сервера на запрос данных пользователя
    responses.add(
        responses.GET,
        f"{BASE_URL}/user-data/mockuser/",  # URL для получения данных пользователя
        json={"data": [{"name": "John", "age": "30"}]},  # Ожидаемый ответ сервера
        status=200,  # Код статуса HTTP
    )

    # Вызываем функцию получения данных пользователя
    result = get_user_data()

    # Проверяем, что результат содержит данные пользователя
    assert "Data for user 'mockuser':" in result

    # Проверяем, что questionary.print был вызван с правильным сообщением
    mock_print.assert_called_with("Data for user 'mockuser':", style="bold fg:blue")
