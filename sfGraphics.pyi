"""
2D graphics module: sprites, text, shapes, ...
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
from . import sfWindow

class Glsl(ModuleType):
    """
    Namespace with GLSL types.

    The sf::Glsl namespace contains types that match their equivalents in GLSL, the OpenGL shading language. These types are exclusively used by the sf::Shader class.

    Types that already exist in SFML, such as sf::Vector2<T> and sf::Vector3<T>, are reused as type aliases, so you can use the types in this namespace as well as the original ones. Others are newly defined, such as Glsl::Vec4 or Glsl::Mat3. Their actual type is an implementation detail and should not be used.

    All vector types support a default constructor that initializes every component to zero, in addition to a constructor with one parameter for each component. The components are stored in member variables called x, y, z, and w.

    All matrix types support a constructor with a float* parameter that points to a float array of the appropriate size (that is, 9 in a 3x3 matrix, 16 in a 4x4 matrix). Furthermore, they can be converted from sf::Transform objects.
    """

    class Vec2:
        """
        2D float vector (vec2 in GLSL)
        """
        def __init__(self, x: float, y: float):
            ...

        x: float
        y: float

    class Vec3:
        """
        3D float vector (vec3 in GLSL)
        """
        def __init__(self, x: float, y: float, z: float):
            ...

        x: float
        y: float
        z: float

    class Vec4:
        """
        4D float vector (vec4 in GLSL)
        """
        def __init__(self, x: float, y: float, z: float, w: float):
            ...

        x: float
        y: float
        z: float
        w: float

    class Ivec2:
        """
        2D integer vector (ivec2 in GLSL)
        """
        def __init__(self, x: int, y: int):
            ...

        x: int
        y: int

    class Ivec3:
        """
        3D integer vector (ivec3 in GLSL)
        """
        def __init__(self, x: int, y: int, z: int):
            ...
        x: int
        y: int
        z: int

    class Ivec4:
        """
        4D integer vector (ivec4 in GLSL)
        """
        def __init__(self, x: int, y: int, z: int, w: int):
            ...

        x: int
        y: int
        z: int
        w: int

    class Bvec2:
        """
        2D boolean vector (bvec2 in GLSL)
        """
        def __init__(self, x: bool, y: bool):
            ...
        x: bool
        y: bool

    class Bvec3:
        """
        3D boolean vector (bvec3 in GLSL)
        """
        def __init__(self, x: bool, y: bool, z: bool):
            ...
        x: bool
        y: bool
        z: bool

    class Bvec4:
        """
        4D boolean vector (bvec4 in GLSL)
        """
        def __init__(self, x: bool, y: bool, z: bool, w: bool):
            ...
        x: bool
        y: bool
        z: bool
        w: bool

    class Mat3:
        """
        3x3 float matrix (mat3 in GLSL)

        The matrix can be constructed from an array with 3x3 elements, aligned in column-major order. For example, a translation by (x, y) looks as follows:

        ```
        float array[9] =
        {
            1, 0, 0,
            0, 1, 0,
            x, y, 1
        };

        sf::Glsl::Mat3 matrix(array);
        ```

        Mat3 can also be implicitly converted from sf::Transform:

        ```
        sf::Transform transform;
        sf::Glsl::Mat3 matrix = transform;
        ```
        """
        def __init__(self, array: List[float]):
            ...
        array: List[float]

    class Mat4:
        """
        4x4 float matrix (mat4 in GLSL)

        The matrix can be constructed from an array with 4x4 elements, aligned in column-major order. For example, a translation by (x, y, z) looks as follows:

        ```
        float array[16] =
        {
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            x, y, z, 1
        };

        sf::Glsl::Mat4 matrix(array);
        ```

        Mat4 can also be implicitly converted from sf::Transform:

        ```
        sf::Transform transform;
        sf::Glsl::Mat4 matrix = transform;
        ```
        """
        def __init__(self, array: List[float]):
            ...
        array: List[float]

class CoordinateType(enum.IntEnum):
    """
    Types of texture coordinates that can be used for rendering.

    - Normalized: Texture coordinates in range [0 .. 1].
    - Pixels: Texture coordinates in range [0 .. size].
    """
    Normalized = 0
    Pixels = 1

class PrimitiveType(enum.IntEnum):
    """
    Types of primitives that a sf::VertexArray can render.

    Points and lines have no area, therefore their thickness will always be 1 pixel, regardless the current transform and view.

    - Points: List of individual points.
    - Lines: List of individual lines.
    - LineStrip: List of connected lines, a point uses the previous point to form a line.
    - Triangles: List of individual triangles.
    - TriangleStrip: List of connected triangles, a point uses the two previous points to form a triangle.
    - TriangleFan: List of connected triangles, a point uses the common center and the previous point to form a triangle.
    """
    Points = 0
    Lines = 1
    LinesStrip = 2
    Triangles = 3
    TrianglesStrip = 4
    TrianglesFan = 5

class Drawable:
    """
    Pure virtual base class for drawable objects.
    """

class IntRect:
    """
    Integer rectangle.

    sf::IntRect is a structure that represents a rectangle defined by two positions and two sizes.
    """

    position: sfSystem.Vector2i
    size: sfSystem.Vector2i

    @overload
    def __init__(self):
        """
        Default constructor.

        Creates an empty rectangle (it is equivalent to calling Rect({0, 0}, {0, 0})).
        """

    @overload
    def __init__(self, position: sfSystem.Vector2i, size: sfSystem.Vector2i):
        """
        Construct the rectangle from its position and size.

        Parameters:
        - position: Position of the top-left corner of the rectangle.
        - size: Size of the rectangle.
        """

    def contains(self, point: sfSystem.Vector2i) -> bool:
        """
        Check if a point is inside the rectangle
        """

    @overload
    def find_intersection(self, rectangle: IntRect) -> IntRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """

    @overload
    def find_intersection(self, rectangle: FloatRect) -> IntRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """

    def get_center(self) -> sfSystem.Vector2i:
        """
        Get the center of the rectangle.

        Returns:
        - The center of the rectangle.
        """

class FloatRect:
    """
    Float rectangle.

    sf::FloatRect is a structure that represents a rectangle defined by two positions and two sizes.
    """

    position: sfSystem.Vector2f
    size: sfSystem.Vector2f

    @overload
    def __init__(self):
        """
        Default constructor.

        Creates an empty rectangle (it is equivalent to calling Rect({0, 0}, {0, 0})).
        """

    @overload
    def __init__(self, position: sfSystem.Vector2f, size: sfSystem.Vector2f):
        """
        Construct the rectangle from its position and size.

        Parameters:
        - position: Position of the top-left corner of the rectangle.
        - size: Size of the rectangle.
        """

    def contains(self, point: sfSystem.Vector2f) -> bool:
        """
        Check if a point is inside the rectangle
        """

    @overload
    def find_intersection(self, rectangle: IntRect) -> FloatRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """

    @overload
    def find_intersection(self, rectangle: FloatRect) -> FloatRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """

    def get_center(self) -> sfSystem.Vector2f:
        """
        Get the center of the rectangle.

        Returns:
        - The center of the rectangle.
        """

class BlendMode:
    """
    Blending modes for drawing.

    sf::BlendMode is a class that represents a blend mode.

    A blend mode determines how the colors of an object you draw are mixed with the colors that are already in the buffer.

    The class is composed of 6 components, each of which has its own public member variable:

    - Color Source Factor (colorSrcFactor)
    - Color Destination Factor (colorDstFactor)
    - Color Blend Equation (colorEquation)
    - Alpha Source Factor (alphaSrcFactor)
    - Alpha Destination Factor (alphaDstFactor)
    - Alpha Blend Equation (alphaEquation)

    The source factor specifies how the pixel you are drawing contributes to the final color. The destination factor specifies how the pixel already drawn in the buffer contributes to the final color.

    The color channels RGB (red, green, blue; simply referred to as color) and A (alpha; the transparency) can be treated separately. This separation can be useful for specific blend modes, but most often you won't need it and will simply treat the color as a single unit.

    The blend factors and equations correspond to their OpenGL equivalents. In general, the color of the resulting pixel is calculated according to the following formula (src is the color of the source pixel, dst the color of the destination pixel, the other variables correspond to the public members, with the equations being + or - operators):

    ```
    dst.rgb = colorSrcFactor * src.rgb (colorEquation) colorDstFactor * dst.rgb
    dst.a   = alphaSrcFactor * src.a   (alphaEquation) alphaDstFactor * dst.a
    ```

    All factors and colors are represented as floating point numbers between 0 and 1. Where necessary, the result is clamped to fit in that range.

    The most common blending modes are defined as constants in the sf namespace:

    ```
    sf::BlendMode alphaBlending          = sf::BlendAlpha;
    sf::BlendMode additiveBlending       = sf::BlendAdd;
    sf::BlendMode multiplicativeBlending = sf::BlendMultiply;
    sf::BlendMode noBlending             = sf::BlendNone;
    ```

    In SFML, a blend mode can be specified every time you draw a sf::Drawable object to a render target. It is part of the sf::RenderStates compound that is passed to the member function sf::RenderTarget::draw().
    """
    class Factor(enum.IntEnum):
        """
        Enumeration of the blending factors.

        The factors are mapped directly to their OpenGL equivalents, specified by glBlendFunc() or glBlendFuncSeparate().

        - Zero: (0, 0, 0, 0)
        - One: (1, 1, 1, 1)
        - SrcColor: (src.r, src.g, src.b, src.a)
        - OneMinusSrcColor: (1, 1, 1, 1) - (src.r, src.g, src.b, src.a)
        - DstColor: (dst.r, dst.g, dst.b, dst.a)
        - OneMinusDstColor: (1, 1, 1, 1) - (dst.r, dst.g, dst.b, dst.a)
        - SrcAlpha: (src.a, src.a, src.a, src.a)
        - OneMinusSrcAlpha: (1, 1, 1, 1) - (src.a, src.a, src.a, src.a)
        - DstAlpha: (dst.a, dst.a, dst.a, dst.a)
        - OneMinusDstAlpha: (1, 1, 1, 1) - (dst.a, dst.a, dst.a, dst.a)
        """
        Zero = 0
        One = 1
        SrcColor = 2
        OneMinusSrcColor = 3
        DstColor = 4
        OneMinusDstColor = 5
        SrcAlpha = 6
        OneMinusSrcAlpha = 7
        DstAlpha = 8
        OneMinusDstAlpha = 9

    class Equation(enum.IntEnum):
        """
        Enumeration of the blending equations.

        The equations are mapped directly to their OpenGL equivalents, specified by glBlendEquation() or glBlendEquationSeparate().

        - Add: Pixel = Src * SrcFactor + Dst * DstFactor.
        - Subtract: Pixel = Src * SrcFactor - Dst * DstFactor.
        - ReverseSubtract: Pixel = Dst * DstFactor - Src * SrcFactor.
        - Min: Pixel = min(Dst, Src)
        - Max: Pixel = max(Dst, Src)
        """
        Add = 0
        Subtract = 1
        ReverseSubtract = 2
        Min = 3
        Max = 4

    @overload
    def __init__(self, sourceFactor: Factor, destinationFactor: Factor, blendEquation: Factor = Equation.Add) -> None:
        """
        Construct the blend mode given the factors and equation.

        This constructor uses the same factors and equation for both color and alpha components. It also defaults to the Add equation.

        Parameters
        - sourceFactor	Specifies how to compute the source factor for the color and alpha channels.
        - destinationFactor	Specifies how to compute the destination factor for the color and alpha channels.
        - blendEquation	Specifies how to combine the source and destination colors and alpha.

        """

    @overload
    def __init__(self, colorSourceFactor: Factor, colorDestinationFactor: Factor, colorBlendEquation: Factor, alphaSourceFactor: Factor, alphaDestinationFactor: Factor, alphaBlendEquation: Factor) -> None:
        """
        Construct the blend mode given the factors and equation.

        Parameters
        - colorSourceFactor	Specifies how to compute the source factor for the color channels.
        - colorDestinationFactor	Specifies how to compute the destination factor for the color channels.
        - colorBlendEquation	Specifies how to combine the source and destination colors.
        - alphaSourceFactor	Specifies how to compute the source factor.
        - alphaDestinationFactor	Specifies how to compute the destination factor.
        - alphaBlendEquation	Specifies how to combine the source and destination alphas.
        """

    color_src_factor: Factor
    color_dst_factor: Factor
    color_equation: Equation
    alpha_src_factor: Factor
    alpha_dst_factor: Factor
    alpha_equation: Equation

blend_alpha: BlendMode
blend_add: BlendMode
blend_multiply: BlendMode
blend_min: BlendMode
blend_max: BlendMode
blend_none: BlendMode

class Transform:
    """
    3x3 transform matrix

    A sf::Transform specifies how to translate, rotate, scale, shear, project, whatever things.

    In mathematical terms, it defines how to transform a coordinate system into another.

    For example, if you apply a rotation transform to a sprite, the result will be a rotated sprite. And anything that is transformed by this rotation transform will be rotated the same way, according to its initial position.

    Transforms are typically used for drawing. But they can also be used for any computation that requires to transform points between the local and global coordinate systems of an entity (like collision detection).
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Creates an identity transform (a transform that does nothing).
        """

    @overload
    def __init__(self, a00: float, a01: float, a02: float, a10: float, a11: float, a12: float, a20: float, a21: float, a22: float) -> None:
        """
        Construct a transform from a 3x3 matrix.

        Parameters
        - a00	Element (0, 0) of the matrix
        - a01	Element (0, 1) of the matrix
        - a02	Element (0, 2) of the matrix
        - a10	Element (1, 0) of the matrix
        - a11	Element (1, 1) of the matrix
        - a12	Element (1, 2) of the matrix
        - a20	Element (2, 0) of the matrix
        - a21	Element (2, 1) of the matrix
        - a22	Element (2, 2) of the matrix
        """

    def get_matrix(self) -> List[float]:
        """
        Return the transform as a 4x4 matrix.

        This function returns a pointer to an array of 16 floats containing the transform elements as a 4x4 matrix, which is directly compatible with OpenGL functions.

        ```
        sf::Transform transform = ...;
        glLoadMatrixf(transform.getMatrix());
        ```

        Returns
        - Pointer to a 4x4 matrix
        """

    def get_inverse(self) -> Transform:
        """
        Return the inverse of the transform.

        If the inverse cannot be computed, an identity transform is returned.

        Returns
        - A new transform which is the inverse of self
        """

    def transform_point(self, point: sfSystem.Vector2f) -> sfSystem.Vector2f:
        """
        Transform a 2D point.

        These two statements are equivalent:

        ```
        sf::Vector2f transformedPoint = matrix.transformPoint(point);
        sf::Vector2f transformedPoint = matrix * point;
        ```

        Parameters
        - point	Point to transform

        Returns
        - Transformed point
        """

    def transform_rect(self, rectangle: FloatRect) -> FloatRect:
        """
        Transform a rectangle.

        Since SFML doesn't provide support for oriented rectangles, the result of this function is always an axis-aligned rectangle. Which means that if the transform contains a rotation, the bounding rectangle of the transformed rectangle is returned.

        Parameters
        - rectangle	Rectangle to transform

        Returns
        - Transformed rectangle
        """

    def combine(self, transform: Transform) -> Transform:
        """
        Combine the current transform with another one.

        The result is a transform that is equivalent to applying transform followed by *this. Mathematically, it is equivalent to a matrix multiplication (*this) * transform.

        These two statements are equivalent:

        ```
        left.combine(right);
        left *= right;
        ```

        Parameters
        - transform	Transform to combine with this transform

        Returns
        - Reference to *this
        """

    def translate(self, offset: sfSystem.Vector2f) -> Transform:
        """
        Combine the current transform with a translation.

        This function returns a reference to *this, so that calls can be chained.

        ```
        sf::Transform transform;
        transform.translate(sf::Vector2f(100, 200)).rotate(sf::degrees(45));
        ```

        Parameters
        - offset	Translation offset to apply

        Returns
        - Reference to *this
        """

    @overload
    def rotate(self, angle: float) -> Transform:
        """
        Combine the current transform with a rotation.

        This function returns a reference to *this, so that calls can be chained.

        ```
        sf::Transform transform;
        transform.rotate(sf::degrees(90)).translate(50, 20);
        ```

        Parameters
        - angle	Rotation angle

        Returns
        - Reference to *this
        """

    @overload
    def rotate(self, angle: float, center: sfSystem.Vector2f) -> Transform:
        """
        Combine the current transform with a rotation.

        The center of rotation is provided for convenience as a second argument, so that you can build rotations around arbitrary points more easily (and efficiently) than the usual translate(-center).rotate(angle).translate(center).

        This function returns a reference to *this, so that calls can be chained.

        ```
        sf::Transform transform;
        transform.rotate(sf::degrees(90), sf::Vector2f(8, 3)).translate(sf::Vector2f(50, 20));
        ```

        Parameters
        - angle	Rotation angle
        - center	Center of rotation

        Returns
        - Reference to *this
        """

    @overload
    def scale(self, factors: sfSystem.Vector2f) -> Transform:
        """
        Combine the current transform with a scaling.

        This function returns a reference to *this, so that calls can be chained.

        ```
        sf::Transform transform;
        transform.scale(sf::Vector2f(2, 1)).rotate(sf::degrees(45));
        ```

        Parameters
        - factors	Scaling factors

        Returns
        - Reference to *this
        """

    @overload
    def scale(self, factors: sfSystem.Vector2f, center: sfSystem.Vector2f) -> Transform:
        """
        Combine the current transform with a scaling.

        The center of scaling is provided for convenience as a second argument, so that you can build scaling around arbitrary points more easily (and efficiently) than the usual translate(-center).scale(factors).translate(center).

        This function returns a reference to *this, so that calls can be chained.

        ```
        sf::Transform transform;
        transform.scale(sf::Vector2f(2, 1), sf::Vector2f(8, 3)).rotate(45);
        ```

        Parameters
        - factors	Scaling factors
        - center	Center of scaling

        Returns
        - Reference to *this
        """

    @staticmethod
    def identity() -> Transform:
        """
        The identity transform (does nothing)
        """

class Transformable:
    """
    Decomposed transform defined by a position, a rotation and a scale.

    This class is provided for convenience, on top of sf::Transform.

    sf::Transform, as a low-level class, offers a great level of flexibility but it is not always convenient to manage. Indeed, one can easily combine any kind of operation, such as a translation followed by a rotation followed by a scaling, but once the result transform is built, there's no way to go backward and, let's say, change only the rotation without modifying the translation and scaling. The entire transform must be recomputed, which means that you need to retrieve the initial translation and scale factors as well, and combine them the same way you did before updating the rotation. This is a tedious operation, and it requires to store all the individual components of the final transform.

    That's exactly what sf::Transformable was written for: it hides these variables and the composed transform behind an easy to use interface. You can set or get any of the individual components without worrying about the others. It also provides the composed transform (as a sf::Transform), and keeps it up-to-date.

    In addition to the position, rotation and scale, sf::Transformable provides an "origin" component, which represents the local origin of the three other components. Let's take an example with a 10x10 pixels sprite. By default, the sprite is positioned/rotated/scaled relatively to its top-left corner, because it is the local point (0, 0). But if we change the origin to be (5, 5), the sprite will be positioned/rotated/scaled around its center instead. And if we set the origin to (10, 10), it will be transformed around its bottom-right corner.

    To keep the sf::Transformable class simple, there's only one origin for all the components. You cannot position the sprite relatively to its top-left corner while rotating it around its center, for example. To do such things, use sf::Transform directly.

    sf::Transformable can be used as a base class. It is often combined with sf::Drawable – that's what SFML's sprites, texts and shapes do.

    It can also be used as a member, if you don't want to use its API directly (because you don't need all its functions, or you have different naming conventions for example).

    A note on coordinates and undistorted rendering:

    By default, SFML (or more exactly, OpenGL) may interpolate drawable objects such as sprites or texts when rendering. While this allows transitions like slow movements or rotations to appear smoothly, it can lead to unwanted results in some cases, for example blurred or distorted objects. In order to render a sf::Drawable object pixel-perfectly, make sure the involved coordinates allow a 1:1 mapping of pixels in the window to texels (pixels in the texture). More specifically, this means:

    - The object's position, origin and scale have no fractional part
    - The object's and the view's rotation are a multiple of 90 degrees
    - The view's center and size have no fractional part
    """
    def __init__(self) -> None:
        """
        Default constructor.
        """

    def set_position(self, position: sfSystem.Vector2f) -> None:
        """
        set the position of the object

        This function completely overwrites the previous position. See the move function to apply an offset based on the previous position instead. The default position of a transformable object is (0, 0).

        Parameters
        - position	New position
        """

    def set_rotation(self, angle: float) -> None:
        """
        set the orientation of the object

        This function completely overwrites the previous rotation. See the rotate function to add an angle based on the previous rotation instead. The default rotation of a transformable object is 0.

        Parameters
        - angle	New rotation
        """

    def set_scale(self, factors: sfSystem.Vector2f) -> None:
        """
        set the scale factors of the object

        This function completely overwrites the previous scale. See the scale function to add a factor based on the previous scale instead. The default scale of a transformable object is (1, 1).

        Parameters
        - factors	New scale factors
        """

    def set_origin(self, origin: sfSystem.Vector2f) -> None:
        """
        set the local origin of the object

        The origin of an object defines the center point for all transformations (position, scale, rotation). The coordinates of this point must be relative to the top-left corner of the object, and ignore all transformations (position, scale, rotation). The default origin of a transformable object is (0, 0).

        Parameters
        - origin	New origin
        """

    def get_position(self) -> sfSystem.Vector2f:
        """
        get the position of the object

        Returns
        - Current position
        """

    def get_rotation(self) -> float:
        """
        get the orientation of the object

        The rotation is always in the range [0, 360].

        Returns
        - Current rotation
        """

    def get_scale(self) -> sfSystem.Vector2f:
        """
        get the current scale of the object

        Returns
        - Current scale factor
        """

    def get_origin(self) -> sfSystem.Vector2f:
        """
        get the local origin of the object

        Returns
        - Current origin
        """

    def move(self, offset: sfSystem.Vector2f) -> None:
        """
        Move the object by a given offset.

        This function adds to the current position of the object, unlike setPosition which overwrites it. Thus, it is equivalent to the following code:

        ```
        object.setPosition(object.getPosition() + offset);
        ```

        Parameters
        - offset	Offset
        """

    def rotate(self, angle: float) -> None:
        """
        Rotate the object.

        This function adds to the current rotation of the object, unlike setRotation which overwrites it. Thus, it is equivalent to the following code:

        ```
        object.setRotation(object.getRotation() + angle);
        ```

        Parameters
        - angle	Angle of rotation
        """

    def scale(self, factor: sfSystem.Vector2f) -> None:
        """
        Scale the object.

        This function multiplies the current scale of the object, unlike setScale which overwrites it. Thus, it is equivalent to the following code:

        ```
        sf::Vector2f scale = object.getScale();
        object.setScale(scale.x * factor.x, scale.y * factor.y);
        ```

        Parameters
        - factor	Scale factors
        """

    def get_transform(self) -> Transform:
        """
        get the combined transform of the object

        Returns
        - Transform combining the position/rotation/scale/origin of the object
        """

    def get_inverse_transform(self) -> Transform:
        """
        get the inverse of the combined transform of the object

        Returns
        - Inverse of the combined transformations applied to the object
        """

class Vertex:
    """
    Point with color and texture coordinates.

    A vertex is an improved point.

    By default, the vertex color is white and texture coordinates are (0, 0).

    It has a position and other extra attributes that will be used for drawing: in SFML, vertices also have a color and a pair of texture coordinates.

    The vertex is the building block of drawing. Everything which is visible on screen is made of vertices. They are grouped as 2D primitives (lines, triangles, ...), and these primitives are grouped to create even more complex 2D entities such as sprites, texts, etc.

    If you use the graphical entities of SFML (sprite, text, shape) you won't have to deal with vertices directly. But if you want to define your own 2D entities, such as tiled maps or particle systems, using vertices will allow you to get maximum performances.

    It is recommended to use aggregate initialization to create vertex objects, which initializes the members in order.

    On a C++20-compliant compiler (or where supported as an extension) it is possible to use "designated initializers" to only initialize a subset of members, with the restriction of having to follow the same order in which they are defined.

    Note: Although texture coordinates are supposed to be an integer amount of pixels, their type is float because of some buggy graphics drivers that are not able to process integer coordinates correctly.
    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, position: sfSystem.Vector2f, color: Color, texCoords: sfSystem.Vector2f) -> None:
        ...

    position: sfSystem.Vector2f
    color: Color
    texCoords: sfSystem.Vector2f

class VertexArray(Drawable):
    """
    Set of one or more 2D primitives.

    sf::VertexArray is a very simple wrapper around a dynamic array of vertices and a primitives type.

    It inherits sf::Drawable, but unlike other drawables it is not transformable.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Creates an empty vertex array.
        """

    @overload
    def __init__(self, type_: PrimitiveType, vertexCount: int = 0) -> None:
        """
        Construct the vertex array with a type and an initial number of vertices.

        Parameters
        - type_	Type of primitives
        - vertexCount	Initial number of vertices in the array
        """

    @overload
    def __getitem__(self, index: int) -> Vertex:
        """
        Subscript operator for read-only access to a vertex.

        The returned vertex is a copy of the vertex in the array,
        so that you can modify it without affecting the original.
        """

    @overload
    def __setitem__(self, index: int, value: Vertex) -> None:
        """
        Subscript operator for write access to a vertex.

        This function provides write access to a vertex in the array.
        """

    def get_vertex_count(self) -> int:
        """
        Return the vertex count.

        Returns
        - Number of vertices in the array
        """

    def clear(self) -> None:
        """
        Clear the vertex array.

        This function removes all the vertices from the array. It doesn't deallocate the corresponding memory, so that adding new vertices after clearing doesn't involve reallocating all the memory.
        """

    def resize(self, vertexCount: int) -> None:
        """
        Resize the vertex array.

        If vertexCount is greater than the current size, the previous vertices are kept and new (default-constructed) vertices are added. If vertexCount is less than the current size, existing vertices are removed from the array.

        Parameters
        - vertexCount	New size of the array (number of vertices)
        """

    def append(self, vertex: Vertex) -> None:
        """
        Add a vertex to the array.

        Parameters
        - vertex	Vertex to add
        """

    def set_primitive_type(self, type_: PrimitiveType) -> None:
        """
        Set the type of primitives to draw.

        This function defines how the vertices must be interpreted when it's time to draw them:

        - As points
        - As lines
        - As triangles The default primitive type is sf::PrimitiveType::Points.

        Parameters
        - type_	Type of primitive
        """

    def get_primitive_type(self) -> PrimitiveType:
        """
        Get the type of primitives drawn by the vertex array.

        Returns
        - Primitive type
        """

    def get_bounds(self) -> FloatRect:
        """
        Compute the bounding rectangle of the vertex array.

        This function returns the minimal axis-aligned rectangle that contains all the vertices of the array.

        Returns
        - Bounding rectangle of the vertex array
        """

class VertexBuffer(Drawable):
    """
    Vertex buffer storage for one or more 2D primitives.

    sf::VertexBuffer is a simple wrapper around a dynamic buffer of vertices and a primitives type.

    Unlike sf::VertexArray, the vertex data is stored in graphics memory.

    In situations where a large amount of vertex data would have to be transferred from system memory to graphics memory every frame, using sf::VertexBuffer can help. By using a sf::VertexBuffer, data that has not been changed between frames does not have to be re-transferred from system to graphics memory as would be the case with sf::VertexArray. If data transfer is a bottleneck, this can lead to performance gains.

    Using sf::VertexBuffer, the user also has the ability to only modify a portion of the buffer in graphics memory. This way, a large buffer can be allocated at the start of the application and only the applicable portions of it need to be updated during the course of the application. This allows the user to take full control of data transfers between system and graphics memory if they need to.

    In special cases, the user can make use of multiple threads to update vertex data in multiple distinct regions of the buffer simultaneously. This might make sense when e.g. the position of multiple objects has to be recalculated very frequently. The computation load can be spread across multiple threads as long as there are no other data dependencies.

    Simultaneous updates to the vertex buffer are not guaranteed to be carried out by the driver in any specific order. Updating the same region of the buffer from multiple threads will not cause undefined behavior, however the final state of the buffer will be unpredictable.

    Simultaneous updates of distinct non-overlapping regions of the buffer are also not guaranteed to complete in a specific order. However, in this case the user can make sure to synchronize the writer threads at well-defined points in their code. The driver will make sure that all pending data transfers complete before the vertex buffer is sourced by the rendering pipeline.

    It inherits sf::Drawable, but unlike other drawables it is not transformable.
    """

    class Usage(enum.IntEnum):
        """
        Usage specifiers.

        If data is going to be updated once or more every frame, set the usage to Stream. If data is going to be set once and used for a long time without being modified, set the usage to Static. For everything else Dynamic should be a good compromise.

        - Stream: Constantly changing data.
        - Dynamic: Occasionally changing data.
        - Static: Rarely changing data.
        """
        Static = 0
        Dynamic = 1
        Stream = 2

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Creates an empty vertex buffer.
        """

    @overload
    def __init__(self, primitiveType: PrimitiveType) -> None:
        """
        Construct a VertexBuffer with a specific PrimitiveType

        Creates an empty vertex buffer and sets its primitive type to type.

        Parameters
        - type	Type of primitive
        """

    @overload
    def __init__(self, usage: Usage) -> None:
        """
        Construct a VertexBuffer with a specific usage specifier.

        Creates an empty vertex buffer and sets its usage to usage.

        Parameters
        - usage	Usage specifier
        """

    @overload
    def __init__(self, type_: PrimitiveType, usage: Usage) -> None:
        """
        Construct a VertexBuffer with a specific PrimitiveType and usage specifier.

        Creates an empty vertex buffer and sets its primitive type to type and usage to usage.

        Parameters
        - type_	Type of primitive
        - usage	Usage specifier
        """

    def create(self, vertexCount: int) -> bool:
        """
        Create the vertex buffer.

        Creates the vertex buffer and allocates enough graphics memory to hold vertexCount vertices. Any previously allocated memory is freed in the process.

        In order to deallocate previously allocated memory pass 0 as vertexCount. Don't forget to recreate with a non-zero value when graphics memory should be allocated again.

        Parameters
        - vertexCount	Number of vertices worth of memory to allocate

        Returns
        - true if creation was successful
        """

    def get_vertex_count(self) -> int:
        """
        Return the vertex count.

        Returns
        - Number of vertices in the vertex buffer
        """

    @overload
    def update(self, vertices: List[Vertex]) -> bool:
        """
        Update the whole buffer from an array of vertices.

        The vertex array is assumed to have the same size as the created buffer.

        No additional check is performed on the size of the vertex array. Passing invalid arguments will lead to undefined behavior.

        This function does nothing if vertices is null or if the buffer was not previously created.

        Parameters
        - vertices	Array of vertices to copy to the buffer

        Returns
        - true if the update was successful
        """

    @overload
    def update(self, vertices: List[Vertex], vertexCount: int, offset: int) -> bool:
        """
        Update a part of the buffer from an array of vertices.

        offset is specified as the number of vertices to skip from the beginning of the buffer.

        If offset is 0 and vertexCount is equal to the size of the currently created buffer, its whole contents are replaced.

        If offset is 0 and vertexCount is greater than the size of the currently created buffer, a new buffer is created containing the vertex data.

        If offset is 0 and vertexCount is less than the size of the currently created buffer, only the corresponding region is updated.

        If offset is not 0 and offset + vertexCount is greater than the size of the currently created buffer, the update fails.

        No additional check is performed on the size of the vertex array. Passing invalid arguments will lead to undefined behavior.

        Parameters
        - vertices	Array of vertices to copy to the buffer
        - vertexCount	Number of vertices to copy
        - offset	Offset in the buffer to copy to

        Returns
        - true if the update was successful
        """

    @overload
    def update(self, vertexBuffer: VertexBuffer) -> bool:
        """
        Copy the contents of another buffer into this buffer.

        Parameters
        - vertexBuffer	Vertex buffer whose contents to copy into this vertex buffer

        Returns
        - true if the copy was successful
        """

    def set_primitive_type(self, type_: PrimitiveType) -> None:
        """
        Set the type of primitives to draw.

        This function defines how the vertices must be interpreted when it's time to draw them.

        The default primitive type is sf::PrimitiveType::Points.

        Parameters
        - type_	Type of primitive
        """

    def get_primitive_type(self) -> PrimitiveType:
        """
        Get the type of primitives drawn by the vertex buffer.

        Returns
        - Primitive type
        """

    def set_usage(self, usage: Usage) -> None:
        """
        Set the usage specifier of this vertex buffer.

        This function provides a hint about how this vertex buffer is going to be used in terms of data update frequency.

        After changing the usage specifier, the vertex buffer has to be updated with new data for the usage specifier to take effect.

        The default usage type is sf::VertexBuffer::Usage::Stream.

        Parameters
        - usage	Usage specifier
        """

    def get_usage(self) -> Usage:
        """
        Get the usage specifier of this vertex buffer.

        Returns
        - Usage specifier
        """

    def get_native_handle(self) -> int:
        """
        Get the underlying OpenGL handle of the vertex buffer.

        You shouldn't need to use this function, unless you have very specific stuff to implement that SFML doesn't support, or implement a temporary workaround until a bug is fixed.

        Returns
        - OpenGL handle of the vertex buffer or 0 if not yet created
        """

    @staticmethod
    def bind(vertexBuffer: VertexBuffer) -> None:
        """
        Bind a vertex buffer for rendering.

        This function is not part of the graphics API, it mustn't be used when drawing SFML entities. It must be used only if you mix sf::VertexBuffer with OpenGL code.

        ```
        sf::VertexBuffer vb1, vb2;
        ...
        sf::VertexBuffer::bind(&vb1);
        // draw OpenGL stuff that use vb1
        ...
        sf::VertexBuffer::bind(&vb2);
        // draw OpenGL stuff that use vb2
        ...
        sf::VertexBuffer::bind(nullptr);
        // draw OpenGL stuff that use no vertex buffer
        ...
        ```

        Parameters
        - vertexBuffer	Pointer to the vertex buffer to bind, can be null to use no vertex buffer
        """

    @staticmethod
    def is_available() -> bool:
        """
        Tell whether or not the system supports vertex buffers.

        This function should always be called before using the vertex buffer features. If it returns false, then any attempt to use sf::VertexBuffer will fail.

        Returns
        - true if vertex buffers are supported, false otherwise
        """

class Shape(Transformable, Drawable):
    """
    Base class for textured shapes with outline.

    sf::Shape is a drawable class that allows to define and display a custom convex shape on a render target.

    It's only an abstract base, it needs to be specialized for concrete types of shapes (circle, rectangle, convex polygon, star, ...).

    In addition to the attributes provided by the specialized shape classes, a shape always has the following attributes:

    - a texture
    - a texture rectangle
    - a fill color
    - an outline color
    - an outline thickness

    Each feature is optional, and can be disabled easily:

    - the texture can be null
    - the fill/outline colors can be sf::Color::Transparent
    - the outline thickness can be zero

    You can write your own derived shape class, there are only two virtual functions to override:

    - getPointCount must return the number of points of the shape
    - getPoint must return the points of the shape
    """
    def set_texture(self, texture: Texture, resetRect: bool = False) -> None:
        """
        Change the source texture of the shape.

        The texture argument refers to a texture that must exist as long as the shape uses it. Indeed, the shape doesn't store its own copy of the texture, but rather keeps a pointer to the one that you passed to this function. If the source texture is destroyed and the shape tries to use it, the behavior is undefined. texture can be a null pointer to disable texturing. If resetRect is true, the TextureRect property of the shape is automatically adjusted to the size of the new texture. If it is false, the texture rect is left unchanged.

        Parameters
        - texture	New texture
        - resetRect	Should the texture rect be reset to the size of the new texture?
        """

    def set_texture_rect(self, rect: IntRect) -> None:
        """
        Set the sub-rectangle of the texture that the shape will display.

        The texture rect is useful when you don't want to display the whole texture, but rather a part of it. By default, the texture rect covers the entire texture.

        Parameters
        - rect	Rectangle defining the region of the texture to display
        """

    def set_fill_color(self, color: Color) -> None:
        """
        Set the fill color of the shape.

        This color is modulated (multiplied) with the shape's texture if any. It can be used to colorize the shape, or change its global opacity. You can use sf::Color::Transparent to make the inside of the shape transparent, and have the outline alone. By default, the shape's fill color is opaque white.

        Parameters
        - color	New color of the shape
        """

    def set_outline_color(self, color: Color) -> None:
        """
        Set the outline color of the shape.

        By default, the shape's outline color is opaque white.

        Parameters
        - color	New outline color of the shape
        """

    def set_outline_thickness(self, thickness: float) -> None:
        """
        Set the thickness of the shape's outline.

        Note that negative values are allowed (so that the outline expands towards the center of the shape), and using zero disables the outline. By default, the outline thickness is 0.

        Parameters
        - thickness	New outline thickness
        """

    def get_texture(self) -> Texture:
        """
        Get the source texture of the shape.

        If the shape has no source texture, a nullptr is returned. The returned pointer is const, which means that you can't modify the texture when you retrieve it with this function.

        Returns
        - Pointer to the shape's texture
        """

    def get_texture_rect(self) -> IntRect:
        """
        Get the sub-rectangle of the texture displayed by the shape.

        Returns
        - Texture rectangle of the shape
        """

    def get_fill_color(self) -> Color:
        """
        Get the fill color of the shape.

        Returns
        - Fill color of the shape
        """

    def get_outline_color(self) -> Color:
        """
        Get the outline color of the shape.

        Returns
        - Outline color of the shape
        """

    def get_outline_thickness(self) -> float:
        """
        Get the outline thickness of the shape.

        Returns
        - Outline thickness of the shape
        """

    def get_point_count(self) -> int:
        """
        Get the total number of points of the shape.

        Returns
        - Number of points of the shape
        """

    def get_point(self, index: int) -> sfSystem.Vector2f:
        """
        Get a point of the shape.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. getPointCount() - 1]

        Returns
        - index-th point of the shape
        """

    def get_geometric_center(self) -> sfSystem.Vector2f:
        """
        Get the geometric center of the shape.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account.

        Returns
        - The geometric center of the shape
        """

    def get_local_bounds(self) -> FloatRect:
        """
        Get the local bounding rectangle of the entity.

        The returned rectangle is in local coordinates, which means that it ignores the transformations (translation, rotation, scale, ...) that are applied to the entity. In other words, this function returns the bounds of the entity in the entity's coordinate system.

        Returns
        - Local bounding rectangle of the entity
        """

    def get_global_bounds(self) -> FloatRect:
        """
        Get the global (non-minimal) bounding rectangle of the entity.

        The returned rectangle is in global coordinates, which means that it takes into account the transformations (translation, rotation, scale, ...) that are applied to the entity. In other words, this function returns the bounds of the shape in the global 2D world's coordinate system.

        This function does not necessarily return the minimal bounding rectangle. It merely ensures that the returned rectangle covers all the vertices (but possibly more). This allows for a fast approximation of the bounds as a first check; you may want to use more precise checks on top of that.

        Returns
        - Global bounding rectangle of the entity
        """

class Color:
    """
    Utility class for manipulating RGBA colors.

    sf::Color is a simple color class composed of 4 components:

    - Red
    - Green
    - Blue
    - Alpha (opacity)

    Each component is a public member, an unsigned integer in the range [0, 255]. Thus, colors can be constructed and manipulated very easily:

    ```
    sf::Color color(255, 0, 0); // red
    color.r = 0;                // make it black
    color.b = 128;              // make it dark blue
    ```

    The fourth component of colors, named "alpha", represents the opacity of the color. A color with an alpha value of 255 will be fully opaque, while an alpha value of 0 will make a color fully transparent, whatever the value of the other components is.

    The most common colors are already defined as static variables:

    ```
    sf::Color black       = sf::Color::Black;
    sf::Color white       = sf::Color::White;
    sf::Color red         = sf::Color::Red;
    sf::Color green       = sf::Color::Green;
    sf::Color blue        = sf::Color::Blue;
    sf::Color yellow      = sf::Color::Yellow;
    sf::Color magenta     = sf::Color::Magenta;
    sf::Color cyan        = sf::Color::Cyan;
    sf::Color transparent = sf::Color::Transparent;
    ```

    Colors can also be added and modulated (multiplied) using the overloaded operators + and *.
    """

    @overload
    def __init__(self, color: bytes) -> None:
        """
        Construct the color from 32-bit unsigned integer.

        Parameters
        - color	Number containing the RGBA components (in that order)
        """

    @overload
    def __init__(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """
        Construct the color from its 4 RGBA components.

        Parameters
        - red	Red component (in the range [0, 255])
        - green	Green component (in the range [0, 255])
        - blue	Blue component (in the range [0, 255])
        - alpha	Alpha (opacity) component (in the range [0, 255])
        """

    def to_integer(self) -> int:
        """
        Retrieve the color as a 32-bit unsigned integer.

        Returns
        - Color represented as a 32-bit unsigned integer
        """

    r: int
    g: int
    b: int
    a: int

    @staticmethod
    def black() -> Color:
        """
        Black color.
        """
    @staticmethod
    def white() -> Color:
        """
        White color.
        """
    @staticmethod
    def red() -> Color:
        """
        Red color.
        """
    @staticmethod
    def green() -> Color:
        """
        Green color.
        """
    @staticmethod
    def blue() -> Color:
        """
        Blue color.
        """
    @staticmethod
    def yellow() -> Color:
        """
        Yellow color.
        """
    @staticmethod
    def magenta() -> Color:
        """
        Magenta color.
        """
    @staticmethod
    def cyan() -> Color:
        """
        Cyan color.
        """
    @staticmethod
    def transparent() -> Color:
        """
        Transparent color.
        """

class Font:
    """
    Class for loading and manipulating character fonts.

    Fonts can be opened from a file, from memory or from a custom stream, and supports the most common types of fonts.

    See the openFromFile function for the complete list of supported formats.

    Once it is opened, a sf::Font instance provides three types of information about the font:

    - Global metrics, such as the line spacing
    - Per-glyph metrics, such as bounding box or kerning
    - Pixel representation of glyphs

    Fonts alone are not very useful: they hold the font data but cannot make anything useful of it. To do so you need to use the sf::Text class, which is able to properly output text with several options such as character size, style, color, position, rotation, etc. This separation allows more flexibility and better performances: indeed a sf::Font is a heavy resource, and any operation on it is slow (often too slow for real-time applications). On the other side, a sf::Text is a lightweight object which can combine the glyphs data and metrics of a sf::Font to display any text on a render target. Note that it is also possible to bind several sf::Text instances to the same sf::Font.

    It is important to note that the sf::Text instance doesn't copy the font that it uses, it only keeps a reference to it. Thus, a sf::Font must not be destructed while it is used by a sf::Text (i.e. never write a function that uses a local sf::Font instance for creating a text).

    Apart from opening font files, and passing them to instances of sf::Text, you should normally not have to deal directly with this class. However, it may be useful to access the font metrics or rasterized glyphs for advanced usage.

    Note that if the font is a bitmap font, it is not scalable, thus not all requested sizes will be available to use. This needs to be taken into consideration when using sf::Text. If you need to display text of a certain size, make sure the corresponding bitmap font that supports that size is used.
    """

    class Info:
        """
        Holds various information about a font.
        """

        def __init__(self) -> None:
            ...

        family: str

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Construct an empty font that does not contain any glyphs.
        """

    @overload
    def __init__(self, data: bytes, sizeInBytes: bytes) -> None:
        """
        Construct the font from a file in memory.

        The supported font formats are: TrueType, Type 1, CFF, OpenType, SFNT, X11 PCF, Windows FNT, BDF, PFR and Type 42.

        Warning
        - SFML cannot preload all the font data in this function, so the buffer pointed by data has to remain valid until the sf::Font object opens a new font or is destroyed.

        Parameters
        - data	Pointer to the file data in memory
        - sizeInBytes	Size of the data to load, in bytes

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, stream: sfSystem.InputStream) -> None:
        """
        Construct the font from a custom stream.

        The supported font formats are: TrueType, Type 1, CFF, OpenType, SFNT, X11 PCF, Windows FNT, BDF, PFR and Type 42. Warning: SFML cannot preload all the font data in this function, so the contents of stream have to remain valid as long as the font is used.

        Warning
        - SFML cannot preload all the font data in this function, so the stream has to remain accessible until the sf::Font object opens a new font or is destroyed.

        Parameters
        - stream	Source stream to read from

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, filename: str) -> None:
        """
        Construct the font from a file.

        The supported font formats are: TrueType, Type 1, CFF, OpenType, SFNT, X11 PCF, Windows FNT, BDF, PFR and Type 42. Note that this function knows nothing about the standard fonts installed on the user's system, thus you can't load them directly.

        Warning
        - SFML cannot preload all the font data in this function, so the file has to remain accessible until the sf::Font object opens a new font or is destroyed.

        Parameters
        - filename	Path of the font file to open

        Exceptions
        - sf::Exception	if opening was unsuccessful
        """

    def open_from_file(self, filename: str) -> bool:
        """
        Open the font from a file.

        The supported font formats are: TrueType, Type 1, CFF, OpenType, SFNT, X11 PCF, Windows FNT, BDF, PFR and Type 42. Note that this function knows nothing about the standard fonts installed on the user's system, thus you can't load them directly.

        Warning
        - SFML cannot preload all the font data in this function, so the file has to remain accessible until the sf::Font object opens a new font or is destroyed.

        Parameters
        - filename	Path of the font file to load

        Returns
        - true if opening succeeded, false if it failed
        """

    def open_from_memory(self, data: bytes, sizeInBytes: bytes) -> bool:
        """
        Open the font from a file in memory.

        The supported font formats are: TrueType, Type 1, CFF, OpenType, SFNT, X11 PCF, Windows FNT, BDF, PFR and Type 42.

        Warning
        - SFML cannot preload all the font data in this function, so the buffer pointed by data has to remain valid until the sf::Font object opens a new font or is destroyed.

        Parameters
        - data	Pointer to the file data in memory
        = sizeInBytes	Size of the data to load, in bytes

        Returns
        - true if opening succeeded, false if it failed
        """

    def open_from_stream(self, stream: sfSystem.InputStream) -> bool:
        """
        Open the font from a custom stream.

        The supported font formats are: TrueType, Type 1, CFF, OpenType, SFNT, X11 PCF, Windows FNT, BDF, PFR and Type 42.

        Warning
        - SFML cannot preload all the font data in this function, so the stream has to remain accessible until the sf::Font object opens a new font or is destroyed.

        Parameters
        - stream	Source stream to read from

        Returns
        - true if opening succeeded, false if it failed
        """

    def get_info(self) -> Info:
        """
        Get the font information.

        Returns
        - A structure that holds the font information
        """

    def get_glyph(self, codePoint: int, characterSize: int, bold: bool, outline_thickness = 0) -> Glyph:
        """
        Retrieve a glyph of the font.

        If the font is a bitmap font, not all character sizes might be available. If the glyph is not available at the requested size, an empty glyph is returned.

        You may want to use hasGlyph to determine if the glyph exists before requesting it. If the glyph does not exist, a font specific default is returned.

        Be aware that using a negative value for the outline thickness will cause distorted rendering.

        Parameters
        - codePoint	Unicode code point of the character to get
        - characterSize	Reference character size
        - bold	Retrieve the bold version or the regular one?
        - outlineThickness	Thickness of outline (when != 0 the glyph will not be filled)

        Returns
        - The glyph corresponding to codePoint and characterSize
        """

    def has_glyph(self, codePoint: int) -> bool:
        """
        Determine if this font has a glyph representing the requested code point.

        Most fonts only include a very limited selection of glyphs from specific Unicode subsets, like Latin, Cyrillic, or Asian characters.

        While code points without representation will return a font specific default character, it might be useful to verify whether specific code points are included to determine whether a font is suited to display text in a specific language.

        Parameters
        - codePoint	Unicode code point to check

        Returns
        - true if the codepoint has a glyph representation, false otherwise
        """

    def get_kerning(self, first: int, second: int, characterSize: int, bold: bool = False) -> float:
        """
        Get the kerning offset of two glyphs.

        The kerning is an extra offset (negative) to apply between two glyphs when rendering them, to make the pair look more "natural". For example, the pair "AV" have a special kerning to make them closer than other characters. Most of the glyphs pairs have a kerning offset of zero, though.

        Parameters
        - first	Unicode code point of the first character
        - second	Unicode code point of the second character
        - characterSize	Reference character size
        - bold	Retrieve the bold version or the regular one?

        Returns
        - Kerning value for first and second, in pixels
        """

    def get_line_spacing(self, characterSize: int) -> float:
        """
        Get the line spacing.

        Line spacing is the vertical offset to apply between two consecutive lines of text.

        Parameters
        - characterSize	Reference character size

        Returns
        - Line spacing, in pixels
        """

    def get_underline_position(self, characterSize: int) -> float:
        """
        Get the position of the underline.

        Underline position is the vertical offset to apply between the baseline and the underline.

        Parameters
        - characterSize	Reference character size

        Returns
        - Underline position, in pixels
        """

    def get_underline_thickness(self, characterSize: int) -> float:
        """
        Get the thickness of the underline.

        Underline thickness is the vertical size of the underline.

        Parameters
        - characterSize	Reference character size

        Returns
        - Underline thickness, in pixel
        """

    def set_smooth(self, smooth: bool) -> None:
        """
        Enable or disable the smooth filter.

        When the filter is activated, the font appears smoother so that pixels are less noticeable. However if you want the font to look exactly the same as its source file, you should disable it. The smooth filter is enabled by default.

        Parameters
        - smooth	true to enable smoothing, false to disable it
        """

    def is_smooth(self) -> bool:
        """
        Tell whether the smooth filter is enabled or not.

        Returns
        - true if smoothing is enabled, false if it is disabled
        """

    def get_texture(self, characterSize: int) -> Texture:
        """
        Retrieve the texture containing the loaded glyphs of a certain size.

        The contents of the returned texture changes as more glyphs are requested, thus it is not very relevant. It is mainly used internally by sf::Text.

        Parameters
        - characterSize	Reference character size
        """

class Glyph:
    """
    Structure describing a glyph.

    A glyph is the visual representation of a character.

    The sf::Glyph structure provides the information needed to handle the glyph:

    - its coordinates in the font's texture
    - its bounding rectangle
    - the offset to apply to get the starting position of the next glyph
    """
    def __init__(self) -> None:
        ...

    advance: float
    lsb_delta: int
    rsb_delta: int
    bounds: FloatRect
    texture_rect: IntRect

class Image:
    """
    Class for loading, manipulating and saving images.

    sf::Image is an abstraction to manipulate images as bi-dimensional arrays of pixels.

    The class provides functions to load, read, write and save pixels, as well as many other useful functions.

    sf::Image can handle a unique internal representation of pixels, which is RGBA 32 bits. This means that a pixel must be composed of 8 bit red, green, blue and alpha channels – just like a sf::Color. All the functions that return an array of pixels follow this rule, and all parameters that you pass to sf::Image functions (such as loadFromMemory) must use this representation as well.

    A sf::Image can be copied, but it is a heavy resource and if possible you should always use [const] references to pass or return them to avoid useless copies.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Constructs an image with width 0 and height 0.
        """

    @overload
    def __init__(self, size: sfSystem.Vector2u, pixels: bytes) -> None:
        """
        Construct the image from an array of pixels.

        The pixel array is assumed to contain 32-bits RGBA pixels, and have the given size. If not, this is an undefined behavior. If pixels is nullptr, an empty image is created.

        Parameters
        - size	Width and height of the image
        - pixels	Array of pixels to copy to the image
        """

    @overload
    def __init__(self, data: bytes, size: bytes) -> None:
        """
        Construct the image from a file in memory.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm.

        Parameters
        - data	Pointer to the file data in memory
        - size	Size of the data to load, in bytes

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, stream: sfSystem.InputStream) -> None:
        """
        Construct the image from a custom stream.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm.

        Parameters
        - stream	Source stream to read from

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, size: sfSystem.Vector2u, color: Color = Color.black) -> None:
        """
        Construct the image and fill it with a unique color.

        Parameters
        - size	Width and height of the image
        - color	Fill color
        """

    @overload
    def resize(self, size: sfSystem.Vector2u, color: Color = Color.black) -> None:
        """
        Resize the image and fill it with a unique color.

        Parameters
        - size	Width and height of the image
        - color	Fill color
        """

    @overload
    def resize(self, size: sfSystem.Vector2u, pixels: bytes) -> None:
        """
        Resize the image from an array of pixels.

        The pixel array is assumed to contain 32-bits RGBA pixels, and have the given size. If not, this is an undefined behavior. If pixels is nullptr, an empty image is created.

        Parameters
        - size	Width and height of the image
        - pixels	Array of pixels to copy to the image
        """

    def load_from_file(self, filename: str) -> bool:
        """
        Load the image from a file on disk.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm. If this function fails, the image is left unchanged.

        Parameters
        - filename	Path of the image file to load
        """

    def load_from_memory(self, data: bytes, size: bytes) -> bool:
        """
        Load the image from a file in memory.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm. If this function fails, the image is left unchanged.

        Parameters
        - data	Pointer to the file data in memory
        - size	Size of the data to load, in bytes

        Returns
        - true if loading was successful
        """

    def load_from_stream(self, stream: sfSystem.InputStream) -> bool:
        """
        Load the image from a custom stream.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm. If this function fails, the image is left unchanged.

        Parameters
        - stream	Source stream to read from

        Returns
        - true if loading was successful
        """

    def save_to_file(self, filename: str) -> bool:
        """
        Save the image to a file on disk.

        The format of the image is automatically deduced from the extension. The supported image formats are bmp, png, tga and jpg. The destination file is overwritten if it already exists. This function fails if the image is empty.

        Parameters
        - filename	Path of the file to save

        Returns
        - true if saving was successful
        """

    def save_to_memory(self, format_: str) -> List[bytes] | None:
        """
        Save the image to a buffer in memory.

        The format of the image must be specified. The supported image formats are bmp, png, tga and jpg. This function fails if the image is empty, or if the format was invalid.

        Parameters
        - format_	Encoding format to use

        Returns
        - Buffer with encoded data if saving was successful, otherwise std::nullopt
        """

    def get_size(self) -> sfSystem.Vector2u:
        """
        Return the size (width and height) of the image.

        Returns
        - Size of the image, in pixels
        """

    def create_mask_from_color(self, color: Color, alpha: int = 0) -> None:
        """
        Create a transparency mask from a specified color-key.

        This function sets the alpha value of every pixel matching the given color to alpha (0 by default), so that they become transparent.

        Parameters
        - color	Color to make transparent
        - alpha	Alpha value to assign to transparent pixels
        """

    def copy(self, source: Image, dest: sfSystem.Vector2u, source_rect: IntRect = IntRect(), apply_alpha: bool = False) -> None:
        """
        Copy pixels from another image onto this one.

        This function does a slow pixel copy and should not be used intensively. It can be used to prepare a complex static image from several others, but if you need this kind of feature in real-time you'd better use sf::RenderTexture.

        If sourceRect is empty, the whole image is copied. If applyAlpha is set to true, alpha blending is applied from the source pixels to the destination pixels using the over operator. If it is false, the source pixels are copied unchanged with their alpha value.

        See https://en.wikipedia.org/wiki/Alpha_compositing for details on the over operator.

        Note that this function can fail if either image is invalid (i.e. zero-sized width or height), or if sourceRect is not within the boundaries of the source parameter, or if the destination area is out of the boundaries of this image.

        On failure, the destination image is left unchanged.

        Parameters
        - source	Source image to copy
        - dest	Coordinates of the destination position
        - sourceRect	Sub-rectangle of the source image to copy
        - applyAlpha	Should the copy take into account the source transparency?
        Returns
        - true if the operation was successful, false otherwise
        """

    def set_pixel(self, coords: sfSystem.Vector2u, color: Color) -> None:
        """
        Change the color of a pixel.

        This function doesn't check the validity of the pixel coordinates, using out-of-range values will result in an undefined behavior.

        Parameters
        - coords	Coordinates of pixel to change
        - color	New color of the pixel
        """

    def get_pixel(self, coords: sfSystem.Vector2u) -> Image:
        """
        Get the color of a pixel.

        This function doesn't check the validity of the pixel coordinates, using out-of-range values will result in an undefined behavior.

        Parameters
        - coords	Coordinates of pixel to change

        Returns
        - Color of the pixel at given coordinates
        """

    def get_pixels_ptr(self) -> bytes:
        """
        Get a read-only pointer to the array of pixels.

        The returned value points to an array of RGBA pixels made of 8 bit integer components. The size of the array is width * height * 4 (getSize().x * getSize().y * 4). Warning: the returned pointer may become invalid if you modify the image, so you should never store it for too long. If the image is empty, a null pointer is returned.

        Returns
        - Read-only pointer to the array of pixels
        """

    def flip_horizontally(self) -> None:
        """
        Flip the image horizontally (left <-> right)
        """

    def flip_vertically(self) -> None:
        """
        Flip the image vertically (top <-> bottom)
        """

class ConvexShape(Shape):
    """
    Specialized shape representing a convex polygon.

    This class inherits all the functions of sf::Transformable (position, rotation, scale, bounds, ...) as well as the functions of sf::Shape (outline, color, texture, ...).

    It is important to keep in mind that a convex shape must always be... convex, otherwise it may not be drawn correctly. Moreover, the points must be defined in order; using a random order would result in an incorrect shape.
    """

    def __init__(self, pointCount: int = 0) -> None:
        """
        Default constructor.

        Parameters
        - pointCount	Number of points of the polygon
        """

    def set_point_count(self, count: int) -> None:
        """
        Set the number of points of the polygon.

        For the shape to be rendered as expected, count must be greater or equal to 3.

        Parameters
        - count	New number of points of the polygon
        """

    def get_point_count(self) -> int:
        """
        Get the number of points of the polygon.

        Returns
        - Number of points of the polygon
        """

    def set_point(self, index: int, point: sfSystem.Vector2f) -> None:
        """
        Set the position of a point.

        Don't forget that the shape must be convex and the order of points matters. Points should not overlap. This applies to rendering; it is explicitly allowed to temporarily have non-convex or degenerate shapes when not drawn (e.g. during shape initialization).

        Point count must be specified beforehand. The behavior is undefined if index is greater than or equal to getPointCount.

        Parameters
        - index	Index of the point to change, in range [0 .. getPointCount() - 1]
        - point	New position of the point
        """

    def get_point(self, index: int) -> sfSystem.Vector2f:
        """
        Get the position of a point.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. getPointCount() - 1]

        Returns
        - Position of the index-th point of the polygon
        """

class CircleShape(Shape):
    """
    Specialized shape representing a circle.

    This class inherits all the functions of sf::Transformable (position, rotation, scale, bounds, ...) as well as the functions of sf::Shape (outline, color, texture, ...).

    Since the graphics card can't draw perfect circles, we have to fake them with multiple triangles connected to each other. The "points count" property of sf::CircleShape defines how many of these triangles to use, and therefore defines the quality of the circle.

    The number of points can also be used for another purpose; with small numbers you can create any regular polygon shape: equilateral triangle, square, pentagon, hexagon, ...
    """

    def __init__(self, radius: float = 0, pointCount: int = 30) -> None:
        """
        Default constructor.

        Parameters
        - radius	Radius of the circle
        - pointCount	Number of points composing the circle
        """

    def set_radius(self, radius: float) -> None:
        """
        Set the radius of the circle.

        Parameters
        - radius	New radius of the circle
        """

    def get_radius(self) -> float:
        """
        Get the radius of the circle.

        Returns
        - Radius of the circle
        """

    def set_point_count(self, count: int) -> None:
        """
        Set the number of points of the circle.

        Parameters
        - count	New number of points of the circle
        """

    def get_point_count(self) -> int:
        """
        Get the number of points of the circle.

        Returns
        - Number of points of the circle
        """

    def get_point(self, index: int) -> sfSystem.Vector2f:
        """
        Get a point of the circle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. getPointCount() - 1]

        Returns
        - index-th point of the shape
        """

    def get_geometric_center(self) -> sfSystem.Vector2f:
        """
        Get the geometric center of the circle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account.

        Returns
        - The geometric center of the shape
        """

class RectangleShape(Shape):
    """
    Specialized shape representing a rectangle.

    This class inherits all the functions of sf::Transformable (position, rotation, scale, bounds, ...) as well as the functions of sf::Shape (outline, color, texture, ...).
    """

    def __init__(self, size: sfSystem.Vector2f = sfSystem.Vector2f()) -> None:
        """
        Default constructor.

        Parameters
        - size	Size of the rectangle
        """

    def set_size(self, size: sfSystem.Vector2f) -> None:
        """
        Set the size of the rectangle.

        Parameters
        - size	New size of the rectangle
        """

    def get_size(self) -> sfSystem.Vector2f:
        """
        Get the size of the rectangle.

        Returns
        - Size of the rectangle
        """

    def get_point_count(self) -> int:
        """
        Get the number of points defining the shape.

        Returns
        - Number of points of the shape. For rectangle shapes, this number is always 4.
        """

    def get_point(self, index: int) -> sfSystem.Vector2f:
        """
        Get a point of the rectangle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. 3]

        Returns
        - index-th point of the shape
        """

    def get_geometric_center(self) -> sfSystem.Vector2f:
        """
        Get the geometric center of the rectangle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account.

        Returns
        - The geometric center of the shape
        """

class RenderStates:
    """
    Define the states used for drawing to a RenderTarget

    There are six global states that can be applied to the drawn objects:

    - the blend mode: how pixels of the object are blended with the background
    - the stencil mode: how pixels of the object interact with the stencil buffer
    - the transform: how the object is positioned/rotated/scaled
    - the texture coordinate type: how texture coordinates are interpreted
    - the texture: what image is mapped to the object
    - the shader: what custom effect is applied to the object

    High-level objects such as sprites or text force some of these states when they are drawn. For example, a sprite will set its own texture, so that you don't have to care about it when drawing the sprite.

    The transform is a special case: sprites, texts and shapes (and it's a good idea to do it with your own drawable classes too) combine their transform with the one that is passed in the RenderStates structure. So that you can use a "global" transform on top of each object's transform.

    Most objects, especially high-level drawables, can be drawn directly without defining render states explicitly – the default set of states is ok in most cases.

    ```
    window.draw(sprite);
    ```

    If you want to use a single specific render state, for example a shader, you can pass it directly to the Draw function: sf::RenderStates has an implicit one-argument constructor for each state.

    ```
    window.draw(sprite, shader);
    ```

    When you're inside the Draw function of a drawable object (inherited from sf::Drawable), you can either pass the render states unmodified, or change some of them. For example, a transformable object will combine the current transform with its own transform. A sprite will set its texture. Etc.
    """

    blend_mode: BlendMode
    stencil_mode: StencilMode
    transform: Transform
    coordinate_type: CoordinateType
    texture: Texture
    shader: Shader

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Constructing a default set of render states is equivalent to using sf::RenderStates::Default. The default set defines:

        - the BlendAlpha blend mode
        - the default StencilMode (no stencil)
        - the identity transform
        - a nullptr texture
        - a nullptr shader
        """

    @overload
    def __init__(self, theBlendMode: BlendMode) -> None:
        """
        Construct a default set of render states with a custom blend mode.

        Parameters
        - theBlendMode	Blend mode to use
        """

    @overload
    def __init__(self, theStencilMode: StencilMode) -> None:
        """
        Construct a default set of render states with a custom stencil mode.

        Parameters
        - theStencilMode	Stencil mode to use
        """

    @overload
    def __init__(self, theTransform: Transform) -> None:
        """
        Construct a default set of render states with a custom transform.

        Parameters
        - theTransform	Transform to use
        """

    @overload
    def __init__(self, theTexture: Texture) -> None:
        """
        Construct a default set of render states with a custom texture.

        Parameters
        - theTexture	Texture to use
        """

    @overload
    def __init__(self, shader: Shader) -> None:
        """
        Construct a default set of render states with a custom shader.

        Parameters
        - theShader	Shader to use
        """

    @overload
    def __init__(self, theBlendMode: BlendMode, theStencilMode: StencilMode, theTransform: Transform, theCoordinateType: CoordinateType, theTexture: Texture, theShader: Shader) -> None:
        """
        Construct a set of render states with all its attributes.

        Parameters
        - theBlendMode	Blend mode to use
        - theStencilMode	Stencil mode to use
        - theTransform	Transform to use
        - theCoordinateType	Texture coordinate type to use
        - theTexture	Texture to use
        - theShader	Shader to use
        """

    @staticmethod
    def default() -> RenderStates:
        """
        Special instance holding the default render states.
        """

class RenderTarget:
    """
    Base class for all render targets (window, texture, ...)

    sf::RenderTarget defines the common behavior of all the 2D render targets usable in the graphics module.

    It makes it possible to draw 2D entities like sprites, shapes, text without using any OpenGL command directly.

    A sf::RenderTarget is also able to use views (sf::View), which are a kind of 2D cameras. With views you can globally scroll, rotate or zoom everything that is drawn, without having to transform every single entity. See the documentation of sf::View for more details and sample pieces of code about this class.

    On top of that, render targets are still able to render direct OpenGL stuff. It is even possible to mix together OpenGL calls and regular SFML drawing commands. When doing so, make sure that OpenGL states are not messed up by calling the pushGLStates/popGLStates functions.

    While render targets are moveable, it is not valid to move them between threads. This will cause your program to crash. The problem boils down to OpenGL being limited with regard to how it works in multithreaded environments. Please ensure you only move render targets within the same thread.
    """

    @overload
    def clear(self, color: Color) -> None:
        """
        Clear the entire target with a single color.

        This function is usually called once every frame, to clear the previous contents of the target.

        Parameters
        - color	Fill color to use to clear the render target
        """

    @overload
    def clear(self, color: Color, stencilValue: StencilValue) -> None:
        """
        Clear the entire target with a single color and stencil value.

        The specified stencil value is truncated to the bit width of the current stencil buffer.

        Parameters
        - color	Fill color to use to clear the render target
        - stencilValue	Stencil value to clear to
        """

    def clear_stencil(self, stencilValue: StencilValue) -> None:
        """
        Clear the stencil buffer to a specific value.

        The specified value is truncated to the bit width of the current stencil buffer.

        Parameters
        - stencilValue	Stencil value to clear to
        """

    def set_view(self, view: View) -> None:
        """
        Change the current active view.

        The view is like a 2D camera, it controls which part of the 2D scene is visible, and how it is viewed in the render target. The new view will affect everything that is drawn, until another view is set. The render target keeps its own copy of the view object, so it is not necessary to keep the original one alive after calling this function. To restore the original view of the target, you can pass the result of getDefaultView() to this function.

        Parameters
        - view	New view to use
        """

    def get_view(self) -> View:
        """
        Get the view currently in use in the render target.

        Returns
        - The view object that is currently used
        """

    def get_default_view(self) -> View:
        """
        Get the default view of the render target.

        The default view has the initial size of the render target, and never changes after the target has been created.

        Returns
        - The default view of the render target
        """

    def get_viewport(self, view: View) -> IntRect:
        """
        Get the viewport of a view, applied to this render target.

        The viewport is defined in the view as a ratio, this function simply applies this ratio to the current dimensions of the render target to calculate the pixels rectangle that the viewport actually covers in the target.

        Parameters
        - view	The view for which we want to compute the viewport

        Returns
        - Viewport rectangle, expressed in pixels
        """

    def get_scissor(self, view: View) -> IntRect:
        """
        Get the scissor rectangle of a view, applied to this render target.

        The scissor rectangle is defined in the view as a ratio. This function simply applies this ratio to the current dimensions of the render target to calculate the pixels rectangle that the scissor rectangle actually covers in the target.

        Parameters
        - view	The view for which we want to compute the scissor rectangle

        Returns
        - Scissor rectangle, expressed in pixels
        """

    def map_pixel_to_coords(self, point: sfSystem.Vector2i, view: View) -> sfSystem.Vector2f:
        """
        Convert a point from target coordinates to world coordinates.

        This function finds the 2D position that matches the given pixel of the render target. In other words, it does the inverse of what the graphics card does, to find the initial position of a rendered pixel.

        Initially, both coordinate systems (world units and target pixels) match perfectly. But if you define a custom view or resize your render target, this assertion is not true anymore, i.e. a point located at (10, 50) in your render target may map to the point (150, 75) in your 2D world – if the view is translated by (140, 25).

        For render-windows, this function is typically used to find which point (or object) is located below the mouse cursor.

        This version uses a custom view for calculations, see the other overload of the function if you want to use the current view of the render target.

        Parameters
        - point	Pixel to convert
        - view	The view to use for converting the point

        Returns
        - The converted point, in "world" units
        """

    def map_coords_to_pixel(self, point: sfSystem.Vector2f) -> sfSystem.Vector2i:
        """
        Convert a point from world coordinates to target coordinates, using the current view.

        This function is an overload of the mapCoordsToPixel function that implicitly uses the current view. It is equivalent to:

        ```
        target.mapCoordsToPixel(point, target.getView());
        ```

        Parameters
        - point	Point to convert

        Returns
        - The converted point, in target coordinates (pixels)
        """

    @overload
    def draw(self, drawable: Drawable, states: RenderStates = RenderStates.default) -> None:
        """
        Draw a drawable object to the render target.

        Parameters
        - drawable	Object to draw
        - states	Render states to use for drawing
        """

    @overload
    def draw(self, vertices: Vertex, vertexCount: int, type_: PrimitiveType, states: RenderStates = RenderStates.default) -> None:
        """
        Draw primitives defined by an array of vertices.

        Parameters
        - vertices	Pointer to the vertices
        - vertexCount	Number of vertices in the array
        - type_	Type of primitives to draw
        - states	Render states to use for drawing
        """

    @overload
    def draw(self, buffer: VertexBuffer, states: RenderStates = RenderStates.default) -> None:
        """
        Draw primitives defined by a vertex buffer.

        Parameters
        - vertexBuffer	Vertex buffer
        - states	Render states to use for drawing
        """

    @overload
    def draw(self, buffer: VertexBuffer, first: int, count: int, states: RenderStates = RenderStates.default) -> None:
        """
        Draw primitives defined by a vertex buffer.

        Parameters
        - vertexBuffer	Vertex buffer
        - firstVertex	Index of the first vertex to render
        - vertexCount	Number of vertices to render
        - states	Render states to use for drawing
        """

    def get_size(self) -> sfSystem.Vector2u:
        """
        Return the size of the rendering region of the target.

        Returns
        - Size in pixels

        Implemented in sf::RenderTexture, and sf::RenderWindow.
        """

    def is_srgb(self) -> bool:
        """
        Tell if the render target will use sRGB encoding when drawing on it.

        Returns
        - true if the render target use sRGB encoding, false otherwise

        Reimplemented in sf::RenderTexture, and sf::RenderWindow.
        """

    def set_active(self, active: bool = True) -> bool:
        """
        Activate or deactivate the render target for rendering.

        This function makes the render target's context current for future OpenGL rendering operations (so you shouldn't care about it if you're not doing direct OpenGL stuff). A render target's context is active only on the current thread, if you want to make it active on another thread you have to deactivate it on the previous thread first if it was active. Only one context can be current in a thread, so if you want to draw OpenGL geometry to another render target don't forget to activate it again. Activating a render target will automatically deactivate the previously active context (if any).

        Parameters
        - active	true to activate, false to deactivate

        Returns
        - true if operation was successful, false otherwise

        Reimplemented in sf::RenderTexture, and sf::RenderWindow.
        """

    def push_gl_states(self) -> None:
        """
        Save the current OpenGL render states and matrices.

        This function can be used when you mix SFML drawing and direct OpenGL rendering. Combined with popGLStates, it ensures that:

        - SFML's internal states are not messed up by your OpenGL code
        - your OpenGL states are not modified by a call to a SFML function

        More specifically, it must be used around code that calls draw functions. Example:

        ```
        // OpenGL code here...
        window.pushGLStates();
        window.draw(...);
        window.draw(...);
        window.popGLStates();
        // OpenGL code here...
        ```

        Note that this function is quite expensive: it saves all the possible OpenGL states and matrices, even the ones you don't care about. Therefore it should be used wisely. It is provided for convenience, but the best results will be achieved if you handle OpenGL states yourself (because you know which states have really changed, and need to be saved and restored). Take a look at the resetGLStates function if you do so.
        """

    def pop_gl_states(self) -> None:
        """
        Restore the previously saved OpenGL render states and matrices.

        See the description of pushGLStates to get a detailed description of these functions.
        """

    def reset_gl_states(self) -> None:
        """
        Reset the internal OpenGL states so that the target is ready for drawing.

        This function can be used when you mix SFML drawing and direct OpenGL rendering, if you choose not to use pushGLStates/popGLStates. It makes sure that all OpenGL states needed by SFML are set, so that subsequent draw() calls will work as expected.

        Example:

        ```
        // OpenGL code here...
        glPushAttrib(...);
        window.resetGLStates();
        window.draw(...);
        window.draw(...);
        glPopAttrib(...);
        // OpenGL code here...
        ```
        """

class RenderTexture(RenderTarget):
    """
    Target for off-screen 2D rendering into a texture.

    sf::RenderTexture is the little brother of sf::RenderWindow.

    It implements the same 2D drawing and OpenGL-related functions (see their base class sf::RenderTarget for more details), the difference is that the result is stored in an off-screen texture rather than being show in a window.

    Rendering to a texture can be useful in a variety of situations:

    - precomputing a complex static texture (like a level's background from multiple tiles)
    - applying post-effects to the whole scene with shaders
    - creating a sprite from a 3D object rendered with OpenGL
    - etc.

    Like sf::RenderWindow, sf::RenderTexture is still able to render direct OpenGL stuff. It is even possible to mix together OpenGL calls and regular SFML drawing commands. If you need a depth buffer for 3D rendering, don't forget to request it when calling RenderTexture::create.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Constructs a render-texture with width 0 and height 0.
        """

    @overload
    def __init__(self, size: sfSystem.Vector2u, context_settings: sfWindow.ContextSettings = sfWindow.ContextSettings()) -> None:
        """
        Construct a render-texture.

        The last parameter, settings, is useful if you want to enable multi-sampling or use the render-texture for OpenGL rendering that requires a depth or stencil buffer. Otherwise it is unnecessary, and you should leave this parameter at its default value.

        After creation, the contents of the render-texture are undefined. Call RenderTexture::clear first to ensure a single color fill.

        Parameters
        - size	Width and height of the render-texture
        - settings	Additional settings for the underlying OpenGL texture and context
        """

    def resize(self, size: sfSystem.Vector2u, settings: sfWindow.ContextSettings = sfWindow.ContextSettings()) -> None:
        """
        Resize the render-texture.

        The last parameter, settings, is useful if you want to enable multi-sampling or use the render-texture for OpenGL rendering that requires a depth or stencil buffer. Otherwise it is unnecessary, and you should leave this parameter at its default value.

        After resizing, the contents of the render-texture are undefined. Call RenderTexture::clear first to ensure a single color fill.

        Parameters
        - size	Width and height of the render-texture
        - settings	Additional settings for the underlying OpenGL texture and context

        Returns
        - true if resizing has been successful, false if it failed
        """

    def set_smooth(self, smooth: bool) -> None:
        """
        Enable or disable texture smoothing.

        This function is similar to Texture::setSmooth. This parameter is disabled by default.

        Parameters
        - smooth	true to enable smoothing, false to disable it
        """

    def is_smooth(self) -> bool:
        """
        Tell whether the smooth filtering is enabled or not.

        Returns
        - true if texture smoothing is enabled
        """

    def set_repeated(self, repeated: bool) -> None:
        """
        Enable or disable texture repeating.

        This function is similar to Texture::setRepeated. This parameter is disabled by default.

        Parameters
        - repeated	true to enable repeating, false to disable it
        """

    def is_repeated(self) -> bool:
        """
        Tell whether the texture is repeated or not.

        Returns
        - true if texture is repeated
        """

    def generate_mipmap(self) -> bool:
        """
        Generate a mipmap using the current texture data.

        This function is similar to Texture::generateMipmap and operates on the texture used as the target for drawing. Be aware that any draw operation may modify the base level image data. For this reason, calling this function only makes sense after all drawing is completed and display has been called. Not calling display after subsequent drawing will lead to undefined behavior if a mipmap had been previously generated.

        Returns
        - true if mipmap generation was successful, false if unsuccessful
        """

    def set_active(self, active: bool = True) -> bool:
        """
        Activate or deactivate the render-texture for rendering.

        This function makes the render-texture's context current for future OpenGL rendering operations (so you shouldn't care about it if you're not doing direct OpenGL stuff). Only one context can be current in a thread, so if you want to draw OpenGL geometry to another render target (like a RenderWindow) don't forget to activate it again.

        Parameters
        - active	true to activate, false to deactivate

        Returns
        - true if operation was successful, false otherwise

        Reimplemented from sf::RenderTarget.
        """

    def display(self) -> None:
        """
        Update the contents of the target texture.

        This function updates the target texture with what has been drawn so far. Like for windows, calling this function is mandatory at the end of rendering. Not calling it may leave the texture in an undefined state.
        """

    def get_size(self) -> sfSystem.Vector2u:
        """
        Return the size of the rendering region of the texture.

        The returned value is the size that you passed to the create function.

        Returns
        - Size in pixels

        Implements sf::RenderTarget.
        """

    def is_srgb(self) -> bool:
        """
        Tell if the render-texture will use sRGB encoding when drawing on it.

        You can request sRGB encoding for a render-texture by having the sRgbCapable flag set for the context parameter of create() method

        Returns
        - true if the render-texture use sRGB encoding, false otherwise

        Reimplemented from sf::RenderTarget.
        """

    def get_texture(self) -> Texture:
        """
        Get a read-only reference to the target texture.

        After drawing to the render-texture and calling Display, you can retrieve the updated texture using this function, and draw it using a sprite (for example). The internal sf::Texture of a render-texture is always the same instance, so that it is possible to call this function once and keep a reference to the texture even after it is modified.

        Returns
        - Const reference to the texture
        """

    @staticmethod
    def get_maximum_anti_aliasing_level() -> int:
        """
        Get the maximum anti-aliasing level supported by the system.

        Returns
        - The maximum anti-aliasing level supported by the system
        """

class RenderWindow(sfWindow.Window, RenderTarget):
    """
    Window that can serve as a target for 2D drawing.

    sf::RenderWindow is the main class of the Graphics module.

    It defines an OS window that can be painted using the other classes of the graphics module.

    sf::RenderWindow is derived from sf::Window, thus it inherits all its features: events, window management, OpenGL rendering, etc. See the documentation of sf::Window for a more complete description of all these features, as well as code examples.

    On top of that, sf::RenderWindow adds more features related to 2D drawing with the graphics module (see its base class sf::RenderTarget for more details). Here is a typical rendering and event loop with a sf::RenderWindow:

    ```
    // Declare and create a new render-window
    sf::RenderWindow window(sf::VideoMode({800, 600}), "SFML window");

    // Limit the framerate to 60 frames per second (this step is optional)
    window.setFramerateLimit(60);

    // The main loop - ends as soon as the window is closed
    while (window.isOpen())
    {
    // Event processing
    while (const std::optional event = window.pollEvent())
    {
        // Request for closing the window
        if (event->is<sf::Event::Closed>())
            window.close();
    }

    // Clear the whole window before rendering a new frame
    window.clear();

    // Draw some graphical entities
    window.draw(sprite);
    window.draw(circle);
    window.draw(text);

    // End the current frame and display its contents on screen
    window.display();
    }
    ```

    Like sf::Window, sf::RenderWindow is still able to render direct OpenGL stuff. It is even possible to mix together OpenGL calls and regular SFML drawing commands.

    ```
    // Create the render window
    sf::RenderWindow window(sf::VideoMode({800, 600}), "SFML OpenGL");

    // Create a sprite and a text to display
    const sf::Texture texture("circle.png");
    sf::Sprite sprite(texture);
    const sf::Font font("arial.ttf");
    sf::Text text(font);
    ...

    // Perform OpenGL initializations
    glMatrixMode(GL_PROJECTION);
    ...

    // Start the rendering loop
    while (window.isOpen())
    {
        // Process events
        ...

        // Draw a background sprite
        window.pushGLStates();
        window.draw(sprite);
        window.popGLStates();

        // Draw a 3D object using OpenGL
        glBegin(GL_TRIANGLES);
            glVertex3f(...);
            ...
        glEnd();

        // Draw text on top of the 3D object
        window.pushGLStates();
        window.draw(text);
        window.popGLStates();

        // Finally, display the rendered frame on screen
        window.display();
    }
    ```
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        This constructor doesn't actually create the window, use the other constructors or call create() to do so.
        """

    @overload
    def __init__(self, mode: sfWindow.VideoMode, title: str, style: sfWindow.Style = sfWindow.Style.Default, state: sfWindow.State = sfWindow.State.Windowed, settings: sfWindow.ContextSettings = sfWindow.ContextSettings()) -> None:
        """
        Construct a new window.

        This constructor creates the window with the size and pixel depth defined in mode. An optional style can be passed to customize the look and behavior of the window (borders, title bar, resizable, closable, ...).

        The last parameter is an optional structure specifying advanced OpenGL context settings such as anti-aliasing, depth-buffer bits, etc. You shouldn't care about these parameters for a regular usage of the graphics module.

        Parameters
        - mode	Video mode to use (defines the width, height and depth of the rendering area of the window)
        - title	Title of the window
        - style	Window style, a bitwise OR combination of sf::Style enumerators
        - state	Window state
        - settings	Additional settings for the underlying OpenGL context
        """

    def get_size(self) -> sfSystem.Vector2u:
        """
        Get the size of the rendering region of the window.

        The size doesn't include the titlebar and borders of the window.

        Returns
        - Size in pixels

        Implements sf::RenderTarget.
        """

    @overload
    def set_icon(self, image: Image) -> None:
        """
        Change the window's icon.

        The OS default icon is used by default.

        Parameters
        - icon	Image to use as the icon. The image is copied, so you need not keep the source alive after calling this function.
        """

    @overload
    def set_icon(self, size: sfSystem.Vector2u, pixels: bytes) -> None:
        """
        Change the window's icon.

        pixels must be an array of size pixels in 32-bits RGBA format.

        The OS default icon is used by default.

        Parameters
        - size	Icon's width and height, in pixels
        - pixels	Pointer to the array of pixels in memory. The pixels are copied, so you need not keep the source alive after calling this function.
        """

    def is_srgb(self) -> bool:
        """
        Tell if the window will use sRGB encoding when drawing on it.

        You can request sRGB encoding for a window by having the sRgbCapable flag set in the ContextSettings

        Returns
        - true if the window use sRGB encoding, false otherwise
        - Reimplemented from sf::RenderTarget.
        """

    def set_active(self, active: bool = True) -> bool:
        """
        Activate or deactivate the window as the current target for OpenGL rendering.

        A window is active only on the current thread, if you want to make it active on another thread you have to deactivate it on the previous thread first if it was active. Only one window can be active on a thread at a time, thus the window previously active (if any) automatically gets deactivated. This is not to be confused with requestFocus().

        Parameters
        - active	true to activate, false to deactivate

        Returns
        - true if operation was successful, false otherwise
        - Reimplemented from sf::RenderTarget.
        """

class Shader:
    """
    Shader class (vertex, geometry and fragment)

    Shaders are programs written using a specific language, executed directly by the graphics card and allowing to apply real-time operations to the rendered entities.

    There are three kinds of shaders:

    ```
    Vertex shaders, that process vertices
    Geometry shaders, that process primitives
    Fragment (pixel) shaders, that process pixels
    ```

    A sf::Shader can be composed of either a vertex shader alone, a geometry shader alone, a fragment shader alone, or any combination of them. (see the variants of the load functions).

    Shaders are written in GLSL, which is a C-like language dedicated to OpenGL shaders. You'll probably need to learn its basics before writing your own shaders for SFML.

    Like any C/C++ program, a GLSL shader has its own variables called uniforms that you can set from your C++ application. sf::Shader handles different types of uniforms:

    ```
    scalars: float, int, bool
    vectors (2, 3 or 4 components)
    matrices (3x3 or 4x4)
    samplers (textures)
    ```

    Some SFML-specific types can be converted:

    ```
    sf::Color as a 4D vector (vec4)
    sf::Transform as matrices (mat3 or mat4)
    ```

    Every uniform variable in a shader can be set through one of the setUniform() or setUniformArray() overloads. For example, if you have a shader with the following uniforms:

    ```
    uniform float offset;
    uniform vec3 point;
    uniform vec4 color;
    uniform mat4 matrix;
    uniform sampler2D overlay;
    uniform sampler2D current;
    ```

    You can set their values from C++ code as follows, using the types defined in the sf::Glsl namespace:

    ```
    shader.setUniform("offset", 2.f);
    shader.setUniform("point", sf::Vector3f(0.5f, 0.8f, 0.3f));
    shader.setUniform("color", sf::Glsl::Vec4(color));          // color is a sf::Color
    shader.setUniform("matrix", sf::Glsl::Mat4(transform));     // transform is a sf::Transform
    shader.setUniform("overlay", texture);                      // texture is a sf::Texture
    shader.setUniform("current", sf::Shader::CurrentTexture);
    The special Shader::CurrentTexture argument maps the given sampler2D uniform to the current texture of the object being drawn (which cannot be known in advance).
    ```

    To apply a shader to a drawable, you must pass it as an additional parameter to the RenderWindow::draw function:

    ```
    window.draw(sprite, &shader);
    ```

    ... which is in fact just a shortcut for this:

    - sf::RenderStates states;
    - states.shader = &shader;
    - window.draw(sprite, states);

    In the code above we pass a pointer to the shader, because it may be null (which means "no shader").

    Shaders can be used on any drawable, but some combinations are not interesting. For example, using a vertex shader on a sf::Sprite is limited because there are only 4 vertices, the sprite would have to be subdivided in order to apply wave effects. Another bad example is a fragment shader with sf::Text: the texture of the text is not the actual text that you see on screen, it is a big texture containing all the characters of the font in an arbitrary order; thus, texture lookups on pixels other than the current one may not give you the expected result.

    Shaders can also be used to apply global post-effects to the current contents of the target. This can be done in two different ways:

    - draw everything to a sf::RenderTexture, then draw it to the main target using the shader
    - draw everything directly to the main target, then use sf::Texture::update(Window&) to copy its contents to a texture and draw it to the main target using the shader

    The first technique is more optimized because it doesn't involve retrieving the target's pixels to system memory, but the second one doesn't impact the rendering process and can be easily inserted anywhere without impacting all the code.

    Like sf::Texture that can be used as a raw OpenGL texture, sf::Shader can also be used directly as a raw shader for custom OpenGL geometry.

    ```
    sf::Shader::bind(&shader);
    ... render OpenGL geometry ...
    sf::Shader::bind(nullptr);
    ```
    """

    class Type(enum.IntEnum):
        """
        Types of shaders.

        Enumerator
        - Vertex: Vertex shader
        - Geometry: Geometry shader.
        - Fragment: Fragment (pixel) shader.
        """

        Vertex = 0
        Geometry = 1
        Fragment = 2

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        This constructor creates an empty shader.

        Binding an empty shader has the same effect as not binding any shader.
        """

    @overload
    def __init__(self, filename: str, type_: Type) -> None:
        """
        Construct from a shader file.

        This constructor loads a single shader, vertex, geometry or fragment, identified by the second argument. The source must be a text file containing a valid shader in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - filename	Path of the vertex, geometry or fragment shader file to load
        - type_	Type of shader (vertex, geometry or fragment)

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, vertexShaderFilename: str, fragmentShaderFilename: str) -> None:
        """
        Construct from vertex and fragment shader files.

        This constructor loads both the vertex and the fragment shaders. If one of them fails to load, the shader is left empty (the valid shader is unloaded). The sources must be text files containing valid shaders in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - vertexShaderFilename	Path of the vertex shader file to load
        - fragmentShaderFilename	Path of the fragment shader file to load

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, vertexShaderFilename: str, geometryShaderFilename: str, fragmentShaderFilename: str) -> None:
        """
        Construct from vertex, geometry and fragment shader files.

        This constructor loads the vertex, geometry and fragment shaders. If one of them fails to load, the shader is left empty (the valid shader is unloaded). The sources must be text files containing valid shaders in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - vertexShaderFilename	Path of the vertex shader file to load
        - geometryShaderFilename	Path of the geometry shader file to load
        - fragmentShaderFilename	Path of the fragment shader file to load

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def load_from_file(self, filename: str, type_: Type) -> bool:
        """
        Load the vertex, geometry or fragment shader from a file.

        This function loads a single shader, vertex, geometry or fragment, identified by the second argument. The source must be a text file containing a valid shader in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - filename	Path of the vertex, geometry or fragment shader file to load
        - type_	Type of shader (vertex, geometry or fragment)

        Returns
        - true if loading succeeded, false if it failed
        """

    @overload
    def load_from_file(self, vertexShaderFilename: str, fragmentShaderFilename: str) -> bool:
        """
        Load both the vertex and fragment shaders from files.

        This function loads both the vertex and the fragment shaders. If one of them fails to load, the shader is left empty (the valid shader is unloaded). The sources must be text files containing valid shaders in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - vertexShaderFilename	Path of the vertex shader file to load
        - fragmentShaderFilename	Path of the fragment shader file to load

        Returns
        - true if loading succeeded, false if it failed
        """

    @overload
    def load_from_file(self, vertexShaderFilename: str, geometryShaderFilename: str, fragmentShaderFilename: str) -> bool:
        """
        Load the vertex, geometry and fragment shaders from files.

        This function loads the vertex, geometry and fragment shaders. If one of them fails to load, the shader is left empty (the valid shader is unloaded). The sources must be text files containing valid shaders in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - vertexShaderFilename	Path of the vertex shader file to load
        - geometryShaderFilename	Path of the geometry shader file to load
        - fragmentShaderFilename	Path of the fragment shader file to load

        Returns
        - true if loading succeeded, false if it failed
        """

    @overload
    def load_from_memory(self, shader: str, type_: Type) -> bool:
        """
        Load the vertex, geometry or fragment shader from a source code in memory.

        This function loads a single shader, vertex, geometry or fragment, identified by the second argument. The source code must be a valid shader in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - shader	String containing the source code of the shader
        - type_	Type of shader (vertex, geometry or fragment)

        Returns
        - true if loading succeeded, false if it failed
        """

    @overload
    def load_from_memory(self, vertexShader: str, fragmentShader: str) -> bool:
        """
        Load both the vertex and fragment shaders from source codes in memory.

        This function loads both the vertex and the fragment shaders. If one of them fails to load, the shader is left empty (the valid shader is unloaded). The sources must be valid shaders in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - vertexShader	String containing the source code of the vertex shader
        - fragmentShader	String containing the source code of the fragment shader

        Returns
        - true if loading succeeded, false if it failed
        """

    @overload
    def load_from_memory(self, vertex: str, geometry: str, fragment: str) -> bool:
        """
        Load the vertex, geometry and fragment shaders from source codes in memory.

        This function loads the vertex, geometry and fragment shaders. If one of them fails to load, the shader is left empty (the valid shader is unloaded). The sources must be valid shaders in GLSL language. GLSL is a C-like language dedicated to OpenGL shaders; you'll probably need to read a good documentation for it before writing your own shaders.

        Parameters
        - vertexShader	String containing the source code of the vertex shader
        - geometryShader	String containing the source code of the geometry shader
        - fragmentShader	String containing the source code of the fragment shader

        Returns
        - true if loading succeeded, false if it failed
        """

    @overload
    def set_uniform(self, name: str, x: float) -> None:
        """
        Specify value for float uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - x	Value of the float scalar
        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Vec2) -> None:
        """
        Specify value for vec2 uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the vec2 vector
        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Vec3) -> None:
        """
        Specify value for vec3 uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the vec3 vector
        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Vec4) -> None:
        """
        Specify value for vec4 uniform.

        This overload can also be called with sf::Color objects that are converted to sf::Glsl::Vec4.

        It is important to note that the components of the color are normalized before being passed to the shader. Therefore, they are converted from range [0 .. 255] to range [0 .. 1]. For example, a sf::Color(255, 127, 0, 255) will be transformed to a vec4(1.0, 0.5, 0.0, 1.0) in the shader.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the vec4 vector

        """

    @overload
    def set_uniform(self, name: str, x: int) -> None:
        """
        Specify value for int uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - x	Value of the int scalar
        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Ivec2) -> None:
        """
        Specify value for ivec2 uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the ivec2 vector
        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Ivec3) -> None:
        """
        Specify value for ivec3 uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the ivec3 vector

        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Ivec4) -> None:
        """
        Specify value for ivec4 uniform.

        This overload can also be called with sf::Color objects that are converted to sf::Glsl::Ivec4.

        If color conversions are used, the ivec4 uniform in GLSL will hold the same values as the original sf::Color instance. For example, sf::Color(255, 127, 0, 255) is mapped to ivec4(255, 127, 0, 255).

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the ivec4 vector
        """

    @overload
    def set_uniform(self, name: str, x: bool) -> None:
        """
        Specify value for bool uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - x	Value of the bool scalar

        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Bvec2) -> None:
        """
        Specify value for bvec2 uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the bvec2 vector
        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Bvec3) -> None:
        """
        Specify value for bvec3 uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the bvec3 vector
        """

    @overload
    def set_uniform(self, name: str, vector: Glsl.Bvec4) -> None:
        """
        pecify value for bvec4 uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vector	Value of the bvec4 vector

        """

    @overload
    def set_uniform(self, name: str, matrix: Glsl.Mat3) -> None:
        """
        Specify value for mat3 matrix.

        Parameters
        - name	Name of the uniform variable in GLSL
        - matrix	Value of the mat3 matrix

        """

    @overload
    def set_uniform(self, name: str, matrix: Glsl.Mat4) -> None:
        """
        Specify value for mat4 matrix.

        Parameters
        - name	Name of the uniform variable in GLSL
        - matrix	Value of the mat4 matrix
        """

    @overload
    def set_uniform(self, name: str, texture: Texture) -> None:
        """
        Specify a texture as sampler2D uniform.

        name is the name of the variable to change in the shader. The corresponding parameter in the shader must be a 2D texture (sampler2D GLSL type).

        Example:

        ```
        uniform sampler2D the_texture; // this is the variable in the shader
        sf::Texture texture;
        ...
        shader.setUniform("the_texture", texture);
        ```

        It is important to note that texture must remain alive as long as the shader uses it, no copy is made internally.

        To use the texture of the object being drawn, which cannot be known in advance, you can pass the special value sf::Shader::CurrentTexture:

        ```
        shader.setUniform("the_texture", sf::Shader::CurrentTexture).
        ```

        Parameters
        - name	Name of the texture in the shader
        - texture	Texture to assign
        """

    @overload
    def set_uniform_array(self, name: str, scalarArray: float, length: int) -> None:
        """
        Specify values for float[] array uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - scalarArray	pointer to array of float values
        - length	Number of elements in the array
        """

    @overload
    def set_uniform_array(self, name: str, vectorArray: Glsl.Vec2, length: int) -> None:
        """
        Specify values for vec2[] array uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vectorArray	pointer to array of vec2 values
        - length	Number of elements in the array
        """

    @overload
    def set_uniform_array(self, name: str, vectorArray: Glsl.Vec3, length: int) -> None:
        """
        Specify values for vec3[] array uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vectorArray	pointer to array of vec3 values
        - length	Number of elements in the array
        """

    @overload
    def set_uniform_array(self, name: str, values: Glsl.Vec4, count: int) -> None:
        """
        Specify values for vec4[] array uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - vectorArray	pointer to array of vec4 values
        - length	Number of elements in the array
        """

    @overload
    def set_uniform_array(self, name: str, matrixArray: Glsl.Mat3, length: int) -> None:
        """
        Specify values for mat3[] array uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - matrixArray	pointer to array of mat3 values
        - length	Number of elements in the array
        """

    @overload
    def set_uniform_array(self, name: str, matrixArray: Glsl.Mat4, length: int) -> None:
        """
        Specify values for mat4[] array uniform.

        Parameters
        - name	Name of the uniform variable in GLSL
        - matrixArray	pointer to array of mat4 values
        - length	Number of elements in the array
        """

    def get_native_handle(self) -> int:
        """
        Get the underlying OpenGL handle of the shader.

        You shouldn't need to use this function, unless you have very specific stuff to implement that SFML doesn't support, or implement a temporary workaround until a bug is fixed.

        Returns
        - OpenGL handle of the shader or 0 if not yet loaded
        """

    @staticmethod
    def bind(shader: Shader) -> None:
        """
        Bind a shader for rendering.

        This function is not part of the graphics API, it mustn't be used when drawing SFML entities. It must be used only if you mix sf::Shader with OpenGL code.

        ```
        sf::Shader s1, s2;
        ...
        sf::Shader::bind(&s1);
        // draw OpenGL stuff that use s1...
        sf::Shader::bind(&s2);
        // draw OpenGL stuff that use s2...
        sf::Shader::bind(nullptr);
        // draw OpenGL stuff that use no shader...
        ```

        Parameters
        - shader	Shader to bind, can be null to use no shader
        """

    @staticmethod
    def is_available() -> bool:
        """
        Tell whether or not the system supports shaders.

        This function should always be called before using the shader features. If it returns false, then any attempt to use sf::Shader will fail.

        Returns
        - true if shaders are supported, false otherwise
        """

    @staticmethod
    def is_geometry_available() -> bool:
        """
        Tell whether or not the system supports geometry shaders.

        This function should always be called before using the geometry shader features. If it returns false, then any attempt to use sf::Shader geometry shader features will fail.

        This function can only return true if isAvailable() would also return true, since shaders in general have to be supported in order for geometry shaders to be supported as well.

        Note: The first call to this function, whether by your code or SFML will result in a context switch.

        Returns
        - true if geometry shaders are supported, false otherwise
        """

class Texture:
    """
    Image living on the graphics card that can be used for drawing.

    sf::Texture stores pixels that can be drawn, with a sprite for example.

    A texture lives in the graphics card memory, therefore it is very fast to draw a texture to a render target, or copy a render target to a texture (the graphics card can access both directly).

    Being stored in the graphics card memory has some drawbacks. A texture cannot be manipulated as freely as a sf::Image, you need to prepare the pixels first and then upload them to the texture in a single operation (see Texture::update).

    sf::Texture makes it easy to convert from/to sf::Image, but keep in mind that these calls require transfers between the graphics card and the central memory, therefore they are slow operations.

    A texture can be loaded from an image, but also directly from a file/memory/stream. The necessary shortcuts are defined so that you don't need an image first for the most common cases. However, if you want to perform some modifications on the pixels before creating the final texture, you can load your file to a sf::Image, do whatever you need with the pixels, and then call Texture(const Image&).

    Since they live in the graphics card memory, the pixels of a texture cannot be accessed without a slow copy first. And they cannot be accessed individually. Therefore, if you need to read the texture's pixels (like for pixel-perfect collisions), it is recommended to store the collision information separately, for example in an array of booleans.

    Like sf::Image, sf::Texture can handle a unique internal representation of pixels, which is RGBA 32 bits. This means that a pixel must be composed of 8 bit red, green, blue and alpha channels – just like a sf::Color.

    When providing texture data from an image file or memory, it can either be stored in a linear color space or an sRGB color space. Most digital images account for gamma correction already, so they would need to be "uncorrected" back to linear color space before being processed by the hardware. The hardware can automatically convert it from the sRGB color space to a linear color space when it gets sampled. When the rendered image gets output to the final framebuffer, it gets converted back to sRGB.

    This option is only useful in conjunction with an sRGB capable framebuffer. This can be requested during window creation.

    Usage example:

    ```
    // This example shows the most common use of sf::Texture:
    // drawing a sprite

    // Load a texture from a file
    const sf::Texture texture("texture.png");

    // Assign it to a sprite
    sf::Sprite sprite(texture);

    // Draw the textured sprite
    window.draw(sprite);
    // This example shows another common use of sf::Texture:
    // streaming real-time data, like video frames

    // Create an empty texture
    sf::Texture texture({640, 480});

    // Create a sprite that will display the texture
    sf::Sprite sprite(texture);

    while (...) // the main loop
    {
        ...

        // update the texture
        std::uint8_t* pixels = ...; // get a fresh chunk of pixels (the next frame of a movie, for example)
        texture.update(pixels);

        // draw it
        window.draw(sprite);

        ...
    }
    ```

    Like sf::Shader that can be used as a raw OpenGL shader, sf::Texture can also be used directly as a raw texture for custom OpenGL geometry.

    ```
    sf::Texture::bind(&texture);
    ... render OpenGL geometry ...
    sf::Texture::bind(nullptr);
    ```
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Creates a texture with width 0 and height 0.
        """

    @overload
    def __init__(self, filename: str, sRgb: bool = False, area: IntRect = IntRect()) -> None:
        """
        Construct the texture from a sub-rectangle of a file on disk.

        The area argument can be used to load only a sub-rectangle of the whole image. If you want the entire image then leave the default value (which is an empty IntRect). If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        Parameters
        - filename	Path of the image file to load
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, data: bytes, size: int, sRgb: bool = False) -> None:
        """
        Construct the texture from a file in memory.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        Parameters
        - data	Pointer to the file data in memory
        - size	Size of the data to load, in bytes
        - sRgb	true to enable sRGB conversion, false to disable it

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, data: bytes, size: int, sRgb: bool, area: IntRect) -> None:
        """
        Construct the texture from a sub-rectangle of a file in memory.

        The area argument can be used to load only a sub-rectangle of the whole image. If you want the entire image then leave the default value (which is an empty IntRect). If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        Parameters
        - data	Pointer to the file data in memory
        - size	Size of the data to load, in bytes
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, stream: sfSystem.InputStream, sRgb: bool = False) -> None:
        """
        Construct the texture from a custom stream.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        Parameters
        - stream	Source stream to read from
        - sRgb	true to enable sRGB conversion, false to disable it

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, stream: sfSystem.InputStream, sRgb: bool, area: IntRect) -> None:
        """
        Construct the texture from a sub-rectangle of a custom stream.

        The area argument can be used to load only a sub-rectangle of the whole image. If you want the entire image then leave the default value (which is an empty IntRect). If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        Parameters
        - stream	Source stream to read from
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, image: Image, sRgb: bool = False) -> None:
        """
        Construct the texture from an image.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        Parameters
        - image	Image to load into the texture
        - sRgb	true to enable sRGB conversion, false to disable it

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, image: Image, sRgb: bool, area: IntRect) -> None:
        """
        Construct the texture from a sub-rectangle of an image.

        The area argument is used to load only a sub-rectangle of the whole image. If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        Parameters
        - image	Image to load into the texture
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, size: sfSystem.Vector2u, sRgb: bool = False) -> None:
        """
        Construct the texture with a given size.

        Parameters
        - size	Width and height of the texture
        - sRgb	true to enable sRGB conversion, false to disable it

        Exceptions
        - sf::Exception	if construction was unsuccessful
        """

    def resize(self, size: sfSystem.Vector2u, sRgb: bool = False) -> None:
        """
        Resize the texture.

        If this function fails, the texture is left unchanged.

        Parameters
        - size	Width and height of the texture
        - sRgb	true to enable sRGB conversion, false to disable it

        Returns
        - true if resizing was successful, false if it failed
        """

    def load_from_file(self, filename: str, sRgb: bool = False, area: IntRect = IntRect()) -> bool:
        """
        Load the texture from a file on disk.

        The area argument can be used to load only a sub-rectangle of the whole image. If you want the entire image then leave the default value (which is an empty IntRect). If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        If this function fails, the texture is left unchanged.

        Parameters
        - filename	Path of the image file to load
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Returns
        - true if loading was successful, false if it failed
        """

    def load_from_memory(self, data: bytes, size: int, sRgb: bool = False, area: IntRect = IntRect()) -> bool:
        """
        Load the texture from a file in memory.

        The area argument can be used to load only a sub-rectangle of the whole image. If you want the entire image then leave the default value (which is an empty IntRect). If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        If this function fails, the texture is left unchanged.

        Parameters
        - data	Pointer to the file data in memory
        - size	Size of the data to load, in bytes
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Returns
        - true if loading was successful, false if it failed
        """

    def load_from_stream(self, stream: sfSystem.InputStream, sRgb: bool = False, area: IntRect = IntRect()) -> bool:
        """
        Load the texture from a custom stream.

        The area argument can be used to load only a sub-rectangle of the whole image. If you want the entire image then leave the default value (which is an empty IntRect). If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        If this function fails, the texture is left unchanged.

        Parameters
        - stream	Source stream to read from
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Returns
        - true if loading was successful, false if it failed
        """

    def load_from_image(self, image: Image, sRgb: bool = False, area: IntRect = IntRect()) -> bool:
        """
        Load the texture from an image.

        The area argument can be used to load only a sub-rectangle of the whole image. If you want the entire image then leave the default value (which is an empty IntRect). If the area rectangle crosses the bounds of the image, it is adjusted to fit the image size.

        The maximum size for a texture depends on the graphics driver and can be retrieved with the getMaximumSize function.

        If this function fails, the texture is left unchanged.

        Parameters
        - image	Image to load into the texture
        - sRgb	true to enable sRGB conversion, false to disable it
        - area	Area of the image to load

        Returns
        - true if loading was successful, false if it failed
        """

    def get_size(self) -> sfSystem.Vector2u:
        """
        Return the size of the texture.

        Returns
        - Size in pixels
        """

    def copy_to_image(self) -> Image:
        """
        Copy the texture pixels to an image.

        This function performs a slow operation that downloads the texture's pixels from the graphics card and copies them to a new image, potentially applying transformations to pixels if necessary (texture may be padded or flipped).

        Returns
        - Image containing the texture's pixels
        """

    @overload
    def update(self, pixels: bytes) -> None:
        """
        Update the whole texture from an array of pixels.

        The pixel array is assumed to have the same size as the area rectangle, and to contain 32-bits RGBA pixels.

        No additional check is performed on the size of the pixel array. Passing invalid arguments will lead to an undefined behavior.

        This function does nothing if pixels is nullptr or if the texture was not previously created.

        Parameters
        - pixels	Array of pixels to copy to the texture
        """

    @overload
    def update(self, pixels: bytes, size: sfSystem.Vector2u, dest: sfSystem.Vector2u) -> None:
        """
        Update a part of the texture from an array of pixels.

        The size of the pixel array must match the size argument, and it must contain 32-bits RGBA pixels.

        No additional check is performed on the size of the pixel array or the bounds of the area to update. Passing invalid arguments will lead to an undefined behavior.

        This function does nothing if pixels is null or if the texture was not previously created.

        Parameters
        - pixels	Array of pixels to copy to the texture
        - size	Width and height of the pixel region contained in pixels
        - dest	Coordinates of the destination position
        """

    @overload
    def update(self, texture: Texture) -> None:
        """
        Update a part of this texture from another texture.

        Although the source texture can be smaller than this texture, this function is usually used for updating the whole texture. The other overload, which has an additional destination argument, is more convenient for updating a sub-area of this texture.

        No additional check is performed on the size of the passed texture. Passing a texture bigger than this texture will lead to an undefined behavior.

        This function does nothing if either texture was not previously created.

        Parameters
        - texture	Source texture to copy to this texture
        """

    @overload
    def update(self, texture: Texture, dest: sfSystem.Vector2u) -> None:
        """
        Update a part of this texture from another texture.

        No additional check is performed on the size of the texture. Passing an invalid combination of texture size and destination will lead to an undefined behavior.

        This function does nothing if either texture was not previously created.

        Parameters
        - texture	Source texture to copy to this texture
        - dest	Coordinates of the destination position
        """

    @overload
    def update(self, image: Image) -> None:
        """
        Update the texture from an image.

        Although the source image can be smaller than the texture, this function is usually used for updating the whole texture. The other overload, which has an additional destination argument, is more convenient for updating a sub-area of the texture.

        No additional check is performed on the size of the image. Passing an image bigger than the texture will lead to an undefined behavior.

        This function does nothing if the texture was not previously created.

        Parameters
        - image	Image to copy to the texture
        """

    @overload
    def update(self, image: Image, dest: sfSystem.Vector2u) -> None:
        """
        Update a part of the texture from an image.

        No additional check is performed on the size of the image. Passing an invalid combination of image size and destination will lead to an undefined behavior.

        This function does nothing if the texture was not previously created.

        Parameters
        - image	Image to copy to the texture
        - dest	Coordinates of the destination position
        """

    @overload
    def update(self, window: sfWindow.Window) -> None:
        """
        Update the texture from the contents of a window.

        Although the source window can be smaller than the texture, this function is usually used for updating the whole texture. The other overload, which has an additional destination argument, is more convenient for updating a sub-area of the texture.

        No additional check is performed on the size of the window. Passing a window bigger than the texture will lead to an undefined behavior.

        This function does nothing if either the texture or the window was not previously created.

        Parameters
        - window	Window to copy to the texture
        """

    @overload
    def update(self, window: sfWindow.Window, dest: sfSystem.Vector2u) -> None:
        """
        Update a part of the texture from the contents of a window.

        No additional check is performed on the size of the window. Passing an invalid combination of window size and destination will lead to an undefined behavior.

        This function does nothing if either the texture or the window was not previously created.

        Parameters
        - window	Window to copy to the texture
        - dest	Coordinates of the destination position
        """

    def set_smooth(self, smooth: bool) -> None:
        """
        Enable or disable the smooth filter.

        When the filter is activated, the texture appears smoother so that pixels are less noticeable. However if you want the texture to look exactly the same as its source file, you should leave it disabled. The smooth filter is disabled by default.

        Parameters
        - smooth	true to enable smoothing, false to disable it
        """

    def is_smooth(self) -> bool:
        """
        Tell whether the smooth filter is enabled or not.

        Returns
        - true if smoothing is enabled, false if it is disabled
        """

    def is_srgb(self) -> bool:
        """
        Tell whether the texture source is converted from sRGB or not.

        Returns
        - true if the texture source is converted from sRGB, false if not
        """

    def set_repeated(self, repeated: bool) -> None:
        """
        Enable or disable repeating.

        Repeating is involved when using texture coordinates outside the texture rectangle [0, 0, width, height]. In this case, if repeat mode is enabled, the whole texture will be repeated as many times as needed to reach the coordinate (for example, if the X texture coordinate is 3 * width, the texture will be repeated 3 times). If repeat mode is disabled, the "extra space" will instead be filled with border pixels. Warning: on very old graphics cards, white pixels may appear when the texture is repeated. With such cards, repeat mode can be used reliably only if the texture has power-of-two dimensions (such as 256x128). Repeating is disabled by default.

        Parameters
        - repeated	true to repeat the texture, false to disable repeating
        """

    def is_repeated(self) -> bool:
        """
        Tell whether the texture is repeated or not.

        Returns
        - true if repeat mode is enabled, false if it is disabled
        """

    def generate_mipmap(self) -> bool:
        """
        Generate a mipmap using the current texture data.

        Mipmaps are pre-computed chains of optimized textures. Each level of texture in a mipmap is generated by halving each of the previous level's dimensions. This is done until the final level has the size of 1x1. The textures generated in this process may make use of more advanced filters which might improve the visual quality of textures when they are applied to objects much smaller than they are. This is known as minification. Because fewer texels (texture elements) have to be sampled from when heavily minified, usage of mipmaps can also improve rendering performance in certain scenarios.

        Mipmap generation relies on the necessary OpenGL extension being available. If it is unavailable or generation fails due to another reason, this function will return false. Mipmap data is only valid from the time it is generated until the next time the base level image is modified, at which point this function will have to be called again to regenerate it.

        Returns
        - true if mipmap generation was successful, false if unsuccessful
        """

    def swap(self, right: Texture) -> None:
        """
        Swap the contents of this texture with those of another.

        Parameters
        - right	Instance to swap with
        """

    def get_native_handle(self) -> int:
        """
        Get the underlying OpenGL handle of the texture.

        You shouldn't need to use this function, unless you have very specific stuff to implement that SFML doesn't support, or implement a temporary workaround until a bug is fixed.

        Returns
        - OpenGL handle of the texture or 0 if not yet created
        """

    @staticmethod
    def bind(texture: Texture, coordinateType: CoordinateType = CoordinateType.Normalized) -> None:
        """
        Bind a texture for rendering.

        This function is not part of the graphics API, it mustn't be used when drawing SFML entities. It must be used only if you mix sf::Texture with OpenGL code.

        ```
        sf::Texture t1, t2;
        ...
        sf::Texture::bind(&t1);
        // draw OpenGL stuff that use t1...
        sf::Texture::bind(&t2);
        // draw OpenGL stuff that use t2...
        sf::Texture::bind(nullptr);
        // draw OpenGL stuff that use no texture...
        ```

        The coordinateType argument controls how texture coordinates will be interpreted. If Normalized (the default), they must be in range [0 .. 1], which is the default way of handling texture coordinates with OpenGL. If Pixels, they must be given in pixels (range [0 .. size]). This mode is used internally by the graphics classes of SFML, it makes the definition of texture coordinates more intuitive for the high-level API, users don't need to compute normalized values.

        Parameters
        - texture	Pointer to the texture to bind, can be null to use no texture
        - coordinateType	Type of texture coordinates to use
        """

    @staticmethod
    def get_maximum_size() -> int:
        """
        Get the maximum texture size allowed.

        This maximum size is defined by the graphics driver. You can expect a value of 512 pixels for low-end graphics card, and up to 8192 pixels or more for newer hardware.

        Returns
        - Maximum size allowed for textures, in pixels
        """


class Sprite(Transformable, Drawable):
    """
    Drawable representation of a texture, with its own transformations, color, etc.

    sf::Sprite is a drawable class that allows to easily display a texture (or a part of it) on a render target.

    It inherits all the functions from sf::Transformable: position, rotation, scale, origin. It also adds sprite-specific properties such as the texture to use, the part of it to display, and some convenience functions to change the overall color of the sprite, or to get its bounding rectangle.

    sf::Sprite works in combination with the sf::Texture class, which loads and provides the pixel data of a given texture.

    The separation of sf::Sprite and sf::Texture allows more flexibility and better performances: indeed a sf::Texture is a heavy resource, and any operation on it is slow (often too slow for real-time applications). On the other side, a sf::Sprite is a lightweight object which can use the pixel data of a sf::Texture and draw it with its own transformation/color/blending attributes.

    It is important to note that the sf::Sprite instance doesn't copy the texture that it uses, it only keeps a reference to it. Thus, a sf::Texture must not be destroyed while it is used by a sf::Sprite (i.e. never write a function that uses a local sf::Texture instance for creating a sprite).

    See also the note on coordinates and undistorted rendering in sf::Transformable.

    Usage example:

    ```
    // Load a texture
    const sf::Texture texture("texture.png");

    // Create a sprite
    sf::Sprite sprite(texture);
    sprite.setTextureRect({{10, 10}, {50, 30}});
    sprite.setColor({255, 255, 255, 200});
    sprite.setPosition({100.f, 25.f});

    // Draw it
    window.draw(sprite);
    ```
    """

    @overload
    def __init__(self, texture: Texture) -> None:
        """
        Construct the sprite from a source texture.

        Parameters
        - texture	Source texture
        """

    @overload
    def __init__(self, texture: Texture, rectangle: IntRect) -> None:
        """
        Construct the sprite from a sub-rectangle of a source texture.

        Parameters
        - texture	Source texture
        - rectangle	Sub-rectangle of the texture to assign to the sprite
        """

    def set_texture(self, texture: Texture, resetRect: bool) -> None:
        """
        Change the source texture of the sprite.

        The texture argument refers to a texture that must exist as long as the sprite uses it. Indeed, the sprite doesn't store its own copy of the texture, but rather keeps a pointer to the one that you passed to this function. If the source texture is destroyed and the sprite tries to use it, the behavior is undefined. If resetRect is true, the TextureRect property of the sprite is automatically adjusted to the size of the new texture. If it is false, the texture rect is left unchanged.

        Parameters
        - texture	New texture
        - resetRect	Should the texture rect be reset to the size of the new texture?
        """

    def set_texture_rect(self, rectangle: IntRect) -> None:
        """
        Set the sub-rectangle of the texture that the sprite will display.

        The texture rect is useful when you don't want to display the whole texture, but rather a part of it. By default, the texture rect covers the entire texture.

        Parameters
        - rectangle	Rectangle defining the region of the texture to display
        """

    def set_color(self, color: Color) -> None:
        """
        Set the global color of the sprite.

        This color is modulated (multiplied) with the sprite's texture. It can be used to colorize the sprite, or change its global opacity. By default, the sprite's color is opaque white.

        Parameters
        - color	New color of the sprite
        """

    def get_texture(self) -> Texture:
        """
        Get the source texture of the sprite.

        The returned reference is const, which means that you can't modify the texture when you retrieve it with this function.

        Returns
        - Reference to the sprite's texture
        """

    def get_texture_rect(self) -> IntRect:
        """
        Get the sub-rectangle of the texture displayed by the sprite.

        Returns
        - Texture rectangle of the sprite
        """

    def get_color(self) -> Color:
        """
        Get the global color of the sprite.

        Returns
        - Global color of the sprite
        """

    def get_local_bounds(self) -> FloatRect:
        """
        Get the local bounding rectangle of the entity.

        The returned rectangle is in local coordinates, which means that it ignores the transformations (translation, rotation, scale, ...) that are applied to the entity. In other words, this function returns the bounds of the entity in the entity's coordinate system.

        Returns
        - Local bounding rectangle of the entity
        """

    def get_global_bounds(self) -> FloatRect:
        """
        Get the global bounding rectangle of the entity.

        The returned rectangle is in global coordinates, which means that it takes into account the transformations (translation, rotation, scale, ...) that are applied to the entity. In other words, this function returns the bounds of the sprite in the global 2D world's coordinate system.

        Returns
        - Global bounding rectangle of the entity
        """



class StencilComparison(enum.IntEnum):
    """
    Enumeration of the stencil test comparisons that can be performed.

    The comparisons are mapped directly to their OpenGL equivalents, specified by glStencilFunc().

    Enumerator
    - Never: The stencil test never passes.
    - Less: The stencil test passes if the new value is less than the value in the stencil buffer.
    - LessEqual: The stencil test passes if the new value is less than or equal to the value in the stencil buffer.
    - Greater: The stencil test passes if the new value is greater than the value in the stencil buffer.
    - GreaterEqual: The stencil test passes if the new value is greater than or equal to the value in the stencil buffer.
    - Equal: The stencil test passes if the new value is strictly equal to the value in the stencil buffer.
    - NotEqual: The stencil test passes if the new value is strictly unequal to the value in the stencil buffer.
    - Always: The stencil test always passes.
    """

    Never = 0
    Less = 1
    LessEqual = 2
    Greater = 3
    GreaterEqual = 4
    Equal = 5
    NotEqual = 6
    Always = 7


class StencilUpdateOperation(enum.IntEnum):
    """
    Enumeration of the stencil buffer update operations.

    The update operations are mapped directly to their OpenGL equivalents, specified by glStencilOp().

    Enumerator
    - Keep: If the stencil test passes, the value in the stencil buffer is not modified.
    - Zero: If the stencil test passes, the value in the stencil buffer is set to zero.
    - Replace: If the stencil test passes, the value in the stencil buffer is set to the new value.
    - Increment: If the stencil test passes, the value in the stencil buffer is incremented and if required clamped.
    - Decrement: If the stencil test passes, the value in the stencil buffer is decremented and if required clamped.
    - Invert: If the stencil test passes, the value in the stencil buffer is bitwise inverted.
    """

    Keep = 0
    Zero = 1
    Replace = 2
    Increment = 3
    Decrement = 4
    Invert = 5


class StencilValue:
    """
    Stencil value type (also used as a mask)
    """

    def __init__(self, value: int) -> None:
        ...

    value: int


class StencilMode:
    """
    Stencil modes for drawing.

    sf::StencilMode is a class that controls stencil testing.

    In addition to drawing to the visible portion of a render target, there is the possibility to "draw" to a so-called stencil buffer. The stencil buffer is a special non-visible buffer that can contain a single value per pixel that is drawn. This can be thought of as a fifth value in addition to red, green, blue and alpha values. The maximum value that can be represented depends on what is supported by the system. Typically support for a 8-bit stencil buffer should always be available. This will also have to be requested when creating a render target via the sf::ContextSettings that is passed during creation. Stencil testing will not work if there is no stencil buffer available in the target that is being drawn to.

    Initially, just like with the visible color buffer, the stencil value of each pixel is set to an undefined value. Calling sf::RenderTarget::clear will set each pixel's stencil value to 0. sf::RenderTarget::clear can be called at any time to reset the stencil values back to 0.

    When drawing an object, before each pixel of the color buffer is updated with its new color value, the stencil test is performed. During this test 2 values are compared with each other: the reference value that is passed via sf::StencilMode and the value that is currently in the stencil buffer. The arithmetic comparison that is performed on the 2 values can also be controlled via sf::StencilMode. Depending on whether the test passes i.e. the comparison yields true, the color buffer is updated with its new RGBA value and if set in sf::StencilMode the stencil buffer is updated accordingly. The new stencil value will be used during stencil testing the next time the pixel is drawn to.

    The class is composed of 5 components, each of which has its own public member variable:

    Stencil Comparison (stencilComparison)
    Stencil Update Operation (stencilUpdateOperation)
    Stencil Reference Value (stencilReference)
    Stencil Mask Value (stencilMask)
    Stencil Only Update (stencilOnly)
    The stencil comparison specifies the comparison that is performed between the reference value of the currently active sf::StencilMode and the value that is currently in the stencil buffer. This comparison determines whether the stencil test passes or fails.

    The stencil update operation specifies how the stencil buffer is updated if the stencil test passes. If the stencil test fails, neither the color or stencil buffers will be modified. If incrementing or decrementing the stencil value, the new value will be clamped to the range from 0 to the maximum representable value given the bit width of the stencil buffer e.g. 255 if an 8-bit stencil buffer is being used.

    The reference value is used both during the comparison with the current stencil buffer value and as the new value to be written when the operation is set to Replace.

    The mask value is used to mask the bits of both the reference value and the value in the stencil buffer during the comparison and when updating. The mask can be used to e.g. segment the stencil value bits into separate regions that are used for different purposes.

    In certain situations, it might make sense to only write to the stencil buffer and not the color buffer during a draw. The written stencil buffer value can then be used in subsequent draws as a masking region.

    In SFML, a stencil mode can be specified every time you draw a sf::Drawable object to a render target. It is part of the sf::RenderStates compound that is passed to the member function sf::RenderTarget::draw().
    """

    def __init__(self) -> None:
        ...

    stencil_comparison: StencilComparison
    stencil_update_operation: StencilUpdateOperation
    stencil_reference: StencilValue
    stencil_mask: StencilValue
    stencil_only: bool

    def __eq__(self, other: StencilMode) -> bool:
        ...

    def __ne__(self, other: StencilMode) -> bool:
        ...


class Text(Transformable, Drawable):
    """
    Graphical text that can be drawn to a render target.

    sf::Text is a drawable class that allows to easily display some text with custom style and color on a render target.

    It inherits all the functions from sf::Transformable: position, rotation, scale, origin. It also adds text-specific properties such as the font to use, the character size, the font style (bold, italic, underlined and strike through), the text color, the outline thickness, the outline color, the character spacing, the line spacing and the text to display of course. It also provides convenience functions to calculate the graphical size of the text, or to get the global position of a given character.

    sf::Text works in combination with the sf::Font class, which loads and provides the glyphs (visual characters) of a given font.

    The separation of sf::Font and sf::Text allows more flexibility and better performances: indeed a sf::Font is a heavy resource, and any operation on it is slow (often too slow for real-time applications). On the other side, a sf::Text is a lightweight object which can combine the glyphs data and metrics of a sf::Font to display any text on a render target.

    It is important to note that the sf::Text instance doesn't copy the font that it uses, it only keeps a reference to it. Thus, a sf::Font must not be destructed while it is used by a sf::Text (i.e. never write a function that uses a local sf::Font instance for creating a text).

    See also the note on coordinates and undistorted rendering in sf::Transformable.
    """

    class Style(enum.IntEnum):
        """
        Enumeration of the string drawing styles.

        Enumerator
        - Regular: Regular characters, no style.
        - Bold: Bold characters.
        - Italic: Italic characters.
        - Underlined: Underlined characters.
        - StrikeThrough: Strike through characters.
        """

        Regular = 0
        Bold = 1 << 0
        Italic = 1 << 1
        Underlined = 1 << 2
        StrikeThrough = 1 << 3

    def __init__(self, font: Font, string: str = "", characterSize: int = 30) -> None:
        """
        Construct the text from a string, font and size.

        Note that if the used font is a bitmap font, it is not scalable, thus not all requested sizes will be available to use. This needs to be taken into consideration when setting the character size. If you need to display text of a certain size, make sure the corresponding bitmap font that supports that size is used.

        Parameters
        - string	Text assigned to the string
        - font	Font used to draw the string
        - characterSize	Base size of characters, in pixels
        """

    def set_string(self, string: str) -> None:
        """
        Set the text's string.

        The string argument is a sf::String, which can automatically be constructed from standard string types. So, the following calls are all valid:

        text.setString("hello");
        text.setString(L"hello");
        text.setString(std::string("hello"));
        text.setString(std::wstring(L"hello"));
        A text's string is empty by default.

        Parameters
        - string	New string
        """

    def set_font(self, font: Font) -> None:
        """
        Set the text's font.

        The font argument refers to a font that must exist as long as the text uses it. Indeed, the text doesn't store its own copy of the font, but rather keeps a pointer to the one that you passed to this function. If the font is destroyed and the text tries to use it, the behavior is undefined.

        Parameters
        - font	New font
        """

    def set_character_size(self, size: int) -> None:
        """
        Set the character size.

        The default size is 30.

        Note that if the used font is a bitmap font, it is not scalable, thus not all requested sizes will be available to use. This needs to be taken into consideration when setting the character size. If you need to display text of a certain size, make sure the corresponding bitmap font that supports that size is used.

        Parameters
        - size	New character size, in pixels
        """

    def set_line_spacing(self, spacing_factor: float) -> None:
        """
        Set the line spacing factor.

        The default spacing between lines is defined by the font. This method enables you to set a factor for the spacing between lines. By default the line spacing factor is 1.

        Parameters
        - spacingFactor	New line spacing factor
        """

    def set_letter_spacing(self, spacing_factor: float) -> None:
        """
        Set the letter spacing factor.

        The default spacing between letters is defined by the font. This factor doesn't directly apply to the existing spacing between each character, it rather adds a fixed space between them which is calculated from the font metrics and the character size. Note that factors below 1 (including negative numbers) bring characters closer to each other. By default the letter spacing factor is 1.

        Parameters
        - spacingFactor	New letter spacing factor
        """

    def set_style(self, style: Style) -> None:
        """
        Set the text's style.

        You can pass a combination of one or more styles, for example sf::Text::Bold | sf::Text::Italic. The default style is sf::Text::Regular.

        Parameters
        - style	New style
        """

    def set_fill_color(self, color: Color) -> None:
        """
        Set the fill color of the text.

        By default, the text's fill color is opaque white. Setting the fill color to a transparent color with an outline will cause the outline to be displayed in the fill area of the text.

        Parameters
        - color	New fill color of the text
        """

    def set_outline_color(self, color: Color) -> None:
        """
        Set the outline color of the text.

        By default, the text's outline color is opaque black.

        Parameters
        - color	New outline color of the text
        """

    def set_outline_thickness(self, thickness: float) -> None:
        """
        Set the thickness of the text's outline.

        By default, the outline thickness is 0.

        Be aware that using a negative value for the outline thickness will cause distorted rendering.

        Parameters
        - thickness	New outline thickness, in pixels
        """

    def get_string(self) -> str:
        """
        Get the text's string.

        The returned string is a sf::String, which can automatically be converted to standard string types. So, the following lines of code are all valid:

        - sf::String   s1 = text.getString();
        - std::string  s2 = text.getString();
        - std::wstring s3 = text.getString();

        **Mark**: We don't have sf::String here. The return type is str.

        Returns
        - Text's string
        """

    def get_font(self) -> Font:
        """
        Get the text's font.

        The returned reference is const, which means that you cannot modify the font when you get it from this function.

        Returns
        - Reference to the text's font
        """

    def get_character_size(self) -> int:
        """
        Get the character size.

        Returns
        - Size of the characters, in pixels
        """

    def get_letter_spacing(self) -> float:
        """
        Get the size of the letter spacing factor.

        Returns
        - Size of the letter spacing factor
        """

    def get_line_spacing(self) -> float:
        """
        Get the size of the line spacing factor.

        Returns
        - Size of the line spacing factor
        """

    def get_style(self) -> int:
        """
        Get the text's style.

        Returns
        - Text's style
        """

    def get_fill_color(self) -> Color:
        """
        Get the fill color of the text.

        Returns
        - Fill color of the text
        """

    def get_outline_color(self) -> Color:
        """
        Get the outline color of the text.

        Returns
        - Outline color of the text
        """

    def get_outline_thickness(self) -> float:
        """
        Get the outline thickness of the text.

        Returns
        - Outline thickness of the text, in pixels
        """

    def find_character_pos(self, index: int) -> sfSystem.Vector2f:
        """
        Return the position of the index-th character.

        This function computes the visual position of a character from its index in the string. The returned position is in global coordinates (translation, rotation, scale and origin are applied). If index is out of range, the position of the end of the string is returned.

        Parameters
        - index	Index of the character

        Returns
        - Position of the character
        """

    def get_local_bounds(self) -> FloatRect:
        """
        Get the local bounding rectangle of the entity.

        The returned rectangle is in local coordinates, which means that it ignores the transformations (translation, rotation, scale, ...) that are applied to the entity. In other words, this function returns the bounds of the entity in the entity's coordinate system.

        Returns
        - Local bounding rectangle of the entity
        """

    def get_global_bounds(self) -> FloatRect:
        """
        Get the global bounding rectangle of the entity.

        The returned rectangle is in global coordinates, which means that it takes into account the transformations (translation, rotation, scale, ...) that are applied to the entity. In other words, this function returns the bounds of the text in the global 2D world's coordinate system.

        Returns
        - Global bounding rectangle of the entity
        """

class View:
    """
    2D camera that defines what region is shown on screen

    sf::View defines a camera in the 2D scene.

    This is a very powerful concept: you can scroll, rotate or zoom the entire scene without altering the way that your drawable objects are drawn.

    A view is composed of a source rectangle, which defines what part of the 2D scene is shown, and a target viewport, which defines where the contents of the source rectangle will be displayed on the render target (window or texture).

    The viewport allows to map the scene to a custom part of the render target, and can be used for split-screen or for displaying a minimap, for example. If the source rectangle doesn't have the same size as the viewport, its contents will be stretched to fit in.

    The scissor rectangle allows for specifying regions of the render target to which modifications can be made by draw and clear operations. Only pixels that are within the region will be able to be modified. Pixels outside of the region will not be modified by draw or clear operations.

    Certain effects can be created by either using the viewport or scissor rectangle. While the results appear identical, there can be times where one method should be preferred over the other. Viewport transformations are applied during the vertex processing stage of the graphics pipeline, before the primitives are rasterized into fragments for fragment processing. Since viewport processing has to be performed and cannot be disabled, effects that are performed using the viewport transform are basically free performance-wise. Scissor testing is performed in the per-sample processing stage of the graphics pipeline, after fragment processing has been performed. Because per-sample processing is performed at the last stage of the pipeline, fragments that are discarded at this stage will cause the highest waste of GPU resources compared to any method that would have discarded vertices or fragments earlier in the pipeline. There are situations in which scissor testing has to be used to control whether fragments are discarded or not. An example of such a situation is when performing the viewport transform on vertices is necessary but a subset of the generated fragments should not have an effect on the stencil buffer or blend with the color buffer.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        This constructor creates a default view of (0, 0, 1000, 1000)
        """

    @overload
    def __init__(self, rectangle: FloatRect) -> None:
        """
        Construct the view from a rectangle.

        Parameters
        - rectangle	Rectangle defining the zone to display
        """

    @overload
    def __init__(self, center: sfSystem.Vector2f, size: sfSystem.Vector2f) -> None:
        """
        Construct the view from its center and size.

        Parameters
        - center	Center of the zone to display
        - size	Size of zone to display
        """

    def set_center(self, center: sfSystem.Vector2f) -> None:
        """
        Set the center of the view.

        Parameters
        - center	New center
        """

    def set_size(self, size: sfSystem.Vector2f) -> None:
        """
        Set the size of the view.

        Parameters
        - size	New size
        """

    def set_rotation(self, angle: sfSystem.Angle) -> None:
        """
        Set the orientation of the view.

        The default rotation of a view is 0 degree.

        Parameters
        - angle	New angle
        """

    def set_viewport(self, viewport: FloatRect) -> None:
        """
        Set the target viewport.

        The viewport is the rectangle into which the contents of the view are displayed, expressed as a factor (between 0 and 1) of the size of the RenderTarget to which the view is applied. For example, a view which takes the left side of the target would be defined with view.setViewport(sf::FloatRect({0.f, 0.f}, {0.5f, 1.f})). By default, a view has a viewport which covers the entire target.

        Parameters
        - viewport	New viewport rectangle
        """

    def set_scissor(self, scissor: FloatRect) -> None:
        """
        Set the target scissor rectangle.

        The scissor rectangle, expressed as a factor (between 0 and 1) of the RenderTarget, specifies the region of the RenderTarget whose pixels are able to be modified by draw or clear operations. Any pixels which lie outside of the scissor rectangle will not be modified by draw or clear operations. For example, a scissor rectangle which only allows modifications to the right side of the target would be defined with view.setScissor(sf::FloatRect({0.5f, 0.f}, {0.5f, 1.f})). By default, a view has a scissor rectangle which allows modifications to the entire target. This is equivalent to disabling the scissor test entirely. Passing the default scissor rectangle to this function will also disable scissor testing.

        Parameters
        - scissor	New scissor rectangle
        """

    def get_center(self) -> sfSystem.Vector2f:
        """
        Get the center of the view.

        Returns
        - Center of the view
        """

    def get_size(self) -> sfSystem.Vector2f:
        """
        Get the size of the view.

        Returns
        - Size of the view
        """

    def get_rotation(self) -> sfSystem.Angle:
        """
        Get the current orientation of the view.

        Returns
        - Rotation angle of the view
        """

    def get_viewport(self) -> FloatRect:
        """
        Get the target viewport rectangle of the view.

        Returns
        - Viewport rectangle, expressed as a factor of the target size
        """

    def get_scissor(self) -> FloatRect:
        """
        Get the scissor rectangle of the view.

        Returns
        - Scissor rectangle, expressed as a factor of the target size
        """

    def move(self, offset: sfSystem.Vector2f) -> None:
        """
        Move the view relatively to its current position.

        Parameters
        - offset	Move offset
        """

    def rotate(self, angle: float) -> None:
        """
        Rotate the view relatively to its current orientation.

        Parameters
        - angle	Angle to rotate
        """

    def zoom(self, factor: float) -> None:
        """
        Resize the view rectangle relatively to its current size.

        Resizing the view simulates a zoom, as the zone displayed on screen grows or shrinks. factor is a multiplier:

        - 1 keeps the size unchanged
        - > 1 makes the view bigger (objects appear smaller)
        - < 1 makes the view smaller (objects appear bigger)

        Parameters
        - factor	Zoom factor to apply
        """

    def get_transform(self) -> Transform:
        """
        Get the projection transform of the view.

        This function is meant for internal use only.

        Returns
        - Projection transform defining the view
        """

    def get_inverse_transform(self) -> Transform:
        """
        Get the inverse projection transform of the view.

        This function is meant for internal use only.

        Returns
        - Inverse of the projection transform defining the view
        """
