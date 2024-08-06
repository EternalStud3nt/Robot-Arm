from motor import Motor
import time

if (__name__ == "__main__"):
	print("Welcome to the controller...")
	
	motor_0 = Motor(0)
	motor_1 = Motor(1)
	motor_2 = Motor(2)
	motor_3 = Motor(3)
	motors = [motor_0, motor_1, motor_2, motor_3]
	
	for motor in motors:
		time.sleep(1)
		motor.set_rotation(90)
