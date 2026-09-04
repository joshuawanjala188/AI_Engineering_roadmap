#Encapsulation means keeping data and behavior together and controlling how the data is accessed or changed

class Model:

    def __init__(self, learning_rate):
        self.learning_rate = learning_rate # _ convention means it is intended for internal use


#Propereties allows you to controll access to attributes
    
    
    
    
    
    
    
    
    
    @property

    def learning_rate(self):

        return self._learning_rate
#Property setters - you can also control changes
    @learning_rate.setter
    def learning_rate(self, value):

        if value <= 0:

            raise ValueError("Learning rate must be positive")

        self._learning_rate = value

                

model =  Model(-1)

print(model.learning_rate)
    

