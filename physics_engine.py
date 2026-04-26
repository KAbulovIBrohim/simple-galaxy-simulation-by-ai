# physics_engine.py
"""
Physics engine for simulating gravitational interactions.
Manages bodies and updates their positions and velocities each frame.
"""
from body import Body
from config import TIMESTEP


class PhysicsEngine:
    """
    Main physics engine for the gravity simulation.

    Responsible for:
    - Managing all celestial bodies
    - Calculating gravitational forces
    - Updating positions and velocities
    - Managing simulation time steps
    """

    def __init__(self, bodies=None):
        """
        Initialize the physics engine.

        Args:
            bodies: Optional initial list of bodies. If None, starts empty.
        """
        self.bodies = bodies if bodies is not None else []
        self.timestep = TIMESTEP

    def add_body(self, body):
        """
        Add a body to the simulation.

        Args:
            body: Body object to add
        """
        self.bodies.append(body)

    def remove_body(self, body):
        """
        Remove a body from the simulation.

        Args:
            body: Body object to remove
        """
        if body in self.bodies:
            self.bodies.remove(body)

    def update(self):
        """
        Perform one simulation step.
        1. Calculate forces on all bodies
        2. Update velocities based on forces
        3. Update positions based on velocities
        """
        # First pass: calculate forces and update velocities
        for body in self.bodies:
            body.add_force(self.bodies, self.timestep)

        # Second pass: update positions
        for body in self.bodies:
            body.update_position(self.timestep)

    def reset(self):
        """Clear all bodies from the simulation."""
        self.bodies = []

    def set_timestep(self, new_timestep):
        """
        Set the time step for simulation.
        Larger timesteps = faster simulation but less accuracy.
        Smaller timesteps = slower simulation but more accurate.

        Args:
            new_timestep: New timestep in seconds
        """
        if new_timestep > 0:
            self.timestep = new_timestep

    def get_total_momentum(self):
        """Calculate total momentum of all bodies."""
        total_mx = 0
        total_my = 0
        for body in self.bodies:
            total_mx += body.mass * body.x_vel
            total_my += body.mass * body.y_vel
        return (total_mx, total_my)

    def get_total_energy(self):
        """Calculate total kinetic energy of all bodies."""
        total_energy = 0
        for body in self.bodies:
            total_energy += body.get_kinetic_energy()
        return total_energy
