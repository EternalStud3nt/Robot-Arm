from InputSystem import InputSystem
from UpdatableType import UpdatableType
import time
from Player import Player

# Instantiate your classes...
input_system = InputSystem()
deltatime = 0

print("Press any key or button...")

while True:
    deltatime = time.time() - deltatime
    # Iterate over all updatable instances
    for instance in UpdatableType.updatable_instances:
        # Check if the instance has an 'update' method
        if hasattr(instance, 'update'):
            # Get the 'update' method
            update_method = getattr(instance, 'update')
            # Call the 'update' method
            update_method()
    time.sleep(0.1)  # Add a small delay
a