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
