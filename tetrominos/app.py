""" In this module, you will find the App class
This class contains a very basic game engine based on pygame.
The approach was heavily inspired by this tutorial:
http://pygametutorials.wikidot.com/tutorials-basic
"""

import pygame

from tetrominos.map import Map
from tetrominos.matrix import Matrix
from tetrominos.movement import Rotation, Translation, TranslationDirection
from tetrominos.window import Window


GRAVITYTIMEREVENT = pygame.USEREVENT + 1
LOCKTETROMINOEVENT = pygame.USEREVENT + 2


class App:
    """A class reprensenting the app"""

    def __init__(self) -> None:
        """Initialize a running Pygame instance with a window of a
        certain size and a clock
        """
        # pygame init
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running: bool = True
        pygame.key.set_repeat(500, 500)

        # timer init
        pygame.time.set_timer(GRAVITYTIMEREVENT, 700, 0)

        # window init
        self.window = Window(width_in_pixels=1280, height_in_pixels=720).surface

        # map init
        self.map = Map()

        # matrix init
        self.matrix = Matrix(
            surface=self.window, block_size_in_pixels=30, game_map=self.map
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
        if event.type == GRAVITYTIMEREVENT:
            Translation(self.map, TranslationDirection.DOWN).execute()
        if event.type == LOCKTETROMINOEVENT:
            self.map.freeze_tetromino()
            self.map.locking_grace_period = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Translation(self.map, TranslationDirection.LEFT).execute()
            if event.key == pygame.K_RIGHT:
                Translation(self.map, TranslationDirection.RIGHT).execute()
            if event.key == pygame.K_UP:
                Rotation(self.map).execute()
            if event.key == pygame.K_DOWN:
                while Translation(self.map, TranslationDirection.DOWN).validate():
                    Translation(self.map, TranslationDirection.DOWN).execute()

    def process_game_logic(self) -> None:
        """Process game logic"""

        # handle tetromino freezing
        if (
            not self.map.locking_grace_period
            and not Translation(self.map, TranslationDirection.DOWN).validate()
        ):
            pygame.time.set_timer(LOCKTETROMINOEVENT, 300, loops=1)
            self.map.locking_grace_period = True

    def render(self, frame_per_second_limit: int):
        """Print out graphics"""
        self.window.fill("grey")
        self.matrix.render_matrix()
        pygame.display.flip()
        self.clock.tick(frame_per_second_limit)


if __name__ == "__main__":
    app = App()
    app.run()
