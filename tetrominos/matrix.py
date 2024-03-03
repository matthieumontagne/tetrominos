"""In this module, you will find the Matrix class.
"""

import pygame

from tetrominos.block import BlockCollection
from tetrominos.map import Map


__all__ = ["Matrix"]


class Matrix:
    """The game matrix is the graphical representation of
    the game board.
    """

    def __init__(
        self, surface: pygame.Surface, block_size_in_pixels: int, game_map: Map
    ) -> None:
        self.surface: pygame.Surface = surface
        self.block_size_in_pixels: int = block_size_in_pixels
        self.map: Map = game_map
        self.default_color = (255, 255, 0)

    @property
    def width_in_pixels(self) -> int:
        """The matrix width expressed in pixels

        Returns:
            The matrix width in pixels
        """
        return self.map.columns * self.block_size_in_pixels

    @property
    def height_in_pixels(self) -> int:
        """The matrix height expressed in pixels

        Returns:
            The matrix height in pixels
        """
        return self.map.lines * self.block_size_in_pixels

    @property
    def origin(self) -> tuple[int, int]:
        """The origin is the coordinates of the left top
        pixel of the game matrix

        Returns:
            The coordinates of the matrix origin (left, top)
        """
        left = int((self.surface.get_width() - self.width_in_pixels) / 2)
        top = int((self.surface.get_height() - self.height_in_pixels) / 2)
        return (left, top)

    def render_matrix(self) -> None:
        """This method renders the game matrix"""

        blocks: BlockCollection = self.map.all_blocks

        for coordinate in self.map.all_possible_coordinates():

            block_rect: pygame.Rect = self.block_rect(coordinate)
            color: tuple[int, int, int]
            if coordinate in blocks.collection:
                color = blocks.collection[coordinate].color
            else:
                color = self.default_color

            pygame.draw.rect(surface=self.surface, color=color, rect=block_rect)

    def block_rect(self, coordinates: tuple[int, int]) -> pygame.Rect:
        """Return the block as a Pygame Rect Object"""
        column = coordinates[0]
        line = coordinates[1]

        left = self.origin[0] + (self.block_size_in_pixels * column) + 1
        top = self.origin[1] + (self.block_size_in_pixels * line) + 1
        return pygame.Rect(
            left, top, self.block_size_in_pixels - 1, self.block_size_in_pixels - 1
        )
