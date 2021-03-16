class Clock:
    frame_duration = 1

    def __init__(self):
        self.time = 0
        self.frame_duration = 1

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        return self.tick == frame_duration
