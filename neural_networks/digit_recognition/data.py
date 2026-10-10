import tensorflow as tf

def load_data():
    #load mnist dataset
    (X_train, y_train), (X_test, y_test) = (
        tf.keras.datasets.mnist.load_data()
    )

#2. Convert pixel values from 0-255 to 0-1

    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32")/255.0

    # add a channel dimensions for grayscal images

    X_train = X_train[..., tf.newaxis]
    X_test = X_test[..., tf.newaxis]

    X_val = X_train[-5000:]
    y_val = y_train[-5000:]

    X_train = X_train[:-5000]
    y_train = y_train[:-5000]

    print("Training images:", X_train.shape)
    print("Training labels:", y_train.shape)

    print("Validation images:", X_val.shape)
    print("Validation labels:", y_val.shape)

    print("Test images:", X_test.shape)
    print("Test labels:", y_test.shape)

    return X_train, y_train, X_val, y_val, X_test, y_test


if __name__ == "__main__":
    load_data()
