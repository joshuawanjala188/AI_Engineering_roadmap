def accuracy(actual, predicted):
    correct = 0

    for a , p in zip(actual, predicted):

        if a == p:

            correct +=1

    return correct / len(actual)        