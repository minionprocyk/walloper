import pyautogui
import os
import time
from GlobalSettings import IMAGES_DIR

class EveWindowManager:

    def __init__(self):
        self.is_running = False

    def click_something(self):
        pyautogui.click(100, 100, 1)

    def click_image(self, file_name):
        image_location = pyautogui.locateOnScreen(os.path.join(IMAGES_DIR, file_name))
        if image_location is None:
            print("Could not find undock_location")
        else:
            image_location_x, image_location_y = pyautogui.center(image_location)
            time.sleep(1)
            pyautogui.click(image_location_x, image_location_y)
            pyautogui.click(image_location_x, image_location_y)


if __name__ == '__main__':
    window_manager = EveWindowManager()
    time.sleep(2)
    window_manager.click_image('undock_2.png')
    print('finished')