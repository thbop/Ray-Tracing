
class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    
    def at(self, t):
        return self.origin + t * self.direction