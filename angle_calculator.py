import numpy as np
from scipy.optimize import fsolve

# Constants
arm_length_a = 8
arm_length_b = 8
base_height = 7.5

# Target values
target_height = 15.5  # replace with your target height
target_length = 8  # replace with your target length

# System of equations
def equations(vars):
    angle_a, angle_b = vars
    eq1 = base_height + arm_length_a * np.cos(np.radians(angle_a)) + arm_length_b * np.sin(np.radians(angle_b)) - target_height
    eq2 = arm_length_a * np.sin(np.radians(angle_a)) + arm_length_b * np.cos(np.radians(angle_b)) - target_length
    return [eq1, eq2]

# Initial guess for angles in degrees
angle_a_guess = 0
angle_b_guess = 0

# Use fsolve to solve the system of equations
angles = fsolve(equations, (angle_a_guess, angle_b_guess))

print(f"Solution: angle_a = {angles[0]}, angle_b = {angles[1]}")
