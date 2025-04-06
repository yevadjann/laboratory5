import pytest

def add(x, y):
    return x + y

@pytest.fixture
def add_test_data():
    return [(2, 3, 5), (-1, 1, 0), (0, 0, 0)]

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected
