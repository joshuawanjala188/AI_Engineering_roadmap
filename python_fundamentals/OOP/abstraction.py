#exposing what something does while hiding unnecessary implementation details
#python provides abstarct base classes through the abc module

from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def predict(self, x):
        pass

class NeuralNetwork(Model):

    def predict(self, x):
        return "Prediction"