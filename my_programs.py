# This file contains the logic from the notebook cells

# Sum of two numbers
def calculate_sum(a, b):
    return a + b

# Subtraction
def calculate_sub(a, b):
    return a - b

# Division
def calculate_div(a, b):
    return a / b

# Modulo
def calculate_mod(a, b):
    return a % b

# Multiplication
def calculate_mul(a, b):
    return a * b

# Even or Odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Armstrong Number
def is_armstrong(num):
    s = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10
    return num == s

# Palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Prime Number
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False
