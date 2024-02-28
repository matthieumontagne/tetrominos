"""This class contains the Block class
"""

from dataclasses import dataclass

__all__ = ["Block"]


@dataclass
class Block:
    """This class represents a block. The block is the smallest subdivision of the game matrix"""

    color: tuple[int]
