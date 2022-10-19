import numpy as np

inputs = [3.0, 1.6, 2.7, 2.4, 3.2, 3.3, 4.9, 4.1, 5.2, 5.4]
weights = [0.4, 0.2, 0.5, 0.3, 2.0, 1.3, 1.2, 1.5, 1.5, 2.7]

bias = 2.0

outputs = np.dot(weights, inputs) + bias
print(outputs)