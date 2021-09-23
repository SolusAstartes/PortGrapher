from utils.controller import Controller
from utils.menu import Menu


def main():
    main_menu = Menu()
    controller = Controller()
    while True:
        main_menu.print_menu()
        selection = int(input())
        controller.process_main_menu_input(selection)


if __name__ == '__main__':
    main()
