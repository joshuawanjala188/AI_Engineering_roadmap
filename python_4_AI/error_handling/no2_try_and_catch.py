"""The basic structure

try:
    risky_operation()

except:
    handle_error()

try:
    10/0

except:
    print("something went wrong")
    
    
 Catching Specific Exceptions
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

This is much better.

Another:

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number")
5. Multiple Exceptions

You can handle different errors separately:

try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

Now the program can respond appropriately to different failures.   
    

#Else - executes when the try block succeeds

try:
    number = int("10")

except ValueError:
    print("Invalid")

else:
    print("Conversation Succeeded")

7. finally

finally runs whether an exception occurred or not.

try:
    print("Working")

except Exception:
    print("Error")

finally:
    print("Cleanup")

Output:

Working
Cleanup

If an error happens:

Error
Cleanup
8. Why finally Is Useful

Suppose you open a resource:

file = open("data.txt")

try:
    data = file.read()

finally:
    file.close()

Even if something fails, finally is used for cleanup.

However, for files, the preferred approach is normally:

with open("data.txt") as file:
    data = file.read()
9. Catching the Exception Object

You can access information about the exception:

try:
    result = 10 / 0

except ZeroDivisionError as error:
    print(error)

Output:

division by zero

The variable:

error

contains the exception object.

10. Catching General Exceptions

Sometimes you genuinely need to catch a broad range of exceptions.

Use:

except Exception as error:

Example:

try:
    result = some_operation()

except Exception as error:
    print(f"Error: {error}")

This is better than:

except:

because it doesn't catch certain special exceptions such as KeyboardInterrupt and SystemExit.

11. Don't Hide Errors

Avoid:

try:
    important_operation()
except:
    pass

This is dangerous.

If something breaks, you'll have no idea why.

Bad:

ERROR
 ↓
ignored
 ↓
program continues incorrectly

Better:

try:
    important_operation()

except Exception as error:
    print(f"Operation failed: {error}")

Even better in production: use logging.

We'll get there shortly.

12. Raising Exceptions

You can deliberately raise an exception using raise.

def divide(a, b):

    if b == 0:
        raise ValueError("b cannot be zero")

    return a / b

Now:

divide(10, 0)

raises:

ValueError: b cannot be zero
13. Why raise Matters in AI

Suppose your model requires a positive learning rate.

def create_model(learning_rate):

    if learning_rate <= 0:
        raise ValueError(
            "Learning rate must be greater than zero"
        )

    ...

Instead of allowing invalid configuration to reach the training stage, you reject it immediately.

This is called fail fast.
"""
