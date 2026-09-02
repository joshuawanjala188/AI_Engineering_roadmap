
for i in range(1, 5):
    print(i)


predictions = [0.2, 0.8, 0.6, 0.9]

for prediction in predictions:

    if prediction >= 0.5:

        print("Positive")

    else:
        print("Negative")    


counter = 0       

while counter < 10:
    counter+=1

    print(counter)