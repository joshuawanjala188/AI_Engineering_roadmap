#inheritance allows one class to derive from another

"""class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()"""

class Model:

    def train(self):
        print("Training model")

    def predict(self, x):
        print("Making prediction")   

class NeuralNetwork(Model):
    pass


model = NeuralNetwork()
model.train()

model.predict([1, 2, 3])


        
    