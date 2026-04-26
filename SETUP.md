# Quick Start Guide

## 30-Second Setup

### 1. Install Dependencies (First Time Only)
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python main.py
```

## That's It!

The application will launch with a random galaxy already generated. You can immediately start interacting:

- **Click and drag** on the screen to create planets
- **Press G** to generate a new galaxy
- **Press SPACE** to pause/unpause
- **Press R** to reset everything

## System Requirements

- **Python**: 3.8+
- **OS**: Windows, macOS, or Linux
- **RAM**: 512 MB minimum
- **GPU**: Not required

## File Structure

```
simulation/
├── main.py                 ← Run this file to start
├── config.py              ← Customize settings here
├── physics_engine.py      ← Gravity calculations
├── body.py                ← Planet class
├── renderer.py            ← Graphics/visualization
├── input_handler.py       ← Controls
├── agent.py               ← AI logic
├── requirements.txt       ← Dependencies
├── README.md              ← Full documentation
└── SETUP.md               ← This file
```

## Controls Reference

### Mouse
- **Click + Drag**: Create planet with velocity

### Keyboard
| Key | Function |
|-----|----------|
| SPACE | Pause/Unpause |
| R | Reset |
| G | Generate galaxy |
| S | Spawn planet |
| O | Create orbit |
| B | Binary system |
| ↑ | Speed up |
| ↓ | Slow down |

## Troubleshooting

### "ModuleNotFoundError: No module named 'pygame'"
```bash
pip install pygame
```

### Application crashes on startup
Make sure you're in the simulation directory:
```bash
cd c:\Users\ibroh\simulation
python main.py
```

### Planets moving too fast
Press DOWN arrow key several times to slow down the simulation.

## What to Try First

1. **Launch and observe** - Run the app, watch the generated galaxy
2. **Pause and explore** - Press SPACE to pause, look at the orbits
3. **Create planets** - Click and drag on screen to add your own planets
4. **Generate systems** - Press G for new galaxies, B for binary systems
5. **Speed control** - Use UP/DOWN arrows to adjust simulation speed

## Next Steps

- Read **README.md** for detailed documentation
- Edit **config.py** to customize physics parameters
- Explore the code to understand the architecture
- Modify **agent.py** to add new autonomous behaviors

## Need Help?

All code is heavily documented with comments and docstrings.
Check the README.md for detailed explanations of each module.

Happy simulating! 🚀
