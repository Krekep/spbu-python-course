import math

def dot_product(vector1, vector2):
    """
    Calculate the dot product of two vectors.

    Args:
        vector1 (list): First vector as a list of numbers.
        vector2 (list): Second vector as a list of numbers.

    Returns:
        float: Dot product of the two vectors.

    Raises:
        ValueError: If vectors have different lengths.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))


def vector_length(vector):
    """
    Calculate the Euclidean length (magnitude) of a vector.

    Args:
        vector (list): Vector as a list of numbers.

    Returns:
        float: Length of the vector.
    """
    return math.sqrt(sum(x * x for x in vector))


def angle_between(vector1, vector2):
    """
    Calculate the angle between two vectors in radians.

    Args:
        vector1 (list): First vector.
        vector2 (list): Second vector.

    Returns:
        float: Angle between vectors in radians.

    Raises:
        ValueError: If either vector is a zero vector.
    """
    dot = dot_product(vector1, vector2)
    len1 = vector_length(vector1)
    len2 = vector_length(vector2)
    
    if len1 == 0 or len2 == 0:
        raise ValueError("Vectors cannot be zero vectors")
    
    # Ensure cosine value is within valid range to avoid floating point errors
    cos_angle = dot / (len1 * len2)
    cos_angle = max(min(cos_angle, 1.0), -1.0)
    
    return math.acos(cos_angle)


class Vector:
    """
    A class representing a mathematical vector.
    
    Attributes:
        components (list): The components of the vector.
    """
    
    def __init__(self, components):
        """
        Initialize a vector with given components.
        
        Args:
            components (list): List of numerical components.
        """
        self.components = list(components)
    
    def dot(self, other):
        """
        Calculate dot product with another vector.
        
        Args:
            other (Vector): Another vector.
            
        Returns:
            float: Dot product.
        """
        return dot_product(self.components, other.components)
    
    def length(self):
        """
        Calculate the length of the vector.
        
        Returns:
            float: Vector length.
        """
        return vector_length(self.components)
    
    def angle_with(self, other):
        """
        Calculate angle with another vector.
        
        Args:
            other (Vector): Another vector.
            
        Returns:
            float: Angle in radians.
        """
        return angle_between(self.components, other.components)
    
    def __repr__(self):
        return f"Vector({self.components})"
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.components == other.components