import pytest


def always_returns_true():
    print("True")


def test_always_returns_true():
    assert always_returns_true()
