from typing import Callable , Tuple, Dict
#Python functions
'''
Think of a function as a little named container for a group 
of your code!
To run the code in a function, you must call the function.
A function can be called from anywhere after the function is defined. 

Syntax of Python Function
Code

def name_of_function( parameters : datatype ) -> return type(if they return something):  
    """This is a docstring"""  
    # code block  

The following elements make up define a function, as seen above.

1.The beginning of a function header is indicated by a keyword 
called def.

2.name_of_function is the function's name that we can use 
to separate it from others. We will use this name to call 
the function later in the program. The same criteria 
apply to naming functions as to naming variables 
in Python.

3.We pass arguments to the defined function using parameters along with their datatypes,as code looks more professional. 
They are optional, though.

4.The function header is terminated by a colon (:).

5.We can use a documentation string called docstring 
in the short form to explain the purpose of the function.

6.The body of the function is made up of several valid Python
statements.The indentation depth of the whole code block must 
be the same (usually 4 spaces).

7.We can use a return expression to return a value from 
a defined function, it is also a professioal practice to define the return datatype.

example...
def demo_func(param:int) -> int :
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc

>>>demo_func(6)
10

Functions can return a value using a return statement. Functions are 
a common feature among all programming languages

The keyword def introduces a function definition. It must 
be followed by the function name and the parenthesized list 
of formal parameters along with their datatypes. The statements that form the body of 
the function start at the next line,and  be indented.

'''
#Basic Example of a User-Defined Function
def square( num: int ) ->int :  
    """ 
    This function computes the square of the number. 
    """  
    return num**2 
     
print(square.__doc__) 
'''.__doc__(This line prints out the docstring associated with the square function.
 It accesses the docstring using the __doc__ attribute of the function.)'''

object_ = square(9)  
print( "The square of the number is: ", object_ ) 

'''
Output
This function computes the square of the number.
The square of the number is:  81
'''

#Example 1
def demo_func(param:int) -> int:
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc

demo_func(6)
print(demo_func(6)) # returns 10

#Example 2
# Defining a function  
def a_function( string ):  
    "This prints the value of length of string"  
    return len(string)  
print( "Length of the string Functions is: ", a_function("Muhammad Hashim") )
print( "Length of the string Functions is: ", a_function( "Functions" ) )  
print( "Length of the string Python is: ", a_function( "Python" ) )

#Example 3
#Note: I will be defining a function to demo :)
#The basics
def number_play(x:int):
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

number_play(-1)
number_play(0)
number_play(1)
number_play(2)

'''
Negative changed to zero
Zero
Single
More
'''
  
#Pass by Reference Vs Value
'''
In the Python programming language, all arguments are supplied by reference.
It implies that if we modify the value of an argument within a function, 
the change is also reflected in the calling function. For instance,
'''
# defining the function  
def square( my_list:list ):  
    '''''This function will find the square of items in list'''  
    squares = []  
    for l in my_list:  
        squares.append( l**2 )  
    return squares  
  
# calling the defined function  
list_:list = [1, 2, 4, 6, 8, 10]
result = square( list_ )  
print( "Squares of the list is: ", result )  

#Function Arguments
'''
The following are the types of arguments that we can use to 
call a function
1.  Default arguments
2.  Keyword arguments
3.  Required arguments
4.  Variable-length arguments
'''
#Default Arguments
'''
A default argument is a kind of parameter that takes input as a default 
value if no value is supplied to the argument when the function is 
called. Default arguments are demonstrated in the following instance.
'''
# Python code to demonstrate the use of default arguments  
# defining a function  
def function( num1 = 40, num2 = 40 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
    
# Calling the function without argument  
print( "Passing without argument" )  
function()
# Calling the function and passing only one argument  
print( "Passing one argument" )  
function(10)  
# Now giving two arguments to the function  
print( "Passing two arguments" )  
function(10,30)  

'''
Passing without argument
num1 is:  40
num2 is:  40
Passing one argument
num1 is:  10
num2 is:  40
Passing two arguments
num1 is:  10
num2 is:  30
'''

#Keyword Arguments
'''
The arguments in a function called are connected to keyword arguments. 
If we provide keyword arguments while calling a function, the user uses 
the parameter label to identify which parameters value it is.

Since the Python interpreter will connect the keywords given to link 
the values with its parameters, we can omit some arguments or 
arrange them out of order. The function() method can also be 
called with keywords in the following manner:
'''
# Python code to demonstrate the use of keyword arguments  
  
# Defining a function  
def function( num1:int, num2: int ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
  
# Calling function and passing arguments without using keyword  
print( "Without using keyword" )  
function( 50, 30)     
      
# Calling function and passing arguments using keyword  
print( "With using keyword" )  
function( num2 = 50, num1 = 30)

'''
Without using keyword
num1 is:  50
num2 is:  30
With using keyword
num1 is:  30
num2 is:  50
'''

#Required Arguments
'''
The arguments given to a function while calling in a pre-defined 
positional sequence are required arguments. The count of required 
arguments in the method call must be equal to the count of arguments 
provided while defining the function.

We must send two arguments to the function function() in the correct 
order,or it will return a syntax error, as seen below.
'''
# Python code to demonstrate the use of default arguments  
  
# Defining a function  
def function( num1: int , num2: int ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  

print( "Passing out of order arguments" )  
function( 30, 20 )     
  
# Calling function and passing only one argument  
print( "Passing only one argument" )  
try:  
    function( 30 )  
except:  
    print("Function needs two positional arguments") 

'''
Output
Passing out of order arguments
num1 is:  30
num2 is:  20
Passing only one argument
Function needs two positional arguments
'''

#Variable-Length Arguments
'''
We can use special characters in Python functions to pass as many 
arguments as we want in a function. There are two types of characters
that we can use for this purpose:

1.  *args -These are Non-Keyword Arguments
2.  **kwargs - These are Keyword Arguments.

'''
# Python code to demonstrate the use of variable-length arguments     
# Defining a function  
def function( *args_list ):  
    ans = []  
    for l in args_list:  
        ans.append( l.upper() )  
    return ans  
# Passing args arguments  
object = function('Python', 'Functions', 'tutorial')  
print( object )  
  
# defining a function  
def function( **kargs_list ):  
    ans = []  
    for key, value in kargs_list.items():  
        ans.append([key, value])  
    return ans  
# Passing kwargs arguments  
object = function(First = "Python", Second = "Functions", Third = "Tutorial")  
print(object)  
'''
Output
['PYTHON', 'FUNCTIONS', 'TUTORIAL']
[['First', 'Python'], ['Second', 'Functions'], ['Third', 'Tutorial']]
'''
#return Statement
'''
We write a return statement in a function to leave a function and give 
the calculated value when a defined function is called.

Syntax:
return < expression to be returned as output >  
An argument, a statement, or a value can be used in the return statement, 
which is given as output when a specific task or function is completed. 
If we do not write a return statement, then None object is returned by a 
defined function.
Here is an example of a return statement in Python functions.
'''
# Python code to demonstrate the use of return statements  
  
# Defining a function with return statement  
def square( num:int ) -> int:  
    return num**2  
   
# Calling function and passing arguments.  
print( "With return statement" )  
print( square( 39 ) )  
  
# Defining a function without return statement   
def square( num:int ) -> int:  
     num**2   
  
# Calling function and passing arguments.  
print( "Without return statement" )  
print( square( 39 ) )  

'''
Output
With return statement
1521
Without return statement
None
'''
#Printing Docstring using __doc__ method
def my_function():
    """Demonstrates triple double quotes
    docstrings and does nothing really."""
   
    return None
  
print("Using __doc__:")
print(my_function.__doc__)
  
print("Using help:")
help(my_function)

'''
Output
Using __doc__:
Demonstrates triple double quotes
    docstrings and does nothing really.
Using help:
Help on function my_function in module __main__:

my_function()
    Demonstrates triple double quotes
    docstrings and does nothing really.
'''

'''
As guidance:

Use positional-only if you want the name of the parameters to not 
be available to the user. This is useful when parameter names have 
no real meaning, if you want to enforce the order of the arguments 
when the function is called or if you need to take some positional 
parameters and arbitrary keywords.

Use keyword-only when names have meaning and the function definition 
is more understandable by being explicit with names or you want to 
prevent users relying on the position of the argument being passed.

For an API, use positional-only to prevent breaking API changes if 
the parameter’s name is modified in the future.
'''

# Higher-order Functions

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

result = apply(lambda x: x ** 2, 5)
print(result)
     
# Closures

def outer_func(x: int) -> Callable[[int], int]:
    def inner_func(y: int) -> int:
        return x + y
    return inner_func

closure = outer_func(10)
print(closure(5))  # Outputs: 15


# Recursion

def factorial(x: int) -> int:
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print("The factorial of", num, "is", factorial(num))
     
#Python Lambda Functions
'''
Lambda Functions in Python are anonymous functions, 
implying they don't have a name. The def keyword is needed to create 
a typical function in Python, as we already know. We can also use 
the "lambda" keyword in Python to define an unnamed function.

Syntax of Python Lambda Function
lambda arguments: expression 
'''
#Example1 
# Code to demonstrate how we can use a lambda function  
add = lambda num: num + 4  
print( add(6) )  
'''
Output
10
'''
#Example2
def reciprocal( num ):  
    return 1 / num  
lambda_reciprocal = lambda num: 1 / num  
print( "Lambda keyword: ", lambda_reciprocal(6) ) 
print( "Def keyword: ", reciprocal(6) )  
'''
Output
Def keyword:  0.16666666666666666
Lambda keyword:  0.16666666666666666
'''
#Example3 Lambda Function with filter()
# Code to filter odd numbers from a given list  
list_ = [34, 12, 64, 55, 75, 13, 63]  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  
print(odd_list)  
'''
Output
[55, 75, 13, 63]
'''
#Example4 Lambda Function with map()
#Code to calculate the square of each number of a list using the map() 
# function    
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]    
squared_list = list(map( lambda num: num ** 2 , numbers_list ))    
print( squared_list ) 
'''
Output
[4, 16, 25, 1, 9, 49, 64, 81, 100]
'''

#Example5 Lambda Function with List Comprehension and For Loop
#Code to calculate square of each number of list using list comprehension  
squares = [lambda num = num: num ** 2 for num in range(0, 11)]     
for square in squares:  
    print( square(), end = " ")  
'''
Output
0 1 4 9 16 25 36 49 64 81 100 
'''    

#Example 6 Lambda Function with if-else
Minimum = lambda x, y : x if (x < y) else y     
print(Minimum( 35, 74 )) 
'''
Output
35
'''

#Example 7 Printing number tables with functions

def demo_func(param:int):
  res: int = demo_func(10)
print(f"The result is {res}")
print(param)
l= [1,2,3,4,5,6,7,8,9,10]

def TableFun(tableNo : int, limit : int ) -> None:
    for i in range(1,len(l)):
        print(f"{tableNo} * {i} = {tableNo*i}")

    TableFun(5,11)
    print(TableFun(5,11))
    TableFun(4,11)
    print()
    TableFun(2,11)
    print()
    TableFun(11,11)

#Example 8 Functions with Exceptions
    
    # Raising an Exception
x : int = 10
if x > 5:
    raise Exception(f'x should not exceed 5. The value of x was: {x}')

num = [3, 4, 5, 7]  
if len(num) > 3:  
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" ) 

# Assertion Exception
def square_root( Number : int ) -> int:  
    assert ( Number < 0), "Give a positive number"
    return Number**(1/2)  
  
#Calling function and passing the values  
no1 : int = square_root(-36)
no2 : int = square_root(36)
print(no1)  
#  print(no2) 

#Example 9 calling functions by arguments,values and errors in functions

# Call by Value
a : int = 5
def abc(num : int ) -> None:
    num = 6
    print(id(num))
    print(num)

print(id(a))
abc(a)
print(a)

# Call by Reference
l : list = [1,2,3,4,5]
def myList(newList : list[int]) -> None:
    print(newList)
    print(id(newList))
    newList.append(6)

print(id(l))
myList(l)
print(l)


a = int(input("Please Enter a Number\t"))
b = int(input("Please Enter another Number\t"))

res : int = (a/b)
print(f"Value is {res}")


a : int = 1
while(True):
    print(a)
    a += a

l: list[int] = [1,2,3]
try:
    # a = int(input("Please Enter a Number\t"))
    # b = int(input("Please Enter another Number\t"))
    # print(a/b)
    print(k[3])
except ZeroDivisionError:
    print("You cannot Divide any number with zero")
except IndexError:
    print('List does not contain that index number')
except NameError:
    print('Variable name is not valid')
    # pass

#Example 9 Arithmetic operations with Functions
    
    def display(a : int, b : int) -> int:
    return a + b

a = display(10,20)
print(a) 


def add_two_numbers(num1 : int , num2 : int)->int:
    print(f"num1 value is {num1} and num 2 value is {num2}")
    return num1 + num2

x : int = add_two_numbers(7,20)
print(f"The sum is {x}")

a = lambda num1, num2 : num1 + num2
sum : Callable[[int,int],int] = lambda no1, no2 : no1 + no2 
print(sum(2,5))
a(7,8)

#Example 10 Squaring a list and shortlisting it's even and odd numbers

square = lambda no : 2 * no + str(2)
print(square('Name'))
data : list[int] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

d1= list(map(lambda x:x**2 , data))
even :list[int] = list(filter(lambda x:x%2==0 ,data))
odd :list[int] = list(filter(lambda x:x%2==1 ,data))


print(data)
print('--------------------')
print(d1)
print(even)
print(odd)

#Example 11 Generator Function
# Generator Function

def my_range(start:int , end:int , step: int=1):
    for i in range(start,end+1,step):
        yield i # Generator fucntion
a = my_range(1,10)
print(next(a))
print(next(a))
print(next(a))
print("Hello World")
print(next(a))
print(next(a))
print(next(a))
print(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print("Hello World")

#Example 12 Greeting Function 

# List Items

def abc(*names : Tuple[str, ...]) -> None:
    """
    This function greets all persons in the names tuple.
    """  
    for name in names:
        print("Hello", name)


a = abc('Muhammad Mowahid','Abdullah Sobadar','Ahmed NotesWala','Ishaque Londonwala','Butt Khamoshi Wala')
print(abc.__doc__)
print(a)

#Dictionary Items

def greet(**greeting: Dict[str,str]) -> None:
    print(f'Hey {greeting}')

greet(a="Mowahid", b='Sobadar')

#Example 11 Functions with Class Callable and Decorator Functions

def my_decorator(func: Callable[[], None])-> Callable[[], None]:
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


