class ActivationState:
    KEY: str = 'activation_state'
    ACTIVATED: str = 'activated' # The node is executed
    DEACTIVATED:str = 'deactivated' # The node is ignored
    BYPASS:str = 'bypass' # The node is informed that it needs to let the data pass by
                        # without doing it's computation.
                        # Each node is responsible on defining how this will be handled.
                        # If a node doesn't define a specific behaviour for this state
                        # it will just be executed like if it was activated.
    INVALID_VERSION:str = 'invalid_version' # A module in the invalid_version state
                        # when it cannot be found within all active packages.
                        # This can happen when opening a pipeline that uses
                        # packages that are not registered in the settings view.
