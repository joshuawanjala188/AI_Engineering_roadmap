
def classify_score(score):

    if score >= 80:
        return "High"

    elif score  >= 50:

        return "Medium"

    else:
        return "Low"


scores = [92, 75, 43, 88, 31]


for score in scores:

    result = classify_score(score)
    print(f"Score: {score} - {result}")
    