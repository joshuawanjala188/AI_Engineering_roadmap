import numpy as np

scores = np.array([85, 45, 72, 91, 8])

print(scores > 50)

passed = scores[scores >= 50]
print(passed)
