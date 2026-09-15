class Model:

    def predict(self, data):

        return [
            sum(row)
            for row in data
        ]