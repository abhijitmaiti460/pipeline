import pytest


def test_addition():
    assert 2 + 2 == 4


def test_string_compare():
    assert "spectrum".upper() == "SPECTRUM"


def test_list_contains():
    devices = ["Samsung", "iPhone", "Pixel"]
    assert "Samsung" in devices


@pytest.mark.smoke
def test_login_demo():
    username = "testuser"
    password = "password123"

    assert username == "testuser"
    assert password == "password123"
