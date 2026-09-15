from ai_project.data.loader import load_data
from ai_project.data.preprocessing import preprocess
from ai_project.models.models import Model
from ai_project.training.trainer import train


def main():

    data = load_data()

    data = preprocess(data)

    model = Model()
    model = train(model, data)

    predictions = model.predict(data)

    print(predictions)


if __name__ == "__main__":

    main()