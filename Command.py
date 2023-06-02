class Command:
    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        self._obj.action()

class SimpleCommand(Command):
    def __init__(self, obj):
        super().__init__(obj)

    def execute(self):
        self._obj.action()

class Receiver:
    def action(self):
        print("Receiver Action")

recv = Receiver()
cmd = SimpleCommand(recv)
cmd.execute()  # Receiver Action
