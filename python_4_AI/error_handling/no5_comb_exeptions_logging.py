"""import logging

logging.basicConfig(level=logging.INFO)


def load_data():

    try:

        logging.info("Loading data")

        data = [1, 2, 3]

        return data


    except Exception:

        logging.exception(
            "failed to load data"
        )

        raise


load_data()"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataValidationError(Exception):
    pass


def load_data():
    logging.info("Loading data")

    data = [10, 20, 30, 40]

    if not data:
        raise DataValidationError(
            "Dataset is empty"
        )

    logging.info(
        "Loaded %d records",
        len(data)
    )

    return data


def preprocess(data):
    logging.info("Preprocessing data")

    if not data:
        raise DataValidationError(
            "Cannot preprocess empty data"
        )

    return [x / 10 for x in data]


def predict(data):
    logging.info("Generating predictions")

    return [x * 2 + 1 for x in data]


def main():

    try:
        data = load_data()

        processed = preprocess(data)

        predictions = predict(processed)

        logging.info(
            "Predictions: %s",
            predictions
        )

    except DataValidationError as error:

        logging.error(
            "Data validation failed: %s",
            error
        )

    except Exception:

        logging.exception(
            "Unexpected application error"
        )


if __name__ == "__main__":
    main()