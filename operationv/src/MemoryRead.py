from GlobalSettings import PROGRAM_NAME, EVE_BASE_ADDRESS
from memorpy import Address, Process
from threading import Thread, ThreadError


def test_read_mem(address, process):
    some_val = Address(address, process).read('float')
    print(some_val)


client_offset = 0x103f0000
client_offset_official = 0xfff0000
player_offset = 0x2d2a606
velocity_offset = 0x7bcac
velocity_other_offset = 0x84664


def get_ship_info(process):
    print("Getting ship info")
    _address = Address(EVE_BASE_ADDRESS + client_offset_official + player_offset, process).read()
    # _address = Address(client_offset+player_offset, process).read()
    print("Address={reg} | Hex={hex}".format(reg=_address, hex=hex(_address)))
    _address += velocity_offset
    print("Reading Player Velocity {}".format(Address(_address, process).read('float')))


def attach_mem():
    print("Attaching to process")
    process = Process(name='exefile.exe')

    if not process:
        print("EVE process not found")
        exit(1)
    return process


if __name__ == '__main__':
    print("hello {program_name}".format(program_name=PROGRAM_NAME))

    proc = attach_mem()
    print("hprocess: {}".format(proc))
    # start a separate thread responsible for updating __insert_object_here___ with ship information
    try:
        Thread(target=get_ship_info, args=(proc,)).start()
    except ThreadError:
        print("Failed to start {}".format(get_ship_info.__name__))

    # test_read_mem(address=0x33c09b70, process=proc)


