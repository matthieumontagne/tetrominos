"""This modules contains the Map class
"""

from itertools import product

from tetrominos.block import BlockCollection
from tetrominos.tetromino import BaseTetromino

__all__ = ["Map"]


class Map:
    """The map is the abstract representation of the game board.
    The board has a defined number of lines and colums.
    The board smallest subdivision is called a block.
    Each block has coordinates expressed as a tuple.
    (0,0) is the block at the top left of the board
    The map is composed of two elements:
    - a dictionary of locked blocks, each having coordinates
    - a moving tetromino object
    """

    def __init__(self, columns: int = 10, lines: int = 20) -> None:
        self.columns: int = columns
        self.lines: int = lines
        self.locked_blocks = BlockCollection()
        self.active_tetromino: BaseTetromino = BaseTetromino.create_random_tetromino()
        self.locking_grace_period: bool = False

    @property
    def active_blocks(self) -> BlockCollection:
        """Return the collection of blocks composing the active tetromino"""
        return self.active_tetromino.get_blocks()

    @property
    def all_blocks(self) -> BlockCollection:
        """Return the collection of all the blocks locked or active"""
        return self.active_blocks | self.locked_blocks

    def all_possible_coordinates(self) -> list[tuple[int, int]]:
        """Return the list of all valid coordinates considering the size of the map"""
        return list(product(range(self.columns), range(self.lines)))

    def freeze_tetromino(self) -> None:
        """Incorporate a tetromino to
        the locked blocks and make a new tetromino must appear
        """
        self.locked_blocks = self.all_blocks
        self.active_tetromino = BaseTetromino.create_random_tetromino()
