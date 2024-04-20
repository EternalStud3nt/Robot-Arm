class UpdatableType(type):
    # List to hold all updatable instances
    updatable_instances = []

    def __call__(cls, *args, **kwargs):
        # Create a new instance
        instance = super().__call__(*args, **kwargs)
        # Add the instance to the list of updatable instances
        UpdatableType.updatable_instances.append(instance)
        return instance