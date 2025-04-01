# maxkufilewizardos

![maxkufilewizardos Logo](https://via.placeholder.com/150x150?text=FWO)

maxkufilewizardos — простая, но мощная библиотека Python для интеллектуальной работы с файлами и директориями.

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://test.pypi.org/)
[![Python versions](https://img.shields.io/badge/python-3.6%2B-brightgreen.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🚀 Возможности

- **Безопасные операции с файлами** - надежное чтение/запись с обработкой ошибок
- **Умный поиск** - гибкий поиск файлов и текста внутри них
- **Мониторинг изменений** - отслеживание изменений в директориях
- **Сравнение файлов и директорий** - выявление различий и поиск дубликатов

## 📦 Установка

```bash
pip install maxkufilewizardos
```

## 🔧 Примеры использования

### Безопасные операции с файлами

```python
from maxkufilewizardos import safe_read, safe_write, safe_delete

# Чтение файла с автоматической обработкой ошибок
content = safe_read('config.txt')

# Запись в файл (автоматически создаст директории при необходимости)
safe_write('logs/app/today.log', 'Application started')

# Безопасное удаление с возможностью восстановления
safe_delete('temp_file.dat')
```

### Поиск файлов и текста

```python
from maxkufilewizardos import find_files, find_text, find_text_in_files

# Найти все Python файлы в проекте
python_files = find_files('./project', '*.py', recursive=True)

# Найти все вхождения паттерна в файле
matches = find_text('app.py', 'def run', use_regex=True)

# Найти текст во всех найденных файлах
results = find_text_in_files(python_files, 'import os')
```

### Мониторинг директорий

```python
from maxkufilewizardos import watch_directory

# Функция-обработчик изменений
def on_file_change(path, changes):
    print(f"В директории {path} обнаружены изменения:")
    for file, status in changes.items():
        print(f"  • {file}: {status}")

# Начать отслеживание директории
watch_directory('./data', on_file_change)
```

### Сравнение и анализ

```python
from maxkufilewizardos import compare_files, file_diff, compare_directories, find_duplicate_files

# Сравнить два файла
if not compare_files('v1.txt', 'v2.txt'):
    # Показать различия между файлами
    differences = file_diff('v1.txt', 'v2.txt')
    print('\n'.join(differences))

# Сравнить директории
diff = compare_directories('./backup', './current')
print(f"Файлы только в backup: {diff['only_in_dir1']}")
print(f"Файлы только в current: {diff['only_in_dir2']}")

# Найти дубликаты файлов
duplicates = find_duplicate_files('./storage')
for hash_id, file_list in duplicates.items():
    print(f"Найдены дубликаты ({len(file_list)} шт.):")
    for f in file_list:
        print(f"  - {f}")
```

## 📘 Документация API

### Модуль Core

| Функция | Описание |
|---------|----------|
| `safe_read(file_path, mode='r', encoding='utf-8')` | Безопасно читает содержимое файла |
| `safe_write(file_path, content, mode='w', encoding='utf-8')` | Безопасно записывает в файл |
| `safe_delete(file_path)` | Удаляет файл с обработкой ошибок |
| `restore_file(file_path, backup_path)` | Восстанавливает файл из бэкапа |
| `get_file_info(file_path)` | Возвращает полную информацию о файле |

### Модуль Search

| Функция | Описание |
|---------|----------|
| `find_files(directory, pattern='*', recursive=True)` | Находит файлы по шаблону |
| `find_text(file_path, search_text, use_regex=False)` | Ищет текст в файле |
| `find_text_in_files(files, search_text)` | Ищет текст во множестве файлов |

### Модуль Monitor

| Функция | Описание |
|---------|----------|
| `watch_directory(path, callback)` | Отслеживает изменения в директории |
| `unwatch_directory(path)` | Прекращает наблюдение за директорией |
| `stop_monitoring()` | Останавливает весь мониторинг |

### Модуль Compare

| Функция | Описание |
|---------|----------|
| `compare_files(file1, file2)` | Сравнивает два файла |
| `file_diff(file1, file2)` | Возвращает различия в текстовых файлах |
| `compare_directories(dir1, dir2)` | Сравнивает две директории |
| `find_duplicate_files(directory)` | Находит дубликаты файлов |

## 🤝 Участие в разработке

Вклады приветствуются! Если вы нашли ошибку или хотите предложить новую функцию:

1. Форкните репозиторий
2. Создайте ветку для вашей функции (`git checkout -b feature/amazing-feature`)
3. Закоммитьте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в ваш форк (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.

## 📞 Контакты

Если у вас есть вопросы или предложения, создайте issue в репозитории или свяжитесь с автором:

- Email: ваша.почта@example.com
- GitHub: [MaxKuklaVod](https://github.com/MaxKuklaVod)

---

Made with ❤️ by [Maxim Nagovitsyn]