#it means different objets can provide the same interface but behave differently

class CNN:

    def predict(self, image):

        return "CNN prediction"


class Transformer:

    def predict(self, image):

        return "Transformer prediction"

models = [CNN(), Transformer()]

for model in models:
    print(model.predict("image"))