# T1W8 Thursday

# 4 Pillars of OOP (contd..)
- Banking System

# __repr__ method
- Special method like __init__, which is used to define a string representation for an object.
- Particularly used for debugging and development because it can give detailed info about an object.

# Composition of OOP
- Sedign principle where a class is composed of one or more objects from other classes.
- It is an alternative to Inheritance and is often more flexible and modular.
- Avoids Inheritance's pitfall: Changes in base class can unintentionally affect the derived class, which may break their functionality.
- Composition does not directly affect the composed class, as the class inherits with compent classes through well-defined interfaces.

# Error Handling
- ## Taxonomy of Python Errors
- Silent Logical Errors - Codes that run fine, but are logically incorrect. Hard to detect so keep testing with print, after each function.
- Assertion Errors - Raised when 'assert' statement fails. If condition is True, nothing happens, if false, raises AssertionError
- Syntax Errors - Errors in the written syntax, that Python interpreter cannot understand. 
- Exceptions - Runtime errors, occurs during program execution. Python has built-in exception to handle common errors.

# Stack Trace Interpretation
- Text that appears when Python encounters an exception, "stack trace"
- When exception occurs, the interpreter prints a stack trace that shows where the error happened and how the code reached that point.
- Start with : Exception, then the trace.
- Example:
Function A started
Function B started
Function C started
Traceback (most recent call last):
  File "/home/chung-v/2024-apr-std/t1w8/t1w8-thursday/stack_trace.py", line 18, in <module>
    function_a()
  File "/home/chung-v/2024-apr-std/t1w8/t1w8-thursday/stack_trace.py", line 3, in function_a
    function_b()
  File "/home/chung-v/2024-apr-std/t1w8/t1w8-thursday/stack_trace.py", line 8, in function_b
    function_c()
  File "/home/chung-v/2024-apr-std/t1w8/t1w8-thursday/stack_trace.py", line 14, in function_c
    result = 10 / 0 
ZeroDivisionError: division by zero

# Try / Except / Finally
- Comprehensive way to handle exceptions.
- Ensures code always runs, regardless whether an error occcurs.
- 'try' block has code that may raise exception.
- 'except' block has code that handles the exception.
- 'finally' block has code that should always be executed.