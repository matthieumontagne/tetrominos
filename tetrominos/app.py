""" In this module, you will find the App class
This class contains a very basic game engine based on pygame.
The approach was heavily inspired by this tutorial:
http://pygametutorials.wikidot.com/tutorials-basic
"""

import pygame

from matrix import Matrix


class App:
    """A class reprensenting the game engine"""

    def __init__(self, window_width: int, window_height: int):
        """Initialize a running Pygame instance with a window of a
        certain size and a clock

        Args:
            window_width: the width of the app window, in pixels
            window_height: the height of the app window, in pixels
        """
        # pygame init
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running: bool = True

        # window init
        self.window_width: int = window_width
        self.window_height: int = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # matrix init
        self.matrix = Matrix(
            window_width_in_pixels=window_width,
            window_height_in_pixels=window_height,
            width_in_blocks=10,
            height_in_blocks=22,
            block_size_in_pixels=30,
        )

    def run(self) -> None:
        """Run the Pygame game loop until it is interrupted"""
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.process_game_logic()
            self.render(frame_per_second_limit=60)
        pygame.quit()

    def handle_event(self, event: pygame.event.Event) -> None:
        """Proceeds events (like pressed keys, mouse motion, exit)

        Args:
            event: a Pygame Event object
        """
        if event.type == pygame.QUIT:
            self.running = False

    def process_game_logic(self):
        """Computes the changes in the game world"""

    def render(self, frame_per_second_limit: int):
        """Print out graphics"""
        self.window.fill("grey")
        pygame.draw.rect(
            surface=self.window, color="white", rect=self.matrix.matrix_rect
        )
        pygame.display.flip()
        self.clock.tick(frame_per_second_limit)


if __name__ == "__main__":
    app = App(window_width=1280, window_height=720)
    app.run()
