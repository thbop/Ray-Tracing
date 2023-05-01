from hittable import *
from math import sqrt


class sphere(hittable):
    def __init__(self, cen, r):
        self.center = cen
        self.radius = r
    
    def hit(self, ray, t_min, t_max, rec):
        oc = ray.origin - self.center
        a = ray.direction.magnitude()**2
        half_b = oc.dot(ray.direction)
        c = oc.magnitude()**2 - self.radius**2

        discriminant = half_b**2 - a*c
        if discriminant < 0: return False
        sqrtd = sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False
        
        
        rec.t = root
        rec.p = ray.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(ray, outward_normal)

        return True