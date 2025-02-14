import enum
from typing import Any, List
from . import System

class CoordinateType(enum.IntEnum):
    """
    Types of texture coordinates that can be used for rendering.

    - Normalized: Texture coordinates in range [0 .. 1].
    - Pixels: Texture coordinates in range [0 .. size].
    """
    Local = 0
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
    pass

class IntRect:
    """
    Integer rectangle.

    sf::IntRect is a structure that represents a rectangle defined by two positions and two sizes.
    """

    position: System.Vector2i
    size: System.Vector2i

    def __init__(self, position: System.Vector2i, size: System.Vector2i):
        """
        Construct the rectangle from its position and size.

        Parameters:
        - position: Position of the top-left corner of the rectangle.
        - size: Size of the rectangle.
        """
        pass

    def contains(self, point: System.Vector2i) -> bool:
        """
        Check if a point is inside the rectangle
        """
        pass

    def find_intersection(self, rectangle: IntRect) -> IntRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """
        pass

    def find_intersection(self, rectangle: FloatRect) -> IntRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """
        pass

    def get_center(self) -> System.Vector2i:
        """
        Get the center of the rectangle.

        Returns:
        - The center of the rectangle.
        """
        pass

class FloatRect:
    """
    Float rectangle.

    sf::FloatRect is a structure that represents a rectangle defined by two positions and two sizes.
    """

    position: System.Vector2f
    size: System.Vector2f

    def __init__(self, position: System.Vector2f, size: System.Vector2f):
        """
        Construct the rectangle from its position and size.

        Parameters:
        - position: Position of the top-left corner of the rectangle.
        - size: Size of the rectangle.
        """
        pass

    def contains(self, point: System.Vector2f) -> bool:
        """
        Check if a point is inside the rectangle
        """
        pass

    def find_intersection(self, rectangle: IntRect) -> FloatRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """
        pass

    def find_intersection(self, rectangle: FloatRect) -> FloatRect | None:
        """
        Find the intersection between two rectangles.

        Parameters:
        - rectangle: The other rectangle to find the intersection with.

        Returns:
        - The intersection rectangle, or None if there is no intersection.
        """
        pass

    def get_center(self) -> System.Vector2f:
        """
        Get the center of the rectangle.

        Returns:
        - The center of the rectangle.
        """
        pass

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

    def __init__(self, sourceFactor: Factor, destinationFactor: Factor, blendEquation: Factor = Equation.Add) -> None: 
        """
        Construct the blend mode given the factors and equation.

        This constructor uses the same factors and equation for both color and alpha components. It also defaults to the Add equation.

        Parameters
        - sourceFactor	Specifies how to compute the source factor for the color and alpha channels.
        - destinationFactor	Specifies how to compute the destination factor for the color and alpha channels.
        - blendEquation	Specifies how to combine the source and destination colors and alpha.

        """
        pass

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
        pass

    color_src_factor: BlendMode.Factor
    color_dst_factor: BlendMode.Factor
    color_equation: BlendMode.Equation
    alpha_src_factor: BlendMode.Factor
    alpha_dst_factor: BlendMode.Factor
    alpha_equation: BlendMode.Equation

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

    def __init__(self) -> None: 
        """
        Default constructor.

        Creates an identity transform (a transform that does nothing).
        """
        pass

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
        pass

    def get_matrix(self) -> List[float]: 
        """
        Return the transform as a 4x4 matrix.

        This function returns a pointer to an array of 16 floats containing the transform elements as a 4x4 matrix, which is directly compatible with OpenGL functions.

        ```
        sf::Transform transform = 

pass;
        glLoadMatrixf(transform.getMatrix());
        ```

        Returns
        - Pointer to a 4x4 matrix
        """
        pass

    def get_inverse(self) -> Transform: 
        """
        Return the inverse of the transform.

        If the inverse cannot be computed, an identity transform is returned.

        Returns
        - A new transform which is the inverse of self
        """
        pass

    def transform_point(self, point: System.Vector2f) -> System.Vector2f: 
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
        pass

    def transform_rect(self, rectangle: FloatRect) -> FloatRect: 
        """
        Transform a rectangle.

        Since SFML doesn't provide support for oriented rectangles, the result of this function is always an axis-aligned rectangle. Which means that if the transform contains a rotation, the bounding rectangle of the transformed rectangle is returned.

        Parameters
        - rectangle	Rectangle to transform

        Returns
        - Transformed rectangle
        """
        pass

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
        pass

    def translate(self, offset: System.Vector2f) -> Transform: 
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
        pass

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
        pass

    def rotate(self, angle: float, center: System.Vector2f) -> Transform: 
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
        pass

    def scale(self, factors: System.Vector2f) -> Transform: 
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
        pass

    def scale(self, factors: System.Vector2f, center: System.Vector2f) -> Transform: 
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
        pass

    @staticmethod
    def identity() -> Transform: 
        """
        The identity transform (does nothing)
        """
        pass

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
        pass

    def set_position(self, position: System.Vector2f) -> None: 
        """
        set the position of the object

        This function completely overwrites the previous position. See the move function to apply an offset based on the previous position instead. The default position of a transformable object is (0, 0).

        Parameters
        - position	New position
        """
        pass

    def set_rotation(self, angle: float) -> None: 
        """
        set the orientation of the object

        This function completely overwrites the previous rotation. See the rotate function to add an angle based on the previous rotation instead. The default rotation of a transformable object is 0.

        Parameters
        - angle	New rotation
        """
        pass

    def set_scale(self, factors: System.Vector2f) -> None: 
        """
        set the scale factors of the object

        This function completely overwrites the previous scale. See the scale function to add a factor based on the previous scale instead. The default scale of a transformable object is (1, 1).

        Parameters
        - factors	New scale factors
        """
        pass

    def set_origin(self, origin: System.Vector2f) -> None: 
        """
        set the local origin of the object

        The origin of an object defines the center point for all transformations (position, scale, rotation). The coordinates of this point must be relative to the top-left corner of the object, and ignore all transformations (position, scale, rotation). The default origin of a transformable object is (0, 0).

        Parameters
        - origin	New origin
        """
        pass

    def get_position(self) -> System.Vector2f: 
        """
        get the position of the object

        Returns
        - Current position
        """
        pass

    def get_rotation(self) -> float: 
        """
        get the orientation of the object

        The rotation is always in the range [0, 360].

        Returns
        - Current rotation
        """
        pass

    def get_scale(self) -> System.Vector2f: 
        """
        get the current scale of the object

        Returns
        - Current scale factor
        """
        pass

    def get_origin(self) -> System.Vector2f: 
        """
        get the local origin of the object

        Returns
        - Current origin
        """
        pass

    def move(self, offset: System.Vector2f) -> None: 
        """
        Move the object by a given offset.

        This function adds to the current position of the object, unlike setPosition which overwrites it. Thus, it is equivalent to the following code:

        ```
        object.setPosition(object.getPosition() + offset);
        ```

        Parameters
        - offset	Offset
        """
        pass

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
        pass

    def scale(self, factor: System.Vector2f) -> None: 
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
        pass

    def get_transform(self) -> Transform: 
        """
        get the combined transform of the object

        Returns
        - Transform combining the position/rotation/scale/origin of the object
        """
        pass

    def get_inverse_transform(self) -> Transform: 
        """
        get the inverse of the combined transform of the object

        Returns
        - Inverse of the combined transformations applied to the object
        """
        pass

class Vertex:
    """
    Point with color and texture coordinates.

    A vertex is an improved point.

    By default, the vertex color is white and texture coordinates are (0, 0).

    It has a position and other extra attributes that will be used for drawing: in SFML, vertices also have a color and a pair of texture coordinates.

    The vertex is the building block of drawing. Everything which is visible on screen is made of vertices. They are grouped as 2D primitives (lines, triangles, 

pass), and these primitives are grouped to create even more complex 2D entities such as sprites, texts, etc.

    If you use the graphical entities of SFML (sprite, text, shape) you won't have to deal with vertices directly. But if you want to define your own 2D entities, such as tiled maps or particle systems, using vertices will allow you to get maximum performances.

    It is recommended to use aggregate initialization to create vertex objects, which initializes the members in order.

    On a C++20-compliant compiler (or where supported as an extension) it is possible to use "designated initializers" to only initialize a subset of members, with the restriction of having to follow the same order in which they are defined.

    Note: Although texture coordinates are supposed to be an integer amount of pixels, their type is float because of some buggy graphics drivers that are not able to process integer coordinates correctly.
    """

    def __init__(self) -> None:
        pass

    def __init__(self, position: System.Vector2f, color: Color, texCoords: System.Vector2f) -> None: 
        pass

    position: System.Vector2f
    color: Color
    texCoords: System.Vector2f

class VertexArray(Drawable):
    """
    Set of one or more 2D primitives.

    sf::VertexArray is a very simple wrapper around a dynamic array of vertices and a primitives type.

    It inherits sf::Drawable, but unlike other drawables it is not transformable.
    """

    def __init__(self) -> None: 
        """
        Default constructor.

        Creates an empty vertex array.
        """
        pass

    def __init__(self, type: PrimitiveType, vertexCount: int) -> None: 
        """
        Construct the vertex array with a type and an initial number of vertices.

        Parameters
        - type	Type of primitives
        - vertexCount	Initial number of vertices in the array
        """
        pass

    def get_vertex_count(self) -> int: 
        """
        Return the vertex count.

        Returns
        - Number of vertices in the array
        """
        pass

    def clear(self) -> None: 
        """
        Clear the vertex array.

        This function removes all the vertices from the array. It doesn't deallocate the corresponding memory, so that adding new vertices after clearing doesn't involve reallocating all the memory.
        """
        pass

    def resize(self, vertexCount: int) -> None: 
        """
        Resize the vertex array.

        If vertexCount is greater than the current size, the previous vertices are kept and new (default-constructed) vertices are added. If vertexCount is less than the current size, existing vertices are removed from the array.

        Parameters
        - vertexCount	New size of the array (number of vertices)
        """
        pass
    def append(self, vertex: Vertex) -> None: 
        """
        Add a vertex to the array.

        Parameters
        - vertex	Vertex to add
        """
        pass

    def set_primitive_type(self, type: PrimitiveType) -> None: 
        """
        Set the type of primitives to draw.

        This function defines how the vertices must be interpreted when it's time to draw them:

        - As points
        - As lines
        - As triangles The default primitive type is sf::PrimitiveType::Points.

        Parameters
        - type	Type of primitive
        """
        pass

    def get_primitive_type(self) -> PrimitiveType: 
        """
        Get the type of primitives drawn by the vertex array.

        Returns
        - Primitive type
        """
        pass

    def get_bounds(self) -> FloatRect: 
        """
        Compute the bounding rectangle of the vertex array.

        This function returns the minimal axis-aligned rectangle that contains all the vertices of the array.

        Returns
        - Bounding rectangle of the vertex array
        """
        pass

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
    
    def __init__(self) -> None: 
        """
        Default constructor.

        Creates an empty vertex buffer.
        """
        pass

    def __init__(self, primitiveType: PrimitiveType) -> None: 
        """
        Construct a VertexBuffer with a specific PrimitiveType

        Creates an empty vertex buffer and sets its primitive type to type.

        Parameters
        - type	Type of primitive
        """
        pass

    def __init__(self, usage: Usage) -> None: 
        """
        Construct a VertexBuffer with a specific usage specifier.

        Creates an empty vertex buffer and sets its usage to usage.

        Parameters
        - usage	Usage specifier
        """
        pass
    def __init__(self, type: PrimitiveType, usage: Usage) -> None: 
        """
        Construct a VertexBuffer with a specific PrimitiveType and usage specifier.

        Creates an empty vertex buffer and sets its primitive type to type and usage to usage.

        Parameters
        - type	Type of primitive
        - usage	Usage specifier
        """
        pass

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
        pass

    def get_vertex_count(self) -> int: 
        """
        Return the vertex count.

        Returns
        - Number of vertices in the vertex buffer
        """
        pass

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
        pass

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
        pass

    def update(self, vertexBuffer: VertexBuffer) -> bool: 
        """
        Copy the contents of another buffer into this buffer.

        Parameters
        - vertexBuffer	Vertex buffer whose contents to copy into this vertex buffer

        Returns
        - true if the copy was successful
        """
        pass

    def set_primitive_type(self, type: PrimitiveType) -> None: 
        """
        Set the type of primitives to draw.

        This function defines how the vertices must be interpreted when it's time to draw them.

        The default primitive type is sf::PrimitiveType::Points.

        Parameters
        - type	Type of primitive
        """
        pass

    def get_primitive_type(self) -> PrimitiveType: 
        """
        Get the type of primitives drawn by the vertex buffer.

        Returns
        - Primitive type
        """
        pass

    def set_usage(self, usage: Usage) -> None: 
        """
        Set the usage specifier of this vertex buffer.

        This function provides a hint about how this vertex buffer is going to be used in terms of data update frequency.

        After changing the usage specifier, the vertex buffer has to be updated with new data for the usage specifier to take effect.

        The default usage type is sf::VertexBuffer::Usage::Stream.

        Parameters
        - usage	Usage specifier
        """
        pass
    
    def get_usage(self) -> Usage: 
        """
        Get the usage specifier of this vertex buffer.

        Returns
        - Usage specifier
        """
        pass

    def get_native_handle(self) -> int: 
        """
        Get the underlying OpenGL handle of the vertex buffer.

        You shouldn't need to use this function, unless you have very specific stuff to implement that SFML doesn't support, or implement a temporary workaround until a bug is fixed.

        Returns
        - OpenGL handle of the vertex buffer or 0 if not yet created
        """
        pass

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
        pass

    @staticmethod
    def is_available() -> bool: 
        """
        Tell whether or not the system supports vertex buffers.

        This function should always be called before using the vertex buffer features. If it returns false, then any attempt to use sf::VertexBuffer will fail.

        Returns
        - true if vertex buffers are supported, false otherwise
        """
        pass

class Shape(Transformable, Drawable):
    """
    Base class for textured shapes with outline.

    sf::Shape is a drawable class that allows to define and display a custom convex shape on a render target.

    It's only an abstract base, it needs to be specialized for concrete types of shapes (circle, rectangle, convex polygon, star, 

pass).

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
        pass

    def set_texture_rect(self, rect: IntRect) -> None: 
        """
        Set the sub-rectangle of the texture that the shape will display.

        The texture rect is useful when you don't want to display the whole texture, but rather a part of it. By default, the texture rect covers the entire texture.

        Parameters
        - rect	Rectangle defining the region of the texture to display
        """
        pass

    def set_fill_color(self, color: Color) -> None: 
        """
        Set the fill color of the shape.

        This color is modulated (multiplied) with the shape's texture if any. It can be used to colorize the shape, or change its global opacity. You can use sf::Color::Transparent to make the inside of the shape transparent, and have the outline alone. By default, the shape's fill color is opaque white.

        Parameters
        - color	New color of the shape
        """
        pass

    def set_outline_color(self, color: Color) -> None: 
        """
        Set the outline color of the shape.

        By default, the shape's outline color is opaque white.

        Parameters
        - color	New outline color of the shape
        """
        pass

    def set_outline_thickness(self, thickness: float) -> None: 
        """
        Set the thickness of the shape's outline.

        Note that negative values are allowed (so that the outline expands towards the center of the shape), and using zero disables the outline. By default, the outline thickness is 0.

        Parameters
        - thickness	New outline thickness
        """
        pass

    def get_texture(self) -> Texture: 
        """
        Get the source texture of the shape.

        If the shape has no source texture, a nullptr is returned. The returned pointer is const, which means that you can't modify the texture when you retrieve it with this function.

        Returns
        - Pointer to the shape's texture
        """
        pass

    def get_texture_rect(self) -> IntRect: 
        """
        Get the sub-rectangle of the texture displayed by the shape.

        Returns
        - Texture rectangle of the shape
        """
        pass

    def get_fill_color(self) -> Color: 
        """
        Get the fill color of the shape.

        Returns
        - Fill color of the shape
        """
        pass

    def get_outline_color(self) -> Color: 
        """
        Get the outline color of the shape.

        Returns
        - Outline color of the shape
        """
        pass

    def get_outline_thickness(self) -> float: 
        """
        Get the outline thickness of the shape.

        Returns
        - Outline thickness of the shape
        """
        pass

    def get_point_count(self) -> int: 
        """
        Get the total number of points of the shape.

        Returns
        - Number of points of the shape
        """
        pass

    def get_point(self, index: int) -> System.Vector2f: 
        """
        Get a point of the shape.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. getPointCount() - 1]

        Returns
        - index-th point of the shape
        """
        pass

    def get_geometric_center(self) -> System.Vector2f: 
        """
        Get the geometric center of the shape.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account.

        Returns
        - The geometric center of the shape
        """
        pass

    def get_local_bounds(self) -> FloatRect: 
        """
        Get the local bounding rectangle of the entity.

        The returned rectangle is in local coordinates, which means that it ignores the transformations (translation, rotation, scale, 

pass) that are applied to the entity. In other words, this function returns the bounds of the entity in the entity's coordinate system.

        Returns
        - Local bounding rectangle of the entity
        """
        pass
    
    def get_global_bounds(self) -> FloatRect: 
        """
        Get the global (non-minimal) bounding rectangle of the entity.

        The returned rectangle is in global coordinates, which means that it takes into account the transformations (translation, rotation, scale, 

pass) that are applied to the entity. In other words, this function returns the bounds of the shape in the global 2D world's coordinate system.

        This function does not necessarily return the minimal bounding rectangle. It merely ensures that the returned rectangle covers all the vertices (but possibly more). This allows for a fast approximation of the bounds as a first check; you may want to use more precise checks on top of that.

        Returns
        - Global bounding rectangle of the entity
        """
        pass

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

    def __init__(self, color: bytes) -> None: 
        """
        Construct the color from 32-bit unsigned integer.

        Parameters
        - color	Number containing the RGBA components (in that order)
        """
        pass

    def __init__(self, red: int, green: int, blue: int, alpha: int = 255) -> None: 
        """
        Construct the color from its 4 RGBA components.

        Parameters
        - red	Red component (in the range [0, 255])
        - green	Green component (in the range [0, 255])
        - blue	Blue component (in the range [0, 255])
        - alpha	Alpha (opacity) component (in the range [0, 255])
        """
        pass

    def to_integer(self) -> int: 
        """
        Retrieve the color as a 32-bit unsigned integer.

        Returns
        - Color represented as a 32-bit unsigned integer
        """
        pass

    r: int
    g: int
    b: int
    a: int

    @staticmethod
    def black() -> Color: 
        pass
    @staticmethod
    def white() -> Color: 
        pass
    @staticmethod
    def red() -> Color: 
        pass
    @staticmethod
    def green() -> Color: 
        pass
    @staticmethod
    def blue() -> Color: 
        pass
    @staticmethod
    def yellow() -> Color: 
        pass
    @staticmethod
    def magenta() -> Color: 
        pass
    @staticmethod
    def cyan() -> Color: 
        pass
    @staticmethod
    def transparent() -> Color: 
        pass

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
            pass

        family: str

    def __init__(self) -> None: 
        """
        Default constructor.

        Construct an empty font that does not contain any glyphs.
        """
        pass
    
    def __init__(self, data: Any, sizeInBytes: bytes) -> None: 
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
        pass

    def __init__(self, stream: System.InputStream) -> None: 
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
        pass

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
        pass

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
        pass

    def open_from_memory(self, data: Any, sizeInBytes: bytes) -> bool: 
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
        pass

    def open_from_stream(self, stream: System.InputStream) -> bool: 
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
        pass

    def get_info(self) -> Info: 
        """
        Get the font information.

        Returns
        - A structure that holds the font information
        """
        pass

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
        pass

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
        pass

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
        pass

    def get_line_spacing(self, characterSize: int) -> float: 
        """
        Get the line spacing.

        Line spacing is the vertical offset to apply between two consecutive lines of text.

        Parameters
        - characterSize	Reference character size

        Returns
        - Line spacing, in pixels
        """
        pass

    def get_underline_position(self, characterSize: int) -> float: 
        """
        Get the position of the underline.

        Underline position is the vertical offset to apply between the baseline and the underline.

        Parameters
        - characterSize	Reference character size

        Returns
        - Underline position, in pixels
        """
        pass

    def get_underline_thickness(self, characterSize: int) -> float: 
        """
        Get the thickness of the underline.

        Underline thickness is the vertical size of the underline.

        Parameters
        - characterSize	Reference character size

        Returns
        - Underline thickness, in pixel
        """
        pass

    def set_smooth(self, smooth: bool) -> None: 
        """
        Enable or disable the smooth filter.

        When the filter is activated, the font appears smoother so that pixels are less noticeable. However if you want the font to look exactly the same as its source file, you should disable it. The smooth filter is enabled by default.

        Parameters
        - smooth	true to enable smoothing, false to disable it
        """
        pass

    def is_smooth(self) -> bool: 
        """
        Tell whether the smooth filter is enabled or not.

        Returns
        - true if smoothing is enabled, false if it is disabled
        """
        pass
    def get_texture(self, characterSize: int) -> Texture: 
        """
        Retrieve the texture containing the loaded glyphs of a certain size.

        The contents of the returned texture changes as more glyphs are requested, thus it is not very relevant. It is mainly used internally by sf::Text.

        Parameters
        - characterSize	Reference character size
        """
        pass

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
        pass

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

    def __init__(self) -> None: 
        """
        Default constructor.

        Constructs an image with width 0 and height 0.
        """
        pass

    def __init__(self, size: System.Vector2u, pixels: bytes) -> None: 
        """
        Construct the image from an array of pixels.

        The pixel array is assumed to contain 32-bits RGBA pixels, and have the given size. If not, this is an undefined behavior. If pixels is nullptr, an empty image is created.

        Parameters
        - size	Width and height of the image
        - pixels	Array of pixels to copy to the image
        """
        pass

    def __init__(self, data: Any, size: bytes) -> None: 
        """
        Construct the image from a file in memory.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm.

        Parameters
        - data	Pointer to the file data in memory
        - size	Size of the data to load, in bytes

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """
        pass

    def __init__(self, stream: System.InputStream) -> None: 
        """
        Construct the image from a custom stream.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm.

        Parameters
        - stream	Source stream to read from

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """
        pass

    def __init__(self, size: System.Vector2u, color: Color = Color.black) -> None: 
        """
        Construct the image and fill it with a unique color.

        Parameters
        - size	Width and height of the image
        - color	Fill color
        """
        pass

    def resize(self, size: System.Vector2u, color: Color = Color.black) -> None: 
        """
        Resize the image and fill it with a unique color.

        Parameters
        - size	Width and height of the image
        - color	Fill color
        """
        pass

    def resize(self, size: System.Vector2u, pixels: bytes) -> None: 
        """
        Resize the image from an array of pixels.

        The pixel array is assumed to contain 32-bits RGBA pixels, and have the given size. If not, this is an undefined behavior. If pixels is nullptr, an empty image is created.

        Parameters
        - size	Width and height of the image
        - pixels	Array of pixels to copy to the image
        """
        pass

    def load_from_file(self, filename: str) -> bool: 
        """
        Load the image from a file on disk.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm. If this function fails, the image is left unchanged.

        Parameters
        - filename	Path of the image file to load
        """
        pass

    def load_from_memory(self, data: Any, size: bytes) -> bool: 
        """
        Load the image from a file in memory.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm. If this function fails, the image is left unchanged.

        Parameters
        - data	Pointer to the file data in memory
        - size	Size of the data to load, in bytes

        Returns
        - true if loading was successful
        """
        pass

    def load_from_stream(self, stream: System.InputStream) -> bool: 
        """
        Load the image from a custom stream.

        The supported image formats are bmp, png, tga, jpg, gif, psd, hdr, pic and pnm. Some format options are not supported, like jpeg with arithmetic coding or ASCII pnm. If this function fails, the image is left unchanged.

        Parameters
        - stream	Source stream to read from

        Returns
        - true if loading was successful
        """
        pass

    def save_to_file(self, filename: str) -> bool: 
        """
        Save the image to a file on disk.

        The format of the image is automatically deduced from the extension. The supported image formats are bmp, png, tga and jpg. The destination file is overwritten if it already exists. This function fails if the image is empty.

        Parameters
        - filename	Path of the file to save

        Returns
        - true if saving was successful
        """
        pass

    def save_to_memory(self, format: str) -> List[bytes] | None: 
        """
        Save the image to a buffer in memory.

        The format of the image must be specified. The supported image formats are bmp, png, tga and jpg. This function fails if the image is empty, or if the format was invalid.

        Parameters
        - format	Encoding format to use

        Returns
        - Buffer with encoded data if saving was successful, otherwise std::nullopt
        """
        pass

    def get_size(self) -> System.Vector2u: 
        """
        Return the size (width and height) of the image.

        Returns
        - Size of the image, in pixels
        """
        pass

    def create_mask_from_color(self, color: Color, alpha: int = 0) -> None: 
        """
        Create a transparency mask from a specified color-key.

        This function sets the alpha value of every pixel matching the given color to alpha (0 by default), so that they become transparent.

        Parameters
        - color	Color to make transparent
        - alpha	Alpha value to assign to transparent pixels
        """
        pass

    def copy(self, source: Image, dest: System.Vector2u, source_rect: IntRect = IntRect(), apply_alpha: bool = False) -> None: 
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
        pass

    def set_pixel(self, coords: System.Vector2u, color: Color) -> None: 
        """
        Change the color of a pixel.

        This function doesn't check the validity of the pixel coordinates, using out-of-range values will result in an undefined behavior.

        Parameters
        - coords	Coordinates of pixel to change
        - color	New color of the pixel
        """
        pass

    def get_pixel(self, coords: System.Vector2u) -> Image: 
        """
        Get the color of a pixel.

        This function doesn't check the validity of the pixel coordinates, using out-of-range values will result in an undefined behavior.

        Parameters
        - coords	Coordinates of pixel to change

        Returns
        - Color of the pixel at given coordinates
        """
        pass

    def get_pixels_ptr(self) -> bytes: 
        """
        Get a read-only pointer to the array of pixels.

        The returned value points to an array of RGBA pixels made of 8 bit integer components. The size of the array is width * height * 4 (getSize().x * getSize().y * 4). Warning: the returned pointer may become invalid if you modify the image, so you should never store it for too long. If the image is empty, a null pointer is returned.

        Returns
        - Read-only pointer to the array of pixels
        """
        pass

    def flip_horizontally(self) -> None: 
        """
        Flip the image horizontally (left <-> right)
        """
        pass

    def flip_vertically(self) -> None: 
        """
        Flip the image vertically (top <-> bottom)
        """
        pass

class ConvexShape(Shape):
    """
    Specialized shape representing a convex polygon.

    This class inherits all the functions of sf::Transformable (position, rotation, scale, bounds, 

pass) as well as the functions of sf::Shape (outline, color, texture, 

pass).

    It is important to keep in mind that a convex shape must always be

pass convex, otherwise it may not be drawn correctly. Moreover, the points must be defined in order; using a random order would result in an incorrect shape.
    """

    def __init__(self, pointCount: int = 0) -> None: 
        """
        Default constructor.

        Parameters
        - pointCount	Number of points of the polygon
        """
        pass

    def set_point_count(self, count: int) -> None: 
        """
        Set the number of points of the polygon.

        For the shape to be rendered as expected, count must be greater or equal to 3.

        Parameters
        - count	New number of points of the polygon
        """
        pass

    def get_point_count(self) -> int: 
        """
        Get the number of points of the polygon.

        Returns
        - Number of points of the polygon
        """
        pass

    def set_point(self, index: int, point: System.Vector2f) -> None: 
        """
        Set the position of a point.

        Don't forget that the shape must be convex and the order of points matters. Points should not overlap. This applies to rendering; it is explicitly allowed to temporarily have non-convex or degenerate shapes when not drawn (e.g. during shape initialization).

        Point count must be specified beforehand. The behavior is undefined if index is greater than or equal to getPointCount.

        Parameters
        - index	Index of the point to change, in range [0 .. getPointCount() - 1]
        - point	New position of the point
        """
        pass

    def get_point(self, index: int) -> System.Vector2f: 
        """
        Get the position of a point.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. getPointCount() - 1]

        Returns
        - Position of the index-th point of the polygon
        """
        pass

class CircleShape(Shape):
    """
    Specialized shape representing a circle.

    This class inherits all the functions of sf::Transformable (position, rotation, scale, bounds, 

pass) as well as the functions of sf::Shape (outline, color, texture, 

pass).

    Since the graphics card can't draw perfect circles, we have to fake them with multiple triangles connected to each other. The "points count" property of sf::CircleShape defines how many of these triangles to use, and therefore defines the quality of the circle.

    The number of points can also be used for another purpose; with small numbers you can create any regular polygon shape: equilateral triangle, square, pentagon, hexagon, 

pass
    """

    def __init__(self, radius: float = 0, pointCount: int = 30) -> None: 
        """
        Default constructor.

        Parameters
        - radius	Radius of the circle
        - pointCount	Number of points composing the circle
        """
        pass

    def set_radius(self, radius: float) -> None: 
        """
        Set the radius of the circle.

        Parameters
        - radius	New radius of the circle
        """
        pass

    def get_radius(self) -> float: 
        """
        Get the radius of the circle.

        Returns
        - Radius of the circle
        """
        pass

    def set_point_count(self, count: int) -> None: 
        """
        Set the number of points of the circle.

        Parameters
        - count	New number of points of the circle
        """
        pass

    def get_point_count(self) -> int: 
        """
        Get the number of points of the circle.

        Returns
        - Number of points of the circle
        """
        pass
    def get_point(self, index: int) -> System.Vector2f: 
        """
        Get a point of the circle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. getPointCount() - 1]

        Returns
        - index-th point of the shape
        """
        pass

    def get_geometric_center(self) -> System.Vector2f: 
        """
        Get the geometric center of the circle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account.

        Returns
        - The geometric center of the shape
        """
        pass

class RectangleShape(Shape):
    """
    Specialized shape representing a rectangle.

    This class inherits all the functions of sf::Transformable (position, rotation, scale, bounds, 

pass) as well as the functions of sf::Shape (outline, color, texture, 

pass).
    """

    def __init__(self, size: System.Vector2f = System.Vector2f()) -> None: 
        """
        Default constructor.

        Parameters
        - size	Size of the rectangle
        """
        pass

    def set_size(self, size: System.Vector2f) -> None: 
        """
        Set the size of the rectangle.

        Parameters
        - size	New size of the rectangle
        """
        pass

    def get_size(self) -> System.Vector2f: 
        """
        Get the size of the rectangle.

        Returns
        - Size of the rectangle
        """
        pass

    def get_point_count(self) -> int: 
        """
        Get the number of points defining the shape.

        Returns
        - Number of points of the shape. For rectangle shapes, this number is always 4.
        """
        pass

    def get_point(self, index: int) -> System.Vector2f: 
        """
        Get a point of the rectangle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account. The result is undefined if index is out of the valid range.

        Parameters
        - index	Index of the point to get, in range [0 .. 3]

        Returns
        - index-th point of the shape
        """
        pass

    def get_geometric_center(self) -> System.Vector2f: 
        """
        Get the geometric center of the rectangle.

        The returned point is in local coordinates, that is, the shape's transforms (position, rotation, scale) are not taken into account.

        Returns
        - The geometric center of the shape
        """
        pass

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
        pass

    def __init__(self, theBlendMode: BlendMode) -> None: 
        """
        Construct a default set of render states with a custom blend mode.

        Parameters
        - theBlendMode	Blend mode to use
        """
        pass

    def __init__(self, theStencilMode: StencilMode) -> None: 
        """
        Construct a default set of render states with a custom stencil mode.

        Parameters
        - theStencilMode	Stencil mode to use
        """
        pass

    def __init__(self, theTransform: Transform) -> None: 
        """
        Construct a default set of render states with a custom transform.

        Parameters
        - theTransform	Transform to use
        """
        pass

    def __init__(self, theTexture: Texture) -> None: 
        """
        Construct a default set of render states with a custom texture.

        Parameters
        - theTexture	Texture to use
        """
        pass

    def __init__(self, shader: Shader) -> None: 
        """
        Construct a default set of render states with a custom shader.

        Parameters
        - theShader	Shader to use
        """
        pass

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
        pass

    @staticmethod
    def default() -> RenderStates: 
        """
        Special instance holding the default render states.
        """
        pass

class RenderTarget:
    def clear(self, color: Color) -> None: 

pass
    def clear_stencil(self) -> None: 

pass
    def clear(self, color: Color, stencil_value: StencilValue) -> None: 

pass
    def set_view(self, view: View) -> None: 

pass
    def get_view(self) -> View: 

pass
    def get_default_view(self) -> View: 

pass
    def get_viewport(self) -> IntRect: 

pass
    def get_scissor(self) -> IntRect: 

pass
    def map_pixel_to_coords(self, point: Vector2i) -> Vector2f: 

pass
    def map_coords_to_pixel(self, point: Vector2f) -> Vector2i: 

pass
    def draw(self, drawable: Drawable, states: RenderStates = 

pass) -> None: 

pass
    def draw(self, vertices: Vertex, vertex_count: int, type: PrimitiveType, states: RenderStates = 

pass) -> None: 

pass
    def draw(self, buffer: VertexBuffer, states: RenderStates = 

pass) -> None: 

pass
    def draw(self, buffer: VertexBuffer, first: int, count: int, states: RenderStates = 

pass) -> None: 

pass
    def get_size(self) -> Vector2u: 

pass
    def is_srgb(self) -> bool: 

pass
    def set_active(self, active: bool) -> bool: 

pass
    def push_gl_states(self) -> None: 

pass
    def pop_gl_states(self) -> None: 

pass
    def reset_gl_states(self) -> None: 

pass

class RenderTexture(RenderTarget):
    def __init__(self) -> None: 

pass
    def __init__(self, size: Vector2u, context_settings: ContextSettings) -> None: 

pass
    def resize(self, size: Vector2u) -> None: 

pass
    def set_smooth(self, smooth: bool) -> None: 

pass
    def is_smooth(self) -> bool: 

pass
    def set_repeated(self, repeated: bool) -> None: 

pass
    def is_repeated(self) -> bool: 

pass
    def generate_mipmap(self) -> bool: 

pass
    def set_active(self, active: bool) -> bool: 

pass
    def display(self) -> None: 

pass
    def get_size(self) -> Vector2u: 

pass
    def is_srgb(self) -> bool: 

pass
    def get_texture(self) -> Texture: 

pass
    @staticmethod
    def get_maximum_anti_aliasing_level() -> int: 

pass

class RenderWindow(Window, RenderTarget):
    def __init__(self) -> None: 

pass
    def __init__(self, mode: VideoMode, title: str, style: int = 

pass, state: State = 

pass, context_settings: ContextSettings = 

pass) -> None: 

pass
    def get_size(self) -> Vector2u: 

pass
    def set_icon(self, image: Image) -> None: 

pass
    def set_icon(self, size: Vector2u, pixels: bytes) -> None: 

pass
    def is_srgb(self) -> bool: 

pass
    def set_active(self, active: bool) -> bool: 

pass

class Shader:
    class Type:
        Vertex: int
        Geometry: int
        Fragment: int

    def __init__(self) -> None: 

pass
    def load_from_file(self, filename: str, type: Type) -> bool: 

pass
    def load_from_file(self, vertex: str, fragment: str) -> bool: 

pass
    def load_from_file(self, vertex: str, geometry: str, fragment: str) -> bool: 

pass
    def load_from_memory(self, source: str, type: Type) -> bool: 

pass
    def load_from_memory(self, vertex: str, fragment: str) -> bool: 

pass
    def load_from_memory(self, vertex: str, geometry: str, fragment: str) -> bool: 

pass
    def set_uniform(self, name: str, x: float) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Vec2) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Vec3) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Vec4) -> None: 

pass
    def set_uniform(self, name: str, x: int) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Ivec2) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Ivec3) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Ivec4) -> None: 

pass
    def set_uniform(self, name: str, x: bool) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Bvec2) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Bvec3) -> None: 

pass
    def set_uniform(self, name: str, vector: Glsl.Bvec4) -> None: 

pass
    def set_uniform(self, name: str, matrix: Glsl.Mat3) -> None: 

pass
    def set_uniform(self, name: str, matrix: Glsl.Mat4) -> None: 

pass
    def set_uniform(self, name: str, texture: Texture) -> None: 

pass
    def set_uniform_array(self, name: str, values: float, count: int) -> None: 

pass
    def set_uniform_array(self, name: str, values: Glsl.Vec2, count: int) -> None: 

pass
    def set_uniform_array(self, name: str, values: Glsl.Vec3, count: int) -> None: 

pass
    def set_uniform_array(self, name: str, values: Glsl.Vec4, count: int) -> None: 

pass
    def set_uniform_array(self, name: str, matrix_array: Glsl.Mat3, count: int) -> None: 

pass
    def set_uniform_array(self, name: str, matrix_array: Glsl.Mat4, count: int) -> None: 

pass
    def get_native_handle(self) -> int: 

pass
    @staticmethod
    def bind(shader: Optional['Shader']) -> None: 

pass
    @staticmethod
    def is_available() -> bool: 

pass
    @staticmethod
    def is_geometry_available() -> bool: 

pass