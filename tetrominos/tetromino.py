"""This module contains the code related to tetrominos
Tetrominos are shapes composed of four adjacent blocks
They move and rotate"""

from dataclasses import dataclass

from tetrominos.block import Block, BlockCollection
from tetrominos.coordinates import coordinates_addition

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

    def __init__(self) -> None:
        self.color: tuple[int, int, int]
        self.rotation_space_origin: tuple[int, int]
        self.rotation_template: list[list[tuple[int, int]]]
        self.rotation_cycle_index: int = 0

    def get_blocks(self) -> BlockCollection:
        """Return  all currents blocks of the tetromino and their coordinates"""
        blocks = BlockCollection()
        print(self.rotation_cycle_index)
        rotation_template = self.rotation_template[self.rotation_cycle_index]
        for template_coordinate in rotation_template:
            map_coordinate: tuple[int, int] = coordinates_addition(
                self.rotation_space_origin,
                template_coordinate,
            )
            blocks.add(map_coordinate, Block(self.color))
        return blocks

    def __str__(self):
        return self.__class__.__name__


@dataclass
class TetrominoI(BaseTetromino):
    """The I tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (0, 255, 255)  # cyan
        self.rotation_space_origin: tuple[int, int] = (3, -2)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 2), (1, 2), (2, 2), (3, 2)],
            [(2, 0), (2, 1), (2, 2), (2, 3)],
        ]
