# 10th Lesson SDA (30.10.2021)


spusteni shellu: poetry shell

python -m unittest test

python -m unittest bank_account.BankAccountTest

```Py
import unittest


class BankAccount:
    def__init__(self, owner):
        self.owner = owner
        self.balance = 0
        
    def deposit(self, owner, amount):
        # self.balance += amount
        if self.owner != user:
            amount -= 10
        amount = 0 if amount < 0 else amount
        self.balance += amount
        
    def withdraw(self. user, amount):
        if user != self.owner or amount > self.balance:
            
        
        return True

        
class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.owner = "Mrkev"
        self.initial_balance = 100
        

    def test_empty_creation(self):
        acc = BankAccount("Mrkev")                 # konstruktor
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

```Py
""" ORIGO """
import unittest


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, user, amount):
        if self.owner != user:
            amount -= 10
        amount = 0 if amount < 0 else amount
        self.balance += amount

    def withdraw(self, user, amount):
        if user != self.owner or amount > self.balance:
            return False

        self.balance -= amount
        return True


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.owner = "Mrkev"
        self.initial_balance = 100
        self.acc = BankAccount(self.owner, balance=self.initial_balance)

    def test_empty_creation(self):
        acc = BankAccount("Mrkev")
        self.assertEqual(acc.owner, "Mrkev")
        self.assertEqual(0, acc.balance)
    
    def test_creation_with_initial_balance(self):
        self.assertEqual(self.acc.owner, self.owner)
        self.assertEqual(self.initial_balance, self.acc.balance)
        
    def test_deposit_owner(self):
        self.acc.deposit(self.owner, 100)
        self.assertEqual(self.initial_balance + 100, self.acc.balance)
        
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

## Modules

modul = slozka 

```Py
import unittest

class Item:
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name

    def __str__(self):
        return f"#{self.id} {self.name}"

    def __repr__(self):
        return self.__str__()

class Warehouse:
    def __init__(self):
        self._items = []

    def stock(self, item: Item):
        self._items.append(item)

    def count(self, item_name: str):
        return len([1 for x in self._items if x.name == item_name])
        # return len(list(filter(lambda x: x.name == item_name, self._items)))

    def unstock_id(self, id: int):
        found_item = None
        for item in self._items:
            if item.id == id:
                found_item = item
                self._items.remove(found_item)
                break
            
        return found_item

    def unstock_name(self, item_name: str):
        found_items = []
        for item in self._items:
            if item.name == item_name:
                found_items.append(item)
                self._items.remove(item)

        return found_items

    def inventory(self):
        inventory = {}
        for item in self._items:
            if item.name in inventory:
                inventory[item.name] += 1
            else:
                inventory[item.name] = 1

        return inventory

    def item_names(self):
        return [item.name for item in self._items]


class WarehouseTestCase(unittest.TestCase):
    def setUp(self):
        self.wh = Warehouse()
        self.item = Item(1, "Sroubovak")
    
    def test_stock_item(self):
        pass
```
