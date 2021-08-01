import socket

class Utility:
    def __init__(self):
        # === Network properties ===
        self.__NUM_CONNECTIONS = 2
        self.__NUM_BITS = 4096     # Amount of information to receive
        self.__PORT = 5555
        self.__SERVER = self.__get_server()

        # === Window properties ===
        self.__FPS = 60
        self.__WIDTH = 500
        self.__HEIGHT = 500
        self.__COLORS = {
            'WHITE': (255, 255, 255), 'GREEN': (0, 255, 0), 'RED': (255, 0, 0), 'BLUE': (0, 0, 255)
        }

    def get_num_connections(self):
        return self.__NUM_CONNECTIONS


    def get_num_bits(self):
        return self.__NUM_BITS


    def get_server_name(self):
        return self.__SERVER


    def get_port(self):
        return self.__PORT


    def __get_server(self):
        return str(socket.gethostbyname(socket.gethostname()))


    def get_fps(self):
        return self.__FPS


    def get_width(self):
        return self.__WIDTH


    def get_height(self):
        return self.__HEIGHT


    def get_colors(self):
        return self.__COLORS
