from mathematics.validators import check_all_elements_are_has_same_type


def add(a: int, b: int, *args: int) -> int:
    elements = [a, b]
    elements.extend(args)
    check_all_elements_are_has_same_type(elements)

    return sum(elements)


if __name__ == "__main__":
    add(1, 1.0)
