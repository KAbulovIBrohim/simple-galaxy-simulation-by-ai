# body.py
"""
Celestial body class representing planets and stars in the simulation.
Handles physics calculations and rendering.
"""
import pygame
import math
from config import SCALE, G


class Body:
    """
    Represents a celestial body (planet, star) in the gravity simulation.

    Attributes:
        x, y: Position in world coordinates (meters)
        radius: Visual radius in pixels
        mass: Mass in kilograms
        color: RGB color tuple
        x_vel, y_vel: Velocity components (m/s)
        is_star: Whether this is a central star
        trail: List of previous positions for visualization
        max_trail_length: Maximum number of trail points to store
    """

    def __init__(self, x, y, radius, mass, color, x_vel=0, y_vel=0):
        """
        Initialize a celestial body.

        Args:
            x, y: Initial position (meters)
            radius: Visual radius (pixels)
            mass: Mass (kilograms)
            color: RGB color tuple
            x_vel, y_vel: Initial velocity (m/s)
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.is_star = False
        self.trail = []
        self.max_trail_length = 100

    def draw(self, win, camera_offset_x, camera_offset_y):
        """
        Draw the body and its trail on the screen.

        Args:
            win: Pygame display surface
            camera_offset_x, camera_offset_y: Camera center offset in pixels
        """
        # Convert physics coordinates to screen coordinates
        scaled_x = self.x * SCALE + camera_offset_x
        scaled_y = self.y * SCALE + camera_offset_y

        # Draw trail (orbit path)
        if len(self.trail) > 1:
            updated_points = []
            for point in self.trail:
                scaled_point_x = point[0] * SCALE + camera_offset_x
                scaled_point_y = point[1] * SCALE + camera_offset_y
                updated_points.append((scaled_point_x, scaled_point_y))
            pygame.draw.lines(win, self.color, False, updated_points, 1)

        # Draw the body itself
        pygame.draw.circle(
            win, self.color, (int(scaled_x), int(scaled_y)), self.radius
        )

    def add_force(self, bodies, timestep):
        """
        Calculate gravitational forces from all other bodies and update velocity.
        Uses Newton's law of universal gravitation: F = G * m1 * m2 / r^2

        Args:
            bodies: List of all bodies in the system
            timestep: Time step for integration (seconds)
        """
        total_fx = 0
        total_fy = 0

        for body in bodies:
            if self == body:  # Don't calculate gravity with self
                continue

            # Vector from self to other body
            distance_x = body.x - self.x
            distance_y = body.y - self.y
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

            if distance == 0:  # Avoid division by zero
                continue

            # Calculate gravitational force magnitude
            force = G * self.mass * body.mass / (distance ** 2)

            # Calculate force direction
            theta = math.atan2(distance_y, distance_x)
            force_x = force * math.cos(theta)
            force_y = force * math.sin(theta)

            total_fx += force_x
            total_fy += force_y

        # Update velocity using F = ma => a = F/m
        # v_new = v_old + a * dt
        self.x_vel += (total_fx / self.mass) * timestep
        self.y_vel += (total_fy / self.mass) * timestep

    def update_position(self, timestep):
        """
        Update position based on current velocity.
        Also updates trail for visualization.

        Args:
            timestep: Time step for integration (seconds)
        """
        # x_new = x_old + v * dt
        self.x += self.x_vel * timestep
        self.y += self.y_vel * timestep

        # Update trail for orbit visualization
        self.trail.append((self.x, self.y))
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)  # Remove oldest trail point

    def get_speed(self):
        """Return the current speed of the body."""
        return math.sqrt(self.x_vel ** 2 + self.y_vel ** 2)

    def get_kinetic_energy(self):
        """Return the kinetic energy of the body."""
        return 0.5 * self.mass * self.get_speed() ** 2
