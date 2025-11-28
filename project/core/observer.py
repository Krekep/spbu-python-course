from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Event:
    def __init__(self, event_type: str, data: Dict[str, Any], source: Any = None):
        self.event_type = event_type
        self.data = data
        self.source = source


class Observer(ABC):
    @abstractmethod
    def on_event(self, event: Event):
        pass


class Observable:
    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, event: Event):
        for observer in self._observers:
            observer.on_event(event)
