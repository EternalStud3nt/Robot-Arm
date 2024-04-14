import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def calculate_position_angles(angles, target_height, target_depth):
    # Constants for the lengths of the arms
    arm_length_a = 8
    arm_length_b = 8
    base_height = 7.5
    
    # Extract the angles from the input array
    angle_a = angles[0]
    angle_b = angles[1]
    
    # Initialize the output array
    output = np.empty(2)
    
    # Calculate the position based on the angles and arm lengths
    output[0] = base_height + arm_length_a * np.cos(angle_a) + arm_length_b * np.sin(angle_b) - target_height
    output[1] = arm_length_a * np.sin(angle_a) + arm_length_b * np.cos(angle_b) - target_depth
    
    return output

def normalize_angle(angle, trig_function):
    # Normalize the angle to the range 0-360
    angle = angle % 360
    
    # Adjust the angle based on the trigonometric function
    if trig_function == 'cos':
        if 90 < angle <= 270:
            angle = 180 - angle
        elif angle > 270:
            angle -= 360
    elif trig_function == 'sin' and angle > 180:
        angle -= 360
    
    return angle

def compute_angles(target_height, target_length):
    # Initial guess for the angles
    initial_guess = np.asarray([0, 0])
    
    # Use fsolve to find the angles that result in the target position
    angles = fsolve(lambda angles: calculate_position_angles(angles, target_height, target_length), initial_guess)
    
    # Convert the angles from radians to degrees
    angle_a_deg = np.rad2deg(angles[0])
    angle_b_deg = np.rad2deg(angles[1])

    # Normalize the angles to the range -90 to 90
    angle_a_deg = normalize_angle(angle_a_deg, 'cos')
    angle_b_deg = normalize_angle(angle_b_deg, 'sin')

    return angle_a_deg, angle_b_deg

# Compute the angles
angle_a_deg, angle_b_deg = compute_angles(7, 7)
print(angle_a_deg, angle_b_deg)

# Create a range of angles for plotting
angles = np.linspace(-np.pi, np.pi, 400)

# Calculate the position for each angle
positions = np.array([calculate_position_angles([angle_a, angle_b], 7, 7) for angle_a in angles for angle_b in angles])

# Plot the two functions
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(angles, positions[:, 0])
#x and y must have same first dimension, but have shapes (400,) and (160000,)
plt.title('Height as a function of angles')
plt.xlabel('Angles (radians)')
plt.ylabel('Height (units)')

plt.subplot(1, 2, 2)
plt.plot(angles, positions[:, 1])
plt.title('Depth as a function of angles')
plt.xlabel('Angles (radians)')
plt.ylabel('Depth (units)')

plt.tight_layout()
plt.show()
