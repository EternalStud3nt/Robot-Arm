#!/usr/bin/python
import time
import math
from Motor import Motor
from PCA9685 import PCA9685
import angle_calculator as ac


class RobotArm:
	base_height = 7.5
	l_a = 8
	l_b = 8
	l_c = 3.5
	l_1 = 3.5
	l_2 = 8
	l_3 = 3.5

	def __init__(self):
		pwm = PCA9685(0x40, debug=False)
		pwm.setPWMFreq(50)

		# Gripper
		self.grip_motor = Motor(pwm, 0, -90, 0, 90, 480, 1500, 2500)
		# Vertical Rotation
		self.rotation_motor = Motor(pwm, 1, -90, 0, 90, 512, 1524, 2580)
		# Y Position
		self.height_motor = Motor(pwm, 2, -60, 0, 81, 600, 1500, 2000)
		# Z Position
		self.length_motor = Motor(pwm, 3, -60, 0, 90, 1000, 1500, 2500)

		self.motors = [
		self.grip_motor,
		self.rotation_motor,
		self.height_motor,
		self.length_motor,
		]

		for motor in self.motors:
			motor.set_rotation(0)
			time.sleep(0.1)

	def get_motor_rotation(self, motor_id):
		return self.motors[motor_id].last_rotation

	def get_height(self):
		length_angle = -math.radians(self.length_motor.last_rotation)
		height_angle = -math.radians(self.height_motor.last_rotation)
		height = self.base_height + self.l_a * math.cos(length_angle) + self.l_b * math.sin(height_angle)
		return height
 
	def get_length(self):
		length_angle = -math.radians(self.length_motor.last_rotation) 
		height_angle = -math.radians(self.height_motor.last_rotation)
		depth = -self.l_a * math.sin(length_angle) + self.l_b * math.cos(height_angle)
		return depth

	def set_motor_rotations(self, data):
		self.grip_motor.send_pulse(data[0])
		self.rotation_motor.set_rotation(math.degrees(data[1]))
		self.height_motor.set_rotation(math.degrees(data[2]))
		self.length_motor.set_rotation(math.degrees(data[3]))
		print(math.degrees(data[2]))
		print(math.degrees(data[3]))


	def set_position(self, grip, x, y, z):
		grip = -grip * (2000/100) + 2000 + self.grip_motor.min_pulse
		print(grip)
		target_length = ac.find_length_xz(x, z)

		angles_zy = ac.find_angles_yz(y, target_length)
		angle_rotation = ac.find_angle_xz(x, z)
		angles = [grip, angle_rotation, angles_zy[1], angles_zy[0]]
		self.set_motor_rotations(angles)

	def debug(self):
		try:
			while True:
				grip = float(input("Enter grip strength (0-100): "))
				x = float(input("Enter x value:"))
				y = float(input("Enter y value: "))
				z = float(input("Enter z value: "))

				self.set_position(grip, x, y, z)
				print(f"Moving to {grip, x, y, z}.")
		except:
			self.debug()


arm = RobotArm()
arm.debug()
