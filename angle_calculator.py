import numpy as np
from scipy.optimize import fsolve

# Constants
arm_length_a = 8
arm_length_b = 8
base_height = 7.5

def find_angles_yz(target_height, target_length):
    # System of equations
    def equations(vars):
        angle_a, angle_b = vars
        eq1 = base_height + arm_length_a * np.cos(angle_a) + arm_length_b * np.sin(angle_b) - target_height
        eq2 = -arm_length_a * np.sin(angle_a) + arm_length_b * np.cos(angle_b) - target_length
        return [eq1, eq2]

    # Initial guess for angles in rad
    angle_a_guess = 0
    angle_b_guess = 0

    # Use fsolve to solve the system of equations
    angles = fsolve(equations, (angle_a_guess, angle_b_guess))
    angles = [-1 * angles[0], -1 * angles[1]]
    return angles

def find_angle_xz(target_x, target_z):
    theta = np.arctan(target_x/target_z)
    return theta

def find_length_xz(target_x, target_z):
    target_length = np.sqrt(target_x**2 + target_z**2)
    return target_length
    

# Usage
target_x = 5
target_y = 15.5  
target_z = 12
target_length = find_length_xz(target_x, target_z)

angles1 = find_angles_yz(target_y, target_length)
angle2 = find_angle_xz(target_x, target_z)
print(f"Solution: angle_a = {np.degrees(angles1[0])}, angle_b = {np.degrees(angles1[1])}")
print(f"Solution: angle_c = {np.degrees(angle2)}")
