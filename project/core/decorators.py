import functools
from typing import Callable
from core.observer import Event


def auto_update_state(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)

        if hasattr(self, 'update'):
            self.update()

        if hasattr(self, 'notify_observers'):
            self.notify_observers(Event(
                event_type="action_completed",
                data={
                    'action': func.__name__,
                    'cell_state': {
                        'health': getattr(self, 'current_health', 'N/A'),
                        'stomach': getattr(self, 'stomach', 'N/A')
                    }
                },
                source=self
            ))

    return wrapper


def log_action(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Cell start: {func.__name__}")
        result = func(self, *args, **kwargs)
        print(f"Cell end: {func.__name__}")
        return result

    return wrapper
