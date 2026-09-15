"""# A protocol describes what an object should be able to do
For example, instead of caring about a specific class:

"Is this a Dog?"

you can care about behavior:

"Does this object have predict()?"

This is closely related to duck typing.

The famous idea is:

If it behaves like the required object, we can use it.

Structural Typing
python's typing module provides protocol

Why Protocols Matter in AI

Imagine your application supports:

Open-source model
       +
Cloud model
       +
Custom model

You can define a common interface:

predict()

Then your application can work with different models without being tightly coupled to one implementation.

"""

from typing import Protocol

class Predictor(Protocol):

    def predict(self, x):
        ...

#Now multiple classes can satisfy the interface

class ModelA:

    def predict(self, x):
        return "A"


class ModelB:
    def predict(self, x):

        return "B"



