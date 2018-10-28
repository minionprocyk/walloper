import pyautogui


class EveWindowManager:

    def __init__(self):
        self.is_running = False

    def click_something(self):
        pyautogui.click(100,100,1)


if __name__ == '__main__':
    window_manager = EveWindowManager()
    window_manager.click_something()