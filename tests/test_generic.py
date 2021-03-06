"""Generic functions tests."""
from flake8_nitpick.generic import get_subclasses


def test_get_subclasses():
    """Test subclasses."""

    class Vehicle:
        pass

    class Car(Vehicle):
        pass

    class Audi(Car):
        pass

    class Bicycle(Vehicle):
        pass

    assert get_subclasses(Vehicle) == [Car, Audi, Bicycle]
