class Menu:
    def __init__(self):
        self.__menu_options = {1: "List Existing COM Ports", 2: "Exit"}

    def print_menu(self) -> None:
        for key in self.__menu_options.keys():
            print(key, "--", self.__menu_options[key])
