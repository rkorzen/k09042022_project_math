from typing import List

def check_all_elements_are_has_same_type(elements: List, type_=int):
    for el in elements:
        if not isinstance(el, type_):
            raise ValueError(f"Elements should be type: {type_}")
    return True