# PySFBoost
PySFBoost is a Python binding interface for SFML **3.0** , providing `.pyi` type hinting files to enhance the development experience when working with SFML in Python. This project is built on top of the PySFML CMake repository, which provides the core bindings for SFML.

## Overview
SFML (Simple and Fast Multimedia Library) is a popular open-source library designed to provide a simple interface for multimedia applications, including graphics, audio, and input handling. With PySFBoost , Python developers can leverage the power of SFML **3.0** while benefiting from modern Python features like type hints and static type checking.

This repository focuses on providing accurate and comprehensive `.pyi` stub files for the Python bindings of SFML **3.0**. These stub files are compatible with Python **3.9.0** and above, ensuring seamless integration with tools like IDEs and linters.

## Features
Type Annotations : Comprehensive type hints for all PySFML classes and methods.
- Type Hinting : Provides `.pyi` files for enhanced code completion, linting, and static type checking.
- Compatibility : Designed for Python **3.9.0** and works seamlessly with the PySFML bindings.
- Developer-Friendly : Improves the development workflow by offering clear and precise type annotations for SFML's Python API.
- **Resource Management**: Includes `TextureMgr`, `FontMgr`, and `AudioMgr` in `ResourceMgr.py` to manage textures, fonts, and audios efficiently.
- **Particle System**: The `Particle.py` file provides a particle system with `Particle` and `ParticleMgr` classes to manage particle behavior.
- **Animation System**: `Animation.py` offers an animation system with `Event`, `Animation`, and `AnimationMgr` classes to manage and display animations.
- **Time Management**: `Time.py` contains the `TimeMgr` class to handle time-related operations such as getting current time and delta time.
- **Enhanced Text Rendering**: The `TextEnhance.py` module provides a class `EText` for rendering enhanced text with various styles and configurations. It supports features such as bold, italic, underlined, strike-through text, custom colors, and custom sizes.

## Installation
To use PySFBoost, clone the repository.

```bash
git clone https://github.com/JasonLeon01/PySFBoost.git
```

If you want to compile the pyd files yourself, you can use [PySFML](https://github.com/JasonLeon01/PySFML) and run the cmake commands:

```bash
git clone https://github.com/JasonLeon01/PySFML.git
cd PySFML
mkdir build && cd build
cmake ..
make
```

## Usage
Once installed, you can use PySFBoost to enhance your Python projects that rely on SFML. Here's an example of how to use SFML with type hints:

```python
from PySFBoost import sfSystem, sfWindow, sfGraphics, sfAudio, sfNetwork

# Create a window with type hints
window: sfGraphics.RenderWindow = sfGraphics.RenderWindow(sfWindow.VideoMode(sfSystem.Vector2u(800, 600)), "pysf Test")

# Set the background color with type hints
background_color: sfGraphics.Color = sfGraphics.Color(50, 50, 50)

# Main loop
while window.is_open:
        while True:
            event = window.poll_event()
            if event is None:
                break
            if event.isClosed():
                window.close()
                break

    window.clear(background_color)
    window.display()
```

## Using Resource Managers
```python
from PySFBoost.ResourceMgr import TextureMgr, FontMgr, AudioMgr

# Get a texture
texture = TextureMgr.block("grass.png")

# Get a font
font = FontMgr.get_font("arial.ttf")

# Play a sound
AudioMgr.play_sound("jump.wav")
```

## Using Particle System
```python
from PySFBoost.Particle import Particle, ParticleMgr
from PySFBoost import sfGraphics, sfSystem

texture = TextureMgr.block("particle.png")
velocity = sfSystem.Vector2f(10, 10)
duration = sfSystem.Time.FromSeconds(5)
particle = Particle(texture, velocity, duration)
mgr = ParticleMgr()
mgr.add_particle(particle)
```

## Using Animation System
```python
from PySFBoost.Animation import Event, Animation, AnimationMgr
from PySFBoost import sfSystem, sfGraphics, sfAudio

# Create an event
sprite = sfGraphics.Sprite(TextureMgr.block("sprite.png"))
duration = sfSystem.Time.FromSeconds(2)
event = Event(sprite, duration)

# Create an animation
animation_len = sfSystem.Time.FromSeconds(5)
animation_events = [(event, sfSystem.Time.Zero())]
animation = Animation(animation_len, animation_events)
mgr = AnimationMgr()
mgr.add_animation(animation)
```

## Using Time Manager
```python
from PySFBoost.Time import TimeMgr

TimeMgr.init()
current_time = TimeMgr.get_current_time()
delta_time = TimeMgr.get_delta_time()
```

## Using Enhanced Text Rendering
```python
from PySFBoost.TextEnhance import EText, StyleConfig
from PySFBoost import sfSystem, sfGraphics

# Load a font
font = sfGraphics.Font.load_from_file("arial.ttf")

# Create a style configuration
style_config = StyleConfig(sfGraphics.Color.White, 24, 1.0, 1.5)

# Create an EText object
text = EText(font, r"\c[red]\s[24]Hello World!\c[white]\s[12] This is enhanced text.", sfSystem.Vector2u(800, 600), style_config)

# Render the text
text.render()

# Display the text on a window
window = sfGraphics.RenderWindow(sfWindow.VideoMode(sfSystem.Vector2u(800, 600)), "Enhanced Text Example")
while window.is_open:
    for event in window.poll_events():
        if event.type == sfWindow.Event.Closed:
            window.close()

    window.clear()
    text.display(window)
    window.display()
```

With PySFBoost , your IDE will provide autocompletion and type checking for all SFML classes and methods.

## Contributing
Contributions to PySFBoost are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and ensure the `.pyi` files are updated accordingly.
4. Submit a pull request with a detailed description of your changes.

## License
PySFBoost is licensed under the Zlib license. See the [LICENSE](license.md) file for more details.

## Acknowledgements
- [SFML](https://www.sfml-dev.org/): The core library that makes multimedia development simple and efficient.
- [PySFML](https://github.com/JasonLeon01/PySFML): The CMake-based Python bindings for SFML 3.0.
