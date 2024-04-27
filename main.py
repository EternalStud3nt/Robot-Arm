from InputSystem import InputSystem
from UpdatableType import UpdatableType
import Constants
from Player import Player
import time

# Instantiate your classes...
input_system = InputSystem()
player = Player(input_system)

print("Press any key or button...")

while True:
    Constants.deltatime = time.time() - Constants.deltatime
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