import os
import filecmp
import difflib
from typing import List, Dict


def compare_files(file1: str, file2: str) -> bool:
    """Сравнивает два файла и определяет, совпадают ли они."""
    if not os.path.exists(file1):
        raise FileNotFoundError(f"Файл не найден: {file1}")
    if not os.path.exists(file2):
        raise FileNotFoundError(f"Файл не найден: {file2}")

    return filecmp.cmp(file1, file2, shallow=False)


def file_diff(file1: str, file2: str, encoding: str = "utf-8") -> List[str]:
    """Находит различия между двумя текстовыми файлами."""
    try:
        with open(file1, "r", encoding=encoding) as f1:
            lines1 = f1.readlines()
        with open(file2, "r", encoding=encoding) as f2:
            lines2 = f2.readlines()
    except UnicodeDecodeError:
        raise ValueError("Файлы не являются текстовыми или имеют другую кодировку")

    diff = difflib.unified_diff(
        lines1,
        lines2,
        fromfile=os.path.basename(file1),
        tofile=os.path.basename(file2),
    )

    return list(diff)


def compare_directories(dir1: str, dir2: str) -> Dict:
    """Сравнивает две директории и находит различия."""
    if not os.path.exists(dir1):
        raise FileNotFoundError(f"Директория не найдена: {dir1}")
    if not os.path.exists(dir2):
        raise FileNotFoundError(f"Директория не найдена: {dir2}")

    comparison = filecmp.dircmp(dir1, dir2)
    result = {
        "only_in_dir1": comparison.left_only,
        "only_in_dir2": comparison.right_only,
        "diff_files": comparison.diff_files,
        "common": comparison.same_files,
    }

    return result


def find_duplicate_files(directory: str) -> Dict[str, List[str]]:
    """Находит дубликаты файлов в директории."""
    import hashlib

    file_hashes = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                with open(filepath, "rb") as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()

                if file_hash in file_hashes:
                    file_hashes[file_hash].append(filepath)
                else:
                    file_hashes[file_hash] = [filepath]
            except Exception:
                pass

    return {h: files for h, files in file_hashes.items() if len(files) > 1}
