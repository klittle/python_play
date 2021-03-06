#!/usr/bin/env python3


class Animal:

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return 'hi'


class Dog(Animal):
    """
    Dog inherits from Animal
    """

    def __init__(self, name: str):
        """
        Note that the syntax changed in Python 3.0:
        you can just say super().__init__()
        instead of super(ChildB, self).__init__()
        https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods#576183
        :param name:
        """
        super().__init__(name)

    def speak(self) -> str:
        """
        override super speak()
        :return:
        """
        # this implementation calls super() method, but doesn't have to
        return super().speak() + ', ' + 'woof'


