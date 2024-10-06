# FILE: manual_test_robot_arm.py
from robot_arm import RobotArm

def manual_test_set_position():
    robot_arm = RobotArm()
    while True:
        x = float(input("Enter x position: "))
        y = float(input("Enter y position: "))
        z = float(input("Enter z position: "))
    
        robot_arm.set_position(x, y, z)
        print(f"Resulting Position: {robot_arm.position}")


if __name__ == "__main__":
    manual_test_set_position()