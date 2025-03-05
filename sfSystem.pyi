"""
Base module of SFML, defining various utilities.

It provides vector classes, Unicode strings and conversion functions, threads and mutexes, timing classes.
"""

# pylint: disable=unused-argument
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=invalid-name

from __future__ import annotations
import typing

class Angle:
    """
    Represents an angle value.

    sf::Angle encapsulates an angle value in a flexible way.

    It allows for defining an angle value either as a number of degrees or radians. It also works the other way around. You can read an angle value as either a number of degrees or radians.

    By using such a flexible interface, the API doesn't impose any fixed type or unit for angle values and lets the user choose their own preferred representation.

    Angle values support the usual mathematical operations. You can add or subtract two angles, multiply or divide an angle by a number, compare two angles, etc.
    """

    def __init__(self) -> None:
        """
        Represents an angle value.

        Angle encapsulates an angle value in a flexible way.

        It allows for defining an angle value either as a number of degrees or radians. It also works the other way around. You can read an angle value as either a number of degrees or radians.

        By using such a flexible interface, the API doesn't impose any fixed type or unit for angle values and lets the user choose their own preferred representation.

        Angle values support the usual mathematical operations. You can add or subtract two angles, multiply or divide an angle by a number, compare two angles, etc.
        """

    @staticmethod
    def degrees(degrees: float) -> "Angle":
        """
        Construct an angle value from a number of degrees.
        """

    @staticmethod
    def radians(radians: float) -> "Angle":
        """
        Overload of operator!= to compare two angle values.
        """

    def as_degrees(self) -> float:
        """
        Return the angle's value in degrees.
        """

    def as_radians(self) -> float:
        """
        Return the angle's value in radians.
        """

    def wrap_signed(self) -> "Angle":
        """
        Wrap to a range such that -180° <= angle < 180°

        Similar to a modulo operation, this returns a copy of the angle constrained to the range [-180°, 180°) == [-Pi, Pi). The resulting angle represents a rotation which is equivalent to *this.

        The name "signed" originates from the similarity to signed integers.
        """

    def wrap_unsigned(self) -> "Angle":
        """
        Wrap to a range such that 0° <= angle < 360°

        Similar to a modulo operation, this returns a copy of the angle constrained to the range [0°, 360°) == [0, Tau) == [0, 2*Pi). The resulting angle represents a rotation which is equivalent to *this.

        The name "unsigned" originates from the similarity to unsigned integers.
        """

class Time:
    """
    Represents a time value.

    sf::Time encapsulates a time value in a flexible way.

    It allows to define a time value either as a number of seconds, milliseconds or microseconds. It also works the other way round: you can read a time value as either a number of seconds, milliseconds or microseconds. It even interoperates with the <chrono> header. You can construct an sf::Time from a chrono::duration and read any sf::Time as a chrono::duration.

    By using such a flexible interface, the API doesn't impose any fixed type or resolution for time values, and let the user choose its own favorite representation.

    Time values support the usual mathematical operations: you can add or subtract two times, multiply or divide a time by a number, compare two times, etc.

    Since they represent a time span and not an absolute time value, times can also be negative.
    """

    def as_seconds(self) -> float:
        """
        Returns the time as seconds.
        """

    def as_milliseconds(self) -> int:
        """
        Returns the time as milliseconds.
        """

    def as_microseconds(self) -> int:
        """
        Returns the time as microseconds.
        """

    def to_duration(self) -> typing.Any:
        """
        Converts the time to a duration object.
        """

    def __repr__(self) -> str:
        """
        Returns a string representation of the time in seconds.
        """

class Clock:
    """
    Utility class that measures the elapsed time.

    sf::Clock is a lightweight class for measuring time.

    The clock starts automatically after being constructed.

    It provides the most precise time that the underlying OS can achieve (generally microseconds or nanoseconds). It also ensures monotonicity, which means that the returned time can never go backward, even if the system time is changed.
    """

    def __init__(self) -> None:
        """
        Utility class that measures the elapsed time.

        Clock is a lightweight class for measuring time.

        The clock starts automatically after being constructed.

        It provides the most precise time that the underlying OS can achieve (generally microseconds or nanoseconds). It also ensures monotonicity, which means that the returned time can never go backward, even if the system time is changed.
        """

    def start(self) -> None:
        """"
        Start the clock.
        """

    def stop(self) -> None:
        """
        Stops the clock.
        """

    def restart(self) -> None:
        """
        Restart the clock.

        This function puts the time counter back to zero, returns the elapsed time, and leaves the clock in a running state.
        """

    def reset(self) -> None:
        """
        Reset the clock.

        This function puts the time counter back to zero, returns the elapsed time, and leaves the clock in a paused state.
        """

    def get_elapsed_time(self) -> Time:
        """
        Get the elapsed time.

        This function returns the time elapsed since the last call to restart() (or the construction of the instance if restart() has not been called).
        """

class Vector2f:
    """
    ```
    template<typename T>
    class sf::Vector2< T >
    ```

    Class template for manipulating 2-dimensional vectors.

    sf::Vector2 is a simple class that defines a mathematical vector with two coordinates (x and y).

    It can be used to represent anything that has two dimensions: a size, a point, a velocity, a scale, etc.

    The API provides basic arithmetic (addition, subtraction, scale), as well as more advanced geometric operations, such as dot/cross products, length and angle computations, projections, rotations, etc.

    The template parameter T is the type of the coordinates. It can be any type that supports arithmetic operations (+, -, /, *) and comparisons (==, !=), for example int or float. Note that some operations are only meaningful for vectors where T is a floating point type (e.g. float or double), often because results cannot be represented accurately with integers. The method documentation mentions "(floating-point)" in those cases.

    You generally don't have to care about the templated form (sf::Vector2<T>), the most common specializations have special type aliases:

    - sf::Vector2<float> is sf::Vector2f
    - sf::Vector2<int> is sf::Vector2i
    - sf::Vector2<unsigned int> is sf::Vector2u

    The sf::Vector2 class has a simple interface, its x and y members can be accessed directly (there are no accessors like setX(), getX()).
    """

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Initializes a Vector2f object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        """

    def x(self) -> float:
        """
        Returns the x component of the vector.
        """

    def y(self) -> float:
        """
        Returns the y component of the vector.
        """

class Vector2i:
    """
    ```
    template<typename T>
    class sf::Vector2< T >
    ```

    Class template for manipulating 2-dimensional vectors.

    sf::Vector2 is a simple class that defines a mathematical vector with two coordinates (x and y).

    It can be used to represent anything that has two dimensions: a size, a point, a velocity, a scale, etc.

    The API provides basic arithmetic (addition, subtraction, scale), as well as more advanced geometric operations, such as dot/cross products, length and angle computations, projections, rotations, etc.

    The template parameter T is the type of the coordinates. It can be any type that supports arithmetic operations (+, -, /, *) and comparisons (==, !=), for example int or float. Note that some operations are only meaningful for vectors where T is a floating point type (e.g. float or double), often because results cannot be represented accurately with integers. The method documentation mentions "(floating-point)" in those cases.

    You generally don't have to care about the templated form (sf::Vector2<T>), the most common specializations have special type aliases:

    - sf::Vector2<float> is sf::Vector2f
    - sf::Vector2<int> is sf::Vector2i
    - sf::Vector2<unsigned int> is sf::Vector2u

    The sf::Vector2 class has a simple interface, its x and y members can be accessed directly (there are no accessors like setX(), getX()).
    """

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """
        Initializes a Vector2i object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        """

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """

class Vector2u:
    """
    ```
    template<typename T>
    class sf::Vector2< T >
    ```

    Class template for manipulating 2-dimensional vectors.

    sf::Vector2 is a simple class that defines a mathematical vector with two coordinates (x and y).

    It can be used to represent anything that has two dimensions: a size, a point, a velocity, a scale, etc.

    The API provides basic arithmetic (addition, subtraction, scale), as well as more advanced geometric operations, such as dot/cross products, length and angle computations, projections, rotations, etc.

    The template parameter T is the type of the coordinates. It can be any type that supports arithmetic operations (+, -, /, *) and comparisons (==, !=), for example int or float. Note that some operations are only meaningful for vectors where T is a floating point type (e.g. float or double), often because results cannot be represented accurately with integers. The method documentation mentions "(floating-point)" in those cases.

    You generally don't have to care about the templated form (sf::Vector2<T>), the most common specializations have special type aliases:

    - sf::Vector2<float> is sf::Vector2f
    - sf::Vector2<int> is sf::Vector2i
    - sf::Vector2<unsigned int> is sf::Vector2u

    The sf::Vector2 class has a simple interface, its x and y members can be accessed directly (there are no accessors like setX(), getX()).
    """

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """
        Initializes a Vector2u object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        """

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """

class Vector3f:
    """
    ```
    template<typename T>
    class sf::Vector3< T >
    ```

    Utility template class for manipulating 3-dimensional vectors.

    sf::Vector3 is a simple class that defines a mathematical vector with three coordinates (x, y and z).

    It can be used to represent anything that has three dimensions: a size, a point, a velocity, etc.

    The template parameter T is the type of the coordinates. It can be any type that supports arithmetic operations (+, -, /, *) and comparisons (==, !=), for example int or float. Note that some operations are only meaningful for vectors where T is a floating point type (e.g. float or double), often because results cannot be represented accurately with integers. The method documentation mentions "(floating-point)" in those cases.

    You generally don't have to care about the templated form (sf::Vector3<T>), the most common specializations have special type aliases:

    - sf::Vector3<float> is sf::Vector3f
    - sf::Vector3<int> is sf::Vector3i

    The sf::Vector3 class has a small
    and simple interface, its x, y and z members can be accessed directly (there are no accessors like setX(), getX()).
    """

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """
        Initializes a Vector3f object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        - z: The z component of the vector.
        """

    def x(self) -> float:
        """
        Returns the x component of the vector.
        """

    def y(self) -> float:
        """
        Returns the y component of the vector.
        """

    def z(self) -> float:
        """
        Returns the z component of the vector.
        """

class Vector3i:
    """
    ```
    template<typename T>
    class sf::Vector3< T >
    ```

    Utility template class for manipulating 3-dimensional vectors.

    sf::Vector3 is a simple class that defines a mathematical vector with three coordinates (x, y and z).

    It can be used to represent anything that has three dimensions: a size, a point, a velocity, etc.

    The template parameter T is the type of the coordinates. It can be any type that supports arithmetic operations (+, -, /, *) and comparisons (==, !=), for example int or float. Note that some operations are only meaningful for vectors where T is a floating point type (e.g. float or double), often because results cannot be represented accurately with integers. The method documentation mentions "(floating-point)" in those cases.

    You generally don't have to care about the templated form (sf::Vector3<T>), the most common specializations have special type aliases:

    - sf::Vector3<float> is sf::Vector3f
    - sf::Vector3<int> is sf::Vector3i

    The sf::Vector3 class has a small
    and simple interface, its x, y and z members can be accessed directly (there are no accessors like setX(), getX()).
    """

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        """
        Initializes a Vector3i object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        - z: The z component of the vector.
        """

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """

    def z(self) -> int:
        """
        Returns the z component of the vector.
        """

class Vector3u:
    """
    ```
    template<typename T>
    class sf::Vector3< T >
    ```

    Utility template class for manipulating 3-dimensional vectors.

    sf::Vector3 is a simple class that defines a mathematical vector with three coordinates (x, y and z).

    It can be used to represent anything that has three dimensions: a size, a point, a velocity, etc.

    The template parameter T is the type of the coordinates. It can be any type that supports arithmetic operations (+, -, /, *) and comparisons (==, !=), for example int or float. Note that some operations are only meaningful for vectors where T is a floating point type (e.g. float or double), often because results cannot be represented accurately with integers. The method documentation mentions "(floating-point)" in those cases.

    You generally don't have to care about the templated form (sf::Vector3<T>), the most common specializations have special type aliases:

    - sf::Vector3<float> is sf::Vector3f
    - sf::Vector3<int> is sf::Vector3i

    The sf::Vector3 class has a small
    and simple interface, its x, y and z members can be accessed directly (there are no accessors like setX(), getX()).
    """

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        """
        Initializes a Vector3u object.

        Parameters:
        - x: The x component of the vector.
        - y: The y component of the vector.
        - z: The z component of the vector.
        """

    def x(self) -> int:
        """
        Returns the x component of the vector.
        """

    def y(self) -> int:
        """
        Returns the y component of the vector.
        """

    def z(self) -> int:
        """
        Returns the z component of the vector.
        """

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

    def seek(self, position: int) -> None:
        """
        Change the current reading position.

        Parameters
        - position	The position to seek to, from the beginning

        Returns
        - The position actually sought to, or std::nullopt on error
        """

    def tell(self) -> int:
        """
        Get the current reading position in the stream.

        Returns
        - The current position, or std::nullopt on error.
        """

    @property
    def size(self) -> int:
        """
        Returns the size of the input stream.

        Returns
        - The total number of bytes available in the stream, or std::nullopt on error
        """

class FileInputStream(InputStream):
    """
    Implementation of input stream based on a file.

    This class is a specialization of InputStream that reads from a file on disk.

    It wraps a file in the common InputStream interface and therefore allows to use generic classes or functions that accept such a stream, with a file on disk as the data source.

    In addition to the virtual functions inherited from InputStream, FileInputStream adds a function to specify the file to open.

    SFML resource classes can usually be loaded directly from a filename, so this class shouldn't be useful to you unless you create your own algorithms that operate on an InputStream.
    """

    def __init__(self) -> None:
        """
        Implementation of input stream based on a file.

        This class is a specialization of InputStream that reads from a file on disk.

        It wraps a file in the common InputStream interface and therefore allows to use generic classes or functions that accept such a stream, with a file on disk as the data source.

        In addition to the virtual functions inherited from InputStream, FileInputStream adds a function to specify the file to open.

        SFML resource classes can usually be loaded directly from a filename, so this class shouldn't be useful to you unless you create your own algorithms that operate on an InputStream.
        """

    def open(self, filename: str) -> bool:
        """
        Open the stream from a file path.

        Parameters
        - filename: Name of the file to open

        Returns
        - true on success, false on error
        """
