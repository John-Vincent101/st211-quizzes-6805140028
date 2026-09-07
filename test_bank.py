from bank import BankAccount

def test_deposti_increases_balance():
    account = BankAccount(balance=100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def testwithdraw():
    account = BankAccount(100)
    new_balance = account.withdraw(67)
    assert new_balance == 33