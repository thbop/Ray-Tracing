from hittable import *

class hittable_list(hittable):
    def __init__(self):
        self.objs = []
    
    def add(self, obj):
        self.objs.append(obj)
    
    def hit(self, ray, t_min, t_max, rec):
        temp_rec = hit_record()
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objs:
            if obj.hit(ray, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec
        
        return {'hit_anything': hit_anything, 'rec': rec}