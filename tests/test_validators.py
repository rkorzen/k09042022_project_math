import pytest

from mathematics.validators import check_all_elements_are_has_same_type


def test_check_all_elements_are_has_same_type_when_all_elements_has_same_type():
    assert check_all_elements_are_has_same_type([1, 1, 1])
    assert check_all_elements_are_has_same_type([1.0, 1.0, 1.0], type_=float)


def test_check_all_elements_are_has_same_type_when_all_elements_has_not_same_type():

    with pytest.raises(ValueError):
        check_all_elements_are_has_same_type([1, 1.0, 1])
    with pytest.raises(ValueError):
        check_all_elements_are_has_same_type([1.0, 1, 1.0], type_=float)
