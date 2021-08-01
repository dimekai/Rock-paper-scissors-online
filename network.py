import socket
import pickle   # Serialize object
from util import Utility

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.util = Utility()
        self.server = self.util.get_server_name()
        self.port = self.util.get_port()
        self.__NUM_BITS = self.util.get_num_bits()
        self.addr = (self.server, self.port)
        self.player = self.connect()

    
    def get_player(self):
        return self.player
    

    def connect(self):
        try:
            self.client.connect(self.addr)
            # Decompose object data
            return pickle.loads(self.client.recv(self.__NUM_BITS))
        
        except :
            pass
    

    def send(self, data):
        try:
            # Converts objects to bits - Serialized
            serialized_data = pickle.dumps(data)
            self.client.send(serialized_data)
            return pickle.loads(self.client.recv(self.__NUM_BITS))
        
        except socket.error as e:
            print(e)



def test():
    net = Network()
    while True:
        print('Type the message to send to the server. (Type QUIT to exit)')
        data = input('> ')
        if data.upper() == 'QUIT':
            break
        else:
            print(net.send(data))


if __name__ == '__main__':
    test()




