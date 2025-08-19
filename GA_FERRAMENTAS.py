"""
vector_utils.py

A Python module for common 3D vector and plane operations.

Functions:
    - prod_esc(v1, v2): Dot product of two vectors.
    - prod_vet(v1, v2): Cross product of two 3D vectors.
    - mod(v): Magnitude (Euclidean norm) of a vector.
    - proj(v1, v2): Projection of v1 onto v2.
    - alt(v1, v2): Component of v1 orthogonal to v2.
    - equacao_plano(v1, v2, point): Plane coefficients [a, b, c, d] from two vectors and a point.
    - print_vet(v): Nicely formatted string for a 3D vector.
    - distancia_ponto_plano(p, n, d): Distance from point p to plane with normal n and offset d.
    - soma_vet(v1, v2): Sum of two vectors.
    - sub_vet(v1, v2): Difference of two vectors.
    - distancia_ponto_reta(P, Po, V): Vector and distance from P to the line through Po in direction V.
"""

import math
from typing import List, Tuple

def prod_esc(v1: List[float], v2: List[float]) -> float:
    """Return the dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length")
    return sum(float(x) * float(y) for x, y in zip(v1, v2))

def prod_vet(v1: List[float], v2: List[float]) -> List[float]:
    """Return the cross product of two 3D vectors."""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Both vectors must have 3 elements.")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

def mod(v: List[float]) -> float:
    """Return the magnitude (Euclidean norm) of a vector."""
    return math.sqrt(sum(x ** 2 for x in v))

def proj(v1: List[float], v2: List[float]) -> List[float]:
    """Project v1 onto v2."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length.")
    denominator = mod(v2) ** 2
    if denominator == 0:
        raise ValueError("Cannot project onto zero vector.")
    alpha = prod_esc(v1, v2) / denominator
    return [alpha * x for x in v2]

def alt(v1: List[float], v2: List[float]) -> List[float]:
    """Return the component of v1 orthogonal to v2."""
    proj_v1_on_v2 = proj(v1, v2)
    return [x - y for x, y in zip(v1, proj_v1_on_v2)]

def equacao_plano(v1: List[float], v2: List[float], point: List[float]) -> List[float]:
    """
    Return coefficients [a, b, c, d] of the plane equation ax + by + cz + d = 0.
    v1 and v2 are direction vectors in the plane; point is a point on the plane.
    """
    normal = prod_vet(v1, v2)
    d = -sum(n * p for n, p in zip(normal, point))
    return normal + [d]

def print_vet(v: List[float]) -> str:
    """Return a formatted string for a 3D vector."""
    return f"[{v[0]:.5f}, {v[1]:.5f}, {v[2]:.5f}]"

def distancia_ponto_plano(p: List[float], n: List[float], d: float) -> float:
    """
    Return the distance from point p to the plane defined by normal n and offset d.
    Plane equation: n[0]*x + n[1]*y + n[2]*z + d = 0
    """
    numerator = abs(sum(ni * pi for ni, pi in zip(n, p)) + d)
    denominator = mod(n)
    if denominator == 0:
        raise ValueError("Normal vector cannot be zero.")
    return numerator / denominator

def soma_vet(v1: List[float], v2: List[float]) -> List[float]:
    """Return the sum of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length")
    return [x + y for x, y in zip(v1, v2)]

def sub_vet(v1: List[float], v2: List[float]) -> List[float]:
    """Return the difference of two vectors (v1 - v2)."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same length")
    return [x - y for x, y in zip(v1, v2)]

def distancia_ponto_reta(P: List[float], Po: List[float], V: List[float]) -> Tuple[List[float], float]:
    """
    Return the vector and distance from point P to the line passing through Po in direction V.
    Returns (vector from P to line, distance).
    """
    if len(P) != 3 or len(Po) != 3 or len(V) != 3:
        raise ValueError("All vectors must be 3D.")
    vec = sub_vet(P, Po)
    alt_vec = alt(vec, V)
    return alt_vec, mod(alt_vec)
