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
        """When a tetromino touch the ground line, it must be incorporated to
        the locked blocks and a new tetromino must appear
        """
        if self.tetromino_in_contact_with_ground():
            self.locked_blocks = self.all_blocks
            self.active_tetromino: BaseTetromino = (
                BaseTetromino.create_random_tetromino()
            )

    def tetromino_in_contact_with_ground(self) -> bool:
        """check if the tetromino is in contact with the ground"""
        blocks: BlockCollection = self.active_tetromino.get_blocks()
        ground_level = self.lines - 1
        for coordinate in blocks.collection:
            line = coordinate[1]
            if line == ground_level:
                return True
        return False
