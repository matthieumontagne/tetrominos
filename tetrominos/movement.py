"""This module contains the code related to movement"""

from copy import deepcopy
from enum import Enum

from tetrominos.block import BlockCollection
from tetrominos.coordinates import coordinates_addition
from tetrominos.map import Map
from tetrominos.tetromino import BaseTetromino


class TranslationDirection(Enum):
    """Enumeration of all possible translations coordinates"""

    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, 1)


class BaseMovement:
    """The common base of movement and rotation"""

    def __init__(self, game_map: Map) -> None:
        self.game_map: Map = game_map

    def execute(self) -> None:
        """Execute a movement"""
        simulated_tetromino: BaseTetromino = self.simulate_tetromino()
        if self.is_inbound(simulated_tetromino):
            self.game_map.active_tetromino = simulated_tetromino

    def is_inbound(self, tetromino: BaseTetromino):
        """Check if all the blocks of a tetromino are inside the game board"""
        blocks: BlockCollection = tetromino.get_blocks()
        possible_coordinates = self.game_map.all_possible_coordinates()

        for coordinates in blocks.collection:
            if coordinates not in possible_coordinates:
                return False
        return True

    def simulate_tetromino(self):
        """template for child classes"""


class Translation(BaseMovement):
    """The class representing the movement of a tetromino
    who move left, right or down

    The translation_coordinate correspond of the translation applied between the
    before position and after position"""

    def __init__(self, game_map: Map, direction: TranslationDirection) -> None:
        self.direction = direction.value
        super().__init__(game_map=game_map)

    def simulate_tetromino(self) -> BaseTetromino:
        """Simulate a movement and return a BaseTetromino"""
        simulated_tetromino = deepcopy(self.game_map.active_tetromino)
        simulated_origin = coordinates_addition(
            simulated_tetromino.rotation_space_origin, self.direction
        )
        simulated_tetromino.rotation_space_origin = simulated_origin
        return simulated_tetromino


class Rotation(BaseMovement):
    """This class implements the movement of a tetromino who rotates"""

    def __init__(self, game_map: Map) -> None:
        super().__init__(game_map=game_map)

    def next_rotation_cycle_index(self, tetromino: BaseTetromino):
        """Return the index of the next rotation cycle"""
        current_cycle = tetromino.rotation_cycle_index
        rotation_cycle_lenght = len(tetromino.rotation_template)
        if current_cycle + 1 < rotation_cycle_lenght:
            return current_cycle + 1
        return 0

    def simulate_tetromino(self) -> BaseTetromino:
        """Simulate a movement and return a BaseTetromino"""
        simulated_tetromino = deepcopy(self.game_map.active_tetromino)
        simulated_tetromino.rotation_cycle_index = self.next_rotation_cycle_index(
            simulated_tetromino
        )
        return simulated_tetromino
