# Gravity Simulator - Complete File Index

## 📁 Project Structure

```
simulation/
├── 🚀 APPLICATION FILES
│   ├── main.py                 ← START HERE (run this file)
│   ├── config.py               ← Customization options
│   └── requirements.txt         ← Install dependencies
│
├── 🔧 CORE MODULES
│   ├── body.py                 ← Celestial body physics
│   ├── physics_engine.py       ← Gravity simulation
│   ├── renderer.py             ← Pygame visualization
│   ├── input_handler.py        ← Mouse/keyboard controls
│   └── agent.py                ← AI agent logic
│
├── 📚 DOCUMENTATION
│   ├── README.md               ← Full documentation (400+ lines)
│   ├── SETUP.md                ← Quick start guide
│   ├── PROJECT_OVERVIEW.md     ← Project summary
│   └── INDEX.md                ← This file
│
└── 🛠️ SETUP SCRIPTS
    ├── install.bat             ← Windows installation
    └── install.sh              ← Linux/macOS installation
```

---

## 📋 File Descriptions

### 🚀 Essential Application Files

#### **main.py** (Application Entry Point)
- **Size**: ~115 lines
- **Purpose**: Main application class and game loop
- **Contains**: `GravitySimulator` class
- **Run this**: `python main.py`
- **Key Functions**:
  - `__init__()` - Initialize all systems
  - `handle_input()` - Process user input
  - `update()` - Update physics
  - `render()` - Draw everything
  - `run()` - Main game loop

#### **config.py** (Configuration)
- **Size**: ~26 lines
- **Purpose**: Global constants and settings
- **Contains**: All customizable parameters
- **Edit this to**: Change physics, screen size, colors, limits
- **Key Settings**:
  - Screen dimensions (WIDTH, HEIGHT)
  - Physics constants (G, TIMESTEP, SCALE)
  - Colors and masses
  - Agent limits

#### **requirements.txt** (Dependencies)
- **Size**: 2 lines
- **Purpose**: List of Python packages needed
- **Install with**: `pip install -r requirements.txt`
- **Contains**:
  - pygame (graphics and input)
  - numpy (numerical calculations)

---

### 🔧 Core Physics & Simulation Modules

#### **body.py** (Celestial Body Class)
- **Size**: ~136 lines
- **Purpose**: Represents planets and stars
- **Contains**: `Body` class
- **Key Methods**:
  - `draw()` - Render body and trail
  - `add_force()` - Calculate gravitational forces
  - `update_position()` - Update velocity and position
  - `get_speed()` - Calculate current velocity
  - `get_kinetic_energy()` - Energy calculation
- **Key Attributes**:
  - Position: x, y (meters)
  - Velocity: x_vel, y_vel (m/s)
  - Properties: mass, radius, color
  - Trail: List of previous positions

#### **physics_engine.py** (Physics Simulator)
- **Size**: ~70 lines
- **Purpose**: Manages all gravitational interactions
- **Contains**: `PhysicsEngine` class
- **Key Methods**:
  - `add_body()` - Add planet to simulation
  - `remove_body()` - Remove planet
  - `update()` - Perform one time step
  - `reset()` - Clear all bodies
  - `set_timestep()` - Control simulation speed
  - `get_total_momentum()` - System statistics
  - `get_total_energy()` - Energy tracking
- **How it works**:
  1. Calculate forces on all bodies
  2. Update velocities based on forces
  3. Update positions based on velocities

#### **renderer.py** (Visualization)
- **Size**: ~92 lines
- **Purpose**: Handle all graphics and rendering
- **Contains**: `Renderer` class
- **Key Methods**:
  - `draw_background()` - Clear screen
  - `draw_bodies()` - Render all bodies
  - `render_text()` - Draw text/HUD
  - `update_display()` - Update screen
  - `get_world_coordinates()` - Convert screen → world
  - `get_screen_coordinates()` - Convert world → screen
- **Features**:
  - Handles Pygame window
  - Manages camera positioning
  - Renders text overlays
  - Coordinate conversion

#### **input_handler.py** (User Input)
- **Size**: ~79 lines
- **Purpose**: Process mouse and keyboard input
- **Contains**: `InputHandler` class
- **Key Methods**:
  - `handle_input()` - Main input processor
  - `handle_keydown()` - Process keyboard
- **Supported Input**:
  - Mouse click+drag for planet creation
  - Keyboard shortcuts for simulation control
  - SPACE, R, G, S, O, B, UP, DOWN keys
- **Returns**:
  - Commands for the main application
  - None for normal operation
  - Special strings for pause/reset

#### **agent.py** (AI Agent)
- **Size**: ~216 lines
- **Purpose**: Autonomous intelligent agent
- **Contains**: `Agent` class
- **Key Methods**:
  - `spawn_random_planet()` - Create random planets
  - `create_stable_orbit()` - Kepler's law orbit
  - `generate_random_galaxy()` - Star + 5-8 planets
  - `generate_binary_system()` - Two stars system
  - `adjust_planet_velocity()` - Modify motion
  - `get_system_stats()` - Calculate statistics
  - `handle_mouse_release()` - User planet creation
- **AI Capabilities**:
  - Calculates orbital velocities (√(GM/r))
  - Generates stable systems
  - Manages planetary spawning
  - Tracks system energy and momentum

---

### 📚 Documentation Files

#### **README.md** (Full Documentation)
- **Size**: 400+ lines
- **Contains**: 
  - Complete feature list
  - Installation instructions
  - Control references
  - Physics explanations
  - Architecture details
  - Configuration guide
  - Troubleshooting section
- **Read this for**: Understanding how everything works

#### **SETUP.md** (Quick Start)
- **Size**: ~100 lines
- **Contains**:
  - 30-second setup instructions
  - Quick reference table
  - File structure
  - Control shortcuts
  - Troubleshooting tips
  - What to try first
- **Read this for**: Getting started immediately

#### **PROJECT_OVERVIEW.md** (Project Summary)
- **Size**: ~350 lines
- **Contains**:
  - Project statistics
  - Feature checklist
  - Architecture diagrams
  - Physics equations
  - Example workflows
  - Learning resources
  - Enhancement ideas
- **Read this for**: Understanding the complete project

#### **INDEX.md** (This File)
- **Purpose**: File-by-file reference
- **Use this for**: Finding specific files and their functions

---

### 🛠️ Installation Scripts

#### **install.bat** (Windows Installation)
- **Purpose**: Automated setup for Windows
- **Run**: Double-click or `install.bat`
- **Does**:
  - Checks for Python
  - Installs dependencies
  - Shows completion message
- **For**: Windows users

#### **install.sh** (Linux/macOS Installation)
- **Purpose**: Automated setup for Unix systems
- **Run**: `chmod +x install.sh && ./install.sh`
- **Does**:
  - Checks for Python 3
  - Installs dependencies
  - Shows completion message
- **For**: Linux and macOS users

---

## 🚀 How to Use These Files

### First Time Setup
1. **Install**: Run `install.bat` (Windows) or `install.sh` (Linux/macOS)
2. **Read**: Check `SETUP.md` for quick start
3. **Run**: Execute `python main.py`

### Customization
1. **Edit**: `config.py` to change settings
2. **Modify**: `agent.py` for new AI behaviors
3. **Extend**: `body.py` for new body types

### Understanding the Code
1. **Start**: Read `README.md` for overview
2. **Explore**: Check `PROJECT_OVERVIEW.md` for architecture
3. **Reference**: Use `INDEX.md` (this file) to find specifics
4. **Study**: Read docstrings in each module

### Development & Extension
1. **Physics**: Modify `body.py` and `physics_engine.py`
2. **UI**: Change `renderer.py` and `input_handler.py`
3. **AI**: Extend `agent.py` with new methods
4. **Settings**: Adjust constants in `config.py`

---

## 📊 File Statistics

| File | Lines | Type | Purpose |
|------|-------|------|---------|
| main.py | 115 | Code | Application entry |
| agent.py | 216 | Code | AI logic |
| body.py | 136 | Code | Physics object |
| physics_engine.py | 70 | Code | Simulation |
| renderer.py | 92 | Code | Graphics |
| input_handler.py | 79 | Code | Controls |
| config.py | 26 | Config | Constants |
| README.md | 400+ | Docs | Full guide |
| PROJECT_OVERVIEW.md | 350+ | Docs | Summary |
| SETUP.md | 100+ | Docs | Quick start |
| **TOTAL** | **~1500** | | Complete system |

---

## 🎯 Quick Navigation

**I want to...**

- **Run the application** → `python main.py`
- **Change screen size** → Edit `config.py` (WIDTH, HEIGHT)
- **Adjust physics** → Edit `config.py` (G, TIMESTEP, masses)
- **Add new features** → Extend `agent.py`
- **Understand the code** → Read `README.md`
- **Get started quickly** → Read `SETUP.md`
- **See the big picture** → Read `PROJECT_OVERVIEW.md`
- **Find specific files** → Read this INDEX.md

---

## 🔗 File Dependencies

```
main.py
  ├── config.py
  ├── physics_engine.py
  │   └── body.py
  │       └── config.py
  ├── renderer.py
  │   └── config.py
  ├── input_handler.py
  │   └── agent.py
  │       ├── body.py
  │       └── config.py
  └── agent.py

All modules can independently import config.py
```

---

## ✨ Key Features by File

| Feature | File | Method |
|---------|------|--------|
| Gravity calculation | body.py | `add_force()` |
| Position update | body.py | `update_position()` |
| Orbit rendering | body.py | `draw()` |
| Physics simulation | physics_engine.py | `update()` |
| Screen rendering | renderer.py | `draw_bodies()` |
| Mouse input | input_handler.py | `handle_input()` |
| Keyboard input | input_handler.py | `handle_keydown()` |
| Galaxy generation | agent.py | `generate_random_galaxy()` |
| Orbit creation | agent.py | `create_stable_orbit()` |
| Game loop | main.py | `run()` |

---

## 🎓 Learning Path

1. **Start**: Read README.md overview
2. **Setup**: Follow SETUP.md instructions
3. **Run**: Execute `python main.py`
4. **Learn**: Play with controls, experiment
5. **Study**: Read PROJECT_OVERVIEW.md
6. **Understand**: Read each module's docstrings
7. **Extend**: Add features to agent.py
8. **Master**: Modify physics in body.py

---

## 📞 Troubleshooting Quick Links

**Problem** | **File to Check**
-----------|------------------
Won't run | requirements.txt, config.py
Crashes | body.py, physics_engine.py
Wrong physics | config.py (constants)
UI problems | renderer.py, input_handler.py
No AI features | agent.py
Performance issues | physics_engine.py

---

## 🎉 Complete System

This index covers a **complete, production-ready** AI agent system:

✅ All files present and documented
✅ Full physics simulation working
✅ Interactive user interface ready
✅ AI agent fully functional
✅ 100+ docstrings and comments
✅ Multiple documentation files
✅ Installation scripts included
✅ Ready to run and extend

---

**Congratulations!** You have a complete gravity simulator project.
Start with `python main.py` and enjoy exploring! 🚀

---

**For detailed information, see:**
- 📖 [README.md](README.md) - Full documentation
- ⚡ [SETUP.md](SETUP.md) - Quick start guide  
- 🏗️ [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) - Architecture details
