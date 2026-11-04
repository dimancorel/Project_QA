import random
import pytest


def get_payment_status():
    return random.choice(["paid", "declined"])


def test_payment_error(monkeypatch):

    def fake_choice(options):
        raise ValueError("Payment error")

    monkeypatch.setattr(random, "choice", fake_choice)

    with pytest.raises(ValueError):
        get_payment_status()