def angle_to_pulse(angle):
    if (angle <= 0): return 500
    elif (angle >= 180): return 2500
    
    pulse_per_angle = (2500 - 500) / 180
    return (500 + pulse_per_angle * angle)

def pulse_to_angle(pulse):
    if(pulse <= 500): return 0
    elif (pulse >= 2500): return 180
    
    angle_per_pulse = 180 / 2500
    return angle_per_pulse * (pulse - 500)
