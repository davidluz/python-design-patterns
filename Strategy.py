class StrategyExample:
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print("Original execution")

def execute_replacement1():
    print("Strategy 1")

def execute_replacement2():
    print("Strategy 2")

stratege = StrategyExample()

stratege.execute()  # Original execution

stratege1 = StrategyExample(execute_replacement1)
stratege1.execute()  # Strategy 1

stratege2 = StrategyExample(execute_replacement2)
stratege2.execute()  # Strategy 2
