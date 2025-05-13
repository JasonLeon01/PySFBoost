# PySFBoost
PySFBoost is a Python binding interface for SFML **3.0** , providing `.pyi` type hinting files to enhance the development experience when working with SFML in Python. This project is built on top of the PySFML CMake repository, which provides the core bindings for SFML.

## Overview
SFML (Simple and Fast Multimedia Library) is a popular open-source library designed to provide a simple interface for multimedia applications, including graphics, audio, and input handling. With PySFBoost , Python developers can leverage the power of SFML **3.0** while benefiting from modern Python features like type hints and static type checking.

This repository focuses on providing accurate and comprehensive `.pyi` stub files for the Python bindings of SFML **3.0**. These stub files are compatible with Python **3.10.0** and above, ensuring seamless integration with tools like IDEs and linters.

## Features
Type Annotations : Comprehensive type hints for all PySFML classes and methods.
- Type Hinting : Provides `.pyi` files for enhanced code completion, linting, and static type checking.
- Compatibility : Designed for Python **3.10.0** and works seamlessly with the PySFML bindings.
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

### **If you are using Windows**
```bash
git clone https://github.com/JasonLeon01/PySFML.git
cd PySFML
mkdir build && cd build
cmake -G "Visual Studio 17 2022" -A x64 ..
cmake --build . --config Release -- /m
```

### **If you are using macOS**
```bash
git clone https://github.com/JasonLeon01/PySFML.git
cd PySFML
mkdir build && cd build
cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DCMAKE_BUILD_TYPE=Release .. --trace-expand
cmake --build . -- -j$(sysctl -n hw.ncpu)
```

For video-related functionality, make sure the following dependencies are installed(Optional):

```bash
pip install opencv-python av
```

## Usage
Once installed, you can use PySFBoost to enhance your Python projects that rely on SFML. Here's an example of how to use SFML with type hints:

```python
from PySFBoost.sfGraphics import *
from PySFBoost.sfWindow import *
from PySFBoost.sfSystem import *

# Create a window with type hints
window: RenderWindow = RenderWindow(VideoMode(Vector2u(800, 600)), "pysf Test")

# Set the background color with type hints
background_color: Color = Color(50, 50, 50)

# Main loop
while window.is_open():
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
from PySFBoost.ResourceMgr import *

# Get a texture
texture = TextureMgr.block("grass.png")

# Get a font
font = FontMgr.get_font("arial.ttf")

# Play a sound
AudioMgr.play_sound("jump.wav")
```

## Using Particle System
```python
texture = TextureMgr.block("particle.png")
velocity = sfSystem.Vector2f(10, 10)
duration = sfSystem.Time.FromSeconds(5)
particle = Particle(texture, velocity, duration)
mgr = ParticleMgr()
mgr.add_particle(particle)
...
mgr.update(delta_time)
mgr.display(window)
...
```

## Using Animation System
```python
sprite = sfGraphics.Sprite(TextureMgr.block("sprite.png"))
duration = sfSystem.Time.FromSeconds(2)
event = Event(sprite, duration)

# Create an animation
animation_len = sfSystem.Time.FromSeconds(5)
animation_events = [(event, sfSystem.Time.Zero())]
animation = Animation(animation_len, animation_events)
mgr = AnimationMgr()
mgr.add_animation(animation)
...
mgr.update(delta_time)
mgr.display(window)
...
```

## Using Time Manager
```python
TimeMgr.init()
TimeMgr.update()
```

## Using Enhanced Text Rendering
```python
# Load a font
font = sfGraphics.Font.load_from_file("arial.ttf")

# Create a style configuration
style_config = StyleConfig(sfGraphics.Color.White, 24, 1.0, 1.5)

# Create an EText object
text = EText(font, r"\c[red]\s[24]Hello World!\c[white]\s[12] This is enhanced text.", sfSystem.Vector2u(800, 600), style_config)

# Render the text
text.render()

...
window.clear()
window.draw(text)
window.display()
...
```

## Using Video Player
To use this module, you need to install opencv-python.

By the way, the video is silent. You can play its back sound with other ways.
```python
from PySFBoost.Time import *
from PySFBoost.sfGraphics import *
from PySFBoost.sfWindow import *
from PySFBoost.sfSystem import *
from PySFBoost.Video import *
TimeMgr.init()
window: RenderWindow = RenderWindow(VideoMode(Vector2u(800, 600)), "pysf video Test")
window.set_framerate_limit(60)
video_player = Video("test.mp4", window)
video_player.play()
```

With PySFBoost , your IDE will provide autocompletion and type checking for all SFML classes and methods.

## Contributing
Contributions to PySFBoost are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and ensure the `.pyi` files are updated accordingly.
4. Submit a pull request with a detailed description of your changes.

## Third-Party Libraries
This project is a pybind11 binding for SFML (Simple and Fast Multimedia Library) and includes the following third-party libraries:

1. **SFML (Simple and Fast Multimedia Library)**
  - License: zlib/png License
  - Website: https://www.sfml-dev.org
  - License Text: [SFML License](https://www.sfml-dev.org/license.php)

2. OpenCV (Open Source Computer Vision Library)
  - License: Apache 2.0
  - Website: https://opencv.org/
  - License Text: Apache 2.0 License

3. PyAV(A Pythonic binding for the FFmpeg libraries.)
  - License: BSD-3-Clause license
  - Website: https://pyav.basswood-io.com/docs/stable/
  - License Text: BSD-3-Clause License

Website: https://ffmpeg.org/

License Text: FFmpeg Licensing


4. **SFML Dependencies**
   - stb_image and stb_image_write (Public Domain)
     - Website: https://github.com/nothings/stb
   - FreeType (FreeType License)
     - Website: https://www.freetype.org
     - License Text: [FreeType License](https://www.freetype.org/license.html)
   - libogg (BSD License)
     - Website: https://xiph.org/ogg/
     - License Text: [libogg License](https://xiph.org/licenses/bsd/)
   - libvorbis (BSD License)
     - Website: https://xiph.org/vorbis/
     - License Text: [libvorbis License](https://xiph.org/licenses/bsd/)
   - libflac (BSD License)
     - Website: https://xiph.org/flac/
     - License Text: [libflac License](https://xiph.org/licenses/bsd/)
   - minimp3 (CC0)
     - Website: https://github.com/lieff/minimp3
   - miniaudio (Public Domain or MIT No Attribution)
     - Website: https://miniaud.io
     - License Text: [miniaudio License](https://github.com/mackron/miniaudio/blob/master/LICENSE)

5. **PyAV Dependencies**
   - FFmpeg (FFmpeg Licensing)
     - Website: https://ffmpeg.org/
     - License Text: [FFmpeg Licensing](https://ffmpeg.org/legal.html)

## License
PySFBoost is licensed under the Zlib license. See the [LICENSE](license.md) file for more details.

## Acknowledgements
- [SFML](https://www.sfml-dev.org/): The core library that makes multimedia development simple and efficient.
- [PySFML](https://github.com/JasonLeon01/PySFML): The CMake-based Python bindings for SFML 3.0.
- [PyAV](https://pyav.basswood-io.com/docs/stable/): A Pythonic binding for the FFmpeg libraries.
