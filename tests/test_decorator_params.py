from typing import Callable, Type

from overrides_extension import override


class SuperClass:
    def method(self) -> int:
        return 2


def my_decorator(name: str) -> Callable:
    def func(cls: Type) -> Type:
        return cls

    return func


class MyClass:
    def __init__(self, name: str) -> None:
        self.my_name: str = name


def test_my_func() -> None:
    my_object = MyClass("Name accessed in decorator")

    @my_decorator(my_object.my_name)
    class SubClass(SuperClass):
        @override
        def method(self) -> int:
            return 1
