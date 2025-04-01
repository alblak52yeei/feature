import os
import re
from typing import List, Optional, Callable


def find_files(directory: str, pattern: str = "*", recursive: bool = True) -> List[str]:
    """Находит файлы, соответствующие шаблону в указанной директории."""
    import fnmatch

    result = []

    for root, _, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                result.append(os.path.join(root, file))

        if not recursive:
            break

    return result


def find_text(
    file_path: str,
    search_text: str,
    use_regex: bool = False,
    case_sensitive: bool = True,
    encoding: str = "utf-8",
) -> List[tuple]:
    """Находит текст в файле."""
    result = []

    try:
        with open(file_path, "r", encoding=encoding) as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        return result

    flags = 0 if case_sensitive else re.IGNORECASE

    if use_regex:
        pattern = re.compile(search_text, flags)
    else:
        pattern = re.compile(re.escape(search_text), flags)

    for line_num, line in enumerate(lines, 1):
        for match in pattern.finditer(line):
            result.append((line_num, line.rstrip("\n"), match.start()))

    return result


def find_text_in_files(files: List[str], search_text: str) -> dict:
    """Находит текст в нескольких файлах."""
    result = {}

    for file_path in files:
        try:
            matches = find_text(file_path, search_text)
            if matches:
                result[file_path] = matches
        except Exception:
            pass

    return result
