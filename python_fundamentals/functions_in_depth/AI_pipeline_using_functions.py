
def load_data():

    return [10, 20, 30, 40, 50]

def clean_data(data):

    return [x for  x in data if x > 0]

def predict(data, weight, bias):

    return [ weight * x + bias  for x in data]


def calculate_average(values):

    return sum(values) / len(values)


data = load_data()

cleaned = clean_data(data)


prediction = predict(
    cleaned,
    0.9,
    1
)

print(prediction)