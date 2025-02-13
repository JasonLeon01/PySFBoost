import typing

"""
This module provides bindings for SFML's system, including classes
for angle, time, clock and more.
"""
class Angle:
    def __init__(self) -> None: 
        """
        Represents an angle value.

        Angle encapsulates an angle value in a flexible way.

        It allows for defining an angle value either as a number of degrees or radians. It also works the other way around. You can read an angle value as either a number of degrees or radians.

        By using such a flexible interface, the API doesn't impose any fixed type or unit for angle values and lets the user choose their own preferred representation.

        Angle values support the usual mathematical operations. You can add or subtract two angles, multiply or divide an angle by a number, compare two angles, etc.
        """
        pass

    @staticmethod
    def degrees(degrees: float) -> "Angle":
        """
        Construct an angle value from a number of degrees.
        """
        pass

    @staticmethod
    def radians(radians: float) -> "Angle":
        """
        Overload of operator!= to compare two angle values.
        """
        pass

    def as_degrees(self) -> float:
        """
        Return the angle's value in degrees.
        """
        pass

    def as_radians(self) -> float:
        """
        Return the angle's value in radians.
        """
        pass

    def wrap_signed(self) -> "Angle":
        """
        Wrap to a range such that -180° <= angle < 180°

        Similar to a modulo operation, this returns a copy of the angle constrained to the range [-180°, 180°) == [-Pi, Pi). The resulting angle represents a rotation which is equivalent to *this.

        The name "signed" originates from the similarity to signed integers.
        """
        pass

    def wrap_unsigned(self) -> "Angle":
        """
        Wrap to a range such that 0° <= angle < 360°

        Similar to a modulo operation, this returns a copy of the angle constrained to the range [0°, 360°) == [0, Tau) == [0, 2*Pi). The resulting angle represents a rotation which is equivalent to *this.

        The name "unsigned" originates from the similarity to unsigned integers.
        """
        pass

# Represents a time duration
class Time:
    def as_seconds(self) -> float:
        """
        Returns the time as seconds.
        """
        pass

    def as_milliseconds(self) -> int:
        """
        Returns the time as milliseconds.
        """
        pass

    def as_microseconds(self) -> int:
        """
        Returns the time as microseconds.
        """
        pass

    def to_duration(self) -> typing.Any:
        """
        Converts the time to a duration object.
        """
        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the time in seconds.
        """
        pass

# Clock for measuring elapsed time
class Clock:
    def __init__(self) -> None:
        """
        Utility class that measures the elapsed time.

        Clock is a lightweight class for measuring time.

        The clock starts automatically after being constructed.

        It provides the most precise time that the underlying OS can achieve (generally microseconds or nanoseconds). It also ensures monotonicity, which means that the returned time can never go backward, even if the system time is changed.
        """
        pass

    def start(self) -> None:
        """"
        Start the clock.
        """
        pass

    def stop(self) -> None:
        """
        Stops the clock.
        """
        pass

    def restart(self) -> None:
        """
        Restart the clock.

        This function puts the time counter back to zero, returns the elapsed time, and leaves the clock in a running state.
        """
        pass

    def reset(self) -> None:
        """
        Reset the clock.

        This function puts the time counter back to zero, returns the elapsed time, and leaves the clock in a paused state.
        """
        pass

    def get_elapsed_time(self) -> Time:
        """
        Get the elapsed time.

        This function returns the time elapsed since the last call to restart() (or the construction of the instance if restart() has not been called).
        """
        pass

# Base class for Vector2f
class Vector2f:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Initializes a Vector2f object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        """
        pass

    def x(self) -> float:
        """
        Returns the x component of the vector.
        """
        pass

    def y(self) -> float:
        """
        Returns the y component of the vector.
        """
        pass

# Base class for Vector2i
class Vector2i:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """
        Initializes a Vector2i object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        """
        pass

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """
        pass

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """
        pass

# Base class for Vector2u
class Vector2u:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        """
        Initializes a Vector2u object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        """
        pass

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """
        pass

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """
        pass

# Base class for Vector3f
class Vector3f:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """
        Initializes a Vector3f object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        - z: The z component of the vector.
        """
        pass

    def x(self) -> float:
        """
        Returns the x component of the vector.
        """
        pass

    def y(self) -> float:
        """
        Returns the y component of the vector.
        """
        pass

    def z(self) -> float:
        """
        Returns the z component of the vector.
        """
        pass

# Base class for Vector3i
class Vector3i:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        """
        Initializes a Vector3i object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        - z: The z component of the vector.
        """
        pass

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """
        pass

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """
        pass

    def z(self) -> int:
        """
        Returns the z component of the vector.
        """
        pass

# Base class for Vector3u

class Vector3u:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        """
        Initializes a Vector3u object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        - z: The z component of the vector.
        """
        pass

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """
        pass

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """
        pass

    def z(self) -> int:
        """
        Returns the z component of the vector.
        """
        pass

# Base class for input streams
class InputStream:
    """
    Abstract class for custom file input streams.

    This class allows users to define their own file input sources from which SFML can load resources.

    SFML resource classes like sf::Texture and sf::SoundBuffer provide loadFromFile and loadFromMemory functions, which read data from conventional sources. However, if you have data coming from a different source (over a network, embedded, encrypted, compressed, etc) you can derive your own class from sf::InputStream and load SFML resources with their loadFromStream function.
    """
    def read(self, count: int) -> bytes:
        """
        Read data from the stream.

        After reading, the stream's reading position must be advanced by the amount of bytes read.

        Parameters
        - data: Buffer where to copy the read data
        - size: Desired number of bytes to read

        Returns
        - The number of bytes actually read, or std::nullopt on error
        """
        pass

    def seek(self, position: int) -> None:
        """
        Change the current reading position.

        Parameters
        - position	The position to seek to, from the beginning

        Returns
        - The position actually sought to, or std::nullopt on error
        """
        pass

    def tell(self) -> int:
        """
        Get the current reading position in the stream.

        Returns
        - The current position, or std::nullopt on error.
        """
        pass

    @property
    def size(self) -> int:
        """
        Returns the size of the input stream.

        Returns
        - The total number of bytes available in the stream, or std::nullopt on error
        """
        pass

# Represents a file input stream
class FileInputStream(InputStream):
    def __init__(self) -> None:
        """
        Implementation of input stream based on a file.

        This class is a specialization of InputStream that reads from a file on disk.

        It wraps a file in the common InputStream interface and therefore allows to use generic classes or functions that accept such a stream, with a file on disk as the data source.

        In addition to the virtual functions inherited from InputStream, FileInputStream adds a function to specify the file to open.

        SFML resource classes can usually be loaded directly from a filename, so this class shouldn't be useful to you unless you create your own algorithms that operate on an InputStream.
        """
        pass

    def open(self, filename: str) -> bool:
        """
        Open the stream from a file path.

        Parameters
        - filename: Name of the file to open

        Returns
        - true on success, false on error
        """
        pass
