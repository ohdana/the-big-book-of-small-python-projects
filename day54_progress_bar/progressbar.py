BAR_SEGMENT = chr(9608) # Character 9608 is '█'
START_CHAR = '['
END_CHAR = ']'
MAX_PROGRESS = 100

class ProgressBar:
    def __init__(self):
        self.progress_percent = 0.0

    def set_progress(self, new_value):
        self.progress_percent = new_value if new_value < MAX_PROGRESS else MAX_PROGRESS

    def build(self):
        bar_body = START_CHAR + BAR_SEGMENT * round(self.progress_percent) + END_CHAR
        progress_info = ' {}% '.format(self.progress_percent)
        return bar_body + progress_info
