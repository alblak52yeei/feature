import os
import sys

# Добавление пути к вашему проекту
sys.path.insert(0, os.path.abspath('..'))

# Основные настройки
project = 'feature'
author = 'Maxim'
release = '1.0'

# Расширения Sphinx
extensions = [
    'sphinx.ext.autodoc',  # Автоматическая документация кода
    'sphinx_rtd_theme',    # Тема Read the Docs
]

# Тема оформления
html_theme = 'sphinx_rtd_theme'

# Путь к исходным файлам документации
source_suffix = {
    '.rst': 'restructuredtext',
}