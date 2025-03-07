"""
Socket-based communication, utilities and higher-level network protocols (HTTP, FTP).
"""

# pylint: disable=unused-argument
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=invalid-name

from __future__ import annotations
import enum
from typing import Optional, overload
from . import sfSystem

class IpAddress:
    """
    Encapsulate an IPv4 network address.

    sf::IpAddress is a utility class for manipulating network addresses.

    It provides a set a implicit constructors and conversion functions to easily build or transform an IP address from/to various representations.
    """

    @overload
    def __init__(self, byte0: int, byte1: int, byte2: int, byte3: int) -> None:
        """
        Construct the address from 4 bytes.

        Calling IpAddress(a, b, c, d) is equivalent to calling IpAddress::resolve("a.b.c.d"), but safer as it doesn't have to parse a string to get the address components.

        Parameters
        - byte0	First byte of the address
        - byte1	Second byte of the address
        - byte2	Third byte of the address
        - byte3	Fourth byte of the address
        """

    @overload
    def __init__(self, address: int) -> None:
        """
        Construct the address from a 32-bits integer.

        This constructor uses the internal representation of the address directly. It should be used for optimization purposes, and only if you got that representation from IpAddress::toInteger().

        Parameters
        - address	4 bytes of the address packed into a 32-bits integer
        """

    @staticmethod
    def resolve(host: str) -> IpAddress:
        """
        Construct the address from a null-terminated string view.

        Here address can be either a decimal address (ex: "192.168.1.56") or a network name (ex: "localhost").

        Parameters
        - address	IP address or network name

        Returns
        - Address if provided argument was valid, otherwise std::nullopt
        """

    def to_string(self) -> str:
        """
        Get a string representation of the address.

        The returned string is the decimal representation of the IP address (like "192.168.1.56"), even if it was constructed from a host name.

        Returns
        - String representation of the address
        """

    def to_integer(self) -> int:
        """
        Get an integer representation of the address.

        The returned number is the internal representation of the address, and should be used for optimization purposes only (like sending the address through a socket). The integer produced by this function can then be converted back to a sf::IpAddress with the proper constructor.

        Returns
        - 32-bits unsigned integer representation of the address
        """

    @staticmethod
    def get_local_address() -> IpAddress:
        """
        Get the computer's local address.

        The local address is the address of the computer from the LAN point of view, i.e. something like 192.168.1.56. It is meaningful only for communications over the local network. Unlike getPublicAddress, this function is fast and may be used safely anywhere.

        Returns
        - Local IP address of the computer on success, std::nullopt otherwise
        """

    @staticmethod
    def get_public_address(timeout: Optional[sfSystem.Time] = None) -> IpAddress:
        """
        Get the computer's public address.

        The public address is the address of the computer from the internet point of view, i.e. something like 89.54.1.169. It is necessary for communications over the world wide web. The only way to get a public address is to ask it to a distant website; as a consequence, this function depends on both your network connection and the server, and may be very slow. You should use it as few as possible. Because this function depends on the network connection and on a distant server, you may use a time limit if you don't want your program to be possibly stuck waiting in case there is a problem; this limit is deactivated by default.

        Parameters
        - timeout	Maximum time to wait

        Returns
        - Public IP address of the computer on success, std::nullopt otherwise
        """

    @staticmethod
    def Any() -> IpAddress:
        """
        Value representing any address (0.0.0.0)
        """

    @staticmethod
    def LocalHost() -> IpAddress:
        """
        The "localhost" address (for connecting a computer to itself locally)
        """

    @staticmethod
    def Broadcast() -> IpAddress:
        """
        The "broadcast" address (for sending UDP messages to everyone on a local network)
        """

class Ftp:
    """
    A FTP client.

    sf::Ftp is a very simple FTP client that allows you to communicate with a FTP server.

    The FTP protocol allows you to manipulate a remote file system (list files, upload, download, create, remove, ...).

    Using the FTP client consists of 4 parts:

    Connecting to the FTP server
    Logging in (either as a registered user or anonymously)
    Sending commands to the server
    Disconnecting (this part can be done implicitly by the destructor)
    Every command returns a FTP response, which contains the status code as well as a message from the server. Some commands such as getWorkingDirectory() and getDirectoryListing() return additional data, and use a class derived from sf::Ftp::Response to provide this data. The most often used commands are directly provided as member functions, but it is also possible to use specific commands with the sendCommand() function.

    Note that response statuses >= 1000 are not part of the FTP standard, they are generated by SFML when an internal error occurs.

    All commands, especially upload and download, may take some time to complete. This is important to know if you don't want to block your application while the server is completing the task.
    """

    class TransferMode(enum.IntEnum):
        """
        Enumeration of transfer modes.

        Enumerator
        - Binary Binary mode (file is transferred as a sequence of bytes)
        - Ascii Text mode using ASCII encoding.
        - Ebcdic Text mode using EBCDIC encoding.
        """
        Binary: int
        Ascii: int
        Ebcdic: int

    class Response:
        """
        FTP response.
        """

        class Status(enum.IntEnum):
            """
            Status codes possibly returned by a FTP response.

            Enumerator
            - RestartMarkerReply: Restart marker reply.
            - ServiceReadySoon: Service ready in N minutes.
            - DataConnectionAlreadyOpened: Data connection already opened, transfer starting.
            - OpeningDataConnection: File status ok, about to open data connection.
            - Ok: Command ok.
            - PointlessCommand: Command not implemented.
            - SystemStatus: System status, or system help reply.
            - DirectoryStatus: Directory status.
            - FileStatus: File status.
            - HelpMessage: Help message.
            - SystemType: NAME system type, where NAME is an official system name from the list in the Assigned Numbers document.
            - ServiceReady: Service ready for new user.
            - ClosingConnection: Service closing control connection.
            - DataConnectionOpened: Data connection open, no transfer in progress.
            - ClosingDataConnection: Closing data connection, requested file action successful.
            - EnteringPassiveMode: Entering passive mode.
            - LoggedIn: User logged in, proceed. Logged out if appropriate.
            - FileActionOk: Requested file action ok.
            - DirectoryOk: PATHNAME created.
            - NeedPassword: User name ok, need password.
            - NeedAccountToLogIn: Need account for login.
            - NeedInformation: Requested file action pending further information.
            - ServiceUnavailable: Service not available, closing control connection.
            - DataConnectionUnavailable: Can't open data connection.
            - TransferAborted: Connection closed, transfer aborted.
            - FileActionAborted: Requested file action not taken.
            - LocalError: Requested action aborted, local error in processing.
            - InsufficientStorageSpace: Requested action not taken; insufficient storage space in system, file unavailable.
            - CommandUnknown: Syntax error, command unrecognized.
            - ParametersUnknown: Syntax error in parameters or arguments.
            - CommandNotImplemented: Command not implemented.
            - BadCommandSequence: Bad sequence of commands.
            - ParameterNotImplemented: Command not implemented for that parameter.
            - NotLoggedIn: Not logged in.
            - NeedAccountToStore: Need account for storing files.
            - FileUnavailable: Requested action not taken, file unavailable.
            - PageTypeUnknown: Requested action aborted, page type unknown.
            - NotEnoughMemory: Requested file action aborted, exceeded storage allocation.
            - FilenameNotAllowed: Requested action not taken, file name not allowed.
            - InvalidResponse: Not part of the FTP standard, generated by SFML when a received response cannot be parsed.
            - ConnectionFailed: Not part of the FTP standard, generated by SFML when the low-level socket connection with the server fails.
            - ConnectionClosed: Not part of the FTP standard, generated by SFML when the low-level socket connection is unexpectedly closed.
            - InvalidFile: Not part of the FTP standard, generated by SFML when a local file cannot be read or written.
            """

            RestartMarkerReply = 110
            ServiceReadySoon = 120
            DataConnectionAlreadyOpened = 125
            OpeningDataConnection = 150
            Ok = 200,
            PointlessCommand = 202,
            SystemStatus = 211,
            DirectoryStatus = 212,
            FileStatus = 213,
            HelpMessage = 214,
            SystemType = 215,
            ServiceReady = 220,
            ClosingConnection = 221,
            DataConnectionOpened = 225,
            ClosingDataConnection = 226,
            EnteringPassiveMode = 227,
            LoggedIn = 230,
            FileActionOk = 250,
            DirectoryOk = 257,
            NeedPassword = 331,
            NeedAccountToLogIn = 332,
            NeedInformation = 350,
            ServiceUnavailable = 421,
            DataConnectionUnavailable = 425,
            TransferAborted = 426,
            FileActionAborted = 450,
            LocalError = 451,
            InsufficientStorageSpace = 452,
            CommandUnknown = 500,
            ParametersUnknown = 501,
            CommandNotImplemented = 502,
            BadCommandSequence = 503,
            ParameterNotImplemented = 504,
            NotLoggedIn = 530,
            NeedAccountToStore = 532,
            FileUnavailable = 550,
            PageTypeUnknown = 551,
            NotEnoughMemory = 552,
            FilenameNotAllowed = 553,
            InvalidResponse = 1000,
            ConnectionFailed = 1001,
            ConnectionClosed = 1002,
            InvalidFile = 1003

        def __init__(self, code: Status = Status.InvalidResponse, message: str = '') -> None:
            """
            Default constructor.

            This constructor is used by the FTP client to build the response.

            Parameters
            - code	Response status code
            - message	Response message
            """

        def is_ok(self) -> bool:
            """
            Check if the status code means a success.

            This function is defined for convenience, it is equivalent to testing if the status code is < 400.

            Returns
            - true if the status is a success, false if it is a failure
            """

        def get_status(self) -> Ftp.Response.Status:
            """
            Get the status code of the response.

            Returns
            - Status code
            """

        def get_message(self) -> str:
            """
            Get the full message contained in the response.

            Returns
            - The response message
            """


    class DirectoryResponse(Response):
        """
        Specialization of FTP response returning a directory.
        """
        def __init__(self, response: Ftp.Response) -> None:
            """
            Default constructor.

            Parameters
            - response	Source response
            """

        def get_directory(self) -> str:
            """
            Get the directory returned in the response.

            Returns
            - Directory name
            """

    class ListingResponse(Response):
        """
        Specialization of FTP response returning a file name listing.
        """

        def __init__(self, response: Ftp.Response, data: str) -> None:
            """
            Default constructor.

            Parameters
            - response	Source response
            - data	Data containing the raw listing
            """

        def get_listing(self) -> list[str]:
            """
            Return the array of directory/file names.

            Returns
            - Array containing the requested listing
            """


    def __init__(self) -> None:
        """
        Default constructor.
        """

    def connect(self, server: str, port: int = 21, timeout: sfSystem.Time = sfSystem.Time.Zero) -> Response:
        """
        Connect to the FTP server.

        Parameters:
        - server: The address of the FTP server.
        - port: The port to connect to, default is 21.
        - timeout: The maximum time to wait for the connection, default is sf::Time::Zero.
        """

    def disconnect(self) -> Response:
        """
        Close the connection with the server.

        Returns
        - Server response to the request
        """

    @overload
    def login(self) -> Response:
        """
        Log in using an anonymous account.

        Logging in is mandatory after connecting to the server. Users that are not logged in cannot perform any operation.

        Returns
        - Server response to the request
        """

    @overload
    def login(self, username: str, password: str) -> Response:
        """
        Log in using a username and a password.

        Logging in is mandatory after connecting to the server. Users that are not logged in cannot perform any operation.

        Parameters
        - username	User name
        - password	Password

        Returns
        - Server response to the request
        """

    def keep_alive(self) -> Response:
        """
        Send a null command to keep the connection alive.

        This command is useful because the server may close the connection automatically if no command is sent.

        Returns
        - Server response to the request
        """

    def get_working_directory(self) -> DirectoryResponse:
        """
        Get the current working directory.

        The working directory is the root path for subsequent operations involving directories and/or filenames.

        Returns
        - Server response to the request
        """

    def get_directory_listing(self, directory: str = "") -> ListingResponse:
        """
        Get the contents of the given directory.

        This function retrieves the sub-directories and files contained in the given directory. It is not recursive. The directory parameter is relative to the current working directory.

        Parameters
        - directory	Directory to list
        Returns
        - Server response to the request
        """

    def change_directory(self, name: str) -> Response:
        """
        Change the current working directory.

        The new directory must be relative to the current one.

        Parameters
        - directory	New working directory

        Returns
        - Server response to the request
        """

    def parent_directory(self) -> Response:
        """
         Go to the parent directory of the current one.

        Returns
        - Server response to the request
        """

    def create_directory(self, name: str) -> Response:
        """
        Create a new directory.

        The new directory is created as a child of the current working directory.

        Parameters
        - name	Name of the directory to create

        Returns
        - Server response to the request
        """

    def delete_directory(self, name: str) -> Response:
        """
        Remove an existing directory.

        The directory to remove must be relative to the current working directory. Use this function with caution, the directory will be removed permanently!

        Parameters
        - name	Name of the directory to remove

        Returns
        - Server response to the request
        """

    def rename_file(self, file: str, newName: str) -> Response:
        """
        Rename an existing file.

        The file names must be relative to the current working directory.

        Parameters
        - file	File to rename
        - newName	New name of the file

        Returns
        - Server response to the request
        """

    def delete_file(self, file: str) -> Response:
        """
        Remove an existing file.

        The file name must be relative to the current working directory. Use this function with caution, the file will be removed permanently!

        Parameters
        - name	File to remove
        Returns
        - Server response to the request
        """

    def download(self, remoteFile: str, localPath: str, mode: TransferMode = TransferMode.Binary) -> Response:
        """
        Download a file from the server.

        The file name of the distant file is relative to the current working directory of the server, and the local destination path is relative to the current directory of your application. If a file with the same file name as the distant file already exists in the local destination path, it will be overwritten.

        Parameters
        - remoteFile	File name of the distant file to download
        - localPath	The directory in which to put the file on the local computer
        - mode	Transfer mode

        Returns
        - Server response to the request
        """

    def upload(self, localFile: str, remotePath: str, mode: TransferMode = TransferMode.Binary, append: bool = False) -> Response:
        """
        Upload a file to the server.

        The name of the local file is relative to the current working directory of your application, and the remote path is relative to the current directory of the FTP server.

        The append parameter controls whether the remote file is appended to or overwritten if it already exists.

        Parameters
        - localFile	Path of the local file to upload
        - remotePath	The directory in which to put the file on the server
        - mode	Transfer mode
        - append	Pass true to append to or false to overwrite the remote file if it already exists

        Returns
        - Server response to the request
        """

    def send_command(self, command: str, parameter: str = "") -> Response:
        """
        Send a command to the FTP server.

        While the most often used commands are provided as member functions in the sf::Ftp class, this method can be used to send any FTP command to the server. If the command requires one or more parameters, they can be specified in parameter. If the server returns information, you can extract it from the response using Response::getMessage().

        Parameters
        - command	Command to send
        - parameter	Command parameter

        Returns
        - Server response to the request
        """

class Http:
    """
    A HTTP client.

    sf::Http is a very simple HTTP client that allows you to communicate with a web server.

    You can retrieve web pages, send data to an interactive resource, download a remote file, etc. The HTTPS protocol is not supported.

    The HTTP client is split into 3 classes:

    - sf::Http::Request
    - sf::Http::Response
    - sf::Http

    sf::Http::Request builds the request that will be sent to the server. A request is made of:

    - a method (what you want to do)
    - a target URI (usually the name of the web page or file)
    - one or more header fields (options that you can pass to the server)
    - an optional body (for POST requests)

    sf::Http::Response parse the response from the web server and provides getters to read them. The response contains:

    - a status code
    - header fields (that may be answers to the ones that you requested)
    - a body, which contains the contents of the requested resource

    sf::Http provides a simple function, SendRequest, to send a sf::Http::Request and return the corresponding sf::Http::Response from the server.
    """

    class Request:
        """
        HTTP request.
        """

        class Method(enum.IntEnum):
            """
            Enumerate the available HTTP methods for a request.

            Enumerator
            - Get: Request in get mode, standard method to retrieve a page.
            - Post: Request in post mode, usually to send data to a page.
            - Head: Request a page's header only.
            - Put: Request in put mode, useful for a REST API.
            - Delete: Request in delete mode, useful for a REST API.
            """

            GET = 0
            POST = 1
            HEAD = 2
            PUT = 3
            DELETE = 4

        def __init__(self, uri: str = '/', method: Method = Method.GET, body: str = '') -> None:
            """
            Default constructor.

            This constructor creates a GET request, with the root URI ("/") and an empty body.

            Parameters
            - uri	Target URI
            - method	Method to use for the request
            - body	Content of the request's body
            """

        def set_field(self, field: str, value: str) -> None:
            """
            Set the value of a field.

            The field is created if it doesn't exist. The name of the field is case-insensitive. By default, a request doesn't contain any field (but the mandatory fields are added later by the HTTP client when sending the request).

            Parameters
            - field	Name of the field to set
            - value	Value of the field
            """

        def set_method(self, method: Method) -> None:
            """
            Set the request method.

            See the Method enumeration for a complete list of all the available methods. The method is Http::Request::Method::Get by default.

            Parameters
            - method	Method to use for the request
            """

        def set_uri(self, uri: str) -> None:
            """
            Set the requested URI.

            The URI is the resource (usually a web page or a file) that you want to get or post. The URI is "/" (the root page) by default.

            Parameters
            - uri	URI to request, relative to the host
            """

        def set_http_version(self, major: int, minor: int) -> None:
            """
            Set the HTTP version for the request.

            The HTTP version is 1.0 by default.

            Parameters
            - major	Major HTTP version number
            - minor	Minor HTTP version number
            """

        def set_body(self, body: str) -> None:
            """
            Set the body of the request.

            The body of a request is optional and only makes sense for POST requests. It is ignored for all other methods. The body is empty by default.

            Parameters
            - body	Content of the body
            """

    class Response:
        """
        HTTP response.
        """

        class Status:
            """
            Enumerate all the valid status codes for a response.

            Enumerator
            - Ok: Most common code returned when operation was successful.
            - Created: The resource has successfully been created.
            - Accepted: The request has been accepted, but will be processed later by the server.
            - NoContent: The server didn't send any data in return.
            - ResetContent: The server informs the client that it should clear the view (form) that caused the request to be sent.
            - PartialContent: The server has sent a part of the resource, as a response to a partial GET request.
            - MultipleChoices: The requested page can be accessed from several locations.
            - MovedPermanently: The requested page has permanently moved to a new location.
            - MovedTemporarily: The requested page has temporarily moved to a new location.
            - NotModified: For conditional requests, means the requested page hasn't changed and doesn't need to be refreshed.
            - BadRequest: The server couldn't understand the request (syntax error)
            - Unauthorized: The requested page needs an authentication to be accessed.
            - Forbidden: The requested page cannot be accessed at all, even with authentication.
            - NotFound: The requested page doesn't exist.
            - RangeNotSatisfiable: The server can't satisfy the partial GET request (with a "Range" header field)
            - InternalServerError: The server encountered an unexpected error.
            - NotImplemented: The server doesn't implement a requested feature.
            - BadGateway: The gateway server has received an error from the source server.
            - ServiceNotAvailable: The server is temporarily unavailable (overloaded, in maintenance, ...)
            - GatewayTimeout: The gateway server couldn't receive a response from the source server.
            - VersionNotSupported: The server doesn't support the requested HTTP version.
            - InvalidResponse: Response is not a valid HTTP one.
            - ConnectionFailed: Connection with server failed.
            """

            Ok = 200,
            Created = 201,
            Accepted = 202,
            NoContent = 204,
            ResetContent = 205,
            PartialContent = 206,

            MultipleChoices = 300,
            MovedPermanently = 301,
            MovedTemporarily = 302,
            NotModified = 304,

            BadRequest = 400,
            Unauthorized = 401,
            Forbidden = 403,
            NotFound = 404,
            RangeNotSatisfiable = 407,

            InternalServerError = 500,
            NotImplemented = 501,
            BadGateway = 502,
            ServiceNotAvailable = 503,
            GatewayTimeout = 504,
            VersionNotSupported = 505,

            InvalidResponse = 1000,
            ConnectionFailed = 1001

        def get_field(self, field: str) -> str:
            """
            Get the value of a field.

            If the field field is not found in the response header, the empty string is returned. This function uses case-insensitive comparisons.

            Parameters
            - field	Name of the field to get

            Returns
            - Value of the field, or empty string if not found
            """

        def get_status(self) -> Status:
            """
            Get the response status code.

            The status code should be the first thing to be checked after receiving a response, it defines whether it is a success, a failure or anything else (see the Status enumeration).

            Returns
            - Status code of the response
            """

        def get_major_http_version(self) -> int:
            """
            Get the major HTTP version number of the response.

            Returns
            - Major HTTP version number
            """

        def get_minor_http_version(self) -> int:
            """
            Get the minor HTTP version number of the response.

            Returns
            - Minor HTTP version number
            """

        def get_body(self) -> str:
            """
            Get the body of the response.

            The body of a response may contain:

            - the requested page (for GET requests)
            - a response from the server (for POST requests)
            - nothing (for HEAD requests)
            - an error message (in case of an error)

            Returns
            - The response body
            """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.
        """

    @overload
    def __init__(self, host: str, port: int = 0) -> None:
        """
        onstruct the HTTP client with the target host.

        This is equivalent to calling setHost(host, port). The port has a default value of 0, which means that the HTTP client will use the right port according to the protocol used (80 for HTTP). You should leave it like this unless you really need a port other than the standard one, or use an unknown protocol.

        Parameters
        - host	Web server to connect to
        - port	Port to use for connection
        """

    def set_host(self, host: str, port: int = 0) -> None:
        """
        Set the target host.

        This function just stores the host address and port, it doesn't actually connect to it until you send a request. The port has a default value of 0, which means that the HTTP client will use the right port according to the protocol used (80 for HTTP). You should leave it like this unless you really need a port other than the standard one, or use an unknown protocol.

        Parameters
        - host	Web server to connect to
        - port	Port to use for connection
        """

    def send_request(self, request: Request, timeout: sfSystem.Time = sfSystem.Time.Zero()) -> Response:
        """
        Send a HTTP request and return the server's response.

        You must have a valid host before sending a request (see setHost). Any missing mandatory header field in the request will be added with an appropriate value. Warning: this function waits for the server's response and may not return instantly; use a thread if you don't want to block your application, or use a timeout to limit the time to wait. A value of Time::Zero means that the client will use the system default timeout (which is usually pretty long).

        Parameters
        - request	Request to send
        - timeout	Maximum time to wait
        Returns
        - Server's response
        """

class Packet:
    """
    Utility class to build blocks of data to transfer over the network.

    Packets provide a safe and easy way to serialize data, in order to send it over the network using sockets (sf::TcpSocket, sf::UdpSocket).

    Packets solve 2 fundamental problems that arise when transferring data over the network:

    - data is interpreted correctly according to the endianness
    - the bounds of the packet are preserved (one send == one receive)

    The sf::Packet class provides both input and output modes. It is designed to follow the behavior of standard C++ streams, using operators >> and << to extract and insert data.

    It is recommended to use only fixed-size types (like std::int32_t, etc.), to avoid possible differences between the sender and the receiver. Indeed, the native C++ types may have different sizes on two platforms and your data may be corrupted if that happens.
    """

    def append(self, data: bytes, sizeInBytes: int) -> None:
        """
        Append data to the end of the packet.

        Parameters
        - data	Pointer to the sequence of bytes to append
        - sizeInBytes	Number of bytes to append
        """

    def get_read_position(self) -> int:
        """
        Get the current reading position in the packet.

        The next read operation will read data from this position

        Returns
        - The byte offset of the current read position
        """

    def clear(self) -> None:
        """
        Clear the packet.

        After calling Clear, the packet is empty.
        """

    def get_data(self) -> bytes:
        """
        Get a pointer to the data contained in the packet.

        Warning: the returned pointer may become invalid after you append data to the packet, therefore it should never be stored. The return pointer is a nullptr if the packet is empty.

        Returns
        - Pointer to the data
        """

    def get_data_size(self) -> int:
        """
        Get the size of the data contained in the packet.

        This function returns the number of bytes pointed to by what getData returns.

        Returns
        - Data size, in bytes
        """

    def end_of_packet(self) -> bool:
        """
        Tell if the reading position has reached the end of the packet.

        This function is useful to know if there is some data left to be read, without actually reading it.

        Returns
        - true if all data was read, false otherwise
        """

class Socket:
    """
    Base class for all the socket types.

    This class mainly defines internal stuff to be used by derived classes.

    The only public features that it defines, and which is therefore common to all the socket classes, is the blocking state. All sockets can be set as blocking or non-blocking.

    In blocking mode, socket functions will hang until the operation completes, which means that the entire program (well, in fact the current thread if you use multiple ones) will be stuck waiting for your socket operation to complete.

    In non-blocking mode, all the socket functions will return immediately. If the socket is not ready to complete the requested operation, the function simply returns the proper status code (Socket::Status::NotReady).

    The default mode, which is blocking, is the one that is generally used, in combination with threads or selectors. The non-blocking mode is rather used in real-time applications that run an endless loop that can poll the socket often enough, and cannot afford blocking this loop.
    """

    class Status:
        """
        Status codes that may be returned by socket functions.

        Enumerator
        - Done: The socket has sent / received the data.
        - NotReady: The socket is not ready to send / receive data yet.
        - Partial: The socket sent a part of the data.
        - Disconnected: The TCP socket has been disconnected.
        - Error: An unexpected error happened.
        """

        Done = 0
        NotReady = 1
        Partial = 2
        Disconnected = 3
        Error = 4

    def set_blocking(self, blocking: bool) -> None:
        """
        Set the blocking state of the socket.

        In blocking mode, calls will not return until they have completed their task. For example, a call to Receive in blocking mode won't return until some data was actually received. In non-blocking mode, calls will always return immediately, using the return code to signal whether there was data available or not. By default, all sockets are blocking.

        Parameters
        - blocking	true to set the socket as blocking, false for non-blocking
        """

    def is_blocking(self) -> bool:
        """
        Tell whether the socket is in blocking or non-blocking mode.

        Returns
        - true if the socket is blocking, false otherwise
        """

class SocketHandle:
    """
    Internal class that holds the handle of a socket.

    This class is used internally by the socket classes to store their handles. It is not meant to be used directly.
    """
    def get_value(self) -> int:
        """
        Get the internal handle of the socket."

        Returns
        - Internal handle of the socket
        """

class SocketSelector:
    """
    Multiplexer that allows to read from multiple sockets.

    Socket selectors provide a way to wait until some data is available on a set of sockets, instead of just one.

    This is convenient when you have multiple sockets that may possibly receive data, but you don't know which one will be ready first. In particular, it avoids to use a thread for each socket; with selectors, a single thread can handle all the sockets.

    All types of sockets can be used in a selector:

    - sf::TcpListener
    - sf::TcpSocket
    - sf::UdpSocket

    A selector doesn't store its own copies of the sockets (socket classes are not copyable anyway), it simply keeps a reference to the original sockets that you pass to the "add" function. Therefore, you can't use the selector as a socket container, you must store them outside and make sure that they are alive as long as they are used in the selector.

    Using a selector is simple:

    - populate the selector with all the sockets that you want to observe
    - make it wait until there is data available on any of the sockets
    - test each socket to find out which ones are ready
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.
        """

    def add(self, socket: Socket) -> None:
        """
        Add a new socket to the selector.

        This function keeps a weak reference to the socket, so you have to make sure that the socket is not destroyed while it is stored in the selector. This function does nothing if the socket is not valid.

        Parameters
        - socket	Reference to the socket to add
        """

    def remove(self, socket: Socket) -> None:
        """
        Remove a socket from the selector.

        This function doesn't destroy the socket, it simply removes the reference that the selector has to it.

        Parameters
        -socket	Reference to the socket to remove
        """

    def clear(self) -> None:
        """
        Remove all the sockets stored in the selector.

        This function doesn't destroy any instance, it simply removes all the references that the selector has to external sockets.
        """

    def wait(self, timeout: sfSystem.Time = sfSystem.Time.Zero()) -> bool:
        """
        Wait until one or more sockets are ready to receive.

        This function returns as soon as at least one socket has some data available to be received. To know which sockets are ready, use the isReady function. If you use a timeout and no socket is ready before the timeout is over, the function returns false.

        Parameters
        - timeout	Maximum time to wait, (use Time::Zero for infinity)

        Returns
        - true if there are sockets ready, false otherwise
        """

    def is_ready(self, socket: Socket) -> bool:
        """
        Test a socket to know if it is ready to receive data.

        This function must be used after a call to Wait, to know which sockets are ready to receive data. If a socket is ready, a call to receive will never block because we know that there is data available to read. Note that if this function returns true for a TcpListener, this means that it is ready to accept a new connection.

        Parameters
        - socket	Socket to test

        Returns
        - true if the socket is ready to read, false otherwise
        """


class TcpListener(Socket):
    """
    Socket that listens to new TCP connections.

    A listener socket is a special type of socket that listens to a given port and waits for connections on that port.

    This is all it can do.

    When a new connection is received, you must call accept and the listener returns a new instance of sf::TcpSocket that is properly initialized and can be used to communicate with the new client.

    Listener sockets are specific to the TCP protocol, UDP sockets are connectionless and can therefore communicate directly. As a consequence, a listener socket will always return the new connections as sf::TcpSocket instances.

    A listener is automatically closed on destruction, like all other types of socket. However if you want to stop listening before the socket is destroyed, you can call its close() function.
    """

    def __init__(self) -> None:
        """
        Default constructor.
        """

    def get_local_port(self) -> int:
        """
        Get the port to which the socket is bound locally.

        If the socket is not listening to a port, this function returns 0.

        Returns
        - Port to which the socket is bound
        """

    def listen(self, port: int, address: IpAddress = IpAddress.Any()) -> Socket.Status:
        """
        Start listening for incoming connection attempts.

        This function makes the socket start listening on the specified port, waiting for incoming connection attempts.

        If the socket is already listening on a port when this function is called, it will stop listening on the old port before starting to listen on the new port.

        When providing sf::Socket::AnyPort as port, the listener will request an available port from the system. The chosen port can be retrieved by calling getLocalPort().

        Parameters
        - port	Port to listen on for incoming connection attempts
        - address	Address of the interface to listen on

        Returns
        - Status code
        """

    def close(self) -> None:
        """
        Stop listening and close the socket.

        This function gracefully stops the listener. If the socket is not listening, this function has no effect.
        """

    def accept(self, socket: TcpSocket) -> Socket.Status:
        """
        Accept a new connection.

        If the socket is in blocking mode, this function will not return until a connection is actually received.

        Parameters
        - socket	Socket that will hold the new connection

        Returns
        - Status code
        """


class TcpSocket(Socket):
    """
    Specialized socket using the TCP protocol.

    TCP is a connected protocol, which means that a TCP socket can only communicate with the host it is connected to.

    It can't send or receive anything if it is not connected.

    The TCP protocol is reliable but adds a slight overhead. It ensures that your data will always be received in order and without errors (no data corrupted, lost or duplicated).

    When a socket is connected to a remote host, you can retrieve information about this host with the getRemoteAddress and getRemotePort functions. You can also get the local port to which the socket is bound (which is automatically chosen when the socket is connected), with the getLocalPort function.

    Sending and receiving data can use either the low-level or the high-level functions. The low-level functions process a raw sequence of bytes, and cannot ensure that one call to Send will exactly match one call to Receive at the other end of the socket.

    The high-level interface uses packets (see sf::Packet), which are easier to use and provide more safety regarding the data that is exchanged. You can look at the sf::Packet class to get more details about how they work.

    The socket is automatically disconnected when it is destroyed, but if you want to explicitly close the connection while the socket instance is still alive, you can call disconnect.
    """

    def __init__(self) -> None:
        """
        Default constructor.
        """

    def get_local_port(self) -> int:
        """
        Get the port to which the socket is bound locally.

        If the socket is not connected, this function returns 0.

        Returns
        - Port to which the socket is bound
        """

    def get_remote_address(self) -> IpAddress | None:
        """
        Get the address of the connected peer.

        If the socket is not connected, this function returns an unset optional.

        Returns
        - Address of the remote peer
        """

    def get_remote_port(self) -> int:
        """
        Get the port of the connected peer to which the socket is connected.

        If the socket is not connected, this function returns 0.

        Returns
        - Remote port to which the socket is connected
        """

    def connect(self, remoteAddress: IpAddress, remotePort: int, timeout: sfSystem.Time = sfSystem.Time.Zero()) -> Socket.Status:
        """
        Connect the socket to a remote peer.

        In blocking mode, this function may take a while, especially if the remote peer is not reachable. The last parameter allows you to stop trying to connect after a given timeout. If the socket is already connected, the connection is forcibly disconnected before attempting to connect again.

        Parameters
        - remoteAddress	Address of the remote peer
        - remotePort	Port of the remote peer
        - timeout	Optional maximum time to wait

        Returns
        - Status code
        """

    def disconnect(self) -> None:
        """
        Disconnect the socket from its remote peer.

        This function gracefully closes the connection. If the socket is not connected, this function has no effect.
        """

    @overload
    def send(self, data: bytes, size: int) -> Socket.Status:
        """
        Send raw data to the remote peer.

        To be able to handle partial sends over non-blocking sockets, use the send(const void*, std::size_t, std::size_t&) overload instead. This function will fail if the socket is not connected.

        Parameters
        - data	Pointer to the sequence of bytes to send
        - size	Number of bytes to send

        Returns
        - Status code
        """

    @overload
    def send(self, data: bytes, size: int, sent: int) -> Socket.Status:
        """
        Send raw data to the remote peer.

        This function will fail if the socket is not connected.

        Parameters
        - data	Pointer to the sequence of bytes to send
        - size	Number of bytes to send
        - sent	The number of bytes sent will be written here

        Returns
        - Status code
        """

    @overload
    def send(self, packet: Packet) -> Socket.Status:
        """
        Send a formatted packet of data to the remote peer.

        In non-blocking mode, if this function returns sf::Socket::Status::Partial, you must retry sending the same unmodified packet before sending anything else in order to guarantee the packet arrives at the remote peer uncorrupted. This function will fail if the socket is not connected.

        Parameters
        - packet	Packet to send

        Returns
        - Status code
        """

    @overload
    def receive(self, data: bytes, size: int, received: int) -> Socket.Status:
        """
        Receive raw data from the remote peer.

        In blocking mode, this function will wait until some bytes are actually received. This function will fail if the socket is not connected.

        Parameters
        - data	Pointer to the array to fill with the received bytes
        - size	Maximum number of bytes that can be received
        - received	This variable is filled with the actual number of bytes received

        Returns
        - Status code
        """

    @overload
    def receive(self, packet: Packet) -> Socket.Status:
        """
        Receive a formatted packet of data from the remote peer.

        In blocking mode, this function will wait until the whole packet has been received. This function will fail if the socket is not connected.

        Parameters
        - packet	Packet to fill with the received data

        Returns
        - Status code
        """


class UdpSocket(Socket):
    """
    Specialized socket using the UDP protocol.

    A UDP socket is a connectionless socket.

    Instead of connecting once to a remote host, like TCP sockets, it can send to and receive from any host at any time.

    It is a datagram protocol: bounded blocks of data (datagrams) are transferred over the network rather than a continuous stream of data (TCP). Therefore, one call to send will always match one call to receive (if the datagram is not lost), with the same data that was sent.

    The UDP protocol is lightweight but unreliable. Unreliable means that datagrams may be duplicated, be lost or arrive reordered. However, if a datagram arrives, its data is guaranteed to be valid.

    UDP is generally used for real-time communication (audio or video streaming, real-time games, etc.) where speed is crucial and lost data doesn't matter much.

    Sending and receiving data can use either the low-level or the high-level functions. The low-level functions process a raw sequence of bytes, whereas the high-level interface uses packets (see sf::Packet), which are easier to use and provide more safety regarding the data that is exchanged. You can look at the sf::Packet class to get more details about how they work.

    It is important to note that UdpSocket is unable to send datagrams bigger than MaxDatagramSize. In this case, it returns an error and doesn't send anything. This applies to both raw data and packets. Indeed, even packets are unable to split and recompose data, due to the unreliability of the protocol (dropped, mixed or duplicated datagrams may lead to a big mess when trying to recompose a packet).

    If the socket is bound to a port, it is automatically unbound from it when the socket is destroyed. However, you can unbind the socket explicitly with the Unbind function if necessary, to stop receiving messages or make the port available for other sockets.
    """

    def __init__(self) -> None:
        """
        Default constructor.
        """

    def getLocalPort(self) -> int:
        """
        Get the port to which the socket is bound locally.

        If the socket is not bound to a port, this function returns 0.

        Returns
        - Port to which the socket is bound
        """

    def bind(self, port: int, address: IpAddress = IpAddress.Any()) -> Socket.Status:
        """
        Bind the socket to a specific port.

        Binding the socket to a port is necessary for being able to receive data on that port.

        When providing sf::Socket::AnyPort as port, the listener will request an available port from the system. The chosen port can be retrieved by calling getLocalPort().

        Since the socket can only be bound to a single port at any given moment, if it is already bound when this function is called, it will be unbound from the previous port before being bound to the new one.

        Parameters
        - port	Port to bind the socket to
        - address	Address of the interface to bind to

        Returns
        - Status code
        """

    def unbind(self) -> None:
        """
        Unbind the socket from the local port to which it is bound.

        The port that the socket was previously bound to is immediately made available to the operating system after this function is called. This means that a subsequent call to bind() will be able to re-bind the port if no other process has done so in the mean time. If the socket is not bound to a port, this function has no effect.
        """

    @overload
    def send(self, data: bytes, size: int, remoteAddress: IpAddress, remotePort: int) -> Socket.Status:
        """
        Send raw data to a remote peer.

        Make sure that size is not greater than UdpSocket::MaxDatagramSize, otherwise this function will fail and no data will be sent.

        Parameters
        - data	Pointer to the sequence of bytes to send
        - size	Number of bytes to send
        - remoteAddress	Address of the receiver
        - remotePort	Port of the receiver to send the data to

        Returns
        - Status code
        """

    @overload
    def send(self, packet: Packet, remoteAddress: IpAddress, remotePort: int) -> Socket.Status:
        """
        Send a formatted packet of data to a remote peer.

        Make sure that the packet size is not greater than UdpSocket::MaxDatagramSize, otherwise this function will fail and no data will be sent.

        Parameters
        - packet	Packet to send
        - remoteAddress	Address of the receiver
        - remotePort	Port of the receiver to send the data to

        Returns
        - Status code
        """

    @overload
    def receive(
        self, data: bytearray, size: int, received: int, remoteAddress: Optional[IpAddress], remotePort: int ) -> Socket.Status:
        """
        Receive a formatted packet of data from a remote peer.

        In blocking mode, this function will wait until the whole packet has been received.

        Parameters
        - packet	Packet to fill with the received data
        - remoteAddress	Address of the peer that sent the data
        - remotePort	Port of the peer that sent the data

        Returns
        - Status code
        """

    @overload
    def receive(self, packet: Packet, remoteAddress: Optional[IpAddress], remotePort: int ) -> Socket.Status:
        """
        Receive raw data from a remote peer.

        In blocking mode, this function will wait until some bytes are actually received. Be careful to use a buffer which is large enough for the data that you intend to receive, if it is too small then an error will be returned and all the data will be lost.

        Parameters
        - data	Pointer to the array to fill with the received bytes
        - size	Maximum number of bytes that can be received
        - received	This variable is filled with the actual number of bytes received
        - remoteAddress	Address of the peer that sent the data
        - remotePort	Port of the peer that sent the data
        Returns
        - Status code
        """
