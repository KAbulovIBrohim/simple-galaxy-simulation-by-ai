# agent.py
"""
AI Agent for autonomous gravity simulation management.
Handles autonomous decision-making for planet spawning, orbit creation, and system generation.
"""
import random
import math
from body import Body
from config import (
    WIDTH, HEIGHT, SCALE, G, PLANET_MASS, STAR_MASS,
    AGENT_MAX_PLANETS, RED, BLUE, GREEN, YELLOW, WHITE
)


class Agent:
    """
    AI Agent for managing the gravity simulation.
    Can autonomously:
    - Spawn planets
    - Create stable orbits
    - Generate galaxy systems
    - Manage planet velocities
    """

    def __init__(self):
        self.spawn_counter = 0
        self.color_palette = [RED, BLUE, GREEN, YELLOW, WHITE]

    def update(self, physics_engine, frame_count):
        """Called each frame to allow agent to make autonomous decisions"""
        self.spawn_counter += 1

    def handle_mouse_release(self, start_pos, end_pos, physics_engine, renderer):
        """
        Handle user mouse input to create planets with velocity.
        start_pos: where user pressed mouse
        end_pos: where user released mouse
        """
        # Convert screen coordinates to world coordinates
        start_world = renderer.get_world_coordinates(start_pos[0], start_pos[1])
        end_world = renderer.get_world_coordinates(end_pos[0], end_pos[1])

        # Planet position is where mouse was pressed
        x = start_world[0] / SCALE
        y = start_world[1] / SCALE

        # Velocity is determined by drag distance
        vel_x = (end_world[0] - start_world[0]) / SCALE * 0.1
        vel_y = (end_world[1] - start_world[1]) / SCALE * 0.1

        # Create planet
        radius = random.randint(5, 12)
        mass = PLANET_MASS
        color = random.choice(self.color_palette)

        planet = Body(x, y, radius, mass, color, vel_x, vel_y)
        physics_engine.add_body(planet)

    def spawn_random_planet(self, physics_engine):
        """Spawn a random planet in the simulation"""
        if len(physics_engine.bodies) >= AGENT_MAX_PLANETS:
            return

        # Random position on screen
        x = random.uniform(-WIDTH / 2 / SCALE, WIDTH / 2 / SCALE)
        y = random.uniform(-HEIGHT / 2 / SCALE, HEIGHT / 2 / SCALE)

        radius = random.randint(3, 8)
        mass = PLANET_MASS
        color = random.choice(self.color_palette)

        # Random velocity
        vel_x = random.uniform(-50000, 50000)
        vel_y = random.uniform(-50000, 50000)

        planet = Body(x, y, radius, mass, color, vel_x, vel_y)
        physics_engine.add_body(planet)

    def create_stable_orbit(self, physics_engine, star_mass=None):
        """
        Create a stable orbit around the most massive body (assumed to be central).
        Calculates orbital velocity needed for a circular orbit.
        """
        if not physics_engine.bodies:
            return

        # Find the most massive body (central star)
        central_body = max(physics_engine.bodies, key=lambda b: b.mass)

        # Create a planet at a reasonable distance
        orbital_distance = random.uniform(0.3, 0.7) # AU-ish
        orbital_distance_m = orbital_distance * 1.496e11

        # Angle in orbit
        angle = random.uniform(0, 2 * math.pi)

        # Position relative to star
        x = central_body.x + orbital_distance_m * math.cos(angle)
        y = central_body.y + orbital_distance_m * math.sin(angle)

        # Calculate orbital velocity for circular orbit: v = sqrt(GM/r)
        orbital_velocity = math.sqrt(G * central_body.mass / orbital_distance_m)

        # Velocity perpendicular to radius (tangential)
        vel_x = central_body.x_vel - orbital_velocity * math.sin(angle)
        vel_y = central_body.y_vel + orbital_velocity * math.cos(angle)

        # Create planet
        radius = random.randint(4, 9)
        mass = PLANET_MASS
        color = random.choice(self.color_palette)

        planet = Body(x, y, radius, mass, color, vel_x, vel_y)
        physics_engine.add_body(planet)

    def generate_random_galaxy(self, physics_engine):
        """
        Generate a random galaxy system with a central star and orbiting planets.
        """
        # Clear existing bodies for clean slate
        physics_engine.reset()

        # Create central star at origin
        star = Body(0, 0, 15, STAR_MASS, YELLOW)
        star.is_star = True
        physics_engine.add_body(star)

        # Create 5-8 planets in stable orbits
        num_planets = random.randint(5, 8)
        for _ in range(num_planets):
            self.create_stable_orbit(physics_engine, STAR_MASS)

    def generate_binary_system(self, physics_engine):
        """
        Create a binary star system with orbiting planets.
        """
        physics_engine.reset()

        # Create two stars orbiting each other
        separation = 5e11  # 3 AU
        star1 = Body(-separation / 2, 0, 12, STAR_MASS / 2, YELLOW)
        star2 = Body(separation / 2, 0, 12, STAR_MASS / 2, WHITE)

        # Give them orbital velocities
        orbital_velocity = math.sqrt(G * (STAR_MASS / 2) / separation)
        star1.y_vel = orbital_velocity
        star2.y_vel = -orbital_velocity

        star1.is_star = True
        star2.is_star = True

        physics_engine.add_body(star1)
        physics_engine.add_body(star2)

        # Add planets around the system
        for _ in range(3):
            self.create_stable_orbit(physics_engine, STAR_MASS)

    def adjust_planet_velocity(self, body, factor=1.1):
        """Adjust planet velocity by a given factor"""
        body.x_vel *= factor
        body.y_vel *= factor

    def get_system_stats(self, physics_engine):
        """Get statistics about the current system"""
        if not physics_engine.bodies:
            return {}

        total_momentum = 0
        total_kinetic_energy = 0
        num_bodies = len(physics_engine.bodies)

        for body in physics_engine.bodies:
            speed = math.sqrt(body.x_vel**2 + body.y_vel**2)
            total_momentum += body.mass * speed
            total_kinetic_energy += 0.5 * body.mass * speed**2

        return {
            "num_bodies": num_bodies,
            "total_momentum": total_momentum,
            "total_kinetic_energy": total_kinetic_energy,
        }
