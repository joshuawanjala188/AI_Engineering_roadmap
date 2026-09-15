import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():

    logging.info("Loading dataset")

    data = [1, 2, 3, 4, 5]

    logging.info(
        "Loaded %d dataset",
        len(data)

        
    )

    return data

def preprocess(data):

    logging.info("Starting preprocessing")

    processed = [x*2 for x in data]

    logging.info("Preprocessing complete")

    return processed

def predict(data):

    logging.info("Starting prediction")

    predictions = [x+1 for x in data]

    logging.info("Prediction complete")

    return predictions


data = load_data()

processed = preprocess(data)

predictions = predict(processed)

print(predictions)
