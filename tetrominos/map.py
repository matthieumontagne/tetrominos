"""This modules contains the Map class
"""

from itertools import product

from tetrominos.block import Block


class Map:
    """The Map is the abstract representation of the game board.
    The map has a defined number of lines and colums.
    The map smallest subdivision is called a block.
    Each block has coordinates expressed as a tuple.
    (0,0) is the block at the top left of the board
    """

    def __init__(self, columns: int = 10, lines: int = 20) -> None:
        self.columns: int = columns
        self.lines: int = lines
        self.current_map: dict[tuple[int], Block] = self.create(
            default_color=(255, 192, 203)
        )

    def create(self, default_color: tuple[int]) -> dict[tuple[int], Block]:
        """Create an empty game board.
        The lines and column default values are fixed according
        to the Tetris official specification.

        Args:
            columns: Number of colums in the board. Defaults to 20.
            lines: Number of lines in the board. Defaults to 10.
        """
        empty_map = {}
        for coordinate in product(range(self.columns), range(self.lines)):
            empty_map[coordinate] = Block(color=default_color)
        return empty_map

    def alter_block(self, coordinate: tuple[int], new_block: Block):
        """Alter a specific block in the current map"""
        self.current_map[coordinate] = new_block


if __name__ == "__main__":
    test_map = Map(3, 3)
