"""In this module, you will find the Matrix class.
"""

from dataclasses import dataclass

import pygame


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
    width_in_blocks: int = 10
    height_in_blocks: int = 20

    @property
    def width_in_pixels(self) -> int:
        """The matrix width expressed in pixels

        Returns:
            The matrix width in pixels
        """
        return self.width_in_blocks * self.block_size_in_pixels

    @property
    def height_in_pixels(self):
        """The matrix height expressed in pixels

        Returns:
            The matrix height in pixels
        """
        return self.height_in_blocks * self.block_size_in_pixels

    @property
    def matrix_rect(self) -> pygame.Rect:
        """Matrix frame

        Returns:
            Return the matrix frame as a Pygame Rect Object
        """
        left = (self.surface.get_width() - self.width_in_pixels) / 2
        top = (self.surface.get_height() - self.height_in_pixels) / 2
        return pygame.Rect(left, top, self.width_in_pixels, self.height_in_pixels)

    def render_matrix(self):
        """This method renders the game matrix"""
        pygame.draw.rect(surface=self.surface, color="white", rect=self.matrix_rect)
