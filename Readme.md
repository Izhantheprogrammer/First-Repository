# Python Functions Overview

Python functions are fundamental components of the language, enhancing code organization and enabling code reuse.

## Table of Contents

- [Predefined Functions](#predefined-functions)
- [User-defined Functions](#user-defined-functions)
- [Handling Arguments and Parameters](#handling-arguments-and-parameters)
- [Default Function Parameters](#default-function-parameters)
- [Varied Argument Types](#varied-argument-types)
- [Lambda Functions](#lambda-functions)
- [Recursive Functions](#recursive-functions)
- [Decorators](#decorators)
- [Handling Unlimited Arguments](#handling-unlimited-arguments)

## Predefined Functions

Python offers a diverse range of built-in functions, such as `len()`, readily available for immediate use without requiring additional imports.

## User-defined Functions

Users have the ability to define their own functions using the `def` keyword, facilitating tailored functionality to suit specific requirements.

## Handling Arguments and Parameters

Functions can receive inputs in the form of arguments, defined within the function signature as parameters.

## Default Function Parameters

Parameters can possess default values, granting them an optional status when the function is invoked.

## Varied Argument Types

Functions accommodate different argument types, including optional arguments with predefined defaults, positional arguments reliant on their order, and keyword arguments specified by name.

## Lambda Functions

Python allows the creation of anonymous functions using the `lambda` keyword for on-the-fly functionality definition.

## Recursive Functions

Functions can call themselves, enabling the resolution of problems in a recursive manner.

## Decorators

Functions can be wrapped by other functions to extend their behavior seamlessly, without direct modification of their core code.

## Handling Unlimited Arguments

Functions can be designed to accept an indefinite number of arguments, either as positional or keyword arguments.

Understanding and proficiently utilizing these diverse features of Python functions empowers developers to craft cleaner, more efficient, and maintainable code.



## Table of Contents
1. [Pre-defined Functions](#pre-defined-functions)
2. [User-defined Functions](#user-defined-functions)
3. [Arguments and Parameters](#arguments-and-parameters)
4. [Default Functions](#default-functions)
5. [Optional, Positional, and Keyword Arguments](#optional-positional-and-keyword-arguments)
6. [Lambda Functions](#lambda-functions)
7. [Recursive Functions](#recursive-functions)
8. [Decorators](#decorators)
9. [Functions with Unlimited Arguments](#functions-with-unlimited-arguments)

---

## Pre-defined Functions

Python provides several built-in functions that are readily available for use.

```python
# Example of a pre-defined function
result: int = len("Hello, World!")
print(result)  # Output: 12
```

---

## User-defined Functions

You can define your own functions in Python using the `def` keyword.

```python
def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!
```

---

## Arguments and Parameters

Parameters are the variables listed inside the parentheses in the function definition, whereas arguments are the values passed to the function when it is called.

```python
def add(a: int, b: int) -> int:
    return a + b

result: int = add(5, 3)
print(result)  # Output: 8
```

---

## Default Functions

You can assign default values to parameters, making them optional during a function call.

```python
def power(base: int, exponent: int = 2) -> int:
    return base ** exponent

print(power(3))        # Output: 9
print(power(3, 3))     # Output: 27
```

---

## Optional, Positional, and Keyword Arguments

### Optional Arguments
Optional arguments are those that have a default value.

```python
def greet(name: str = "Guest") -> None:
    print(f"Hello, {name}!")

greet()            # Output: Hello, Guest!
greet("John")      # Output: Hello, John!
```

### Positional Arguments
Positional arguments are arguments that need to be included in the proper position or order.

```python
def subtract(a: int, b: int) -> int:
    return a - b

result: int = subtract(10, 5)
print(result)  # Output: 5
```

### Keyword Arguments
Keyword arguments are arguments passed to a function by explicitly specifying the name of the parameter.

```python
def divide(dividend: int, divisor: int) -> float:
    return dividend / divisor

result: float = divide(divisor=5, dividend=25)
print(result)  # Output: 5.0
```

---

## Lambda Functions

Lambda functions are anonymous functions defined using the `lambda` keyword.

```python
square: callable = lambda x: x * x
print(square(4))  # Output: 16
```

---

## Recursive Functions

A recursive function is a function that calls itself.

```python
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result: int = factorial(5)
print(result)  # Output: 120
```

---

## Decorators

Decorators are a way to modify or extend the behavior of a function.

```python
def my_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> None:
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(name: str) -> None:
    print(f"Hello {name}!")

say_hello("John")
```

---

## Functions with Unlimited Arguments

You can define functions that accept an arbitrary number of arguments.

### Unlimited Positional Arguments

```python
def add(*numbers: int) -> int:
    return sum(numbers)

result: int = add(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

### Unlimited Keyword Arguments

```python
def print_key_values(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(name="John", age="30", country="USA")
```