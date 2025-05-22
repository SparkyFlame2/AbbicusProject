import math
import random

def calculate_drift(value):
    gamma = random.uniform(0.8, 1.2)
    noise = random.gauss(0, 0.1)
    return math.sin(value) * gamma + noise
