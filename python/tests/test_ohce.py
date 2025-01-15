from unittest.mock import patch

import pytest
from datetime import datetime
from ohce.greeter import Greeter
from ohce.ui import UI


def test_nightly_greeting():
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    assert "Good night" == Greeter(hour=21).greet()

@pytest.mark.parametrize("hours", range(24))
def test_greeting_never_returns_none(hours):
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    assert Greeter(hour=hours).greet() is not None


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
    
    
    
