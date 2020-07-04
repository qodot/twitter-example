from pytest import raises

from twitter.common.container import NotContainedTypeError
from twitter.common.container import TestDIContainer as DIContainer


class TestDIContainer:
    def test_register(self):
        class MyClass:
            pass

        container = DIContainer()
        obj = MyClass()

        # when
        container.register(obj)

        # then
        assert container._container[MyClass] is obj

    def test_get(self):
        class MyClass:
            pass

        container = DIContainer()
        obj = MyClass()
        container.register(obj)

        # when
        resolved_obj = container.get(MyClass)

        # then
        assert resolved_obj is obj

    def test_get_raise_not_container_error(self):
        class MyClass:
            pass

        container = DIContainer()
        obj = MyClass()
        container.register(obj)

        class WrongClass:
            pass

        # when then
        with raises(NotContainedTypeError):
            container.get(WrongClass())
