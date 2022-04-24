import pytest

from mathematics import algebra


class TestAdd:
    def test_add_two_ints(self):
        assert algebra.add(1, 2) == 3
        assert algebra.add(1, -2) == -1
        assert algebra.add(1, 1, 1, 1, 1, 1) == 6

    def test_add_exception(self):
        with pytest.raises(ValueError):
            algebra.add(1, 2.0)
