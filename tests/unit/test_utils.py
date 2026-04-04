from curly_fiesta.utils import greet


def test_greet(sample_name):
    assert greet(sample_name) == "Hello, Curly!"


def test_greet_empty():
    assert greet("") == "Hello, !"
