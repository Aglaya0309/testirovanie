def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b


def remainder(a, b):
   if b == 0:
      raise ZeroDivisionError("Деление на ноль невозможно")
   return a % b