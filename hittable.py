

class hittable:
    def hit(self, ray, t_min, t_max, rec): return 0

class hit_record:
    def __init__(self):
        self.p = None
        self.normal = None
        self.t = None
        self.front_face = None
    
    def set_face_normal(self, ray, outward_normal):
        self.front_face = ray.direction.dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

