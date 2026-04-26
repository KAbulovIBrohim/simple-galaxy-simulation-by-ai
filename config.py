# config.py
"""
Global configuration and constants for the gravity simulator.
"""

# Screen dimensions
WIDTH, HEIGHT = 1200, 800
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

# Physics constants
G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)
AU = 1.496e11  # Astronomical Unit in meters

# Masses (kg)
PLANET_MASS = 5e24  # Earth-like mass
STAR_MASS = 1.989e30  # Solar mass

# Scaling for visualization
SCALE = 150 / AU  # 1 AU = 150 pixels
TIMESTEP = 3600 * 24  # 1 day in seconds

# Agent settings
AGENT_SPAWN_INTERVAL = 300  # frames between automatic spawns
AGENT_MAX_PLANETS = 15  # maximum planets agent can spawn
