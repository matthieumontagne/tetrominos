"""This modules contains the Map class
"""

from tetrominos.block import Block


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
        self.locked_blocks: dict[tuple[int], Block] = {}
        self.active_blocks: dict[tuple[int], Block] = {}

    def lock_block(self, coordinates: [tuple[int]], block: Block):
        """Add a new block to the locked_blocks dictionary"""
        self.locked_blocks[coordinates] = block

    @property
    def all_blocks(self) -> dict[tuple[int], Block]:
        """Return all the blocks locked or active.
        The resulting dict is intented to be feeded to the
        matrix graphical renderer
        """
        return self.active_blocks | self.locked_blocks
