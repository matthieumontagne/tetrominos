"""In this module, you will find the Matrix class.
"""

from dataclasses import dataclass

import pygame

__all__ = ["Matrix"]


@dataclass
class Matrix:
    """The Matrix class represent the game "matrix".
    The game matrix is the grid where tetrominos exist
    and move
    """

    window_width_in_pixels: int
    window_height_in_pixels: int
    width_in_blocks: int
    height_in_blocks: int
    block_size_in_pixels: int

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
            Rerurn the matrix frame as a Pygame Rect Object
        """
        left = (self.window_width_in_pixels - self.width_in_pixels) / 2
        top = (self.window_height_in_pixels - self.height_in_pixels) / 2
        return pygame.Rect(left, top, self.width_in_pixels, self.height_in_pixels)
