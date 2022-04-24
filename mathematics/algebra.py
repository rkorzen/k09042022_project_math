from mathematics.validators import check_all_elements_are_has_same_type


def add(a: int, b: int, *args: int) -> int:
    elements = [a, b]
    elements.extend(args)
    check_all_elements_are_has_same_type(elements)

    return sum(elements)


def sub(a: int, b: int) -> int:
    check_all_elements_are_has_same_type([a, b])
    return a - b


if __name__ == "__main__":
    a, b = 1, 1.0

    add(a, b)
