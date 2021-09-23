from serial.tools import list_ports
from serial import Serial
import logging
from utils.readline import ReadLine


# noinspection SpellCheckingInspection
class COMPorts:
    def __init__(self):
        self.sorted_ports = []

    def print_available_ports(self) -> None:
        logging.basicConfig(filename='triumph.log', filemode='w')
        self.sorted_ports = sorted(list_ports.comports())
        if self.sorted_ports:
            for idx, (port, desc, hwid) in enumerate(self.sorted_ports):
                print("{}- {}: {} [{}]".format(idx, port, desc, hwid))
                print(self.sorted_ports[0][0])
        else:
            logging.error("No valid port detected!. Possibly, device not plugged/detected.")

    def get_selected_port(self, index: int) -> list:
        if index not in range(0, len(self.sorted_ports)):  # if index>=0 and index<=len(self.sorted_ports)
            return []
        return self.sorted_ports[index]

    def read_selected_port(self, port: list):
        port_name = port[0]
        com_port = Serial(port_name)
        port_data_reader = ReadLine(com_port)
        print( port_data_reader.readline())
