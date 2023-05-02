import pygame
import pygame.gfxdraw
from pygame.locals import *
from pygame.math import Vector3 as vec3

# from vec3 import vec3

from math import sqrt, radians
from random import random, uniform

from time import time

from ray import ray
from hittable import *
from hittable_list import hittable_list
from sphere import sphere
from camera import camera

pygame.init()


def ray_color(r, world, depth):
    rec = hit_record()
    
    if depth <= 0:
        return vec3(0, 0, 0)

    world_hit = world.hit(r, 0, INFINITY, rec)
    if world_hit['hit_anything']:
        rec = world_hit['rec']
        target = rec.p + rec.normal + random_in_unit_sphere()
        return 0.5 * ray_color(ray( rec.p, target - rec.p ), world, depth-1)

    unit_direction = r.direction.normalize()
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
    a = ray.direction.magnitude()**2
    half_b = oc.dot(ray.direction)
    c = oc.magnitude()**2 - radius**2
    discriminant = half_b**2 - a*c
    
    if discriminant < 0:
        return -1.0
    else:
        return (-half_b - sqrt(discriminant)) / a

def clamp(x, mn, mx):
    if x < mn: return mn
    if x > mx: return mx
    return x

def write_color(surf, x, y, pixel_color, samples_per_pixel):
    scale = 1.0 / samples_per_pixel

    pixel_color.x = sqrt(scale * pixel_color.x)
    pixel_color.y = sqrt(scale * pixel_color.y)
    pixel_color.z = sqrt(scale * pixel_color.z)
    
    pixel_color.x = clamp(pixel_color.x, 0, 0.999)
    pixel_color.y = clamp(pixel_color.y, 0, 0.999)
    pixel_color.z = clamp(pixel_color.z, 0, 0.999)



    pygame.gfxdraw.pixel(surf, x, y, get_display_color(pixel_color))

def random_vec():
    return vec3(random(), random(), random())

def uniform_vec(mn, mx):
    return vec3(uniform(mn, mx), uniform(mn, mx), uniform(mn, mx))

def random_in_unit_sphere():
    while True:
        p = uniform_vec(-1, 1)
        if p.magnitude()**2 >= 1: continue
        return p



INFINITY = float('inf')
PI = 3.1415926535897932385

# Image
aspect_ratio = 16 / 9
image_width = 400
image_height = int(image_width / aspect_ratio)
screen = pygame.display.set_mode((image_width, image_height))
screen.fill('white')

samples_per_pixel = 100
max_depth = 50

# World
world = hittable_list()
world.add( sphere(vec3(0, 0, -1), 0.5) )
world.add( sphere(vec3(0, -100.5, -1), 100) )

# Camera
cam = camera(aspect_ratio)


start_time = time()
for j in range(image_height):
    for i in range(image_width):
        pixel_color = vec3(0, 0, 0)
        for s in range(samples_per_pixel):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pass

            u = (i + random()) / (image_width-1)
            v = (j + random()) / (image_height-1)
            r = cam.get_ray(u, v)
            pixel_color += ray_color(r, world, max_depth)
            
        write_color(screen, i, j, pixel_color, samples_per_pixel)
        pygame.display.flip()


screen = pygame.transform.flip(screen, False, True)
pygame.image.save(screen, 'out.png')

print('Finished in ' + str(time() - start_time) + ' seconds.')



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False