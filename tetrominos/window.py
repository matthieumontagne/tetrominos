"""This module contains the Windows class
"""

from dataclasses import dataclass

import pygame


@dataclass
class Window:
    """The windows class represent the game window."""

    width_in_pixels: int
    height_in_pixels: int

    @property
    def surface(self) -> pygame.Surface:
        """Create a Pygame Surface object reprenting the app window

        Returns:
            A Pygame Surface object reprenting the app window
        """
        return pygame.display.set_mode((self.width_in_pixels, self.height_in_pixels))
