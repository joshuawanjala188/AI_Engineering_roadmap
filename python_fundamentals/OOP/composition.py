#composition means buiding a class using other objects

class Tokenizer:

    def tokenize(self, text):
        return text.split()

class Model:

    def predict(self, token):
        return "prediction"


class AIPipeline:

    def __init__(self):
        self.tokenizer = Tokenizer()
        self.model = Model()


    def run(self, text):
        tokens = self.tokenizer.tokenize(text)
        return self.model.predict(tokens)    

pipeline = AIPipeline()

print(pipeline.run("Hello AI"))