from robot_arm.motor import Motor
from robot_arm.PCA9685 import PCA9685
import math


class RobotArm:
    def __init__(self) -> None:
        pwm = PCA9685(0x40, debug=False)
        pwm.setPWMFreq(50)
        
        self.base_motor = Motor(0, pwm) # base motor
        self.shoulder_motor = Motor(4, pwm) # shoulder arm motor
        self.elbow_motor = Motor(8, pwm) # elbow arm motor
        self.claw_motor = Motor(12, pwm) # claw motor
        
        self.motors = {
            "base": self.base_motor,
            "elbow": self.elbow_motor,
            "shoulder": self.shoulder_motor,
            "claw": self.claw_motor
        }
        
        self.max_s_motor_rotation = 170
        self.max_e_motor_rotation = 110
        self.min_e_motor_rotation = 10
        self.min_s_motor_rotation = 5
        self.min_grip = 8
        
        self.l_s = 8
        self.rotation = 0
        self.depth = 8
        self.height = 8
        self.grip = 90
        self.reset()
        
    # region Set methods
    def set_motor_rotation(self, motor_id, angle):
        self.motors[motor_id].set_rotation_smooth(angle)
           
    def set_vertical_rotation(self, angle):
        theta_b = angle + 90
        
        if not(theta_b >= 0 and theta_b <= 180):
            return
        else:
            self.base_motor.set_rotation_smooth(theta_b)
        
        self.rotation = angle      
    
    def set_depth(self, depth):
        if(depth > 15 or depth < 4 or self.height > 15 or self.height < -5):
            return
        
        # try-catch block to handle math domain error
        try:
            y = self.height
            l_xz = depth
            l = math.sqrt(y**2 + l_xz**2)
            
            theta = math.atan(y/l_xz)
            omega = math.acos((l/2)/self.l_s)
            theta_1 = theta + omega
            theta_2 = theta - omega
        except:
            print("It's not possible to reach that depth")
            return
        
        theta_s = math.pi - theta_1
        theta_e = math.pi/2 + theta_2
        
        theta_s_deg = math.degrees(theta_s)
        theta_e_deg = math.degrees(theta_e)
        
        
        # check if the angles are within the range of motor rotation
        if(theta_s_deg < self.min_s_motor_rotation or theta_s_deg > self.max_s_motor_rotation):
            print("Impossible to reach that position")
            return
        elif(theta_e_deg < self.min_e_motor_rotation or theta_e_deg > self.max_e_motor_rotation):
            print("Impossible to reach that position")
            return
        
        self.elbow_motor.set_rotation_smooth(theta_s_deg)
        self.shoulder_motor.set_rotation_smooth(theta_e_deg)
        
        
        self.depth = depth
        print(f"Current depth: {self.depth}, height: {self.height}, base rotation: {self.rotation}, grip: {self.grip}")

    def set_height(self, height):
        if(self.depth > 15 or self.depth < 4 or height > 15 or height < -5):
            return
        
         # try-catch block to handle math domain error
        try:
            y = height
            l_xz = self.depth
            l = math.sqrt(y**2 + l_xz**2)
            
            theta = math.atan(y/l_xz)
            omega = math.acos((l/2)/self.l_s)
            
            theta_1 = theta + omega
            theta_2 = theta - omega
        except:
            print("It's not possible to reach that height")
            return
        
        theta_e = math.pi/2 + theta_2
        theta_s = math.pi - theta_1
        
        theta_e_deg = math.degrees(theta_e)
        theta_s_deg = math.degrees(theta_s)
        
        # check if the angles are within the range of motor rotation
        if(theta_e_deg < self.min_s_motor_rotation or theta_e_deg > self.max_s_motor_rotation):
            print("Impossible to reach that position")
            return
        elif(theta_s_deg < self.min_e_motor_rotation or theta_s_deg > self.max_e_motor_rotation):
            print("Impossible to reach that position")
            return
        
        self.elbow_motor.set_rotation_smooth(theta_e_deg)
        self.shoulder_motor.set_rotation_smooth(theta_s_deg)
        
        # update height
        self.height = height
        print(f"Current depth: {self.depth}, height: {self.height}, base rotation: {self.rotation}, grip: {self.grip}")
    
    def set_grip(self, grip):
            if grip < self.min_grip: grip = self.min_grip
            elif grip > 90: grip = 90
            
            angle = grip * 180 / 100
            self.claw_motor.set_rotation_smooth(angle)
            self.grip = grip
            print(f"Current depth: {self.depth}, height: {self.height}, base rotation: {self.rotation}, grip: {self.grip}")
    # endregion
    
    # region Move methods
    def rotate_vertically(self, delta_angle):
            self.set_vertical_rotation(self.rotation + delta_angle)
        
    def move_forwards(self, distance):
        self.set_depth(self.depth + distance)

    def move_upwards(self, distance):
        self.set_height(self.height + distance)
        
    def change_grip(self, delta_grip):
        self.set_grip(self.grip + delta_grip)
    # endregion
    
    def reset(self):
        self.set_depth(4)
        self.set_height(8)
        self.set_vertical_rotation(0)
        
if __name__ == "__main__":
    arm = RobotArm()
    while True:
        motor_channel = input("Enter motor channel (base, depth, height, claw): ").strip().lower()
        if motor_channel not in arm.motors:
            print("Invalid motor channel. Please try again.")
            continue
        
        try:
            degrees = float(input("Enter degrees to rotate: "))
        except ValueError:
            print("Invalid input for degrees. Please enter a number.")
            continue
        
        arm.set_motor_rotation(motor_channel, degrees)