import math

class Vector:
    def __init__(self, *component):
        self.component = component

    def __str__(self):
        return f"Vector: {self.component}"
        
    def dot(self, other):
        if len(self.component) != len(other.component):
            raise ValueError("vectors must have the same number of component")
        return sum(a * b for a, b in zip(self.component, other.component))
    
    def length(self):
        return math.sqrt(sum(x**2 for x in self.component))
    
    def angle(self, other):
        dot_product = self.dot(other)
        length_self = self.length()
        length_other = other.length()

        if length_self == 0 or length_other == 0:
            raise ValueError("vectors cannot have zero length")
        
        cosine_angle = dot_product / (length_self * length_other)

        cosine_angle = min(cosine_angle, 1)
        cosine_angle = max(cosine_angle, -1)

        angle_degree = math.degrees(math.acos(cosine_angle))

        return angle_degree
