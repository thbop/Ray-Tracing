from pygame.math import Vector3 as vec3
# from vec3 import vec3

from ray import ray

class camera:
    def __init__(self, aspect_ratio):
        self.viewport_height = 2
        self.viewport_width = aspect_ratio * self.viewport_height
        self.focal_length = 1

        self.origin = vec3(0, 0, 0)
        self.horizontal = vec3(self.viewport_width, 0, 0)
        self.vertical = vec3(0, self.viewport_height, 0)
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - vec3(0, 0, self.focal_length)
    
    def get_ray(self, u, v):
        return ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)