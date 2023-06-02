class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This is a singleton class!")
        else:
            Singleton._instance = self

s = Singleton.getInstance()  # Creates a singleton instance
print(s)  # <__main__.Singleton object at 0x10e2b7d60>

s1 = Singleton.getInstance()  # Retrieves the singleton instance
print(s1)  # <__main__.Singleton object at 0x10e2b7d60> (same as before)
