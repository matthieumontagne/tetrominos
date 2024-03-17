"""This module contains the code related to tetrominos
Tetrominos are shapes composed of four adjacent blocks
They move and rotate"""

from __future__ import annotations
from dataclasses import dataclass
from random import choice

from tetrominos.block import Block, BlockCollection
from tetrominos.coordinates import coordinates_addition

__all__ = [
    "BaseTetromino",
    "TetrominoI",
    "TetrominoO",
    "TetrominoL",
    "TetrominoJ",
    "TetrominoS",
    "TetrominoZ",
    "TetrominoT",
]


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

    @classmethod
    def create_random_tetromino(cls) -> BaseTetromino:
        """Return a random tetromino"""
        random_tetromino_class = choice(
            [
                TetrominoI,
                TetrominoO,
                TetrominoL,
                TetrominoJ,
                TetrominoS,
                TetrominoZ,
                TetrominoT,
            ]
        )
        return random_tetromino_class()


@dataclass
class TetrominoI(BaseTetromino):
    """The I tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (0, 255, 255)  # cyan
        self.rotation_space_origin: tuple[int, int] = (3, -2)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(2, 0), (2, 1), (2, 2), (2, 3)],
        ]


@dataclass
class TetrominoO(BaseTetromino):
    """The O tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (255, 255, 0)  # yellow
        self.rotation_space_origin: tuple[int, int] = (4, 0)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 0), (0, 1), (1, 0), (1, 1)],
        ]


@dataclass
class TetrominoJ(BaseTetromino):
    """The J tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (0, 0, 139)  # dark blue
        self.rotation_space_origin: tuple[int, int] = (4, 0)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 1), (1, 1), (2, 1), (2, 2)],
            [(1, 0), (1, 1), (1, 2), (0, 2)],
            [(0, 1), (0, 2), (1, 2), (2, 2)],
            [(1, 0), (2, 0), (2, 1), (2, 2)],
        ]


@dataclass
class TetrominoL(BaseTetromino):
    """The L tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (255, 136, 0)  # orange
        self.rotation_space_origin: tuple[int, int] = (4, 0)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 2), (0, 1), (1, 1), (2, 1)],
            [(0, 0), (1, 0), (1, 1), (1, 2)],
            [(2, 1), (2, 2), (1, 2), (0, 2)],
            [(1, 0), (1, 1), (1, 2), (2, 2)],
        ]


@dataclass
class TetrominoS(BaseTetromino):
    """The S tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (0, 128, 0)  # green
        self.rotation_space_origin: tuple[int, int] = (4, 0)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 2), (1, 2), (1, 1), (2, 1)],
            [(0, 0), (0, 1), (1, 1), (1, 2)],
        ]


@dataclass
class TetrominoZ(BaseTetromino):
    """The Z tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (178, 34, 34)  # fire brick
        self.rotation_space_origin: tuple[int, int] = (4, 0)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 1), (1, 1), (1, 2), (2, 2)],
            [(1, 2), (1, 1), (2, 1), (2, 0)],
        ]


@dataclass
class TetrominoT(BaseTetromino):
    """The T tretromino"""

    def __init__(self) -> None:
        super().__init__()
        self.color: tuple[int, int, int] = (186, 85, 211)  # medium orchid
        self.rotation_space_origin: tuple[int, int] = (4, 0)
        self.rotation_template: list[list[tuple[int, int]]] = [
            [(0, 1), (1, 1), (2, 1), (1, 2)],
            [(1, 0), (1, 1), (1, 2), (0, 1)],
            [(0, 2), (1, 2), (2, 2), (1, 1)],
            [(1, 0), (1, 1), (1, 2), (2, 1)],
        ]
