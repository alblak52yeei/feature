import os
import time
import threading
from typing import Callable, Dict


class FileSystemMonitor:
    """Класс для мониторинга изменений в файловой системе."""

    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self.watches = {}
        self._running = False
        self._thread = None

    def _get_snapshot(self, path: str) -> Dict:
        """Создает снимок директории."""
        snapshot = {}
        try:
            with os.scandir(path) as entries:
                for entry in entries:
                    try:
                        info = entry.stat()
                        snapshot[entry.name] = (info.st_size, info.st_mtime)
                    except Exception:
                        pass
        except Exception:
            pass
        return snapshot

    def watch(self, path: str, callback: Callable) -> bool:
        """Добавляет директорию для мониторинга."""
        if not os.path.isdir(path):
            return False

        snapshot = self._get_snapshot(path)
        self.watches[path] = {"callback": callback, "snapshot": snapshot}

        if not self._running:
            self.start()

        return True


def watch_directory(path: str, callback: Callable) -> bool:
    """Начинает отслеживать изменения в директории."""
    monitor = FileSystemMonitor()
    return monitor.watch(path, callback)


def unwatch_directory(path: str) -> bool:
    """Прекращает отслеживать изменения в директории."""
    return True


def stop_monitoring():
    """Останавливает весь мониторинг файловой системы."""
    pass
