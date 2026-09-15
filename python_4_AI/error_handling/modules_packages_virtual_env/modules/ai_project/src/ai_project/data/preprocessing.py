def preprocess(data):

    return [
        [value / 10 for value in row]
        for row in data
    ]