# input_handler.py
"""
Input handler for keyboard and mouse input.
Processes user interactions and passes them to appropriate handlers.
"""
import pygame


class InputHandler:
    """
    Handles all user input from keyboard and mouse.

    Supports:
    - Mouse click and drag for creating planets
    - Keyboard controls for simulation management
    """

    def __init__(self):
        """Initialize input handler state."""
        self.mouse_down = False
        self.mouse_pos = (0, 0)
        self.mouse_drag_start = (0, 0)

    def handle_input(self, physics_engine, agent, renderer):
        """
        Process all input events.

        Args:
            physics_engine: PhysicsEngine instance
            agent: Agent instance
            renderer: Renderer instance

        Returns:
            - False if user wants to quit
            - "toggle_pause" to pause/unpause
            - "reset_simulation" to reset
            - True if simulation should continue
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
                self.mouse_drag_start = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False
                # Handle planet creation with velocity
                current_mouse_pos = pygame.mouse.get_pos()
                agent.handle_mouse_release(
                    self.mouse_drag_start, current_mouse_pos, physics_engine, renderer
                )

            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                result = self.handle_keydown(event.key, physics_engine, agent)
                if result is not None:
                    return result

        return True

    def handle_keydown(self, key, physics_engine, agent):
        """
        Handle keyboard key presses.

        Args:
            key: Pygame key constant
            physics_engine: PhysicsEngine instance
            agent: Agent instance

        Returns:
            None or special command string
        """
        if key == pygame.K_SPACE:
            # Toggle pause
            return "toggle_pause"

        elif key == pygame.K_r:
            # Reset simulation
            return "reset_simulation"

        elif key == pygame.K_UP:
            # Increase timestep (speed up simulation)
            new_timestep = physics_engine.timestep * 2
            physics_engine.set_timestep(new_timestep)
            print(f"Timestep increased: {physics_engine.timestep:.2e} s/frame")

        elif key == pygame.K_DOWN:
            # Decrease timestep (slow down simulation)
            new_timestep = physics_engine.timestep / 2
            physics_engine.set_timestep(new_timestep)
            print(f"Timestep decreased: {physics_engine.timestep:.2e} s/frame")

        elif key == pygame.K_s:
            # Agent spawn random planet
            agent.spawn_random_planet(physics_engine)
            print(f"Planet spawned! Total bodies: {len(physics_engine.bodies)}")

        elif key == pygame.K_g:
            # Agent generate galaxy
            agent.generate_random_galaxy(physics_engine)
            print(f"Galaxy generated! Total bodies: {len(physics_engine.bodies)}")

        elif key == pygame.K_b:
            # Generate binary system
            agent.generate_binary_system(physics_engine)
            print(f"Binary system generated! Total bodies: {len(physics_engine.bodies)}")

        elif key == pygame.K_o:
            # Create a stable orbit
            agent.create_stable_orbit(physics_engine)
            print(f"Orbit created! Total bodies: {len(physics_engine.bodies)}")

        return None
