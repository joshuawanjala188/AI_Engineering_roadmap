#A child class can replace a parents's behavior

class Model:

    def predict(self):
        print("Generic prediction")

class NeuralNetwork(Model):

    def predict(self):
        print("Neural network prediction")

model = NeuralNetwork()
model.predict()