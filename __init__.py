"""
SFML provides a simple interface to the various components of your PC, to ease the development of games and multimedia applications. It is composed of five modules: system, window, graphics, audio and network.
"""

from . import sfSystem
from . import sfWindow
from . import sfGraphics
from . import sfAudio
from . import sfNetwork
from . import Particle
from . import ResourceMgr
from . import Time
from . import Animation

__all__ = [
    "sfSystem",
    "sfWindow",
    "sfGraphics",
    "sfAudio",
    "sfNetwork",
    "Particle",
    "ResourceMgr",
    "Time",
    "Animation"
]
