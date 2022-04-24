from mathematics import algebra

class TestAdd:
    def test_add_two_ints(self):
        assert algebra.add(1, 2) == 3
        assert algebra.add(1, -2) == -1

