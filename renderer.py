# renderer.py
"""
Renderer module for visualizing the gravity simulation using Pygame.
Handles all drawing operations.
"""
import pygame
from config import WIDTH, HEIGHT, BLACK, WHITE


class Renderer:
    """
    Handles all rendering operations for the simulation.

    Manages:
    - Display surface
    - Camera positioning
    - Body drawing
    - UI text rendering
    """

    def __init__(self, width, height):
        """
        Initialize the renderer.

        Args:
            width: Screen width in pixels
            height: Screen height in pixels
        """
        pygame.init()
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Gravity Simulator - AI Agent System")

        # Font for UI text
        self.font = pygame.font.SysFont("monospace", 14)
        self.font_large = pygame.font.SysFont("monospace", 20)

        # Camera position (center of view in pixels)
        self.camera_offset_x = self.width / 2
        self.camera_offset_y = self.height / 2

    def draw_background(self):
        """Fill the screen with black background."""
        self.win.fill(BLACK)

    def draw_bodies(self, bodies):
        """
        Draw all bodies in the simulation.

        Args:
            bodies: List of Body objects to draw
        """
        for body in bodies:
            body.draw(self.win, self.camera_offset_x, self.camera_offset_y)

    def update_display(self):
        """Update the display with all drawn elements."""
        pygame.display.update()

    def render_text(self, text, x, y, color=WHITE, large=False):
        """
        Render text on screen.

        Args:
            text: Text string to render
            x, y: Position on screen
            color: RGB color tuple
            large: If True, use larger font
        """
        font = self.font_large if large else self.font
        label = font.render(text, 1, color)
        self.win.blit(label, (x, y))

    def get_world_coordinates(self, screen_x, screen_y):
        """
        Convert screen coordinates to world coordinates.

        Args:
            screen_x, screen_y: Screen pixel coordinates

        Returns:
            Tuple of world coordinates
        """
        world_x = screen_x - self.camera_offset_x
        world_y = screen_y - self.camera_offset_y
        return (world_x, world_y)

    def get_screen_coordinates(self, world_x, world_y):
        """
        Convert world coordinates to screen coordinates.

        Args:
            world_x, world_y: World coordinates

        Returns:
            Tuple of screen coordinates
        """
        screen_x = world_x + self.camera_offset_x
        screen_y = world_y + self.camera_offset_y
        return (screen_x, screen_y)

    def clear_screen(self):
        """Clear the screen (same as draw_background)."""
        self.draw_background()
