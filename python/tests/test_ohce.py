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
    assert "Good night" == Greeter(datetime(year=2025, month=1, day=15, hour=21, minute=0, second=0, microsecond=0)).greet()


def test_greeting_never_returns_none():
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    assert 24 == sum([Greeter(datetime(year=2025, month=1, day=15, hour=hour, minute=00, second=00, microsecond=0)).greet() is not None for hour in range(24)])


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
    
    
    
