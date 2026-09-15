def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name
                    }"



def average(values: list[float]) -> float:
    return sum(values) / len(values)




def config() -> dict[str, float]:

    return {
        "learning_rate": 0.01
    }


def find_user(user_id: int) -> str | None:
    return str or None

#Custom types

class Model:
    pass


def train(model: Model) -> None:
    print("Training...")



#Dataclasses


class ModelConfig:

    def __init__(self, learning_data, epochs, batch_size):

        self.learning_data = learning_data
        self.epochs = epochs
        self.batch_size = batch_size


#With data class
from dataclasses import dataclass

@dataclass
class ModelConfig:

    learning_rate: float
    epochs: int
    batch_size: int


config = ModelConfig(learning_rate=0.01, epochs=20, batch_size=32)



"""6. AI Configuration

Dataclasses are excellent for model configuration.
"""
from dataclasses import dataclass


@dataclass
class TrainingConfig:

    learning_rate: float = 0.001
    epochs: int = 10
    batch_size: int = 32
    model_name: str = "classifier"

#Then:

config = TrainingConfig()

#Or:

config = TrainingConfig(
    learning_rate=0.0001,
    epochs=50
)