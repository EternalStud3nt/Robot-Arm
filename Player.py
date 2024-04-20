class Player:
    def __init__(self, input_system):
        self.input_system = input_system
        self.subscribe_to_actions()

    def subscribe_to_actions(self):
        for action in self.input_system.action_map.keys():
            # Create a new function that calls handle_action with the action
            handler = lambda action=action: self.handle_action(action)
            self.input_system.action_triggered_event.subscribe(handler)

    def handle_action(self, action):
        print(f"Player handled action '{action}'")
