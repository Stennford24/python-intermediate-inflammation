import numpy as np
from inflammation.models import daily_mean
test_input = np.array([[2,0],[4,0]])
test_result = np.array([2,0])
assert daily_mean(test_input) == test_result