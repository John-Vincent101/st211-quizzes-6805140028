import pytest
from bank import BankAccount

def test_deposti_increases_balance():
    account = BankAccount(balance=100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_withdraw_decreases_balance():
    account = BankAccount(100)
    new_balance = account.withdraw(67)
    assert new_balance == 33

def test_deposit_negative_amount_raises_value_error():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdraw_more_than_balance_raises_value_error():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(200)

def test_withdraw_exact_balance_leaves_zero_balance():
    account = BankAccount(100)
    new_balance = account.withdraw(100)
    assert new_balance == 0