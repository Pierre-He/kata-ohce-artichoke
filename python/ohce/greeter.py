from datetime import datetime

class SystemClock:
    def current_hour(self):
        now = datetime.now()
        return now.hour


class Greeter:
    def __init__(self, stubClock=None):
        self.clock = SystemClock() if stubClock is None else stubClock

    def greet(self):
        current_hour = self.clock.current_hour()
        if 6 <= current_hour < 12:
            return "Good morning"
        if 12 <= current_hour <= 19:
            return "Good afternoon"
        if current_hour >= 20 or current_hour < 6:
            return "Good night"
