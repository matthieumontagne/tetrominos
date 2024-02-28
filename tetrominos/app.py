""" In this module, you will find the App class
This class contains a very basic game engine based on pygame.
The approach was heavily inspired by this tutorial:
http://pygametutorials.wikidot.com/tutorials-basic
"""

import pygame

from tetrominos.matrix import Matrix
from tetrominos.window import Window


class App:
    """A class reprensenting the app"""

    def __init__(self):
        """Initialize a running Pygame instance with a window of a
        certain size and a clock
        """
        # pygame init
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running: bool = True

        # window init
        self.window = Window(width_in_pixels=1280, height_in_pixels=720).surface

        # matrix init
        self.matrix = Matrix(
            surface=self.window,
            block_size_in_pixels=30,
        )

    def run(self) -> None:
        """Run the Pygame game loop (event -> logic -> rendering) until game is interrupted"""
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.process_game_logic()
            self.render(frame_per_second_limit=60)
        pygame.quit()

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle events like pressed keys, mouse motion or exit

        Args:
            event: a Pygame Event object
        """
        if event.type == pygame.QUIT:
            self.running = False

    def process_game_logic(self):
        """Computes changes happening to the game world"""

    def render(self, frame_per_second_limit: int):
        """Print out graphics"""
        self.window.fill("grey")
        self.matrix.render_matrix()
        pygame.display.flip()
        self.clock.tick(frame_per_second_limit)


if __name__ == "__main__":
    app = App()
    app.run()
