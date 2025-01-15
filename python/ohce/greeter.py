from datetime import datetime

class Clock:
    def current_hour(self, now):
        pass

class SystemClock(Clock):
    def current_hour(self, now=None):
        now = datetime.now()
        return now.hour


class Greeter:
    def __init__(self, clock=None):
        self.clock = SystemClock() if clock is None else clock

    def greet(self):
        current_hour = self.clock.current_hour()
        if 6 <= current_hour < 12:
            return "Good morning"
        if 12 <= current_hour <= 19:
            return "Good afternoon"
        if current_hour >= 20 or current_hour < 6:
            return "Good night"
