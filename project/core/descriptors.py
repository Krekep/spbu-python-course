from .observer import Event


class ValidatedField:
    def __init__(self, min_value=None, max_value=None, field_type=None, clamp_min=False):
        self.min_value = min_value
        self.max_value = max_value
        self.field_type = field_type
        self.clamp_min = clamp_min
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        old_value = getattr(obj, self.private_name)
        new_value, event = self._validate_and_adjust(value, obj)

        setattr(obj, self.private_name, new_value)

        if old_value != new_value and hasattr(obj, 'notify_observers') and (event is not None):
            obj.notify_observers(event)

    def _validate_and_adjust(self, value, obj):
        event = None

        if self.field_type and not isinstance(value, self.field_type):
            raise TypeError(f"Expected {self.field_type}, got {type(value)}")

        if self.min_value is not None and value < self.min_value:
            if self.clamp_min:
                event = Event(
                    event_type="value_underflow",
                    data={
                        'field_name': self.private_name[1:],
                        'attempted_value': value,
                        'clamped_value': self.min_value,
                        'difference': value - self.min_value
                    },
                    source=obj
                )
                value = self.min_value
            else:
                raise ValueError(f"Value can't be less than {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            event = Event(
                event_type="value_overflow",
                data={
                    'field_name': self.private_name[1:],
                    'attempted_value': value,
                    'clamped_value': self.max_value,
                    'difference': value - self.max_value
                },
                source=obj
            )
            value = self.max_value

        return value, event


class StomachDescriptor(ValidatedField):
    def __init__(self):
        super().__init__(min_value=0, clamp_min=True)

    def __set__(self, obj, value):
        old_value = getattr(obj, self.private_name)
        super().__set__(obj, value)

        new_value = getattr(obj, self.private_name)
        if (new_value <= 0) and (old_value >= 0) and (hasattr(obj, 'notify_observers')):
            obj.notify_observers(Event(
                event_type="cell_starving",
                data={'reason': 'not enough food in stomach',
                      'damage': abs(value)},
                source=obj
            ))


class HealthDescriptor(ValidatedField):
    def __init__(self):
        super().__init__(min_value=0, clamp_min=True)

    def __set__(self, obj, value):
        old_value = getattr(obj, self.private_name)
        super().__set__(obj, value)

        new_value = getattr(obj, self.private_name)

        if (new_value <= 0) and (old_value > 0) and hasattr(obj, 'notify_observers'):
            obj.notify_observers(Event(
                event_type="health_on_zero",
                data={'reason': 'health_depleted'},
                source=obj
            ))

        elif (new_value <= 5) and (hasattr(obj, 'notify_observers')):
            obj.notify_observers(Event(
                event_type="low_health",
                data={'health_level': new_value},
                source=obj
            ))


class CoordinateDescriptor(ValidatedField):
    def __init__(self):
        super().__init__()

    def __set__(self, obj, value):
        old_value = getattr(obj, self.private_name)
        super().__set__(obj, value)
        new_value = getattr(obj, self.private_name)

        if hasattr(obj, 'notify_observers'):
            obj.notify_observers(Event(
                event_type="coordinate_changed",
                data={"coordinate": self.private_name,
                      "old": old_value,
                      "new": new_value},
                source=obj
            ))


class IsAliveDescriptor(ValidatedField):
    def __init__(self):
        super().__init__(field_type=bool)

    def __set__(self, obj, value):
        old_value = getattr(obj, self.private_name)
        super().__set__(obj, value)
        new_value = getattr(obj, self.private_name)

        if old_value and (not new_value) and hasattr(obj, 'notify_observers'):
            if hasattr(obj, 'notify_observers'):
                obj.notify_observers(Event(
                    event_type="cell_dead",
                    data={"old": old_value,
                          "new": new_value},
                    source=obj
                ))


class CellFieldDescriptor(ValidatedField):
    def __init__(self):
        super().__init__()

    def __set__(self, obj, value):
        old_value = getattr(obj, self.private_name)
        super().__set__(obj, value)
        new_value = getattr(obj, self.private_name)

        if old_value != new_value and hasattr(obj, 'notify_observers'):
            if hasattr(obj, 'notify_observers'):
                obj.notify_observers(Event(
                    event_type="new_cell_placement",
                    data={"old": old_value,
                          "new": new_value},
                    source=obj
                ))

        obj.x = new_value.x
        obj.y = new_value.y
