import pyautogui
import os
from GlobalSettings import IMAGES_DIR

class EveWindowManager:

    def __init__(self):
        self.is_running = False

    def click_something(self):
        pyautogui.click(100, 100, 1)

    def undock(self, file_name):
        undock_location = pyautogui.locateOnScreen(os.path.join(IMAGES_DIR, file_name))
        undock_location_x, undock_location_y = pyautogui.center(undock_location)
        pyautogui.click(undock_location_x, undock_location_y)


if __name__ == '__main__':
    window_manager = EveWindowManager()
    window_manager.undock('testme.png')