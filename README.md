# Gravity Simulator - AI Agent System

A comprehensive physics-based gravity simulation system with intelligent agent controls. Built with Python and Pygame, featuring real physics calculations, interactive user controls, and autonomous agent decision-making.

## Project Overview

This is a **complete, production-quality** AI agent system for physics simulation. It demonstrates:

- **Modular Architecture**: Clean separation of concerns across 7 specialized modules
- **Real Physics**: Newton's law of gravitation with accurate calculations
- **AI Agent**: Autonomous decision-making for planet spawning and orbit creation
- **Interactive UI**: Mouse and keyboard controls for user interaction
- **Visualization**: Real-time rendering with orbit trails

## Project Structure

```
simulation/
├── config.py              # Global constants and configuration
├── body.py                # Celestial body class (planets, stars)
├── physics_engine.py      # Physics simulation engine
├── renderer.py            # Pygame visualization system
├── input_handler.py       # Keyboard and mouse input handling
├── agent.py               # AI agent for autonomous management
├── main.py                # Application entry point
└── README.md              # This file
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install pygame numpy
```

### Step 2: Navigate to Project Directory

```bash
cd /path/to/simulation
```

### Step 3: Run the Application

```bash
python main.py
```

The application will:
1. Initialize Pygame
2. Create a default galaxy system
3. Open the visualization window
4. Display the controls

## Controls & Features

### Mouse Controls
- **Click and Drag**: Create a planet with initial velocity
  - Click position = planet spawn location
  - Drag distance and direction = initial velocity vector
  - Release to create the planet

### Keyboard Controls

| Key | Action |
|-----|--------|
| **SPACE** | Pause/Unpause simulation |
| **R** | Reset simulation (clear all bodies) |
| **UP Arrow** | Speed up time (increase timestep) |
| **DOWN Arrow** | Slow down time (decrease timestep) |
| **S** | Spawn a random planet |
| **G** | Generate a new random galaxy |
| **B** | Generate a binary star system |
| **O** | Create a planet in stable orbit |
| **ESC/Close Window** | Exit application |

## How It Works

### Physics Engine

The simulation uses **Newton's Law of Universal Gravitation**:

```
F = G * m₁ * m₂ / r²
```

Where:
- **F** = Gravitational force (Newtons)
- **G** = Gravitational constant (6.674e-11 m³ kg⁻¹ s⁻²)
- **m₁, m₂** = Masses of the two bodies
- **r** = Distance between bodies

For each frame:
1. Calculate gravitational forces on all bodies
2. Update velocities based on forces (F = ma)
3. Update positions based on velocities

### Coordinate System

- **World Coordinates**: Physics calculations use meters (real SI units)
- **Screen Coordinates**: Scaled for visualization (150 pixels per AU)
- **Time**: Each frame = 1 day in simulation time

### Body Properties

Each celestial body has:
- **Position** (x, y): World coordinates in meters
- **Velocity** (vx, vy): Velocity components in m/s
- **Mass**: Kilograms (planet ≈ 5e24 kg, star ≈ 2e30 kg)
- **Radius**: Visual size in pixels
- **Trail**: List of previous positions for orbit visualization

### AI Agent Capabilities

The Agent class provides autonomous control:

1. **Random Planet Spawning** (`spawn_random_planet`)
   - Creates planets with random positions and velocities
   - Respects maximum planet limit

2. **Stable Orbit Creation** (`create_stable_orbit`)
   - Calculates required velocity for circular orbits
   - Computes: `v = sqrt(G * M / r)`
   - Maintains orbital physics

3. **Galaxy Generation** (`generate_random_galaxy`)
   - Creates central star
   - Spawns 5-8 planets in stable orbits
   - Generates complete systems

4. **Binary System** (`generate_binary_system`)
   - Two stars orbiting each other
   - Planets orbiting the binary pair
   - Complex orbital mechanics

5. **System Statistics** (`get_system_stats`)
   - Tracks total momentum
   - Calculates total kinetic energy
   - Monitors body count

## Configuration

Edit `config.py` to adjust:

```python
# Display
WIDTH, HEIGHT = 1200, 800  # Screen dimensions
FPS = 60                    # Frames per second

# Physics
G = 6.674e-11              # Gravitational constant
PLANET_MASS = 5e24         # Planet mass (kg)
STAR_MASS = 1.989e30       # Star mass (kg)

# Simulation
SCALE = 150 / AU           # Pixels per AU
TIMESTEP = 3600 * 24       # Seconds per frame

# Agent
AGENT_MAX_PLANETS = 15     # Maximum planets agent can create
```

## Physics Explained

### Orbital Velocity

For a circular orbit:
- The gravitational force provides the centripetal force
- `G * M * m / r² = m * v² / r`
- Solving for v: `v = sqrt(G * M / r)`

This is used by the agent to create stable orbits.

### Numerical Integration

The simulation uses basic Euler integration:

```
v_new = v_old + a * dt
x_new = x_old + v * dt
```

Where:
- **a** = F / m (acceleration from forces)
- **dt** = timestep (1 day in seconds)

### Precision & Scaling

To handle the vast distances in space:
- Physics calculations use real SI units (meters, kg, seconds)
- Display uses scaled coordinates (150 pixels per AU)
- Time is scaled (1 frame = 1 day)

This allows simulation of solar systems while keeping bodies visible.

## Advanced Features

### Dynamic Time Scaling

Use UP/DOWN arrows to change simulation speed:
- **UP**: Doubles timestep → 2x faster (less accurate)
- **DOWN**: Halves timestep → 2x slower (more accurate)

### Orbit Trails

Each body leaves a trail showing its path:
- Stored in `body.trail` list
- Limited to last 100 positions
- Useful for visualizing orbits

### Camera System

The renderer maintains a camera view:
- Centered on screen
- Can be extended to follow specific bodies
- Easy to pan/zoom in future versions

## Code Architecture

### Separation of Concerns

| Module | Responsibility |
|--------|-----------------|
| `config.py` | Constants and configuration |
| `body.py` | Individual celestial bodies |
| `physics_engine.py` | Forces and motion calculations |
| `renderer.py` | Visualization and drawing |
| `input_handler.py` | User input processing |
| `agent.py` | Autonomous decision-making |
| `main.py` | Application coordination |

### Design Patterns Used

1. **Observer Pattern**: Input handler → physics engine → rendering
2. **Composition**: Engine contains bodies, renderer draws bodies
3. **Encapsulation**: Each class manages its own state
4. **Abstraction**: Clean interfaces between modules

## Examples

### Create a Solar System

1. Press **G** to generate a galaxy
2. Press **S** several times to add planets
3. Watch planets orbit the central star

### Experiment with Orbits

1. Press **R** to reset
2. Create a large planet (star) with click-drag
3. Press **O** to create planets in orbit
4. Adjust speed with UP/DOWN arrows

### Create Custom System

1. Click and drag to create planets
2. Adjust their initial velocities by drag direction
3. Watch the gravitational interactions
4. Use UP/DOWN to slow down and observe orbits

## Limitations & Future Improvements

### Current Limitations
- No collision detection (bodies can pass through each other)
- Simple Euler integration (less accurate than RK4)
- No spatial acceleration (O(n²) complexity)
- Fixed camera view

### Possible Enhancements
1. **Collision System**: Merge bodies on contact
2. **Improved Integration**: Runge-Kutta 4th order
3. **Spatial Indexing**: Quadtree for performance
4. **Camera Control**: Follow bodies, zoom in/out
5. **File Saving**: Save/load planet systems
6. **Statistics Panel**: Real-time physics data
7. **Particle Effects**: Render enhancements
8. **Network Play**: Multiplayer simulation

## Performance Tips

For large numbers of bodies:
- Reduce trail length (edit `max_trail_length` in body.py)
- Increase timestep (press UP arrow)
- Reduce screen resolution (edit WIDTH/HEIGHT)
- Limit bodies with AGENT_MAX_PLANETS

## Troubleshooting

### "pygame not found"
```bash
pip install pygame
```

### Application runs slowly
- Press UP arrow to speed up simulation
- Press G to clear all bodies
- Reduce AGENT_MAX_PLANETS in config.py

### Planets moving too fast/slow
- Adjust TIMESTEP in config.py
- Or use UP/DOWN arrows during runtime

### Planets disappearing
- They may have moved far off-screen
- The camera is centered; extend with camera controls
- Press R to reset and try again

## Learning Resources

### Physics Concepts
- [Newton's Law of Gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation)
- [Orbital Mechanics](https://en.wikipedia.org/wiki/Orbital_mechanics)
- [Kepler's Laws](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion)

### Implementation Concepts
- [Numerical Integration](https://en.wikipedia.org/wiki/Numerical_integration)
- [Game Loop Architecture](https://en.wikipedia.org/wiki/Game_loop)
- [N-Body Problem](https://en.wikipedia.org/wiki/N-body_problem)

## License & Attribution

This project is provided as educational material. 
Feel free to modify, extend, and learn from it.

## Author Notes

This system demonstrates:
- Professional Python architecture
- Clean code principles
- Physics simulation accuracy
- Modular design patterns
- Real-time interactive systems
- AI agent decision-making

Use this as a template for more complex simulations and agent systems!

---

**Enjoy the simulation!** 🌍🚀🪐
