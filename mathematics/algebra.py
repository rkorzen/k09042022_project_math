from typing import Union, List

from mathematics.validators import check_all_elements_are_has_same_type


def add(a: int, b: int, *args: int) -> int:
    elements = [a, b]
    elements.extend(args)
    check_all_elements_are_has_same_type(elements)

    return sum(elements)


def sub(a: int, b: int) -> int:
    check_all_elements_are_has_same_type([a, b])
    return a - b


def square_roots(
    a: Union[float, str], b: Union[float, str], c: Union[float, str]
) -> List[Union[float, int]]:

    results = []

    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = (-b - delta**0.5) / (2 * a)
        x2 = (-b + delta**0.5) / (2 * a)
        results = [x1, x2]

    elif delta == 0:
        x = -b / (2 * a)
        results = [x]

    return results


if __name__ == "__main__":
    a, b = 1, 1.0

    add(a, b)
