"""
FileWizard - простая, но мощная утилита для работы с файлами и директориями.
"""

__version__ = "0.1.0"
__author__ = "Maxim Nagovitsyn"

# Импорты из основных модулей
from .core import safe_read, safe_write, safe_delete, restore_file, get_file_info
from .search import find_files, find_text, find_text_in_files
from .monitor import watch_directory, unwatch_directory, stop_monitoring
from .compare import compare_files, file_diff, compare_directories, find_duplicate_files
