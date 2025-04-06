import pytest

def add(x, y):
    return x + y

@pytest.fixture
def add_test_data():
    return [(2, 3, 5), (-1, 1, 0), (0, 0, 0)]

def test_add_with_fixture(add_test_data):
    for a, b, expected in add_test_data:
        assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected
