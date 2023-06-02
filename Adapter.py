class EuropeanSocketInterface:
    def voltage(self): pass

class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

class AmericanSocket:
    def voltage(self):
        return 110

class Adapter(EuropeanSocketInterface):
    def __init__(self, socket):
        self._socket = socket

    def voltage(self):
        return self._socket.voltage()

american_socket = AmericanSocket()

adapter = Adapter(american_socket)
print(adapter.voltage())  # 110
