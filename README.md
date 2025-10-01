# Alien Invasion Game (Python)

Practice project built with Python and [Pygame](https://www.pygame.org/) to recreate the classic Alien Invasion arcade shooter from *Python Crash Course*. The repo also includes a handful of small Python language exercises in `basic/` for reference.

## Repository Layout

- `alien_invasion/` – main game package (entry point, sprites, settings, art assets)
- `basic/` – stand-alone scripts used for Python fundamentals practice
- `README.md` – this guide

## Prerequisites

- Python 3.10+ (the code uses modern typing-friendly idioms but no 3.11-specific features)
- `pip` (comes with Python) and optionally `python -m venv` for isolated environments

> **macOS note:** The project has been tested on macOS using the system Python launcher (`python3`). On Linux/Windows replace `python3` with `python` as appropriate.

## Quick Start

```bash
# from the project root
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install pygame

python alien_invasion/alien_invasion.py
```

When the game window appears, steer with the arrow keys, press Space to fire bullets, and press `Q` to quit.

If you prefer a requirements file you can capture the environment once it works:

```bash
pip freeze > requirements.txt
```

Anyone cloning the project can then run `pip install -r requirements.txt` to reproduce your exact dependency set.

## Game Configuration

Runtime options live in `alien_invasion/settings.py`. Update the attributes below, then restart the game to apply the changes:

| Setting | Default | Effect |
|---------|---------|--------|
| `screen_width` | 1200 | Window width in pixels |
| `screen_height` | 800 | Window height in pixels |
| `bg_color` | `(230, 230, 230)` | Background RGB tuple |
| `ship_speed` | 1.5 | Player ship horizontal speed |
| `bullet_speed` | 2.0 | Vertical bullet speed |
| `bullet_width` | 3 | Bullet thickness in pixels |
| `bullet_height` | 15 | Bullet height in pixels |
| `bullet_color` | `(60, 60, 60)` | Bullet RGB color |
| `bullet_allowed` | 3 | Simultaneous bullets on screen |

For alternate setups, commit the tweaked `settings.py` alongside notes on the hardware (monitor resolution, refresh rate) to help others replicate the same feel. Keep `images/ship.bmp` in place or update `ship.py` to load your custom sprite.

## Development Tips

- Use `python -m pygame.examples.aliens` to confirm Pygame installed correctly if the game fails to open a window.
- The main loop caps the frame rate at 60 FPS via `pygame.time.Clock`; adjust there if you experiment with higher refresh rates.
- To package or distribute, consider freezing dependencies (`pip freeze`) and shipping the `images/` assets with the script.

## Next Steps

- Expand gameplay by adding aliens (see later chapters in the book for guidance).
- Add automated tests around settings or sprite helpers with `pytest` if you want regression coverage.
- Document any new modules here so others know how to run them.
