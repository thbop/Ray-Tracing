import pygame
import pygame.gfxdraw
from pygame.locals import *
from pygame.math import Vector3 as vec3

from math import sqrt

from ray import Ray

pygame.init()


def ray_color(ray):
    t = hit_sphere(vec3(0, 0, -1), 0.5, ray)
    if t > 0.0:
        N = ( r.at(t) - vec3(0, 0, -1) ).normalize()
        return 0.5 * vec3(N.x+1, N.y+1, N.z+1)

    unit_direction = ray.direction.normalize()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * vec3(1.0, 1.0, 1.0) + t * vec3(0.5, 0.7, 1.0)

def get_display_color(color):
    color *= 255
    return (
        int(round(color.x)),
        int(round(color.y)),
        int(round(color.z)),
        )

def hit_sphere(center, radius, ray):
    oc = r.origin - center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * oc.dot(ray.direction)
    c = oc.dot(oc) - radius**2
    discriminant = b*b - 4 * a * c
    
    if discriminant < 0:
        return -1.0
    else:
        return (-b - sqrt(discriminant)) / (2.0 * a)

aspect_ratio = 16 / 9
image_width = 400
image_height = int(image_width / aspect_ratio)
screen = pygame.display.set_mode((image_width, image_height))

viewport_height = 2
viewport_width = aspect_ratio * viewport_height
focal_length = 1

origin = vec3(0, 0, 0)
horizontal = vec3(viewport_width, 0, 0)
verticle = vec3(0, viewport_height, 0)
lower_left_corner = origin - horizontal/2 - verticle/2 - vec3(0, 0, focal_length)



for j in range(image_height):
    for i in range(image_width):
        u = i / (image_width-1)
        v = j / (image_height-1)
        r = Ray(origin, lower_left_corner + u * horizontal + v * verticle - origin)
        pixel_color = ray_color(r)
        # print(get_display_color(pixel_color))
        pygame.gfxdraw.pixel(screen, i, j, get_display_color(pixel_color))
    
pygame.display.flip()



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False