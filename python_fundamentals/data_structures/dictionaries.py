#They store key -> value example:

"""person = {
    "name": "Joshua",
    "age": 20,
    "country": "Kenya"
}

#modify  dictionaries
#add

person["gender"] = "male"

#delete
 #del person["age"]
 #del person["country"]

#Dictionary methods

for key, value in person.items():

    print(f"{key}: {value}")


print(person.keys(), person.values())"""

#Nested dictionar
"""data = {
    "user": {
        "profile": {
            "location": {
                "country": "Kenya"
            }
        }
    }
}
print(data["user"]["profile"]["location"]["country"])"""

#Lists + Dictionaries

"""users = [
      {
        "name": "Alice",
        "age": 20
    },
    {
        "name": "Bob",
        "age": 25
    },
    {
        "name": "Charlie",
        "age": 30
    }
]

for user in users:
    print(user["name"])"""

predictions = [
    {
        "class": "cat",
        "confidence": 0.92
    },
    {
        "class": "dog",
        "confidence": 0.87
    },
    {
        "class": "bird",
        "confidence": 0.73
    }
]


for prediction in predictions:
    if prediction["confidence"] > 0.8:
        print(prediction["class"])

