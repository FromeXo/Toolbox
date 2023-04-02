import socket

class Scanner:

    _s = None

    def __init__(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self._s.bind(('', 67))
        except Exception as e:
            print(e)
        print("Socket binding operation completed")
    
    def scan(self):
        return True