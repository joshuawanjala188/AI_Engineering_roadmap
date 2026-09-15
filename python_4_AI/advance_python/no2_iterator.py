# it is an object that produces values one at a time
#You can create using iter()

numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

"""
This idea becomes extremely important for:

Large datasets
Data pipelines
Streaming
File processing
ML training
LLM responses
"""