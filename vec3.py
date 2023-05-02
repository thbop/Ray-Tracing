'''
This is my un-used vec3 class.
I was quite sad when testing (on average), this vec3 class ran 1s slower than the pygame.math.Vector3 class.
'''

class vec3:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)
    
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return vec3(self.x * other, self.y * other, self.z * other)
        return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return vec3(self.x / other, self.y / other, self.z / other)
        return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
    
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def magnitude(self):
        return ( self.x**2 + self.y**2 + self.z**2 ) ** 0.5
    
    def normalize(self):
        return self / self.magnitude()
    
    def __repr__(self):
        return 'vec3( ' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ' )'
    


