# tests/test_dummy.py

def test_always_passes():
    assert 1 + 1 == 2

def test_string_match():
    greeting = "hello"
    assert greeting.upper() == "HELLO"
