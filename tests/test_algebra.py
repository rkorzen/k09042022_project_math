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


class TestSub:
    def test_sub_two_ints(self):
        assert algebra.sub(1, 2) == -1
        assert algebra.sub(1, -2) == 3

    def test_sub_exception(self):
        with pytest.raises(ValueError):
            algebra.sub(1, 1.0)


class TestSquareRootsOfQuadraticeEquation:
    def test_two_square_roots(self):
        assert algebra.square_roots(1, 0, -1) == [-1, 1]

    def test_one_square_root(self):
        assert algebra.square_roots(1, 0, 0) == [0]

    def test_zero_square_roots(self):
        assert algebra.square_roots(1, 0, 1) == []
