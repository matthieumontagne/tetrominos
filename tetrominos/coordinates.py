"""module related to coordinates"""

from operator import add


def coordinates_addition(coordinate1: tuple[int, int], coordinate2: tuple[int, int]):
    """Add two coordinates"""
    return tuple(map(add, coordinate1, coordinate2))
