#Is creating your own exception type, which allows application to distinguish between different types of failures

"""
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

14. Custom Exceptions

You can create your own exception types.

class ModelTrainingError(Exception):
    pass

Then:

raise ModelTrainingError(
    "Model training failed"
)

This allows your application to distinguish between different types of failures.

15. AI Example — Custom Exceptions
class DataValidationError(Exception):
    pass


class ModelTrainingError(Exception):
    pass

Then:

def validate_data(data):

    if not data:
        raise DataValidationError(
            "Dataset is empty"
        )

And:

try:
    validate_data([])

except DataValidationError as error:
    print(f"Data error: {error}")

Output:

Data error: Dataset is empty
16. Exception Hierarchy

Python exceptions form a hierarchy.

Simplified:

BaseException
    │
    ├── Exception
    │     │
    │     ├── ValueError
    │     ├── TypeError
    │     ├── RuntimeError
    │     ├── KeyError
    │     ├── IndexError
    │     ├── FileNotFoundError
    │     └── ...
    │
    ├── KeyboardInterrupt
    └── SystemExit

Most application errors derive from:

Exception

Your custom exceptions should normally inherit from Exception.

17. Catching Parent Exceptions

Because:

ValueError
   ↓
Exception

this works:

try:
    int("hello")

except Exception:
    print("An exception occurred")

But it's generally preferable to catch the most specific exception you reasonably can.

18. Chaining Exceptions

Sometimes one error causes another.

You can preserve the original cause:

try:
    number = int("hello")

except ValueError as error:
    raise RuntimeError(
        "Failed to process user input"
    ) from error

The from error part tells Python:

This new exception was caused by the original exception.

This is useful when building layers of software.

19. Assertions

Python provides assert.

age = 20

assert age >= 0

If the condition is false:

assert age >= 0

Python raises:

AssertionError

You can add a message:

assert age >= 0, "Age cannot be negative"
20. Assertions vs Exceptions

Use assertions mainly for internal assumptions and development checks.

For user-controlled or external data, use explicit validation:

if age < 0:
    raise ValueError("Age cannot be negative")

Don't rely on assertions as your main input-validation mechanism.
"""