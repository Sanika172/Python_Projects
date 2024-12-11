from pythondemo_Decorators.project04 import myclass


class myclass:
    def __init__(self, value):
        self._value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            self._value = new_value


obj = myclass(10)
print(obj._value)
obj.value = 20
print(obj.value)
