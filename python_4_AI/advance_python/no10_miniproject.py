from dataclasses import dataclass


@dataclass

class DataConfig:
    multiplier: float = 2.0


def load_data():
    for i in range(5):
        yield i



def preprocess(data, config):
    for value in data:

        yield value * config.multiplier


def predict(data):
    for value in data:
        yield value + 1


config = DataConfig()

data = load_data()

processed = preprocess(data, config)

predictions = predict(processed)

for prediction in predictions:
    print(prediction)
