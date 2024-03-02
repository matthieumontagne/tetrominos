"""This modules contains the Map class
"""

from tetrominos.block import BlockCollection
from tetrominos.tetromino import BaseTetromino, TetrominoI

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
        self.active_tetromino: BaseTetromino = TetrominoI()

    @property
    def active_blocks(self) -> BlockCollection:
        """Return the collection of blocks composing the active tetromino"""
        return self.active_tetromino.get_blocks()

    @property
    def all_blocks(self) -> BlockCollection:
        """Return all the blocks locked or active.
        The resulting dict is intented to be feeded to the
        matrix graphical renderer
        """
        return self.active_blocks | self.locked_blocks
