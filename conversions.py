def angle_to_pulse(angle):
    if (angle <= 0): return 500
    elif (angle >= 180): return 2500
    
    pulse_per_angle = (2500 - 500) / 180
    return (500 + pulse_per_angle * angle)
