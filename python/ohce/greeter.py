from datetime import datetime

class Clock:
    def __init__(self, clock):
        self.clock = clock
    
    def current_hour(self):
        return self.clock.hour

class SystemClock(Clock):
    def __init__(self, clock=None):
        super().__init__(datetime.now())
        
    def current_hour(self):
        return self.clock


class Greeter:
    def __init__(self, clock=None):
        self.clock = SystemClock() if clock is None else Clock(clock)

    def greet(self):
        current_hour = self.clock.current_hour()
        if 6 <= current_hour < 12:
            return "Good morning"
        if 12 <= current_hour <= 19:
            return "Good afternoon"
        if current_hour >= 20 or current_hour < 6:
            return "Good night"
