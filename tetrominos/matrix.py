"""In this module, you will find the Matrix class.
"""

from dataclasses import dataclass

import pygame

from tetrominos.map import Map


__all__ = ["Matrix"]


@dataclass
class Matrix:
    """The Matrix class represent the game "matrix".
    The game matrix is the graphical representation of
    the grid where tetrominos exist, move and interact.
    Each subdivision of the matrix is called a "block".
    """

    surface: pygame.Surface
    block_size_in_pixels: int
    map: Map

    @property
    def width_in_pixels(self) -> int:
        """The matrix width expressed in pixels

        Returns:
            The matrix width in pixels
        """
        return self.map.columns * self.block_size_in_pixels

    @property
    def height_in_pixels(self):
        """The matrix height expressed in pixels

        Returns:
            The matrix height in pixels
        """
        return self.map.lines * self.block_size_in_pixels

    @property
    def origin(self):
        """The matrix origin

        Returns:
            The coordinates of the matrix origin (left, top)
        """
        left = (self.surface.get_width() - self.width_in_pixels) / 2
        top = (self.surface.get_height() - self.height_in_pixels) / 2
        return (left, top)

    @property
    def matrix_rect(self) -> pygame.Rect:
        """Return the matrix frame as a Pygame Rect Object"""
        return pygame.Rect(
            self.origin,
            (
                self.width_in_pixels,
                self.height_in_pixels,
            ),
        )

    def render_matrix(self):
        """This method renders the game matrix"""
        for coordinates, block in self.map.current_map.items():
            block_rect: pygame.Rect = self.block_rect(coordinates)
            color: tuple[int] = block.color

            pygame.draw.rect(surface=self.surface, color=color, rect=block_rect)

    def block_rect(self, coordinates: tuple[int]) -> pygame.Rect:
        """Return the block as a Pygame Rect Object"""
        column = coordinates[0]
        line = coordinates[1]

        left = self.origin[0] + (self.block_size_in_pixels * column) + 1
        top = self.origin[1] + (self.block_size_in_pixels * line) + 1
        return pygame.Rect(
            left, top, self.block_size_in_pixels - 1, self.block_size_in_pixels - 1
        )
