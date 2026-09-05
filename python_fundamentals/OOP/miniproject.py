
class DataLoader:

    def load(self):

        return [1, 2, 3, 4, 5]


class Preprocessor:

    def process(self, data):

        return [x* 2 for x in data]


class Model:

    def predict(self, data):
        return [x + 1 for x in data]

class Pipeline:

    def __init__(self):
        self.loader = DataLoader()

        self.preprocessor = Preprocessor()
        self.model = Model()


    def run(self):

        data = self.loader.load()
        data = self.preprocessor.process(data)

        predictions = self.model.predict(data)

        return predictions    



pipeline = Pipeline()

print(pipeline.run())