"""This module contains the code related to movement"""

from copy import deepcopy
from enum import Enum

from tetrominos.block import BlockCollection
from tetrominos.coordinates import coordinates_addition
from tetrominos.map import Map
from tetrominos.tetromino import BaseTetromino


class Translation(Enum):
    """Enumeration of all possible translations coordinates"""

    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, 1)


class Movement:
    """The class representing the movement that can happen to a tetromino

    The translation_coordinate correspond of the translation applied between the
    before position and after position"""

    def __init__(self, game_map: Map, translation: Translation) -> None:
        self.map: Map = game_map
        self.translation = translation.value

    def execute(self) -> None:
        """Execute a movement"""
        simulated_tetromino: BaseTetromino = self.simulate_tetromino()
        if self.is_inbound(simulated_tetromino):
            self.map.active_tetromino = simulated_tetromino

    def simulate_tetromino(self) -> BaseTetromino:
        """Simulate a movement and return a BaseTetromino"""
        simulated_tetromino = deepcopy(self.map.active_tetromino)
        simulated_origin = coordinates_addition(
            simulated_tetromino.rotation_space_origin, self.translation
        )
        simulated_tetromino.rotation_space_origin = simulated_origin
        return simulated_tetromino

    def is_inbound(self, tetromino: BaseTetromino):
        """Check if all the blocks of a tetromino are inside the game board"""
        blocks: BlockCollection = tetromino.get_blocks()
        possible_coordinates = self.map.all_possible_coordinates()

        for coordinates in blocks.collection:
            if coordinates not in possible_coordinates:
                return False
        return True
