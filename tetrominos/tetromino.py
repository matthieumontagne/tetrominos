"""This module contains the code related to tetrominos
Tetrominos are shapes composed of four adjacent blocks
They move and rotate"""

from operator import add

from tetrominos.block import Block

__all__ = ["BaseTetromino", "TetrominoI"]


class BaseTetromino:
    """The base tetromino

    The Base tetromino class represent the active tetromino.

    The rotation space is the space the tetromino can occupy in
    all its possible rotations

    The left-top block of the rotation space is its origin

    The rotation_template list the coordinates of all the possibles positions of
    the tetromino in the rotation space.

    """

    def __init__(self):
        self.color: tuple[int]
        self.rotation_space_origin: tuple[int]
        self.rotation_template: list[list[tuple[int]]]
        self.rotation_cycle_index: int = 0

    def get_blocks(self) -> dict[tuple[int], Block]:
        """Return  all currents blocks of the tetromino and their coordinates"""
        rotation_template = self.rotation_template[self.rotation_cycle_index]

        blocks = {}

        for template_coordinate in rotation_template:
            map_coordinate = self.get_block_coordinates(
                origin=self.rotation_space_origin,
                template_coordinate=template_coordinate,
            )
            blocks[map_coordinate] = Block(color=self.color)
        return blocks

    def get_block_coordinates(
        self, origin: tuple[int], template_coordinate: tuple[int]
    ):
        """Get the coordinate of a block considering:
        - the origin of its rotation space
        - its position in the rotation template
        """
        return tuple(map(add, template_coordinate, origin))


class TetrominoI(BaseTetromino):
    """The I tretromino"""

    def __init__(self):
        super().__init__()
        self.color: tuple[int] = (0, 255, 255)  # cyan
        self.rotation_space_origin: tuple[int] = (3, -2)
        self.rotation_template: list[list[tuple[int]]] = [
            [(0, 2), (1, 2), (2, 2), (3, 2)],
            [(2, 0), (2, 1), (2, 2), (2, 3)],
        ]
