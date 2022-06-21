"""
EXCEPTION
    An exception can be defined as an unusual condition in a program resulting in the interruption in the flow of the program.
    Whenever an exception occurs, the program stops the execution, and thus the further code is not executed.
    If we do not handle the exception, the interpreter doesn't execute all the code that exists after the exception.
    Python has many built-in exceptions that enable our program to run without interruption and give the output.
    These exceptions are given below:
                        ZeroDivisionError: Occurs when a number is divided by zero.
                        NameError: It occurs when a name is not found. It may be local or global.
                        IndentationError: If incorrect indentation is given.
                        IOError: It occurs when Input Output operation fails.
                        EOFError:t occurs when the end of the file is reached, and yet operations are being performed.

    To raise an exception, the raise statement is used. The exception class name follows it.
    An exception can be provided with a value that can be given in the parenthesis.
    To access the value "as" keyword is used. "e" is used as a reference variable which stores the value of the exception.
    We can pass the value to an exception to specify the exception type.

    To create a custom exception we need to create a class

try:
    run this code
except:
    run this code if exception occurs
else:
    run this code if ecxeption is not occurs
finally:
    always run the code
"""