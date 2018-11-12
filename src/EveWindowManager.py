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

    def key_press(self, key_name):
        if key_name != '':
            pyautogui.press(key_name)
        else:
            print('No key_name value exists.')

    def type(self, text):
        if text != '':
            # interval value being replaced with a random human typing speed
            # value to simulate real person would be nice. give this random value
            # a range of randomness too!. (about 1, to about 3 for example)
            # would produce (1.1,2.7) (0.8,2.9) (0.9,3.1) cool.
            interval = 0.1
            pyautogui.typewrite(text, interval)
        else:
            print('No text value found.')

    def key_press_c(self, key_name):
        if key_name != '':
            interval = 0.015
            pyautogui.keyDown(key_name)
            time.sleep(interval)
            pyautogui.keyUp(key_name)
        else:
            print('No key_name value exists')







if __name__ == '__main__':
    window_manager = EveWindowManager()
    time.sleep(2)
    window_manager.click_image('undock_2.png')
    print('finished')