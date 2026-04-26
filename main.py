# main.py
"""
Gravity Simulator - AI Agent System
Main entry point for the application.

A physics-based gravity simulation with intelligent agent controls.
Users can create planets and orbits, while the AI agent can autonomously
generate galaxy systems and manage orbital mechanics.
"""
import pygame
import sys
from config import WIDTH, HEIGHT, FPS, BLACK, WHITE, RED
from physics_engine import PhysicsEngine
from renderer import Renderer
from input_handler import InputHandler
from agent import Agent
from body import Body


class GravitySimulator:
    """
    Main application class that orchestrates the gravity simulation.
    Manages the game loop, physics, rendering, and input.
    """

    def __init__(self):
        self.renderer = Renderer(WIDTH, HEIGHT)
        self.physics_engine = PhysicsEngine()
        self.input_handler = InputHandler()
        self.agent = Agent()

        self.running = True
        self.paused = False
        self.clock = pygame.time.Clock()
        self.frame_count = 0

        # Initialize with a default galaxy
        self.initialize_default_system()

    def initialize_default_system(self):
        """Create an initial galaxy for the user to observe"""
        self.agent.generate_random_galaxy(self.physics_engine)

    def handle_input(self):
        """Process user input"""
        result = self.input_handler.handle_input(
            self.physics_engine, self.agent, self.renderer
        )

        if result is False:
            self.running = False
        elif result == "toggle_pause":
            self.paused = not self.paused
        elif result == "reset_simulation":
            self.physics_engine.reset()
            self.initialize_default_system()

    def update(self):
        """Update simulation state"""
        if not self.paused:
            self.physics_engine.update()
            self.agent.update(self.physics_engine, self.frame_count)

    def render(self):
        """Render the simulation to screen"""
        self.renderer.draw_background()
        self.renderer.draw_bodies(self.physics_engine.bodies)

        # Draw HUD (heads-up display)
        self.renderer.render_text(f"Bodies: {len(self.physics_engine.bodies)}", 10, 10, WHITE)
        self.renderer.render_text(
            f"Timestep: {self.physics_engine.timestep:.2e}",
            10, 30, WHITE
        )
        if self.paused:
            self.renderer.render_text("PAUSED", 10, 50, RED)

        # Draw controls
        controls = [
            "CONTROLS:",
            "Click+Drag: Create planet with velocity",
            "SPACE: Pause/Unpause",
            "R: Reset simulation",
            "UP/DOWN: Speed up/slow down time",
            "S: Spawn random planet",
            "G: Generate new galaxy",
        ]
        y_offset = HEIGHT - 140
        for i, control in enumerate(controls):
            self.renderer.render_text(control, 10, y_offset + i * 18, WHITE)

        self.renderer.update_display()

    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_input()
            self.update()
            self.render()

            self.frame_count += 1
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


def main():
    """Entry point for the application"""
    print("=" * 60)
    print("GRAVITY SIMULATOR - AI AGENT SYSTEM")
    print("=" * 60)
    print("\nInitializing simulation...")
    print("Press the window to start interacting!")
    print("\nControls:")
    print("  Left Click + Drag: Create a planet with velocity")
    print("  SPACE: Toggle pause/unpause")
    print("  R: Reset the simulation")
    print("  UP arrow: Speed up time")
    print("  DOWN arrow: Slow down time")
    print("  S: Spawn a random planet")
    print("  G: Generate a new random galaxy")
    print("\n" + "=" * 60 + "\n")

    simulator = GravitySimulator()
    simulator.run()


if __name__ == "__main__":
    main()
