#super() allows you to call functionality from the parent class

class Model:

    def __init__(self, name):

        self.name = name


class NeuralNetwork(Model):

    def __init__(self, name, layers):
        super().__init__(name)
        self.layers = layers

