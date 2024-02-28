"""This modules contains the Map class
"""

from dataclasses import dataclass

# from tetrominos.block import Block


@dataclass
class Map:
    """The Map is the abstract representation of the game board."""

    height_in_blocks: int = 20
    width_in_blocks: int = 10
