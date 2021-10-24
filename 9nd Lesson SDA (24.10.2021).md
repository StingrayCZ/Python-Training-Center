# 9nd Lesson SDA (24.10.2021)

• edge case (okrajový případ) </p>
• class </p>
• prefix test

```Py
class Calculator:
    def __init__(self, initial_value):
        self.current_value = initial_value
        self.results_history = []

    def add(self, x):
        self.results_history.append(self.current_value)
        self.current_value += x
    
    def divide(self, x):
        self.results_history += [self.current_value]
        self.current_value /= x
    
    def subtract(self, x):
        self.results_history += [self.current_value]
        self.current_value -= x
    
    def multiply(self, x):
        self.results_history += [self.current_value]
        self.multiply = self.multiply * x

    def undo(self):
        if not self.results_history:
            self.current_value = 0
        else:
            self.current_value = self.results_history.pop()
            
        # self.current_value = self.results_history.pop() if self.results_history else 0
       
```

Spoustet v Shellu


```Py
import unittest

from calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def test_init_calculator(self):
        calculator = Calculator(727)
        self.assertEqual(calculator.current_value, 727)
        self.assertEqual(calculator.results_history, [])
```

```Py
python -m unittest
```


```Py
import unittest

import list_analysis


class TransformToStringTestCase(unittest.TestCase):
    def test_transform_list(self):
        input_data = [1, "a", 10.1]
        self.assertEqual(
            list_analysis.transform_items_to_string(input_data),
            ["1", "a", "10.1"]
        )
    
    def test_transform_not_list(self):
        self.assertFalse(
            list_analysis.transform_items_to_string(10)
        )

    def test_transform_string(self):
        self.assertFalse(
            list_analysis.transform_items_to_string("100")
        )
```
