"""
Provides OpenGL-based windows, and abstractions for events and input handling.
"""

# pylint: disable=unused-argument
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=invalid-name

from __future__ import annotations
import enum
from typing import List, overload
from types import ModuleType
from . import sfSystem

class Style(ModuleType):
    """
    Enumeration of the window styles.
    - Empty: No border / title bar (this flag and all others are mutually exclusive).
    - TitlebarTitle: bar + fixed border.
    - ResizeTitle: bar + resizable border + maximize button.
    - CloseTitle: bar + close button.

    Default: Default window style.
    """
    Empty = 0
    Titlebar = 1 << 0
    Resize = 1 << 1
    Close = 1 << 2
    Default = Titlebar | Resize | Close

class State(enum.IntEnum):
    """
    Enumeration of the window states.
    - Windowed: Floating window.
    - Fullscreen: Fullscreen window.
    """
    Windowed = 0
    Fullscreen = 1

class Context:
    """
    Class holding a valid drawing context.

    If you need to make OpenGL calls without having an active window (like in a thread), you can use an instance of this class to get a valid context.

    Having a valid context is necessary for every OpenGL call.

    Note that a context is only active in its current thread, if you create a new thread it will have no valid context by default.

    To use a Context instance, just construct it and let it live as long as you need a valid context. No explicit activation is needed, all it has to do is to exist. Its destructor will take care of deactivating and freeing all the attached resources.
    """
    def __init__(self, settings: ContextSettings, size: sfSystem.Vector2u) -> None:
        """
        Construct a in-memory context.

        This constructor is for internal use, you don't need to bother with it.

        Parameters
        - settings: Creation parameters
        - size: Back buffer size
        """

    def set_active(self, active: bool = True) -> None:
        """
        Activate or deactivate explicitly the context.

        Parameters

        - active: true to activate, false to deactivate
        Returns

        - true on success, false on failure
        """

    def get_settings(self) -> ContextSettings:
        """
        Get the settings of the context.

        Note that these settings may be different than the ones passed to the constructor; they are indeed adjusted if the original settings are not directly supported by the system.

        Returns
        - Structure containing the settings
        """

class ContextSettings:
    """
    Structure defining the settings of the OpenGL context attached to a window.

    ContextSettings allows to define several advanced settings of the OpenGL context attached to a window.

    All these settings with the exception of the compatibility flag and anti-aliasing level have no impact on the regular SFML rendering (graphics module), so you may need to use this structure only if you're using SFML as a windowing system for custom OpenGL rendering.

    The depthBits and stencilBits members define the number of bits per pixel requested for the (respectively) depth and stencil buffers.

    antiAliasingLevel represents the requested number of multisampling levels for anti-aliasing.

    majorVersion and minorVersion define the version of the OpenGL context that you want. Only versions greater or equal to 3.0 are relevant; versions lesser than 3.0 are all handled the same way (i.e. you can use any version < 3.0 if you don't want an OpenGL 3 context).

    When requesting a context with a version greater or equal to 3.2, you have the option of specifying whether the context should follow the core or compatibility profile of all newer (>= 3.2) OpenGL specifications. For versions 3.0 and 3.1 there is only the core profile. By default a compatibility context is created. You only need to specify the core flag if you want a core profile context to use with your own OpenGL rendering. Warning: The graphics module will not function if you request a core profile context. Make sure the attributes are set to Default if you want to use the graphics module.

    Setting the debug attribute flag will request a context with additional debugging features enabled. Depending on the system, this might be required for advanced OpenGL debugging. OpenGL debugging is disabled by default.

    Special Note for macOS: Apple only supports choosing between either a legacy context (OpenGL 2.1) or a core context (OpenGL version depends on the operating system version but is at least 3.2). Compatibility contexts are not supported. Further information is available on the OpenGL Capabilities Tables page. macOS also currently does not support debug contexts.

    Please note that these values are only a hint. No failure will be reported if one or more of these values are not supported by the system; instead, SFML will try to find the closest valid match. You can then retrieve the settings that the window actually used to create its context, with Window::getSettings().
    """

    class Attribute(enum.IntEnum):
        """
        Enumeration of the context attribute flags.
        - Default: Non-debug, compatibility context (this and the core attribute are mutually exclusive)
        - Core: Core attribute.
        - Debug: Debug attribute.
        """
        Default = 0
        Core = 1 << 0
        Debug = 1 << 2

    depthBits: int
    stencilBits: int
    antiAliasingLevel: int
    majorVersion: int
    minorVersion: int
    attributeFlags: int
    sRgbCapable: bool

    def __init__(self) -> None:
        """
        Initializes the ContextSettings object.
        """


class Cursor:
    """
    Cursor defines the appearance of a system cursor.

    Warning

    Features related to Cursor are not supported on iOS and Android.

    This class abstracts the operating system resources associated with either a native system cursor or a custom cursor.

    After loading the cursor graphical appearance with either createFromPixels() or createFromSystem(), the cursor can be changed with sf::WindowBase::setMouseCursor().

    The behavior is undefined if the cursor is destroyed while in use by the window.
    """

    class Type(enum.IntEnum):
        """
        Enumeration of the native system cursor types.

        Refer to the following table to determine which cursor is available on which platform.

        Type	Linux	macOS	Windows

        sf::Cursor::Type::Arrow                 	yes	yes	    yes

        sf::Cursor::Type::ArrowWait             	no	no	    yes

        sf::Cursor::Type::Wait                  	yes	no	    yes

        sf::Cursor::Type::Text                  	yes	yes	    yes

        sf::Cursor::Type::Hand                  	yes	yes	    yes

        sf::Cursor::Type::SizeHorizontal        	yes	yes	    yes

        sf::Cursor::Type::SizeVertical          	yes	yes	    yes

        sf::Cursor::Type::SizeTopLeftBottomRight	no	yes*	yes

        sf::Cursor::Type::SizeBottomLeftTopRight	no	yes*	yes

        sf::Cursor::Type::SizeLeft              	yes	yes**	yes**

        sf::Cursor::Type::SizeRight             	yes	yes**	yes**

        sf::Cursor::Type::SizeTop               	yes	yes**	yes**

        sf::Cursor::Type::SizeBottom            	yes	yes**	yes**

        sf::Cursor::Type::SizeTopLeft           	yes	yes**	yes**

        sf::Cursor::Type::SizeTopRight          	yes	yes**	yes**

        sf::Cursor::Type::SizeBottomLeft        	yes	yes**	yes**

        sf::Cursor::Type::SizeBottomRight       	yes	yes**	yes**

        sf::Cursor::Type::SizeAll               	yes	no	    yes

        sf::Cursor::Type::Cross                 	yes	yes	    yes

        sf::Cursor::Type::Help                  	yes	yes*	yes

        sf::Cursor::Type::NotAllowed            	yes	yes	    yes

        These cursor types are undocumented so may not be available on all versions, but have been tested on 10.13

        ** On Windows and macOS, double-headed arrows are used

        - Arrow: Arrow cursor (default)
        - ArrowWait: Busy arrow cursor.
        - Wait: Busy cursor.
        - Text: I-beam, cursor when hovering over a field allowing text entry.
        - Hand: Pointing hand cursor.
        - SizeHorizontal: Horizontal double arrow cursor.
        - SizeVertical: Vertical double arrow cursor.
        - SizeTopLeftBottomRight: Double arrow cursor going from top-left to bottom-right.
        - SizeBottomLeftTopRight: Double arrow cursor going from bottom-left to top-right.
        - SizeLeft: Left arrow cursor on Linux, same as SizeHorizontal on other platforms.
        - SizeRight: Right arrow cursor on Linux, same as SizeHorizontal on other platforms.
        - SizeTop: Up arrow cursor on Linux, same as SizeVertical on other platforms.
        - SizeBottom: Down arrow cursor on Linux, same as SizeVertical on other platforms.
        - SizeTopLeft: Top-left arrow cursor on Linux, same as SizeTopLeftBottomRight on other platforms.
        - SizeBottomRight: Bottom-right arrow cursor on Linux, same as SizeTopLeftBottomRight on other platforms.
        - SizeBottomLeft: Bottom-left arrow cursor on Linux, same as SizeBottomLeftTopRight on other platforms.
        - SizeTopRight: Top-right arrow cursor on Linux, same as SizeBottomLeftTopRight on other platforms.
        - SizeAll: Combination of SizeHorizontal and SizeVertical.
        - Cross: Crosshair cursor.
        - Help: Help cursor.
        - NotAllowed: Action not allowed cursor.
        """
        Arrow = 0
        ArrowWait = 1
        Wait = 2
        Text = 3
        Hand = 4
        SizeHorizontal = 5
        SizeVertical = 6
        SizeTopLeftBottomRight = 7
        SizeBottomLeftTopRight = 8
        SizeLeft = 9
        SizeRight = 10
        SizeTop = 11
        SizeBottom = 12
        SizeTopLeft = 13
        SizeTopRight = 14
        SizeBottomLeft = 15
        SizeBottomRight = 16
        SizeAll = 17
        Cross = 18
        Help = 19
        NotAllowed = 20

    @overload
    def __init__(self, type_: Type) -> None:
        """
        Create a native system cursor.

        Refer to the list of cursor available on each system (see sf::Cursor::Type) to know whether a given cursor is expected to load successfully or is not supported by the operating system.

        Parameters
        - type_: Native system cursor type

        Exceptions
        - sf::Exception: if the corresponding cursor is not natively supported by the operating system
        """

    @overload
    def __init__(self, pixels: bytes, size: sfSystem.Vector2u, hotspot: sfSystem.Vector2u) -> None:
        """
        Construct a cursor with the provided image.

        pixels must be an array of size pixels in 32-bit RGBA format. If not, this will cause undefined behavior.

        If pixels is nullptr or either of size's properties are 0, the current cursor is left unchanged and the function will return false.

        In addition to specifying the pixel data, you can also specify the location of the hotspot of the cursor. The hotspot is the pixel coordinate within the cursor image which will be located exactly where the mouse pointer position is. Any mouse actions that are performed will return the window/screen location of the hotspot.

        Warning

        On Unix platforms which do not support colored cursors, the pixels are mapped into a monochrome bitmap: pixels with an alpha channel to 0 are transparent, black if the RGB channel are close to zero, and white otherwise.

        Parameters
        - pixels: Array of pixels of the image
        - size: Width and height of the image
        - hotspot	(x,y): location of the hotspot

        Exceptions
        - sf::Exception: if the cursor could not be constructed
        """

    def createFromPixels(self, pixels: bytes, size: sfSystem.Vector2u) -> bool:
        """
        Creates a cursor from an array of pixel data.

        :param pixels: Array of pixel data.
        :param size: Size of the cursor.
        :return: True if creation is successful, False otherwise.
        """

    def createFromSystem(self) -> bool:
        """
        Creates a cursor using system resources.
        """

class Event:
    """
    Defines a system event and its parameters.

    sf::Event holds all the information about a system event that just happened.

    Events are retrieved using the sf::Window::pollEvent and sf::Window::waitEvent functions.

    A sf::Event instance contains the subtype of the event (mouse moved, key pressed, window closed, pass) as well as the details about this particular event. Each event corresponds to a different subtype struct which contains the data required to process that event.

    Event subtypes are event types belonging to sf::Event, such as sf::Event::Closed or sf::Event::MouseMoved.

    The way to access the current active event subtype is via sf::Event::getIf. This member function returns the address of the event subtype struct if the event subtype matches the active event, otherwise it returns nullptr.

    sf::Event::is is used to check the active event subtype without actually reading any of the corresponding event data.
    """

    # Event subclasses for specific event types
    class Closed:
        """
        Closed event.
        """
    class Resized:
        """
        Resized event.
        """
        size: sfSystem.Vector2u
    class FocusLost:
        """
        Focus lost event.
        """
    class FocusGained:
        """
        Focus gained event.
        """
    class TextEntered:
        """
        Text entered event.
        """
        unicode: str
    class KeyPressed:
        """
        Key pressed event.
        """
        code: Keyboard.Key
        scancode: Keyboard.Scan
        alt: bool
        control: bool
        shift: bool
        system: bool
    class KeyReleased:
        """
        Key released event.
        """
        code: Keyboard.Key
        scancode: Keyboard.Scan
        alt: bool
        control: bool
        shift: bool
        system: bool
    class MouseWheelScrolled:
        """
        Mouse wheel scrolled event.
        """
        wheel: Mouse.Wheel
        delta: float
        position: sfSystem.Vector2i
    class MouseButtonPressed:
        """
        Mouse button pressed event.
        """
        button: Mouse.Button
        position: sfSystem.Vector2i
    class MouseButtonReleased:
        """
        Mouse button released event.
        """
        button: Mouse.Button
        position: sfSystem.Vector2i
    class MouseMoved:
        """
        Mouse moved event.
        """
        position: sfSystem.Vector2i
    class MouseMovedRaw:
        """
        Mouse moved event (raw).
        """
        delta: sfSystem.Vector2i
    class MouseEntered:
        """
        Mouse entered event.
        """
    class MouseLeft:
        """
        Mouse left event.
        """
    class JoystickButtonPressed:
        """
        Joystick button pressed event.
        """
        joystick_id: int
        button: int
    class JoystickButtonReleased:
        """
        Joystick button released event.
        """
        joystick_id: int
        button: int
    class JoystickMoved:
        """
        Joystick moved event.
        """
        joystick_id: int
        axis: Joystick.Axis
        position: float
    class JoystickConnected:
        """
        Joystick connected event.
        """
        joystick_id: int
    class JoystickDisconnected:
        """
        Joystick disconnected event.
        """
        joystick_id: int
    class TouchBegan:
        """
        Touch began event.
        """
        finger: int
        position: sfSystem.Vector2i
    class TouchMoved:
        """
        Touch moved event.
        """
        finger: int
        position: sfSystem.Vector2i
    class TouchEnded:
        """
        Touch ended event.
        """
        finger: int
        position: sfSystem.Vector2i
    class SensorChanged:
        """
        Sensor changed event.
        """
        sensor_type: Sensor.Type
        value: sfSystem.Vector3f

    def __init__(self, event_type: Event) -> None:
        """
        Construct from a given sf::Event subtype.
        """

    def isClosed(self) -> bool:
        """
        Judge whether the event is a closed event.

        Returns
        - True if the event is a closed event, false otherwise.
        """
    def isResized(self) -> bool:
        """
        Judge whether the event is a resized event.

        Returns
        - True if the event is a resized event, false otherwise.
        """
    def isFocusLost(self) -> bool:
        """
        Judge whether the event is a focus lost event.

        Returns
        - True if the event is a focus lost event, false otherwise.
        """
    def isFocusGained(self) -> bool:
        """
        Judge whether the event is a focus gained event.

        Returns
        - True if the event is a focus gained event, false otherwise.
        """
    def isTextEntered(self) -> bool:
        """
        Judge whether the event is a text entered event.

        Returns
        - True if the event is a text entered event, false otherwise.
        """
    def isKeyPressed(self) -> bool:
        """
        Judge whether the event is a key pressed event.

        Returns
        - True if the event is a key pressed event, false otherwise.
        """
    def isKeyReleased(self) -> bool:
        """
        Judge whether the event is a key released event.

        Returns
        - True if the event is a key released event, false otherwise.
        """
    def isMouseWheelScrolled(self) -> bool:
        """
        Judge whether the event is a mouse wheel scrolled event.

        Returns
        - True if the event is a mouse wheel scrolled event, false otherwise.
        """
    def isMouseButtonPressed(self) -> bool:
        """
        Judge whether the event is a mouse button pressed event.

        Returns
        - True if the event is a mouse button pressed event, false otherwise.
        """
    def isMouseButtonReleased(self) -> bool:
        """
        Judge whether the event is a mouse button released event.

        Returns
        - True if the event is a mouse button released event, false otherwise.
        """
    def isMouseMoved(self) -> bool:
        """
        Judge whether the event is a mouse moved event.

        Returns
        - True if the event is a mouse moved event, false otherwise.
        """
    def isMouseMovedRaw(self) -> bool:
        """
        Judge whether the event is a mouse moved event (raw).

        Returns
        - True if the event is a mouse moved event (raw), false otherwise.
        """
    def isMouseEntered(self) -> bool:
        """
        Judge whether the event is a mouse entered event.

        Returns
        - True if the event is a mouse entered event, false otherwise.
        """
    def isMouseLeft(self) -> bool:
        """
        Judge whether the event is a mouse left event.

        Returns
        - True if the event is a mouse left event, false otherwise.
        """
    def isJoystickButtonPressed(self) -> bool:
        """
        Judge whether the event is a joystick button pressed event.

        Returns
        - True if the event is a joystick button pressed event, false otherwise.
        """
    def isJoystickButtonReleased(self) -> bool:
        """
        Judge whether the event is a joystick button released event.

        Returns
        - True if the event is a joystick button released event, false otherwise.
        """
    def isJoystickMoved(self) -> bool:
        """
        Judge whether the event is a joystick moved event.

        Returns
        - True if the event is a joystick moved event, false otherwise.
        """
    def isJoystickConnected(self) -> bool:
        """
        Judge whether the event is a joystick connected event.

        Returns
        - True if the event is a joystick connected event, false otherwise.
        """
    def isJoystickDisconnected(self) -> bool:
        """
        Judge whether the event is a joystick disconnected event.

        Returns
        - True if the event is a joystick disconnected event, false otherwise.
        """
    def isTouchBegan(self) -> bool:
        """
        Judge whether the event is a touch began event.

        Returns
        - True if the event is a touch began event, false otherwise.
        """
    def isTouchMoved(self) -> bool:
        """
        Judge whether the event is a touch moved event.

        Returns
        - True if the event is a touch moved event, false otherwise.
        """
    def isTouchEnded(self) -> bool:
        """
        Judge whether the event is a touch ended event.

        Returns
        - True if the event is a touch ended event, false otherwise.
        """
    def isSensorChanged(self) -> bool:
        """
        Judge whether the event is a sensor changed event.

        Returns
        - True if the event is a sensor changed event, false otherwise.
        """
    def getIfClosed(self) -> Closed:
        """
        Get the closed event if the event is a closed event.

        Returns
        - The closed event if the event is a closed event, nullptr otherwise.
        """
    def getIfResized(self) -> Resized:
        """
        Get the resized event if the event is a resized event.

        Returns
        - The resized event if the event is a resized event, nullptr otherwise.
        """
    def getIfFocusLost(self) -> FocusLost:
        """
        Get the focus lost event if the event is a focus lost event.

        Returns
        - The focus lost event if the event is a focus lost event, nullptr otherwise.
        """
    def getIfFocusGained(self) -> FocusGained:
        """
        Get the focus gained event if the event is a focus gained event.

        Returns
        - The focus gained event if the event is a focus gained event, nullptr otherwise.
        """
    def getIfTextEntered(self) -> TextEntered:
        """
        Get the text entered event if the event is a text entered event.

        Returns
        - The text entered event if the event is a text entered event, nullptr otherwise.
        """
    def getIfKeyPressed(self) -> KeyPressed:
        """
        Get the key pressed event if the event is a key pressed event.

        Returns
        - The key pressed event if the event is a key pressed event, nullptr otherwise.
        """
    def getIfKeyReleased(self) -> KeyReleased:
        """
        Get the key released event if the event is a key released event.

        Returns
        - The key released event if the event is a key released event, nullptr otherwise.
        """
    def getIfMouseWheelScrolled(self) -> MouseWheelScrolled:
        """
        Get the mouse wheel scrolled event if the event is a mouse wheel scrolled event.

        Returns
        - The mouse wheel scrolled event if the event is a mouse wheel scrolled event, nullptr otherwise.
        """
    def getIfMouseButtonPressed(self) -> MouseButtonPressed:
        """
        Get the mouse button pressed event if the event is a mouse button pressed event.

        Returns
        - The mouse button pressed event if the event is a mouse button pressed event, nullptr otherwise.
        """
    def getIfMouseButtonReleased(self) -> MouseButtonReleased:
        """
        Get the mouse button released event if the event is a mouse button released event.

        Returns
        - The mouse button released event if the event is a mouse button released event, nullptr otherwise.
        """
    def getIfMouseMoved(self) -> MouseMoved:
        """
        Get the mouse moved event if the event is a mouse moved event.

        Returns
        - The mouse moved event if the event is a mouse moved event, nullptr otherwise.
        """
    def getIfMouseMovedRaw(self) -> MouseMovedRaw:
        """
        Get the mouse moved event (raw) if the event is a mouse moved event (raw).

        Returns
        - The mouse moved event (raw) if the event is a mouse moved event (raw), nullptr otherwise.
        """
    def getIfMouseEntered(self) -> MouseEntered:
        """
        Get the mouse entered event if the event is a mouse entered event.

        Returns
        - The mouse entered event if the event is a mouse entered event, nullptr otherwise.
        """
    def getIfMouseLeft(self) -> MouseLeft:
        """
        Get the mouse left event if the event is a mouse left event.

        Returns
        - The mouse left event if the event is a mouse left event, nullptr otherwise.
        """
    def getIfJoystickButtonPressed(self) -> JoystickButtonPressed:
        """
        Get the joystick button pressed event if the event is a joystick button pressed event.

        Returns
        - The joystick button pressed event if the event is a joystick button pressed event, nullptr otherwise.
        """
    def getIfJoystickButtonReleased(self) -> JoystickButtonReleased:
        """
        Get the joystick button released event if the event is a joystick button released event.

        Returns
        - The joystick button released event if the event is a joystick button released event, nullptr otherwise.
        """
    def getIfJoystickMoved(self) -> JoystickMoved:
        """
        Get the joystick moved event if the event is a joystick moved event.

        Returns
        - The joystick moved event if the event is a joystick moved event, nullptr otherwise.
        """
    def getIfJoystickConnected(self) -> JoystickConnected:
        """
        Get the joystick connected event if the event is a joystick connected event.

        Returns
        - The joystick connected event if the event is a joystick connected event, nullptr otherwise.
        """
    def getIfJoystickDisconnected(self) -> JoystickDisconnected:
        """
        Get the joystick disconnected event if the event is a joystick disconnected event.

        Returns
        - The joystick disconnected event if the event is a joystick disconnected event, nullptr otherwise.
        """
    def getIfTouchBegan(self) -> TouchBegan:
        """
        Get the touch began event if the event is a touch began event.

        Returns
        - The touch began event if the event is a touch began event, nullptr otherwise.
        """
    def getIfTouchMoved(self) -> TouchMoved:
        """
        Get the touch moved event if the event is a touch moved event.

        Returns
        - The touch moved event if the event is a touch moved event, nullptr otherwise.
        """
    def getIfTouchEnded(self) -> TouchEnded:
        """
        Get the touch ended event if the event is a touch ended event.

        Returns
        - The touch ended event if the event is a touch ended event, nullptr otherwise.
        """
    def getIfSensorChanged(self) -> SensorChanged:
        """
        Get the sensor changed event if the event is a sensor changed event.

        Returns
        - The sensor changed event if the event is a sensor changed event, nullptr otherwise.
        """

class VideoMode:
    """
    VideoMode defines a video mode (size, bpp)

    A video mode is defined by a width and a height (in pixels) and a depth (in bits per pixel).

    Video modes are used to setup windows (sf::Window) at creation time.

    The main usage of video modes is for fullscreen mode: indeed you must use one of the valid video modes allowed by the OS (which are defined by what the monitor and the graphics card support), otherwise your window creation will just fail.

    sf::VideoMode provides a static function for retrieving the list of all the video modes supported by the system: getFullscreenModes().

    A custom video mode can also be checked directly for fullscreen compatibility with its isValid() function.

    Additionally, sf::VideoMode provides a static function to get the mode currently used by the desktop: getDesktopMode(). This allows to build windows with the same size or pixel depth as the current resolution.
    """

    size: sfSystem.Vector2u
    bits_per_pixel: int

    def __init__(self, modeSize: sfSystem.Vector2u, modeBitsPerPixel: int = 32) -> None:
        """
        Construct the video mode with its attributes.

        Parameters
        - modeSize: Width and height in pixels.
        - modeBitsPerPixel: Pixel depths in bits per pixel.

        """

    @staticmethod
    def get_desktop_mode() -> VideoMode:
        """
        Get the current desktop video mode.

        Returns
        - Current desktop video mode
        """

    @staticmethod
    def get_fullscreen_modes() -> List[VideoMode]:
        """
        Retrieve all the video modes supported in fullscreen mode.

        When creating a fullscreen window, the video mode is restricted to be compatible with what the graphics driver and monitor support. This function returns the complete list of all video modes that can be used in fullscreen mode. The returned array is sorted from best to worst, so that the first element will always give the best mode (higher width, height and bits-per-pixel).

        Returns
        - Array containing all the supported fullscreen modes
        """

    def isValid(self) -> bool:
        """
        Tell whether or not the video mode is valid.

        The validity of video modes is only relevant when using fullscreen windows; otherwise any video mode can be used with no restriction.

        Returns
        - true if the video mode is valid for fullscreen mode
        """

class WindowBase:
    """
    Window that serves as a base for other windows.

    sf::WindowBase serves as the base class for all Windows.

    A sf::WindowBase can create its own new window, or be embedded into an already existing control using the create(handle) function.

    The sf::WindowBase class provides a simple interface for manipulating the window: move, resize, show/hide, control mouse cursor, etc. It also provides event handling through its pollEvent() and waitEvent() functions.
    """

    def __init__(self, mode: VideoMode, title: str, style: int = Style.Default, state: State = State.Windowed):
        """
        Construct a new window.

        This constructor creates the window with the size and pixel depth defined in mode. An optional style can be passed to customize the look and behavior of the window (borders, title bar, resizable, closable, pass). An optional state can be provided. If state is State::Fullscreen, then mode must be a valid video mode.

        Parameters
        - mode: Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title: Title of the window
        - style: Window style, a bitwise OR combination of sf::Style enumerators
        - state: Window state
        """

    @overload
    def create(self, mode: VideoMode, title: str, style: int = Style.Default, state: State = State.Windowed) -> None:
        """
        Create (or recreate) the window.

        If the window was already created, it closes it first. If state is State::Fullscreen, then mode must be a valid video mode.

        Parameters
        - mode	Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title	Title of the window
        - style	Window style, a bitwise OR combination of sf::Style enumerators
        - state	Window state

        - Reimplemented in sf::Window.
        """

    @overload
    def create(self, mode: VideoMode, title: str, state: State) -> None:
        """
        Create (or recreate) the window.

        If the window was already created, it closes it first. If state is State::Fullscreen, then mode must be a valid video mode.

        Parameters
        - mode	Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title	Title of the window
        - state	Window state

        - Reimplemented in sf::Window.
        """

    def is_open(self) -> bool:
        """
        Tell whether or not the window is open.

        This function returns whether or not the window exists. Note that a hidden window (setVisible(false)) is open (therefore this function would return true).

        Returns
        - true if the window is open, false if it has been closed
        """

    def close(self) -> None:
        """
        Close the window and destroy all the attached resources.

        After calling this function, the sf::Window instance remains valid and you can call create() to recreate the window. All other functions such as pollEvent() or display() will still work (i.e. you don't have to test isOpen() every time), and will have no effect on closed windows.

        Reimplemented in sf::Window.
        """

    def poll_event(self) -> Event:
        """
        Pop the next event from the front of the FIFO event queue, if any, and return it.

        This function is not blocking: if there's no pending event then it will return a std::nullopt. Note that more than one event may be present in the event queue, thus you should always call this function in a loop to make sure that you process every pending event.

        Returns
        - The event, otherwise std::nullopt if no events are pending
        """

    def wait_event(self, timeout: sfSystem.Time = 0) -> Event:
        """
        Wait for an event and return it.

        This function is blocking: if there's no pending event then it will wait until an event is received or until the provided timeout elapses. Only if an error or a timeout occurs the returned event will be std::nullopt. This function is typically used when you have a thread that is dedicated to events handling: you want to make this thread sleep as long as no new event is received.

        Parameters
        - timeout	Maximum time to wait (Time::Zero for infinite)

        Returns
        - The event, otherwise std::nullopt on timeout or if window was closed
        """

    def get_position(self) -> sfSystem.Vector2i:
        """
        Get the position of the window.

        Returns
        - Position of the window, in pixels

        """

    def set_position(self, position: sfSystem.Vector2i) -> None:
        """
        Change the position of the window on screen.

        This function only works for top-level windows (i.e. it will be ignored for windows created from the handle of a child window/control).

        Parameters
        - position	New position, in pixels

        """

    def get_size(self) -> sfSystem.Vector2u:
        """
        Get the size of the rendering region of the window.

        The size doesn't include the titlebar and borders of the window.

        Returns
        - Size in pixels
        """

    def set_size(self, size: sfSystem.Vector2u) -> None:
        """
        Change the size of the rendering region of the window.

        Parameters
        - size	New size, in pixels

        """

    def set_minimum_size(self, minimumSize: sfSystem.Vector2u | None) -> None:
        """
        Set the minimum window rendering region size.

        Pass std::nullopt to unset the minimum size

        Parameters
        - minimumSize	New minimum size, in pixels

        """

    def set_maximum_size(self, maximumSize: sfSystem.Vector2u | None) -> None:
        """
        Set the maximum window rendering region size.

        Pass std::nullopt to unset the maximum size

        Parameters
        - maximumSize	New maximum size, in pixels
        """

    def set_title(self, title: str) -> None:
        """
        Change the title of the window.

        Parameters
        - title	New title

        """

    def set_icon(self, size: sfSystem.Vector2u, pixels: bytes) -> None:
        """
        Change the window's icon.

        pixels must be an array of size pixels in 32-bits RGBA format.

        The OS default icon is used by default.

        Parameters
        size	Icon's width and height, in pixels
        pixels	Pointer to the array of pixels in memory. The pixels are copied, so you need not keep the source alive after calling this function.
        """

    def set_visible(self, visible: bool) -> None:
        """
        Show or hide the window.

        The window is shown by default.

        Parameters
        - visible	true to show the window, false to hide it

        """

    def set_mouse_cursor_visible(self, visible: bool) -> None:
        """
        Show or hide the mouse cursor.

        The mouse cursor is visible by default.

        Warning

        On Windows, this function needs to be called from the thread that created the window.

        Parameters
        - visible	true to show the mouse cursor, false to hide it

        """

    def set_mouse_cursor_grabbed(self, grabbed: bool) -> None:
        """
        Grab or release the mouse cursor.

        If set, grabs the mouse cursor inside this window's client area so it may no longer be moved outside its bounds. Note that grabbing is only active while the window has focus.

        Parameters
        - grabbed	true to enable, false to disable
        """

    def set_mouse_cursor(self, cursor: Cursor) -> None:
        """
        Set the displayed cursor to a native system cursor.

        Upon window creation, the arrow cursor is used by default.

        Warning

        The cursor must not be destroyed while in use by the window.

        Features related to Cursor are not supported on iOS and Android.

        Parameters
        - cursor	Native system cursor type to display
        """

    def set_key_repeat_enabled(self, enabled: bool) -> None:
        """
        Enable or disable automatic key-repeat.

        If key repeat is enabled, you will receive repeated KeyPressed events while keeping a key pressed. If it is disabled, you will only get a single event when the key is pressed.

        Key repeat is enabled by default.

        Parameters
        - enabled	true to enable, false to disable
        """

    def set_joystick_threshold(self, threshold: float) -> None:
        """
        Change the joystick threshold.

        The joystick threshold is the value below which no JoystickMoved event will be generated.

        The threshold value is 0.1 by default.

        Parameters
        - threshold	New threshold, in the range [0, 100]

        """

    def request_focus(self) -> None:
        """
        Request the current window to be made the active foreground window.

        At any given time, only one window may have the input focus to receive input events such as keystrokes or mouse events. If a window requests focus, it only hints to the operating system, that it would like to be focused. The operating system is free to deny the request. This is not to be confused with setActive().
        """

    def has_focus(self) -> bool:
        """
        Check whether the window has the input focus.

        At any given time, only one window may have the input focus to receive input events such as keystrokes or most mouse events.

        Returns
        - true if window has focus, false otherwise
        """


class Window(WindowBase):
    """
    Window that serves as a target for OpenGL rendering.

    sf::Window is the main class of the Window module.

    It defines an OS window that is able to receive an OpenGL rendering.

    A sf::Window can create its own new window, or be embedded into an already existing control using the create(handle) function. This can be useful for embedding an OpenGL rendering area into a view which is part of a bigger GUI with existing windows, controls, etc. It can also serve as embedding an OpenGL rendering area into a window created by another (probably richer) GUI library like Qt or wxWidgets.

    The sf::Window class provides a simple interface for manipulating the window: move, resize, show/hide, control mouse cursor, etc. It also provides event handling through its pollEvent() and waitEvent() functions.

    Note that OpenGL experts can pass their own parameters (anti-aliasing level, bits for the depth and stencil buffers, etc.) to the OpenGL context attached to the window, with the sf::ContextSettings structure which is passed as an optional argument when creating the window.

    On dual-graphics systems consisting of a low-power integrated GPU and a powerful discrete GPU, the driver picks which GPU will run an SFML application. In order to inform the driver that an SFML application can benefit from being run on the more powerful discrete GPU, #SFML_DEFINE_DISCRETE_GPU_PREFERENCE can be placed in a source file that is compiled and linked into the final application. The macro should be placed outside of any scopes in the global namespace.
    """

    def __init__(self, mode: VideoMode, title: str, style: int = Style.Default, state: State = State.Windowed, settings: ContextSettings = ContextSettings()):
        """
        Construct a new window.

        This constructor creates the window with the size and pixel depth defined in mode. An optional style can be passed to customize the look and behavior of the window (borders, title bar, resizable, closable, pass). An optional state can be provided. If state is State::Fullscreen, then mode must be a valid video mode.

        The last parameter is an optional structure specifying advanced OpenGL context settings such as anti-aliasing, depth-buffer bits, etc.

        Parameters
        - mode	Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title	Title of the window
        - style	Window style, a bitwise OR combination of sf::Style enumerators
        - state	Window state
        - settings	Additional settings for the underlying OpenGL context
        """

    @overload
    def create(self, mode: VideoMode, title: str, style: int = Style.Default, state: State = State.Windowed) -> None:
        """
        Create (or recreate) the window.

        If the window was already created, it closes it first. If state is State::Fullscreen, then mode must be a valid video mode.

        The last parameter is a structure specifying advanced OpenGL context settings such as anti-aliasing, depth-buffer bits, etc.

        Parameters
        - mode	Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title	Title of the window
        - style	Window style, a bitwise OR combination of sf::Style enumerators
        - state	Window state
        """

    @overload
    def create(self, mode: VideoMode, title: str, state: State) -> None:
        """
        Create (or recreate) the window.

        If the window was already created, it closes it first. If state is State::Fullscreen, then mode must be a valid video mode.

        Parameters
        - mode	Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title	Title of the window
        - state	Window state

        Reimplemented from sf::WindowBase.
        """

    @overload
    def create(self, mode: VideoMode, title: str, style: int, state: State, settings: ContextSettings) -> None:
        """
        Create (or recreate) the window.

        If the window was already created, it closes it first. If state is State::Fullscreen, then mode must be a valid video mode.

        The last parameter is a structure specifying advanced OpenGL context settings such as anti-aliasing, depth-buffer bits, etc.

        Parameters
        - mode	Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title	Title of the window
        - style	Window style, a bitwise OR combination of sf::Style enumerators
        - state	Window state
        - settings	Additional settings for the underlying OpenGL context
        """

    def close(self) -> None:
        """
        Close the window and destroy all the attached resources.

        After calling this function, the sf::Window instance remains valid and you can call create() to recreate the window. All other functions such as pollEvent() or display() will still work (i.e. you don't have to test isOpen() every time), and will have no effect on closed windows.

        Reimplemented from sf::WindowBase.
        """

    def set_vertical_sync_enabled(self, enabled: bool) -> None:
        """
        Enable or disable vertical synchronization.

        Activating vertical synchronization will limit the number of frames displayed to the refresh rate of the monitor. This can avoid some visual artifacts, and limit the framerate to a good value (but not constant across different computers).

        Vertical synchronization is disabled by default.

        Parameters
        - enabled	true to enable v-sync, false to deactivate it
        """

    def set_framerate_limit(self, limit: int) -> None:
        """
        Limit the framerate to a maximum fixed frequency.

        If a limit is set, the window will use a small delay after each call to display() to ensure that the current frame lasted long enough to match the framerate limit. SFML will try to match the given limit as much as it can, but since it internally uses sf::sleep, whose precision depends on the underlying OS, the results may be a little imprecise as well (for example, you can get 65 FPS when requesting 60).

        Parameters
        - limit	Framerate limit, in frames per seconds (use 0 to disable limit)

        """

    def set_active(self, active: bool = True) -> bool:
        """
        Activate or deactivate the window as the current target for OpenGL rendering.

        A window is active only on the current thread, if you want to make it active on another thread you have to deactivate it on the previous thread first if it was active. Only one window can be active on a thread at a time, thus the window previously active (if any) automatically gets deactivated. This is not to be confused with requestFocus().

        Parameters
        - active	true to activate, false to deactivate

        Returns
        - true if operation was successful, false otherwise
        """

    def display(self) -> None:
        """
        Display on screen what has been rendered to the window so far.

        This function is typically called after all OpenGL rendering has been done for the current frame, in order to show it on screen.
        """

    def get_settings(self) -> ContextSettings:
        """
        Get the settings of the OpenGL context of the window.

        Note that these settings may be different from what was passed to the constructor or the create() function, if one or more settings were not supported. In this case, SFML chose the closest match.

        Returns
        - Structure containing the OpenGL context settings
        """

class Clipboard(ModuleType):
    """
    Give access to the system clipboard.

    sf::Clipboard provides an interface for getting and setting the contents of the system clipboard.

    It is important to note that due to limitations on some operating systems, setting the clipboard contents is only guaranteed to work if there is currently an open window for which events are being handled.
    """
    @staticmethod
    def get_string() -> str:
        """
        Get the content of the clipboard as string data.

        This function returns the content of the clipboard as a string. If the clipboard does not contain string it returns an empty sf::String object.

        Returns
        - Clipboard contents as string object
        """

    @staticmethod
    def set_string(text: str) -> None:
        """
        et the content of the clipboard as string data.

        This function sets the content of the clipboard as a string.

        Warning
        - Due to limitations on some operating systems, setting the clipboard contents is only guaranteed to work if there is currently an open window for which events are being handled.

        Parameters
        - text	sf::String containing the data to be sent to the clipboard

        """


class Joystick(ModuleType):
    """
    Give access to the real-time state of the joysticks.

    sf::Joystick provides an interface to the state of the joysticks.

    Each joystick is identified by an index that is passed to the functions in this namespace.

    This namespace allows users to query the state of joysticks at any time and directly, without having to deal with a window and its events. Compared to the JoystickMoved, JoystickButtonPressed and JoystickButtonReleased events, sf::Joystick can retrieve the state of axes and buttons of joysticks at any time (you don't need to store and update a boolean on your side in order to know if a button is pressed or released), and you always get the real state of joysticks, even if they are moved, pressed or released when your window is out of focus and no event is triggered.

    SFML supports:

    - 8 joysticks (sf::Joystick::Count)
    - 32 buttons per joystick (sf::Joystick::ButtonCount)
    - 8 axes per joystick (sf::Joystick::AxisCount)
    - Unlike the keyboard or mouse, the state of joysticks is sometimes not directly available (depending on the OS), therefore an update() function must be called in order to update the current state of joysticks. When you have a window with event handling, this is done automatically, you don't need to call anything. But if you have no window, or if you want to check joysticks state before creating one, you must call sf::Joystick::update explicitly.
    """

    class Axis(enum.IntEnum):
        """
        Axes supported by SFML joysticks.

        - X     The X axis.
        - Y     The Y axis.
        - Z     The Z axis.
        - R     The R axis.
        - U     The U axis.
        - V     The V axis.
        - PovX  The X axis of the point-of-view hat.
        - PovY  The Y axis of the point-of-view hat.
        """
        X = 0
        Y = 1
        Z = 2
        R = 3
        U = 4
        V = 5
        PovX = 6
        PovY = 7

    class Identification(enum.IntEnum):
        """
        Structure holding a joystick's identification.
        """

        vendor_id: int = 0
        product_id: int = 0

        def __init__(self):
            ...

        def get_name(self) -> str:
            """
            Name of the joystick.
            """

        def set_name(self, value: str) -> None:
            """
            Sets the joystick name.
            """

    @staticmethod
    def is_connected(joystick: int) -> bool:
        """
        Check if a joystick is connected.

        Parameters
        - joystick	Index of the joystick to check

        Returns
        - true if the joystick is connected, false otherwise
        """

    @staticmethod
    def get_button_count(joystick: int) -> int:
        """
        Return the number of buttons supported by a joystick.

        If the joystick is not connected, this function returns 0.

        Parameters
        - joystick	Index of the joystick

        Returns
        - Number of buttons supported by the joystick
        """

    @staticmethod
    def has_axis(joystick: int, axis: Axis) -> bool:
        """
        Check if a joystick supports a given axis.

        If the joystick is not connected, this function returns false.

        Parameters
        - joystick	Index of the joystick
        - axis	Axis to check

        Returns
        - true if the joystick supports the axis, false otherwise
        """

    @staticmethod
    def is_button_pressed(joystick: int, button: int) -> bool:
        """
        Check if a joystick button is pressed.

        If the joystick is not connected, this function returns false.

        Parameters
        - joystick	Index of the joystick
        - button	Button to check

        Returns
        - true if the button is pressed, false otherwise
        """

    @staticmethod
    def get_axis_position(joystick: int, axis: Axis) -> float:
        """
        Returns the position of the specified axis on the joystick.
        """

    @staticmethod
    def get_identification(joystick: int) -> Identification:
        """
        Get the joystick information.

        Parameters
        - joystick	Index of the joystick

        Returns
        - Structure containing joystick information.
        """

    @staticmethod
    def update() -> None:
        """
        Update the states of all joysticks.

        This function is used internally by SFML, so you normally don't have to call it explicitly. However, you may need to call it if you have no window yet (or no window at all): in this case the joystick states are not updated automatically.
        """


class Keyboard(ModuleType):
    """
    Give access to the real-time state of the keyboard.

    sf::Keyboard provides an interface to the state of the keyboard.

    This namespace allows users to query the keyboard state at any time and directly, without having to deal with a window and its events. Compared to the KeyPressed and KeyReleased events, sf::Keyboard can retrieve the state of a key at any time (you don't need to store and update a boolean on your side in order to know if a key is pressed or released), and you always get the real state of the keyboard, even if keys are pressed or released when your window is out of focus and no event is triggered.
    """

    class Key(enum.IntEnum):
        """
        Key codes.

        The enumerators refer to the "localized" key; i.e. depending on the layout set by the operating system, a key can be mapped to Y or Z.
        - Unknown: Unhandled key.
        - A: The A key.
        - B: The B key.
        - C: The C key.
        - D: The D key.
        - E: The E key.
        - F: The F key.
        - G: The G key.
        - H: The H key.
        - I: The I key.
        - J: The J key.
        - K: The K key.
        - L: The L key.
        - M: The M key.
        - N: The N key.
        - O: The O key.
        - P: The P key.
        - Q: The Q key.
        - R: The R key.
        - S: The S key.
        - T: The T key.
        - U: The U key.
        - V: The V key.
        - W: The W key.
        - X: The X key.
        - Y: The Y key.
        - Z: The Z key.
        - Num0: The 0 key.
        - Num1: The 1 key.
        - Num2: The 2 key.
        - Num3: The 3 key.
        - Num4: The 4 key.
        - Num5: The 5 key.
        - Num6: The 6 key.
        - Num7: The 7 key.
        - Num8: The 8 key.
        - Num9: The 9 key.
        - Escape: The Escape key.
        - LControl: The left Control key.
        - LShift: The left Shift key.
        - LAlt: The left Alt key.
        - LSystem: The left OS specific key: window (Windows and Linux), apple (macOS),         - RControl: The right Control key.
        - RShift: The right Shift key.
        - RAlt: The right Alt key.
        - RSystem: The right OS specific key: window (Windows and Linux), apple (macOS),         - Menu: The Menu key.
        - LBracket: The [ key.
        - RBracket: The ] key.
        - Semicolon: The ; key.
        - Comma: The , key.
        - Period: The . key.
        - Apostrophe: The ' key.
        - Slash: The / key.
        - Backslash: The \\ key.
        - Grave: The ` key.
        - Equal: The = key.
        - Hyphen: The - key (hyphen)
        - Space: The Space key.
        - Enter: The Enter/Return keys.
        - Backspace: The Backspace key.
        - Tab: The Tabulation key.
        - PageUp: The Page up key.
        - PageDown: The Page down key.
        - End: The End key.
        - Home: The Home key.
        - Insert: The Insert key.
        - Delete: The Delete key.
        - Add: The + key.
        - Subtract: The - key (minus, usually from numpad)
        - Multiply: The * key.
        - Divide: The / key.
        - Left: Left arrow.
        - Right: Right arrow.
        - Up: Up arrow.
        - Down: Down arrow.
        - Numpad0: The numpad 0 key.
        - Numpad1: The numpad 1 key.
        - Numpad2: The numpad 2 key.
        - Numpad3: The numpad 3 key.
        - Numpad4: The numpad 4 key.
        - Numpad5: The numpad 5 key.
        - Numpad6: The numpad 6 key.
        - Numpad7: The numpad 7 key.
        - Numpad8: The numpad 8 key.
        - Numpad9: The numpad 9 key.
        - F1: The F1 key.
        - F2: The F2 key.
        - F3: The F3 key.
        - F4: The F4 key.
        - F5: The F5 key.
        - F6: The F6 key.
        - F7: The F7 key.
        - F8: The F8 key.
        - F9: The F9 key.
        - F10: The F10 key.
        - F11: The F11 key.
        - F12: The F12 key.
        - F13: The F13 key.
        - F14: The F14 key.
        - F15: The F15 key.
        - Pause: The Pause key.
        """
        Unknown = -1
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        F = 5
        G = 6
        H = 7
        I = 8
        J = 9
        K = 10
        L = 11
        M = 12
        N = 13
        O = 14
        P = 15
        Q = 16
        R = 17
        S = 18
        T = 19
        U = 20
        V = 21
        W = 22
        X = 23
        Y = 24
        Z = 25
        Num0 = 26
        Num1 = 27
        Num2 = 28
        Num3 = 29
        Num4 = 30
        Num5 = 31
        Num6 = 32
        Num7 = 33
        Num8 = 34
        Num9 = 35
        Escape = 36
        LControl = 37
        LShift = 38
        LAlt = 39
        LSystem = 40
        RControl = 41
        RShift = 42
        RAlt = 43
        RSystem = 44
        Menu = 45
        LBracket = 46
        RBracket = 47
        Semicolon = 48
        Comma = 49
        Period = 50
        Apostrophe = 51
        Slash = 52
        Backslash = 53
        Grave = 54
        Equal = 55
        Hyphen = 56
        Space = 57
        Enter = 58
        Backspace = 59
        Tab = 60
        PageUp = 61
        PageDown = 62
        End = 63
        Home = 64
        Insert = 65
        Delete = 66
        Add = 67
        Subtract = 68
        Multiply = 69
        Divide = 70
        Left = 71
        Right = 72
        Up = 73
        Down = 74
        Numpad0 = 75
        Numpad1 = 76
        Numpad2 = 77
        Numpad3 = 78
        Numpad4 = 79
        Numpad5 = 80
        Numpad6 = 81
        Numpad7 = 82
        Numpad8 = 83
        Numpad9 = 84
        F1 = 85
        F2 = 86
        F3 = 87
        F4 = 88
        F5 = 89
        F6 = 90
        F7 = 91
        F8 = 92
        F9 = 93
        F10 = 94
        F11 = 95
        F12 = 96
        F13 = 97
        F14 = 98
        F15 = 99
        Pause = 100

    class Scan(enum.IntEnum):
        """
        Scancodes.

        The enumerators are bound to a physical key and do not depend on the keyboard layout used by the operating system. Usually, the AT-101 keyboard can be used as reference for the physical position of the keys.
        - Unknown: Represents any scancode not present in this enum.
        - A: Keyboard a and A key.
        - B: Keyboard b and B key.
        - C: Keyboard c and C key.
        - D: Keyboard d and D key.
        - E: Keyboard e and E key.
        - F: Keyboard f and F key.
        - G: Keyboard g and G key.
        - H: Keyboard h and H key.
        - I: Keyboard i and I key.
        - J: Keyboard j and J key.
        - K: Keyboard k and K key.
        - L: Keyboard l and L key.
        - M: Keyboard m and M key.
        - N: Keyboard n and N key.
        - O: Keyboard o and O key.
        - P: Keyboard p and P key.
        - Q: Keyboard q and Q key.
        - R: Keyboard r and R key.
        - S: Keyboard s and S key.
        - T: Keyboard t and T key.
        - U: Keyboard u and U key.
        - V: Keyboard v and V key.
        - W: Keyboard w and W key.
        - X: Keyboard x and X key.
        - Y: Keyboard y and Y key.
        - Z: Keyboard z and Z key.
        - Num1: Keyboard 1 and ! key.
        - Num2: Keyboard 2 and @ key.
        - Num3: Keyboard 3 and # key.
        - Num4: Keyboard 4 and $ key.
        - Num5: Keyboard 5 and % key.
        - Num6: Keyboard 6 and ^ key.
        - Num7: Keyboard 7 and & key.
        - Num8: Keyboard 8 and * key.
        - Num9: Keyboard 9 and ) key.
        - Num0: Keyboard 0 and ) key.
        - Enter: Keyboard Enter/Return key.
        - Escape: Keyboard Escape key.
        - Backspace: Keyboard Backspace key.
        - Tab: Keyboard Tab key.
        - Space: Keyboard Space key.
        - Hyphen: Keyboard - and _ key.
        - Equal: Keyboard = and +.
        - LBracket: Keyboard [ and { key.
        - RBracket: Keyboard ] and } key.
        - Backslash: Keyboard \\ and | key OR various keys for Non-US keyboards.
        - Semicolon: Keyboard ; and : key.
        - Apostrophe: Keyboard ' and " key.
        - Grave: Keyboard ` and ~ key.
        - Comma: Keyboard , and < key.
        - Period: Keyboard . and > key.
        - Slash: Keyboard / and ? key.
        - F1: Keyboard F1 key.
        - F2: Keyboard F2 key.
        - F3: Keyboard F3 key.
        - F4: Keyboard F4 key.
        - F5: Keyboard F5 key.
        - F6: Keyboard F6 key.
        - F7: Keyboard F7 key.
        - F8: Keyboard F8 key.
        - F9: Keyboard F9 key.
        - F10: Keyboard F10 key.
        - F11: Keyboard F11 key.
        - F12: Keyboard F12 key.
        - F13: Keyboard F13 key.
        - F14: Keyboard F14 key.
        - F15: Keyboard F15 key.
        - F16: Keyboard F16 key.
        - F17: Keyboard F17 key.
        - F18: Keyboard F18 key.
        - F19: Keyboard F19 key.
        - F20: Keyboard F20 key.
        - F21: Keyboard F21 key.
        - F22: Keyboard F22 key.
        - F23: Keyboard F23 key.
        - F24: Keyboard F24 key.
        - CapsLock: Keyboard Caps Lock key.
        - PrintScreen: Keyboard Print Screen key.
        - ScrollLock: Keyboard Scroll Lock key.
        - Pause: Keyboard Pause key.
        - Insert: Keyboard Insert key.
        - Home: Keyboard Home key.
        - PageUp: Keyboard Page Up key.
        - Delete: Keyboard Delete Forward key.
        - End: Keyboard End key.
        - PageDown: Keyboard Page Down key.
        - Right: Keyboard Right Arrow key.
        - Left: Keyboard Left Arrow key.
        - Down: Keyboard Down Arrow key.
        - Up: Keyboard Up Arrow key.
        - NumLock: Keypad Num Lock and Clear key.
        - NumpadDivide: Keypad / key.
        - NumpadMultiply: Keypad * key.
        - NumpadMinus: Keypad - key.
        - NumpadPlus: Keypad + key.
        - NumpadEqual: keypad = key.
        - NumpadEnter: Keypad Enter/Return key.
        - NumpadDecimal: Keypad . and Delete key.
        - Numpad1: Keypad 1 and End key.
        - Numpad2: Keypad 2 and Down Arrow key.
        - Numpad3: Keypad 3 and Page Down key.
        - Numpad4: Keypad 4 and Left Arrow key.
        - Numpad5: Keypad 5 key.
        - Numpad6: Keypad 6 and Right Arrow key.
        - Numpad7: Keypad 7 and Home key.
        - Numpad8: Keypad 8 and Up Arrow key.
        - Numpad9: Keypad 9 and Page Up key.
        - Numpad0: Keypad 0 and Insert key.
        - NonUsBackslash: Keyboard Non-US \\ and | key.
        - Application: Keyboard Application key.
        - Execute: Keyboard Execute key.
        - ModeChange: Keyboard Mode Change key.
        - Help: Keyboard Help key.
        - Menu: Keyboard Menu key.
        - Select: Keyboard Select key.
        - Redo: Keyboard Redo key.
        - Undo: Keyboard Undo key.
        - Cut: Keyboard Cut key.
        - Copy: Keyboard Copy key.
        - Paste: Keyboard Paste key.
        - VolumeMute: Keyboard Volume Mute key.
        - VolumeUp: Keyboard Volume Up key.
        - VolumeDown: Keyboard Volume Down key.
        - MediaPlayPause: Keyboard Media Play Pause key.
        - MediaStop: Keyboard Media Stop key.
        - MediaNextTrack: Keyboard Media Next Track key.
        - MediaPreviousTrack: Keyboard Media Previous Track key.
        - LControl: Keyboard Left Control key.
        - LShift: Keyboard Left Shift key.
        - LAlt: Keyboard Left Alt key.
        - LSystem: Keyboard Left System key.
        - RControl: Keyboard Right Control key.
        - RShift: Keyboard Right Shift key.
        - RAlt: Keyboard Right Alt key.
        - RSystem: Keyboard Right System key.
        - Back: Keyboard Back key.
        - Forward: Keyboard Forward key.
        - Refresh: Keyboard Refresh key.
        - Stop: Keyboard Stop key.
        - Search: Keyboard Search key.
        - Favorites: Keyboard Favorites key.
        - HomePage: Keyboard Home Page key.
        - LaunchApplication1: Keyboard Launch Application 1 key.
        - LaunchApplication2: Keyboard Launch Application 2 key.
        - LaunchMail: Keyboard Launch Mail key.
        - LaunchMediaSelect: Keyboard Launch Media Select key.
        """
        Unknown = -1
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        F = 5
        G = 6
        H = 7
        I = 8
        J = 9
        K = 10
        L = 11
        M = 12
        N = 13
        O = 14
        P = 15
        Q = 16
        R = 17
        S = 18
        T = 19
        U = 20
        V = 21
        W = 22
        X = 23
        Y = 24
        Z = 25
        Num1 = 26
        Num2 = 27
        Num3 = 28
        Num4 = 29
        Num5 = 30
        Num6 = 31
        Num7 = 32
        Num8 = 33
        Num9 = 34
        Num0 = 35
        Enter = 36
        Escape = 37
        Backspace = 38
        Tab = 39
        Space = 40
        Hyphen = 41
        Equal = 42
        LBracket = 43
        RBracket = 44
        Backslash = 45
        Semicolon = 46
        Apostrophe = 47
        Grave = 48
        Comma = 49
        Period = 50
        Slash = 51
        F1 = 52
        F2 = 53
        F3 = 54
        F4 = 55
        F5 = 56
        F6 = 57
        F7 = 58
        F8 = 59
        F9 = 60
        F10 = 61
        F11 = 62
        F12 = 63
        F13 = 64
        F14 = 65
        F15 = 66
        F16 = 67
        F17 = 68
        F18 = 69
        F19 = 70
        F20 = 71
        F21 = 72
        F22 = 73
        F23 = 74
        F24 = 75
        CapsLock = 76
        PrintScreen = 77
        ScrollLock = 78
        Pause = 79
        Insert = 80
        Home = 81
        PageUp = 82
        Delete = 83
        End = 84
        PageDown = 85
        Right = 86
        Left = 87
        Down = 88
        Up = 89
        NumLock = 90
        NumpadDivide = 91
        NumpadMultiply = 92
        NumpadMinus = 93
        NumpadPlus = 94
        NumpadEnter = 95
        NumpadDecimal = 96
        Numpad1 = 97
        Numpad2 = 98
        Numpad3 = 99
        Numpad4 = 100
        Numpad5 = 101
        Numpad6 = 102
        Numpad7 = 103
        Numpad8 = 104
        Numpad9 = 105
        Numpad0 = 106
        NonUsBackslash = 107
        Application = 108
        Execute = 109
        ModeChange = 110
        Help = 111
        Menu = 112
        Select = 113
        Redo = 114
        Undo = 115
        Cut = 116
        Copy = 117
        Paste = 118
        VolumeMute = 119
        VolumeUp = 120
        VolumeDown = 121
        MediaPlayPause = 122
        MediaStop = 123
        MediaNextTrack = 124
        MediaPreviousTrack = 125
        LControl = 126
        LShift = 127
        LAlt = 128
        LSystem = 129
        RControl = 130
        RShift = 131
        RAlt = 132
        RSystem = 133
        Back = 134
        Forward = 135
        Refresh = 136
        Stop = 137
        Search = 138
        Favorites = 139
        HomePage = 140
        LaunchApplication1 = 141
        LaunchApplication2 = 142
        LaunchMail = 143
        LaunchMediaSelect = 144

    @overload
    @staticmethod
    def is_key_pressed(key: Key | Scan) -> bool:
        """
        Returns whether the specified key is pressed.
        """

    @overload
    @staticmethod
    def is_key_pressed(scan: Key | Scan) -> bool:
        """
        Returns whether the specified scan code is pressed.
        """

class Mouse(ModuleType):
    """
    Give access to the real-time state of the mouse.

    sf::Mouse provides an interface to the state of the mouse.

    A single mouse is assumed.

    This namespace allows users to query the mouse state at any time and directly, without having to deal with a window and its events. Compared to the MouseMoved, MouseButtonPressed and MouseButtonReleased events, sf::Mouse can retrieve the state of the cursor and the buttons at any time (you don't need to store and update a boolean on your side in order to know if a button is pressed or released), and you always get the real state of the mouse, even if it is moved, pressed or released when your window is out of focus and no event is triggered.

    The setPosition and getPosition functions can be used to change or retrieve the current position of the mouse pointer. There are two versions: one that operates in global coordinates (relative to the desktop) and one that operates in window coordinates (relative to a specific window).
    """
    class Button(enum.IntEnum):
        """
        Mouse buttons.

        - Left: The left mouse button.
        - Right: The right mouse button.
        - Middle: The middle (wheel) mouse button.
        - Extra1: The first extra mouse button.
        - Extra2: The second extra mouse button.
        """
        Left = 0
        Right = 1
        Middle = 2
        Extra1 = 3
        Extra2 = 4

    class Wheel(enum.IntEnum):
        """
        Mouse wheels.

        - Vertical: The vertical mouse wheel.
        - Horizontal: The horizontal mouse wheel.
        """
        Vertical = 0
        Horizontal = 1

    @staticmethod
    def is_button_pressed(button: Button) -> bool:
        """
        Check if a mouse button is pressed.

        Warning
        - Checking the state of buttons Mouse::Button::Extra1 and Mouse::Button::Extra2 is not supported on Linux with X11.

        Parameters
        - button	Button to check

        Returns
        - true if the button is pressed, false otherwise
        """

    @overload
    @staticmethod
    def get_position() -> sfSystem.Vector2i:
        """
        Get the current position of the mouse in desktop coordinates.

        This function returns the global position of the mouse cursor on the desktop.

        Returns
        - Current position of the mouse
        """

    @overload
    @staticmethod
    def get_position(relativeTo: WindowBase) -> sfSystem.Vector2i:
        """
        Get the current position of the mouse in window coordinates.

        This function returns the current position of the mouse cursor, relative to the given window.

        Parameters
        - relativeTo	Reference window

        Returns
        - Current position of the mouse
        """

    @overload
    @staticmethod
    def set_position(x: int, y: int) -> None:
        """
        Set the current position of the mouse in desktop coordinates.

        This function sets the global position of the mouse cursor on the desktop.

        Parameters
        - position	New position of the mouse
        """

    @overload
    @staticmethod
    def set_position(x: int, y: int, relativeTo: WindowBase) -> None:
        """
        Set the current position of the mouse in window coordinates.

        This function sets the current position of the mouse cursor, relative to the given window.

        Parameters
        - position	New position of the mouse
        - relativeTo	Reference window
        """

class Sensor(ModuleType):
    """
    Give access to the real-time state of the sensors.

    sf::Sensor provides an interface to the state of the various sensors that a device provides.

    This namespace allows users to query the sensors values at any time and directly, without having to deal with a window and its events. Compared to the SensorChanged event, sf::Sensor can retrieve the state of a sensor at any time (you don't need to store and update its current value on your side).

    Depending on the OS and hardware of the device (phone, tablet, ...), some sensor types may not be available. You should always check the availability of a sensor before trying to read it, with the sf::Sensor::isAvailable function.

    You may wonder why some sensor types look so similar, for example Accelerometer and Gravity / UserAcceleration. The first one is the raw measurement of the acceleration, and takes into account both the earth gravity and the user movement. The others are more precise: they provide these components separately, which is usually more useful. In fact they are not direct sensors, they are computed internally based on the raw acceleration and other sensors. This is exactly the same for Gyroscope vs Orientation.

    Because sensors consume a non-negligible amount of current, they are all disabled by default. You must call sf::Sensor::setEnabled for each sensor in which you are interested.
    """
    class Type(enum.IntEnum):
        """
        Sensor type.
        - Accelerometer: Measures the raw acceleration (m/s^2)
        - Gyroscope: Measures the raw rotation rates (radians/s)
        - Magnetometer: Measures the ambient magnetic field (micro-teslas)
        - Gravity: Measures the direction and intensity of gravity, independent of device acceleration (m/s^2)
        - UserAcceleration: Measures the direction and intensity of device acceleration, independent of the gravity (m/s^2)
        - Orientation: Measures the absolute 3D orientation (radians)
        """
        Accelerometer = 0
        Gyroscope = 1
        Magnetometer = 2
        Gravity = 3
        UserAcceleration = 4
        Orientation = 5

    @staticmethod
    def is_available(sensor: Type) -> bool:
        """
        Check if a sensor is available on the underlying platform.

        Parameters
        - sensor	Sensor to check

        Returns
        - true if the sensor is available, false otherwise
        """

    @staticmethod
    def set_enabled(sensor: Type, enabled: bool) -> None:
        """
        Enable or disable a sensor.

        All sensors are disabled by default, to avoid consuming too much battery power. Once a sensor is enabled, it starts sending events of the corresponding type.

        This function does nothing if the sensor is unavailable.

        Parameters
        - sensor	Sensor to enable
        - enabled	true to enable, false to disable
        """

    @staticmethod
    def get_value(sensor: Type) -> float:
        """
        Get the current sensor value.

        Parameters
        - sensor	Sensor to read

        Returns
        - The current sensor value
        """

class Touch(ModuleType):
    """
    Give access to the real-time state of the touches.

    sf::Touch provides an interface to the state of the touches.

    This namespace allows users to query the touches state at any time and directly, without having to deal with a window and its events. Compared to the TouchBegan, TouchMoved and TouchEnded events, sf::Touch can retrieve the state of the touches at any time (you don't need to store and update a boolean on your side in order to know if a touch is down), and you always get the real state of the touches, even if they happen when your window is out of focus and no event is triggered.

    The getPosition function can be used to retrieve the current position of a touch. There are two versions: one that operates in global coordinates (relative to the desktop) and one that operates in window coordinates (relative to a specific window).

    Touches are identified by an index (the "finger"), so that in multi-touch events, individual touches can be tracked correctly. As long as a finger touches the screen, it will keep the same index even if other fingers start or stop touching the screen in the meantime. As a consequence, active touch indices may not always be sequential (i.e. touch number 0 may be released while touch number 1 is still down).
    """
    @staticmethod
    def isDown(finger: int) -> bool:
        """
        Check if a touch event is currently down.

        Parameters
        - finger	Finger index

        Returns
        - true if finger is currently touching the screen, false otherwise
        """

    @overload
    @staticmethod
    def getPosition(finger: int) -> sfSystem.Vector2i:
        """
        Get the current position of a touch in desktop coordinates.

        This function returns the current touch position in global (desktop) coordinates.

        Parameters
        - finger	Finger index

        Returns
        - Current position of finger, or undefined if it's not down
        """

    @overload
    @staticmethod
    def getPosition(finger: int, relativeTo: WindowBase) -> sfSystem.Vector2i:
        """
        Get the current position of a touch in window coordinates.

        This function returns the current touch position relative to the given window.

        Parameters
        - finger	Finger index
        - relativeTo	Reference window

        Returns
        - Current position of finger, or undefined if it's not down
        """
