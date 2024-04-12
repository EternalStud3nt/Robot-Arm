#!/usr/bin/python
import time
import math
from Motor import Motor
from PCA9685 import PCA9685
from angle_calculator import compute_angles


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
		self.height_motor = Motor(pwm, 2, -45, 0, 81, 600, 1500, 2000)
		# Z Position
		self.length_motor = Motor(pwm, 3, -45, 0, 90, 1000, 1500, 2500)

		self.motors = [
		self.grip_motor,
		self.rotation_motor,
		self.height_motor,
		self.length_motor,
		]

		for motor in self.motors:
			motor.set_rotation(0)
			time.sleep(0.1)

	def set_theta(self, motor_id, angle):
		self.motors[motor_id].set_rotation(angle)

	def get_theta(self, motor_id):
		return self.motors[motor_id].last_rotation

	def get_height(self):
		length_angle = math.radians(self.get_theta(self.length_motor.channel))
		height_angle = math.radians(self.get_theta(self.height_motor.channel))
		y_1 = self.base_height + self.l_a * math.cos(length_angle)
		y_2 = y_1 + self.l_b * math.sin(-height_angle)
		return y_2

	def get_length(self):
		print(self.get_theta(0))
		length_angle_rad = math.radians(self.get_theta(self.length_motor.channel)) 
		height_angle_rad = math.radians(self.get_theta(self.height_motor.channel))
		z_1 = self.l_a * math.sin(length_angle_rad)
		z_2 = z_1 + self.l_b * math.cos(-height_angle_rad)
		return z_2

	def set_z(self, target_z):
		last_rotation = math.radians(self.get_theta(self.rotation_motor.channel))
		x = self.get_length() * math.sin(last_rotation)
		target_rotation = math.atan(x / target_z)
		rotation_angle = math.degrees(target_rotation)
		target_length = target_z
		if math.sin(target_rotation) != 0:
			target_length = x / math.sin(rotation_angle)
		self.set_theta(self.rotation_motor.channel, target_rotation)
		self.set_length(target_length)

	def set_y(self, target_y):
		[theta_a, theta_b] = compute_angles(self.get_length(), target_y)
		self.set_theta(self.length_motor.channel, theta_a)
		self.set_theta(self.height_motor.channel, theta_b)

	def set_x(self, target_x):
		last_rotation = math.radians(self.get_theta(self.rotation_motor.channel))
		z = self.get_length() * math.cos(last_rotation)
		target_rotation = math.atan(target_x / z)
		rotation_angle = math.degrees(target_rotation)
		target_length = z
		if math.sin(target_rotation) != 0:
			target_length = target_x / math.sin(rotation_angle)
			
		self.set_theta(self.rotation_motor.channel, rotation_angle)
		self.set_length(target_length)

	def set_length(self, target_length):
		[theta_a, theta_b] = compute_angles(self.get_height(), target_length)
		self.set_theta(self.length_motor.channel, theta_a)
		self.set_theta(self.height_motor.channel, theta_b)

	def set_position(self, x, y, z):
		self.set_x(x)
		time.sleep(1)
		self.set_y(y)
		time.sleep(1)
		self.set_z(z)

	def debug(self):

		try:
			while True:
				x = float(input("Enter x value:"))
				y = float(input("Enter y value: "))
				z = float(input("Enter z value: "))

				self.set_position(x, y, z)
				print(f"Moving to {x, y, z}.")
		except:
			self.debug()


arm = RobotArm()
arm.debug()
