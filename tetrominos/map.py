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

    def is_row_complete(self, row: int) -> bool:
        """return True if a row is complete"""
        row_size = self.columns
        row_counter = 0
        for coordinate in self.locked_blocks.collection.keys():
            if coordinate[1] == row:
                row_counter += 1
        return row_size == row_counter

    def list_complete_rows(self) -> list[int]:
        """List all complete rows and return a list containing their number"""
        row_list = []
        for row_number in range(0, self.lines):
            if self.is_row_complete(row_number):
                row_list.append(row_number)
        return row_list

    def pop_complete_rows(self) -> None:
        """ "Delete complete rows"""
        rows_to_pop = self.list_complete_rows()

        for row_number in rows_to_pop:
            self.locked_blocks.delete_row(row_number)
