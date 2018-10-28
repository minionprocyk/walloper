from operationv.GlobalSettings import PROGRAM_NAME, EVE_BASE_ADDRESS
from memorpy import Address, Process
from threading import Thread, ThreadError


class MemoryRead(object):
    client_offset = 0x103f0000
    client_offset_official = 0xfff0000
    player_offset = 0x2d2a606
    velocity_offset = 0x7bcac
    velocity_other_offset = 0x84664
    stop_threads = False  # either stop all threads or none

    def __init__(self):
        self.process = self.attach_mem()

    @staticmethod
    def attach_mem(self):
        print("Attaching to process")
        process = Process(name='exefile.exe')

        if not process:
            print("EVE process not found")
            # exit(1)
        return process

    @staticmethod
    def test_read_mem(address, process):
        some_val = Address(address, process).read('float')
        print(some_val)

    def get_ship_info(self, ship_info, process):
        print("Getting ship info")
        _address = Address(EVE_BASE_ADDRESS + self.client_offset_official + self.player_offset, process).read()
        # _address = Address(client_offset+player_offset, process).read()
        print("Address={reg} | Hex={hex}".format(reg=_address, hex=hex(_address)))
        _address += self.velocity_offset
        ship_velocity = Address(_address, process).read('float')
        print("Reading Player Velocity {}".format(ship_velocity))
        ship_info.velocity = ship_velocity

    def test_memory_async_read(self):
        """
            A test method for seeing memory values laid out in this class
        """
        # start a separate thread responsible for updating __insert_object_here___ with ship information
        try:
            Thread(target=self.get_ship_info, args=(self.process,)).start()
        except ThreadError:
            print("Failed to start {}".format(self.get_ship_info.__name__))

    def is_attached(self):
        return self.process is not None


if __name__ == '__main__':
    print("hello {program_name}".format(program_name=PROGRAM_NAME))
    readmem = MemoryRead()
    address = 0x0000
    if readmem.is_attached() is False:
        proc = readmem.attach_mem()
        readmem.test_read_mem(address, proc)


