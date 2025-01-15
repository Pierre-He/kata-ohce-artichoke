import pytest
from datetime import datetime
from python.ohce.greeter import Greeter


# 9, 15, 21

def test_nightly_greeting():
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    
    response = Greeter(datetime.replace(year=2025, month=1, day=15, hour=21, minute=00, second=00))
    
    assert response == "Good night"


def test_greeting_never_returns_none():
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """

    assert [True * 24] == [Greeter(datetime.replace(year=2025, month=1, day=15, hour=hour, minute=00, second=00)) is not None for hour in range(24)]


def test_ohce_main_loop():
    """
    Given the following inputs:
    - hello
    - oto
    - quit

    Check that the following messages are printed:
    - olleh
    - oto
    - That was a palindrome!
    """
    pytest.fail("TODO")
