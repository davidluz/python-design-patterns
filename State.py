class State:
    def write_program(self):
        raise NotImplementedError("This method should be overwritten.")

class WorkState(State):
    def write_program(self):
        print("Working...")

class RelaxState(State):
    def write_program(self):
        print("Relaxing...")

class Developer:
    def __init__(self):
        self.state = None

    def change_activity(self):
        if isinstance(self.state, WorkState):
            self.state = RelaxState()
        else:
            self.state = WorkState()

    def write_program(self):
        self.state.write_program()

developer = Developer()
developer.state = WorkState()

developer.write_program()  # Working...
developer.change_activity()
developer.write_program()  # Relaxing...
