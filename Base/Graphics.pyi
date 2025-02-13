import enum
from typing import List
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
        sf::Transform transform = ...;
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

    def set_scale(self, scale: System.Vector2f) -> None: 
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

    def scale(self, factors: System.Vector2f) -> None: 
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

    The vertex is the building block of drawing. Everything which is visible on screen is made of vertices. They are grouped as 2D primitives (lines, triangles, ...), and these primitives are grouped to create even more complex 2D entities such as sprites, texts, etc.

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

    def __init__(self, primitiveType: PrimitiveType, vertexCount: int) -> None: 
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
    def __init__(self, primitiveType: PrimitiveType, usage: Usage) -> None: 
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

    def update(self, other: VertexBuffer) -> bool: 
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
    def bind(buffer: VertexBuffer) -> None: 
        """
        Bind a vertex buffer for rendering.

        This function is not part of the graphics API, it mustn't be used when drawing SFML entities. It must be used only if you mix sf::VertexBuffer with OpenGL code.

        ```
        sf::VertexBuffer vb1, vb2;
        ...
        sf::VertexBuffer::bind(&vb1);
        // draw OpenGL stuff that use vb1...
        sf::VertexBuffer::bind(&vb2);
        // draw OpenGL stuff that use vb2...
        sf::VertexBuffer::bind(nullptr);
        // draw OpenGL stuff that use no vertex buffer...
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
