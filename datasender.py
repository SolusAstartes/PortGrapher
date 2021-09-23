from random import randint
from serial import Serial

"""
Used for testing.
Sends dummy data from COM port.
"""
def send_dummy_data(serial_port):
    serial_port.write(b'hello\n')


def main():
    com_port = Serial("COM2")
    for i in range(5000000):
        send_dummy_data(com_port)
    com_port.close()


if __name__ == '__main__':
    main()
