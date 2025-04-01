import os
import shutil
from typing import Optional, Union


def safe_read(
    file_path: str, mode: str = "r", encoding: Optional[str] = "utf-8"
) -> str:
    """Безопасно читает содержимое файла с обработкой ошибок."""
    try:
        if "b" in mode:
            with open(file_path, mode) as f:
                return f.read()
        else:
            with open(file_path, mode, encoding=encoding) as f:
                return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except PermissionError:
        raise PermissionError(f"Недостаточно прав для чтения файла: {file_path}")
    except Exception as e:
        raise IOError(f"Ошибка при чтении файла {file_path}: {str(e)}")


def safe_write(
    file_path: str,
    content: Union[str, bytes],
    mode: str = "w",
    encoding: Optional[str] = "utf-8",
) -> None:
    """Безопасно записывает содержимое в файл с обработкой ошибок."""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    try:
        if "b" in mode:
            with open(file_path, mode) as f:
                f.write(content)
        else:
            with open(file_path, mode, encoding=encoding) as f:
                f.write(content)
    except Exception as e:
        raise IOError(f"Ошибка при записи в файл {file_path}: {str(e)}")


def safe_delete(file_path: str) -> bool:
    """Безопасно удаляет файл."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except Exception as e:
        raise IOError(f"Ошибка при удалении файла {file_path}: {str(e)}")


def restore_file(file_path: str, backup_path: str) -> bool:
    """Восстанавливает файл из резервной копии."""
    if os.path.exists(backup_path):
        shutil.copy2(backup_path, file_path)
        return True
    return False


def get_file_info(file_path: str) -> dict:
    """Получает информацию о файле."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    stat_info = os.stat(file_path)
    import datetime

    return {
        "size": stat_info.st_size,
        "modified": datetime.datetime.fromtimestamp(stat_info.st_mtime),
        "is_file": os.path.isfile(file_path),
        "is_dir": os.path.isdir(file_path),
        "extension": (
            os.path.splitext(file_path)[1] if os.path.isfile(file_path) else ""
        ),
        "name": os.path.basename(file_path),
    }
