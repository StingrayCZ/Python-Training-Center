# 10th Lesson SDA (30.10.2021)


spusteni shellu: poetry shell

python -m unittest test

```Py
import unittest


class BankAccount:
    pass

        
class BankAccountTest(unittest.TestCase):
    def test_empty_creation(self):
        acc = BankAccount("Mrkev")
        self.assertEqual(acc.owner, "Mrkev")
        self.assertEqual(0, acc.balance)
    
    def test_creation_with_initial_balance(self):
        acc = BankAccount("Mrkev", balance=100)
        self.assertEqual(acc.owner, "Mrkev")
        self.assertEqual(100, acc.balance)
        
    def test_deposit_owner(self):
        acc = BankAccount("Mrkev", balance=100)
        acc.deposit("Mrkev", 100)
        self.assertEqual(200, acc.balance)
        
    def test_deposit_not_owner(self):
        acc = BankAccount("Mrkev", balance=100)
        acc.deposit("Kedluben", 100)
        self.assertEqual(190, acc.balance)
                          
    def test_deposit_not_owner_just_above_fee(self):
        acc = BankAccount("Mrkev", balance=100)
        acc.deposit("Kedluben", 11)
        self.assertEqual(101, acc.balance)
        
    def test_deposit_lower_than_fee(self):
        acc = BankAccount("Mrkev", balance=100)
        acc.deposit("Kedluben", 9)
        self.assertEqual(100, acc.balance)
                        
    def test_withdraw_owner_available_amount(self):
        acc = BankAccount("Mrkev", balance=100)
        result = acc.withdraw("Mrkev", 100)
        self.assertTrue(result)
        self.assertEqual(0, acc.balance)
        
    def test_withdraw_owner_not_available_amount(self):
        acc = BankAccount("Mrkev", balance=10)
        result = acc.withdraw("Mrkev", 100)
        self.assertFalse(result)
        self.assertEqual(10, acc.balance)
        
    def test_withdraw_not_owner(self):
        acc = BankAccount("Mrkev", balance=100)
        result = acc.withdraw("Kedluben", 100)
        self.assertFalse(result)
        self.assertEqual(100, acc.balance)
```
