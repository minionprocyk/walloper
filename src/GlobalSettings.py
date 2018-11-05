import os


PROGRAM_NAME = "WAIT_WOT???"
MAIN_WINDOW_TITLE = "Main UI Window"


SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SRC_DIR, os.pardir))
IMAGES_DIR = os.path.join(ROOT_DIR, 'images')

# TODO calculate base address when process loads
EVE_BASE_ADDRESS = 0x400000

