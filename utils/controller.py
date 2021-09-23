from utils.comports import COMPorts
import sys


class Controller:
    def __init__(self):
        self.ports_class = COMPorts()
        self.selected_port=[]

    def process_main_menu_input(self, selection):
        if selection == 1:
            self.ports_class.print_available_ports()
            selection = int(input("Select COM Port which your device is attached."))
            self.selected_port = self.ports_class.get_selected_port(selection)
            self.ports_class.read_selected_port(self.selected_port)

        elif selection == 2:
            sys.exit(0)

