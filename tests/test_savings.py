from savings.savings import SavingsAccount

def test_deposit():
    account = SavingsAccount("John Doe")
    assert account.deposit(1000) == "1000 deposited. Total balance: 1000"

def test_withdraw():
    account = SavingsAccount("John Doe")
    account.deposit(2000)
    assert account.withdraw(1500) == "1500 withdrawn. Remaining balance: 500"
