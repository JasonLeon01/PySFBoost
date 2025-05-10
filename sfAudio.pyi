"""
Sounds, streaming (musics or custom sources), recording, spatialization.
"""

# pylint: disable=unused-argument
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=invalid-name

from __future__ import annotations
import enum
from typing import Callable, List, Tuple, overload
from types import ModuleType
from . import sfSystem

class SoundChannel(enum.IntEnum):
    """
    Types of sound channels that can be read/written from sound buffers/files.

    In multi-channel audio, each sound channel can be assigned a position. The position of the channel is used to determine where to place a sound when it is spatialized. Assigning an incorrect sound channel will result in multi-channel audio being positioned incorrectly when using spatialization.
    """

    Unspecified = 0
    Mono = 1
    FrontLeft = 2
    FrontRight = 3
    FrontCenter = 4
    FrontLeftOfCenter = 5
    FrontRightOfCenter = 6
    LowFrequencyEffects = 7
    BackLeft = 8
    BackRight = 9
    BackCenter = 10
    SideLeft = 11
    SideRight = 12
    TopCenter = 13
    TopFrontLeft = 14
    TopFrontRight = 15
    TopFrontCenter = 16
    TopBackLeft = 17
    TopBackRight = 18
    TopBackCenter = 19


class Listener(ModuleType):
    """
    The audio listener is the point in the scene from where all the sounds are heard.

    The audio listener defines the global properties of the audio environment, it defines where and how sounds and musics are heard.

    If sf::View is the eyes of the user, then sf::Listener are their ears (by the way, they are often linked together – same position, orientation, etc.).

    sf::Listener is a simple interface, which allows to setup the listener in the 3D audio environment (position, direction and up vector), and to adjust the global volume.
    """

    class Cone:
        """
        Structure defining the properties of a directional cone.

        Sounds will play at gain 1 when they are positioned within the inner angle of the cone. Sounds will play at outerGain when they are positioned outside the outer angle of the cone. The gain declines linearly from 1 to outerGain as the sound moves from the inner angle to the outer angle.
        """

        def __init__(self) -> None:
            """
            Initialize the attributes to their default values.
            """

        inner_angle: sfSystem.Angle
        outer_angle: sfSystem.Angle
        outer_gain: float

    @staticmethod
    def set_global_volume(volume: float) -> None:
        """
        Change the global volume of all the sounds and musics.

        volume is a number between 0 and 100; it is combined with the individual volume of each sound / music. The default value for the volume is 100 (maximum).

        Parameters
        - volume	New global volume, in the range [0, 100]
        """

    @staticmethod
    def get_global_volume() -> float:
        """
        Get the current value of the global volume.

        Returns
        - Current global volume, in the range [0, 100]
        """

    @staticmethod
    def set_position(position: sfSystem.Vector3f) -> None:
        """
        Set the position of the listener in the scene.

        The default listener's position is (0, 0, 0).

        Parameters
        - position	New listener's position

        """

    @staticmethod
    def get_position() -> sfSystem.Vector3f:
        """
        Get the current position of the listener in the scene.

        Returns
        - Listener's position
        """

    @staticmethod
    def set_direction(direction: sfSystem.Vector3f) -> None:
        """
        Set the forward vector of the listener in the scene.

        The direction (also called "at vector") is the vector pointing forward from the listener's perspective. Together with the up vector, it defines the 3D orientation of the listener in the scene. The direction vector doesn't have to be normalized. The default listener's direction is (0, 0, -1).

        Parameters
        - direction	New listener's direction

        """

    @staticmethod
    def get_direction() -> sfSystem.Vector3f:
        """
        Get the current forward vector of the listener in the scene.

        Returns
        - Listener's forward vector (not normalized)
        """

    @staticmethod
    def set_velocity(velocity: sfSystem.Vector3f) -> None:
        """
        Set the velocity of the listener in the scene.

        The default listener's velocity is (0, 0, -1).

        Parameters
        - velocity	New listener's velocity

        """

    @staticmethod
    def get_velocity() -> sfSystem.Vector3f:
        """
        Get the current forward vector of the listener in the scene.

        Returns
        - Listener's velocity
        """

    @staticmethod
    def set_cone(cone: Cone) -> None:
        """
        Set the cone properties of the listener in the audio scene.

        The cone defines how directional attenuation is applied. The default cone of a sound is (2 * PI, 2 * PI, 1).

        Parameters
        - cone	Cone properties of the listener in the scene
        """

    @staticmethod
    def get_cone() -> Cone:
        """
        Get the cone properties of the listener in the audio scene.

        Returns
        - Cone properties of the listener
        """

    @staticmethod
    def set_up_vector(upVector: sfSystem.Vector3f) -> None:
        """
        Set the upward vector of the listener in the scene.

        The up vector is the vector that points upward from the listener's perspective. Together with the direction, it defines the 3D orientation of the listener in the scene. The up vector doesn't have to be normalized. The default listener's up vector is (0, 1, 0). It is usually not necessary to change it, especially in 2D scenarios.

        Parameters
        - upVector	New listener's up vector
        """

    @staticmethod
    def get_up_vector() -> sfSystem.Vector3f:
        """
        Get the current upward vector of the listener in the scene.

        Returns
        - Listener's upward vector (not normalized)
        """


class SoundSource:
    """
    Base class defining a sound's properties.

    sf::SoundSource is not meant to be used directly, it only serves as a common base for all audio objects that can live in the audio environment.

    It defines several properties for the sound: pitch, volume, position, attenuation, etc. All of them can be changed at any time with no impact on performances.
    """

    class Status(enum.IntEnum):
        """
        Enumeration of the sound source states.

        Enumerato
        - Stopped: Sound is not playing.
        - Paused: Sound is paused.
        - Playing: Sound is playing.
        """

        Stopped = 0
        Paused = 1
        Playing = 2

    class Cone:
        """
        Structure defining the properties of a directional cone.

        Sounds will play at gain 1 when the listener is positioned within the inner angle of the cone. Sounds will play at outerGain when the listener is positioned outside the outer angle of the cone. The gain declines linearly from 1 to outerGain as the listener moves from the inner angle to the outer angle.
        """
        def __init__(self) -> None:
            """
            Initialize the attributes to their default values.
            """

        inner_angle: sfSystem.Angle
        outer_angle: sfSystem.Angle
        outer_gain: float

    def set_pitch(self, pitch: float) -> None:
        """
        Set the pitch of the sound.

        The pitch represents the perceived fundamental frequency of a sound; thus you can make a sound more acute or grave by changing its pitch. A side effect of changing the pitch is to modify the playing speed of the sound as well. The default value for the pitch is 1.

        Parameters
        - pitch	New pitch to apply to the sound
        """

    def set_pan(self, pan: float) -> None:
        """
        Set the pan of the sound.

        Using panning, a mono sound can be panned between stereo channels. When the pan is set to -1, the sound is played only on the left channel, when the pan is set to +1, the sound is played only on the right channel.

        Parameters
        - pan	New pan to apply to the sound [-1, +1]
        """

    def set_volume(self, volume: float) -> None:
        """
        Set the volume of the sound.

        The volume is a value between 0 (mute) and 100 (full volume). The default value for the volume is 100.

        Parameters
        - volume	Volume of the sound
        """

    def set_spatialization_enabled(self, enabled: bool) -> None:
        """
        Set whether spatialization of the sound is enabled.

        Spatialization is the application of various effects to simulate a sound being emitted at a virtual position in 3D space and exhibiting various physical phenomena such as directional attenuation and doppler shift.

        Parameters
        - enabled	true to enable spatialization, false to disable
        """

    def set_position(self, position: sfSystem.Vector3f) -> None:
        """
        Set the 3D position of the sound in the audio scene.

        Only sounds with one channel (mono sounds) can be spatialized. The default position of a sound is (0, 0, 0).

        Parameters
        - position	Position of the sound in the scene
        """

    def set_direction(self, direction: sfSystem.Vector3f) -> None:
        """
        Set the 3D direction of the sound in the audio scene.

        The direction defines where the sound source is facing in 3D space. It will affect how the sound is attenuated if facing away from the listener. The default direction of a sound is (0, 0, -1).

        Parameters
        - direction	Direction of the sound in the scene
        """

    def set_cone(self, cone: Cone) -> None:
        """
        Set the cone properties of the sound in the audio scene.

        The cone defines how directional attenuation is applied. The default cone of a sound is (2 * PI, 2 * PI, 1).

        Parameters
        - cone	Cone properties of the sound in the scene
        """

    def set_velocity(self, velocity: sfSystem.Vector3f) -> None:
        """
        Set the 3D velocity of the sound in the audio scene.

        The velocity is used to determine how to doppler shift the sound. Sounds moving towards the listener will be perceived to have a higher pitch and sounds moving away from the listener will be perceived to have a lower pitch.

        Parameters
        - velocity	Velocity of the sound in the scene
        """

    def set_doppler_factor(self, factor: float) -> None:
        """
        Set the doppler factor of the sound.

        The doppler factor determines how strong the doppler shift will be.

        Parameters
        - factor	New doppler factor to apply to the sound
        """

    def set_directional_attenuation_factor(self, factor: float) -> None:
        """
        Set the directional attenuation factor of the sound.

        Depending on the virtual position of an output channel relative to the listener (such as in surround sound setups), sounds will be attenuated when emitting them from certain channels. This factor determines how strong the attenuation based on output channel position relative to the listener is.

        Parameters
        - factor	New directional attenuation factor to apply to the sound
        """

    def set_relative_to_listener(self, relative: bool) -> None:
        """
        Make the sound's position relative to the listener or absolute.

        Making a sound relative to the listener will ensure that it will always be played the same way regardless of the position of the listener. This can be useful for non-spatialized sounds, sounds that are produced by the listener, or sounds attached to it. The default value is false (position is absolute).

        Parameters
        - relative	true to set the position relative, false to set it absolute
        """

    def set_min_distance(self, distance: float) -> None:
        """
        Set the minimum distance of the sound.

        The "minimum distance" of a sound is the maximum distance at which it is heard at its maximum volume. Further than the minimum distance, it will start to fade out according to its attenuation factor. A value of 0 ("inside the head of the listener") is an invalid value and is forbidden. The default value of the minimum distance is 1.

        Parameters
        - distance	New minimum distance of the sound
        """

    def set_max_distance(self, distance: float) -> None:
        """
        Set the maximum distance of the sound.

        The "maximum distance" of a sound is the minimum distance at which it is heard at its minimum volume. Closer than the maximum distance, it will start to fade in according to its attenuation factor. The default value of the maximum distance is the maximum value a float can represent.

        Parameters
        - distance	New maximum distance of the sound
        """

    def set_min_gain(self, gain: float) -> None:
        """
        Set the minimum gain of the sound.

        When the sound is further away from the listener than the "maximum distance" the attenuated gain is clamped so it cannot go below the minimum gain value.

        Parameters
        - gain	New minimum gain of the sound
        """

    def set_max_gain(self, gain: float) -> None:
        """
        Set the maximum gain of the sound.

        When the sound is closer from the listener than the "minimum distance" the attenuated gain is clamped so it cannot go above the maximum gain value.

        Parameters
        - gain	New maximum gain of the sound
        """

    def set_attenuation(self, attenuation: float) -> None:
        """
        Set the attenuation factor of the sound.

        The attenuation is a multiplicative factor which makes the sound more or less loud according to its distance from the listener. An attenuation of 0 will produce a non-attenuated sound, i.e. its volume will always be the same whether it is heard from near or from far. On the other hand, an attenuation value such as 100 will make the sound fade out very quickly as it gets further from the listener. The default value of the attenuation is 1.

        Parameters
        - attenuation	New attenuation factor of the sound
        """

    def set_effect_processor(self, effectProcessor: Callable[[memoryview, int, memoryview, int, int], None]) -> None:
        """
        Set the effect processor to be applied to the sound.

        The effect processor is a callable that will be called with sound data to be processed.

        Parameters
        - effectProcessor	The effect processor to attach to this sound, attach an empty processor to disable processing
        """

    def get_pitch(self) -> float:
        """
        Get the pitch of the sound.

        Returns
        - Pitch of the sound
        """

    def get_pan(self) -> float:
        """
        Get the pan of the sound.

        Returns
        - Pan of the sound
        """

    def get_volume(self) -> float:
        """
        Get the volume of the sound.

        Returns
        - Volume of the sound, in the range [0, 100]
        """

    def is_spatialization_enabled(self) -> bool:
        """
        Tell whether spatialization of the sound is enabled.

        Returns
        - true if spatialization is enabled, false if it's disabled
        """

    def get_position(self) -> sfSystem.Vector3f:
        """
        Get the 3D position of the sound in the audio scene.

        Returns
        - Position of the sound
        """

    def get_direction(self) -> sfSystem.Vector3f:
        """
        Get the 3D direction of the sound in the audio scene.

        Returns
        - Direction of the sound
        """

    def get_cone(self) -> Cone:
        """
        Get the cone properties of the sound in the audio scene.

        Returns
        - Cone properties of the sound
        """

    def get_velocity(self) -> sfSystem.Vector3f:
        """
        Get the 3D velocity of the sound in the audio scene.

        - Returns
        Velocity of the sound
        """

    def get_doppler_factor(self) -> float:
        """
        Get the doppler factor of the sound.

        Returns
        - Doppler factor of the sound
        """

    def get_directional_attenuation_factor(self) -> float:
        """
        Get the directional attenuation factor of the sound.

        Returns
        - Directional attenuation factor of the sound
        """

    def is_relative_to_listener(self) -> bool:
        """
        Tell whether the sound's position is relative to the listener or is absolute.

        Returns
        - true if the position is relative, false if it's absolute
        """

    def get_min_distance(self) -> float:
        """
        Get the minimum distance of the sound.

        Returns
        - Minimum distance of the sound
        """

    def get_max_distance(self) -> float:
        """
        Get the maximum distance of the sound.

        Returns
        - Maximum distance of the sound
        """

    def get_min_gain(self) -> float:
        """
        Get the minimum gain of the sound.

        Returns
        - Minimum gain of the sound
        """

    def get_max_gain(self) -> float:
        """
        Get the maximum gain of the sound source.
        """

    def get_attenuation(self) -> float:
        """
        Get the attenuation factor of the sound.

        Returns
        - Attenuation factor of the sound
        """

    def get_status(self) -> Status:
        """
        Get the current status of the sound (stopped, paused, playing)

        Returns
        - Current status of the sound
        """

    def play(self) -> None:
        """
        Start or resume playing the sound source.

        This function starts the source if it was stopped, resumes it if it was paused, and restarts it from the beginning if it was already playing.
        """

    def pause(self) -> None:
        """
        Pause the sound source.

        This function pauses the source if it was playing, otherwise (source already paused or stopped) it has no effect.
        """

    def stop(self) -> None:
        """
        Stop playing the sound source.

        This function stops the source if it was playing or paused, and does nothing if it was already stopped. It also resets the playing position (unlike pause()).
        """

class SoundStream(SoundSource):
    """
    Abstract base class for streamed audio sources.

    Unlike audio buffers (see sf::SoundBuffer), audio streams are never completely loaded in memory.

    Instead, the audio data is acquired continuously while the stream is playing. This behavior allows to play a sound with no loading delay, and keeps the memory consumption very low.

    Sound sources that need to be streamed are usually big files (compressed audio musics that would eat hundreds of MB in memory) or files that would take a lot of time to be received (sounds played over the network).

    sf::SoundStream is a base class that doesn't care about the stream source, which is left to the derived class. SFML provides a built-in specialization for big files (see sf::Music). No network stream source is provided, but you can write your own by combining this class with the network module.

    A derived class has to override two virtual functions:

    - onGetData fills a new chunk of audio data to be played
    - onSeek changes the current playing position in the source

    It is important to note that each SoundStream is played in its own separate thread, so that the streaming loop doesn't block the rest of the program. In particular, the onGetData and onSeek virtual functions may sometimes be called from this separate thread. It is important to keep this in mind, because you may have to take care of synchronization issues if you share data between threads.
    """

    def play(self) -> None:
        """
        Start or resume playing the audio stream.

        This function starts the stream if it was stopped, resumes it if it was paused, and restarts it from the beginning if it was already playing. This function uses its own thread so that it doesn't block the rest of the program while the stream is played.

        Implements sf::SoundSource.
        """

    def pause(self) -> None:
        """
        Pause the audio stream.

        This function pauses the stream if it was playing, otherwise (stream already paused or stopped) it has no effect.

        Implements sf::SoundSource.
        """

    def stop(self) -> None:
        """
        Stop playing the audio stream.

        This function stops the stream if it was playing or paused, and does nothing if it was already stopped. It also resets the playing position (unlike pause()).

        Implements sf::SoundSource.
        """

    def get_channel_count(self) -> int:
        """
        Return the number of channels of the stream.

        1 channel means a mono sound, 2 means stereo, etc.

        Returns
        - Number of channels
        """

    def get_sample_rate(self) -> int:
        """
        Get the stream sample rate of the stream.

        The sample rate is the number of audio samples played per second. The higher, the better the quality.

        Returns
        - Sample rate, in number of samples per second
        """

    def get_channel_map(self) -> List[SoundChannel]:
        """
        Get the map of position in sample frame to sound channel.

        This is used to map a sample in the sample stream to a position during spatialization.

        Returns
        - Map of position in sample frame to sound channel
        """

    def get_status(self) -> SoundSource.Status:
        """
        Get the current status of the stream (stopped, paused, playing)

        Returns
        - Current status

        Implements sf::SoundSource.
        """

    def set_playing_offset(self, timeOffset: sfSystem.Time) -> None:
        """
        Change the current playing position of the stream.

        The playing position can be changed when the stream is either paused or playing. Changing the playing position when the stream is stopped has no effect, since playing the stream would reset its position.

        Parameters
        timeOffset	New playing position, from the beginning of the stream
        """

    def get_playing_offset(self) -> sfSystem.Time:
        """
        Get the current playing position of the stream.

        Returns
        - Current playing position, from the beginning of the stream
        """

    def set_looping(self, loop: bool) -> None:
        """
        Set whether or not the stream should loop after reaching the end.

        If set, the stream will restart from beginning after reaching the end and so on, until it is stopped or setLooping(false) is called. The default looping state for streams is false.

        Parameters
        - loop	true to play in loop, false to play once
        """

    def is_looping(self) -> bool:
        """
        Tell whether or not the stream is in loop mode.

        Returns
        - true if the stream is looping, false otherwise
        """

    def set_effect_processor(self, effectProcessor: Callable[[memoryview, int, memoryview, int, int], None]) -> None:
        """
        Set the effect processor to be applied to the sound.

        The effect processor is a callable that will be called with sound data to be processed.

        Parameters
        - effectProcessor	The effect processor to attach to this sound, attach an empty processor to disable processing

        Reimplemented from sf::SoundSource.
        """

class SoundBuffer:
    """
    Storage for audio samples defining a sound.

    A sound buffer holds the data of a sound, which is an array of audio samples.

    A sample is a 16 bit signed integer that defines the amplitude of the sound at a given time. The sound is then reconstituted by playing these samples at a high rate (for example, 44100 samples per second is the standard rate used for playing CDs). In short, audio samples are like texture pixels, and a sf::SoundBuffer is similar to a sf::Texture.

    A sound buffer can be loaded from a file, from memory, from a custom stream (see sf::InputStream) or directly from an array of samples. It can also be saved back to a file.

    Sound buffers alone are not very useful: they hold the audio data but cannot be played. To do so, you need to use the sf::Sound class, which provides functions to play/pause/stop the sound as well as changing the way it is outputted (volume, pitch, 3D position, ...). This separation allows more flexibility and better performances: indeed a sf::SoundBuffer is a heavy resource, and any operation on it is slow (often too slow for real-time applications). On the other side, a sf::Sound is a lightweight object, which can use the audio data of a sound buffer and change the way it is played without actually modifying that data. Note that it is also possible to bind several sf::Sound instances to the same sf::SoundBuffer.

    It is important to note that the sf::Sound instance doesn't copy the buffer that it uses, it only keeps a reference to it. Thus, a sf::SoundBuffer must not be destructed while it is used by a sf::Sound (i.e. never write a function that uses a local sf::SoundBuffer instance for loading a sound).

    When loading sound samples from an array, a channel map needs to be provided, which specifies the mapping of the position in the sample frame to the sound channel. For example when you have six samples in a frame and a 5.1 sound system, the channel map defines how each of those samples map to which speaker channel.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Construct an empty sound buffer that does not contain any samples.
        """

    @overload
    def __init__(self, filename: str) -> None:
        """
        Construct the sound buffer from a file.

        See the documentation of sf::InputSoundFile for the list of supported formats.

        Parameters
        - filename	Path of the sound file to load

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, data: bytes) -> None:
        """
        Construct the sound buffer from a file in memory.

        See the documentation of sf::InputSoundFile for the list of supported formats.

        Parameters
        - data	Pointer to the file data in memory

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, stream: sfSystem.InputStream) -> None:
        """
        Construct the sound buffer from a custom stream.

        See the documentation of sf::InputSoundFile for the list of supported formats.

        Parameters
        - stream	Source stream to read from

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, samples: List[List[float]], sampleRate: int, channelMap: List[SoundChannel]) -> None:
        """
        Construct the sound buffer from an array of audio samples.

        The assumed format of the audio samples is 16 bit signed integer.

        Parameters
        - samples	Pointer to the array of samples in memory
        - sampleRate	Sample rate (number of samples to play per second)
        - channelMap	Map of position in sample frame to sound channel

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    def load_from_file(self, filename: str) -> bool:
        """
        Load the sound buffer from a file.

        See the documentation of sf::InputSoundFile for the list of supported formats.

        Parameters
        - filename	Path of the sound file to load

        Returns
        - true if loading succeeded, false if it failed
        """

    def load_from_memory(self, data: bytes) -> bool:
        """
        Load the sound buffer from a file in memory.

        See the documentation of sf::InputSoundFile for the list of supported formats.

        Parameters
        - data	Bytes data in memory

        Returns
        - true if loading succeeded, false if it failed
        """

    def load_from_stream(self, stream: sfSystem.InputStream) -> bool:
        """
        Load the sound buffer from a custom stream.

        See the documentation of sf::InputSoundFile for the list of supported formats.

        Parameters
        - stream	Source stream to read from

        Returns
        - true if loading succeeded, false if it failed
        """

    def load_from_samples(self, samples: List[int], sampleCount: int, channelCount: int, sampleRate: int, channelMap: List[SoundChannel]) -> bool:
        """
        Load the sound buffer from an array of audio samples.

        The assumed format of the audio samples is 16 bit signed integer.

        Parameters
        - samples	Pointer to the array of samples in memory
        - sampleCount	Number of samples in the array
        - channelCount	Number of channels (1 = mono, 2 = stereo, ...)
        - sampleRate	Sample rate (number of samples to play per second)
        - channelMap	Map of position in sample frame to sound channel

        Returns
        - true if loading succeeded, false if it failed
        """

    def save_to_file(self, filename: str) -> bool:
        """
        Save the sound buffer to an audio file.

        See the documentation of sf::OutputSoundFile for the list of supported formats.

        Parameters
        - filename	Path of the sound file to write

        Returns
        - true if saving succeeded, false if it failed
        """

    def get_samples(self) -> List[int]:
        """
        Get the array of audio samples stored in the buffer.

        The format of the returned samples is 16 bit signed integer. The total number of samples in this array is given by the getSampleCount() function.

        Returns
        - Read-only pointer to the array of sound samples
        """

    def get_sample_count(self) -> int:
        """
        Get the number of samples stored in the buffer.

        The array of samples can be accessed with the getSamples() function.

        Returns
        - Number of samples
        """

    def get_sample_rate(self) -> int:
        """
        Get the sample rate of the sound.

        The sample rate is the number of samples played per second. The higher, the better the quality (for example, 44100 samples/s is CD quality).

        Returns
        - Sample rate (number of samples per second)
        """

    def get_channel_count(self) -> int:
        """
        Get the number of channels used by the sound.

        If the sound is mono then the number of channels will be 1, 2 for stereo, etc.

        Returns
        - Number of channels
        """

    def get_channel_map(self) -> List[SoundChannel]:
        """
        Get the map of position in sample frame to sound channel.

        This is used to map a sample in the sample stream to a position during spatialization.

        Returns
        - Map of position in sample frame to sound channel
        """

    def get_duration(self) -> float:
        """
        Get the total duration of the sound.

        Returns
        - Sound duration
        """

class PlaybackDevice(ModuleType):
    """
    The playback device is the audio output that the sound system uses.
    """

    @staticmethod
    def get_available_devices() -> List[str]:
        """
        Get a list of the names of all available audio playback devices.

        This function returns a vector of strings containing the names of all available audio playback devices.

        If the operating system reports multiple devices with the same name, a number will be appended to the name of all subsequent devices to distinguish them from each other. This guarantees that every entry returned by this function will represent a unique device.

        For example, if the operating system reports multiple devices with the name "Sound Card", the entries returned would be:

        Sound Card
        Sound Card 2
        Sound Card 3
        ...
        The default device, if one is marked as such, will be placed at the beginning of the vector.

        If no devices are available, this function will return an empty vector.

        Returns
        - A vector of strings containing the device names or an empty vector if no devices are available
        """

    @staticmethod
    def get_default_device() -> str | None:
        """
        Get the name of the default audio playback device.

        This function returns the name of the default audio playback device. If none is available, an empty string is returned.

        Returns
        - The name of the default audio playback device
        """

    @staticmethod
    def set_device(name: str) -> bool:
        """
        Set the audio playback device.

        This function sets the audio playback device to the device with the given name. It can be called on the fly (i.e: while sounds are playing).

        If there are sounds playing when the audio playback device is switched, the sounds will continue playing uninterrupted on the new audio playback device.

        Parameters
        - name	The name of the audio playback device

        Returns
        - true, if it was able to set the requested device
        """

    @staticmethod
    def get_device() -> str | None:
        """
        Get the name of the current audio playback device.

        Returns
        - The name of the current audio playback device or std::nullopt if there is none
        """

class Music(SoundStream):
    """
    Streamed music played from an audio file.

    Musics are sounds that are streamed rather than completely loaded in memory.

    This is especially useful for compressed musics that usually take hundreds of MB when they are uncompressed: by streaming it instead of loading it entirely, you avoid saturating the memory and have almost no loading delay. This implies that the underlying resource (file, stream or memory buffer) must remain valid for the lifetime of the sf::Music object.

    Apart from that, a sf::Music has almost the same features as the sf::SoundBuffer / sf::Sound pair: you can play/pause/stop it, request its parameters (channels, sample rate), change the way it is played (pitch, volume, 3D position, ...), etc.

    As a sound stream, a music is played in its own thread in order not to block the rest of the program. This means that you can leave the music alone after calling play(), it will manage itself very well.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Construct an empty music that does not contain any data.
        """

    @overload
    def __init__(self, filename: str) -> None:
        """
        Construct a music from an audio file.

        This function doesn't start playing the music (call play() to do so). See the documentation of sf::InputSoundFile for the list of supported formats.

        Warning
        - Since the music is not loaded at once but rather streamed continuously, the file must remain accessible until the sf::Music object loads a new music or is destroyed.

        Parameters
        - filename	Path of the music file to open

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, data: bytes) -> None:
        """
        Construct a music from an audio file in memory.

        This function doesn't start playing the music (call play() to do so). See the documentation of sf::InputSoundFile for the list of supported formats.

        Warning
        - Since the music is not loaded at once but rather streamed continuously, the data buffer must remain accessible until the sf::Music object loads a new music or is destroyed. That is, you can't deallocate the buffer right after calling this function.

        Parameters
        - data	Pointer to the file data in memory

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    @overload
    def __init__(self, stream: sfSystem.InputStream) -> None:
        """
        Construct a music from an audio file in a custom stream.

        This function doesn't start playing the music (call play() to do so). See the documentation of sf::InputSoundFile for the list of supported formats.

        Warning
        - Since the music is not loaded at once but rather streamed continuously, the stream must remain accessible until the sf::Music object loads a new music or is destroyed.

        Parameters
        - stream	Source stream to read from

        Exceptions
        - sf::Exception	if loading was unsuccessful
        """

    def open_from_file(self, filename: str) -> bool:
        """
        Open a music from an audio file.

        This function doesn't start playing the music (call play() to do so). See the documentation of sf::InputSoundFile for the list of supported formats.

        Warning
        - Since the music is not loaded at once but rather streamed continuously, the file must remain accessible until the sf::Music object loads a new music or is destroyed.

        Parameters
        - filename	Path of the music file to open

        Returns
        - true if loading succeeded, false if it failed
        """

    def open_from_memory(self, data: bytes) -> bool:
        """
        Open a music from an audio file in memory.

        This function doesn't start playing the music (call play() to do so). See the documentation of sf::InputSoundFile for the list of supported formats.

        Warning
        - Since the music is not loaded at once but rather streamed continuously, the data buffer must remain accessible until the sf::Music object loads a new music or is destroyed. That is, you can't deallocate the buffer right after calling this function.

        Parameters
        - data	Pointer to the file data in memory

        Returns
        - true if loading succeeded, false if it failed
        """

    def open_from_stream(self, stream: sfSystem.InputStream) -> bool:
        """
        Open a music from an audio file in a custom stream.

        This function doesn't start playing the music (call play() to do so). See the documentation of sf::InputSoundFile for the list of supported formats.

        Warning
        - Since the music is not loaded at once but rather streamed continuously, the stream must remain accessible until the sf::Music object loads a new music or is destroyed.

        Parameters
        - stream	Source stream to read from

        Returns
        - true if loading succeeded, false if it failed
        """

    def get_duration(self) -> sfSystem.Time:
        """
        Get the total duration of the music.

        Returns
        - Music duration
        """

    def get_loop_points(self) -> Tuple[sfSystem.Time, sfSystem.Time]:
        """
        Get the positions of the of the sound's looping sequence.

        Returns
        - Loop Time position class.

        Warning
        - Since setLoopPoints() performs some adjustments on the provided values and rounds them to internal samples, a call to getLoopPoints() is not guaranteed to return the same times passed into a previous call to setLoopPoints(). However, it is guaranteed to return times that will map to the valid internal samples of this Music if they are later passed to setLoopPoints().
        """

    def set_loop_points(self, timePoints: Tuple[sfSystem.Time, sfSystem.Time]) -> None:
        """
        Sets the beginning and duration of the sound's looping sequence using sf::Time

        setLoopPoints() allows for specifying the beginning offset and the duration of the loop such that, when the music is enabled for looping, it will seamlessly seek to the beginning whenever it encounters the end of the duration. Valid ranges for timePoints.offset and timePoints.length are [0, Dur) and (0, Dur-offset] respectively, where Dur is the value returned by getDuration(). Note that the EOF "loop point" from the end to the beginning of the stream is still honored, in case the caller seeks to a point after the end of the loop range. This function can be safely called at any point after a stream is opened, and will be applied to a playing sound without affecting the current playing offset.

        Warning
        - Setting the loop points while the stream's status is Paused will set its status to Stopped. The playing offset will be unaffected.

        Parameters
        - timePoints	The definition of the loop. Can be any time points within the sound's length
        """

class Sound(SoundSource):
    """
    Regular sound that can be played in the audio environment.

    sf::Sound is the class to use to play sounds.

    It provides:

    - Control (play, pause, stop)
    - Ability to modify output parameters in real-time (pitch, volume, ...)
    - 3D spatial features (position, attenuation, ...).
    sf::Sound is perfect for playing short sounds that can fit in memory and require no latency, like foot steps or gun shots. For longer sounds, like background musics or long speeches, rather see sf::Music (which is based on streaming).

    In order to work, a sound must be given a buffer of audio data to play. Audio data (samples) is stored in sf::SoundBuffer, and attached to a sound when it is created or with the setBuffer() function. The buffer object attached to a sound must remain alive as long as the sound uses it. Note that multiple sounds can use the same sound buffer at the same time.
    """

    def __init__(self, buffer: SoundBuffer) -> None:
        """
        Construct the sound with a buffer.

        Parameters
        - buffer	Sound buffer containing the audio data to play with the sound
        """

    def play(self) -> None:
        """
        Start or resume playing the sound.

        This function starts the stream if it was stopped, resumes it if it was paused, and restarts it from beginning if it was it already playing. This function uses its own thread so that it doesn't block the rest of the program while the sound is played.

        Implements sf::SoundSource.
        """

    def pause(self) -> None:
        """
        Pause the sound.

        This function pauses the sound if it was playing, otherwise (sound already paused or stopped) it has no effect.

        Implements sf::SoundSource.
        """

    def stop(self) -> None:
        """
        stop playing the sound

        This function stops the sound if it was playing or paused, and does nothing if it was already stopped. It also resets the playing position (unlike pause()).

        Implements sf::SoundSource.
        """

    def set_buffer(self, buffer: SoundBuffer) -> None:
        """
        Set the source buffer containing the audio data to play.

        It is important to note that the sound buffer is not copied, thus the sf::SoundBuffer instance must remain alive as long as it is attached to the sound.

        Parameters
        - buffer	Sound buffer to attach to the sound

        """

    def set_looping(self, looping: bool) -> None:
        """
        Set whether or not the sound should loop after reaching the end.

        If set, the sound will restart from beginning after reaching the end and so on, until it is stopped or setLooping(false) is called. The default looping state for sound is false.

        Parameters
        - loop	true to play in loop, false to play once
        """

    def set_playing_offset(self, timeOffset: sfSystem.Time) -> None:
        """
        Change the current playing position of the sound.

        The playing position can be changed when the sound is either paused or playing. Changing the playing position when the sound is stopped has no effect, since playing the sound will reset its position.

        Parameters
        - timeOffset	New playing position, from the beginning of the sound

        """

    def get_buffer(self) -> SoundBuffer:
        """
        Get the audio buffer attached to the sound.

        Returns
        - Sound buffer attached to the sound
        """

    def is_looping(self) -> bool:
        """
        Tell whether or not the sound is in loop mode.

        Returns
        - true if the sound is looping, false otherwise
        """

    def get_playing_offset(self) -> sfSystem.Time:
        """
        Get the current playing position of the sound.

        Returns
        - Current playing position, from the beginning of the sound
        """

class SoundRecorder:
    """
    Abstract base class for capturing sound data.

    sf::SoundBuffer provides a simple interface to access the audio recording capabilities of the computer (the microphone).

    As an abstract base class, it only cares about capturing sound samples, the task of making something useful with them is left to the derived class. Note that SFML provides a built-in specialization for saving the captured data to a sound buffer (see sf::SoundBufferRecorder).

    A derived class has only one virtual function to override:

    - onProcessSamples provides the new chunks of audio samples while the capture happens

    Moreover, two additional virtual functions can be overridden as well if necessary:

    - onStart is called before the capture happens, to perform custom initializations
    - onStop is called after the capture ends, to perform custom cleanup

    The audio capture feature may not be supported or activated on every platform, thus it is recommended to check its availability with the isAvailable() function. If it returns false, then any attempt to use an audio recorder will fail.

    If you have multiple sound input devices connected to your computer (for example: microphone, external sound card, webcam mic, ...) you can get a list of all available devices through the getAvailableDevices() function. You can then select a device by calling setDevice() with the appropriate device. Otherwise the default capturing device will be used.

    By default the recording is in 16-bit mono. Using the setChannelCount method you can change the number of channels used by the audio capture device to record. Note that you have to decide whether you want to record in mono or stereo before starting the recording.

    It is important to note that the audio capture happens in a separate thread, so that it doesn't block the rest of the program. In particular, the onProcessSamples virtual function (but not onStart and not onStop) will be called from this separate thread. It is important to keep this in mind, because you may have to take care of synchronization issues if you share data between threads. Another thing to bear in mind is that you must call stop() in the destructor of your derived class, so that the recording thread finishes before your object is destroyed.
    """

    def start_recording(self, sample_rate: int = 44100) -> bool:
        """
        Start the capture.

        The sampleRate parameter defines the number of audio samples captured per second. The higher, the better the quality (for example, 44100 samples/sec is CD quality). This function uses its own thread so that it doesn't block the rest of the program while the capture runs. Please note that only one capture can happen at the same time. You can select which capture device will be used by passing the name to the setDevice() method. If none was selected before, the default capture device will be used. You can get a list of the names of all available capture devices by calling getAvailableDevices().

        Parameters
        - sampleRate	Desired capture rate, in number of samples per second

        Returns
        - true, if start of capture was successful
        """

    def stop_recording(self) -> None:
        """
        Stop the capture.
        """

    def get_sample_rate(self) -> int:
        """
        Get the sample rate.

        The sample rate defines the number of audio samples captured per second. The higher, the better the quality (for example, 44100 samples/sec is CD quality).

        Returns
        - Sample rate, in samples per second
        """

    @staticmethod
    def get_available_devices() -> List[str]:
        """
        Get a list of the names of all available audio capture devices.

        This function returns a vector of strings, containing the names of all available audio capture devices.

        Returns
        - A vector of strings containing the names
        """

    @staticmethod
    def get_default_device() -> str:
        """
        Get the name of the default audio capture device.

        This function returns the name of the default audio capture device. If none is available, an empty string is returned.

        Returns
        - The name of the default audio capture device
        """

    def set_device(self, name: str) -> bool:
        """
        Set the audio capture device.

        This function sets the audio capture device to the device with the given name. It can be called on the fly (i.e: while recording). If you do so while recording and opening the device fails, it stops the recording.

        Parameters
        - name	The name of the audio capture device

        Returns
        - true, if it was able to set the requested device
        """

    def get_device(self) -> str:
        """
        Get the name of the current audio capture device.

        Returns
        - The name of the current audio capture device
        """

    def set_channel_count(self, channelCount: int) -> None:
        """
        Set the channel count of the audio capture device.

        This method allows you to specify the number of channels used for recording. Currently only 16-bit mono and 16-bit stereo are supported.

        Parameters
        - channelCount	Number of channels. Currently only mono (1) and stereo (2) are supported.
        """

    def get_channel_count(self) -> int:
        """
        Get the number of channels used by this recorder.

        Currently only mono and stereo are supported, so the value is either 1 (for mono) or 2 (for stereo).

        Returns
        - Number of channels
        """

    def get_channel_map(self) -> List[SoundChannel]:
        """
        Get the map of position in sample frame to sound channel.

        This is used to map a sample in the sample stream to a position during spatialization.

        Returns
        - Map of position in sample frame to sound channel
        """

    @staticmethod
    def is_available() -> bool:
        """
        Check if the system supports audio capture.

        This function should always be called before using the audio capture features. If it returns false, then any attempt to use sf::SoundRecorder or one of its derived classes will fail.

        Returns
        - true if audio capture is supported, false otherwise
        """

class SoundBufferRecorder(SoundRecorder):
    """
    Specialized SoundRecorder which stores the captured audio data into a sound buffer.

    sf::SoundBufferRecorder allows to access a recorded sound through a sf::SoundBuffer, so that it can be played, saved to a file, etc.

    It has the same simple interface as its base class (start(), stop()) and adds a function to retrieve the recorded sound buffer (getBuffer()).

    As usual, don't forget to call the isAvailable() function before using this class (see sf::SoundRecorder for more details about this).
    """

    def get_buffer(self) -> SoundBuffer:
        """
        Get the sound buffer containing the captured audio data.

        The sound buffer is valid only after the capture has ended. This function provides a read-only access to the internal sound buffer, but it can be copied if you need to make any modification to it.

        Returns
        - Read-only access to the sound buffer
        """

    @staticmethod
    def is_available() -> bool:
        """
        Check if the system supports audio capture.

        This function should always be called before using the audio capture features. If it returns false, then any attempt to use sf::SoundRecorder or one of its derived classes will fail.

        Returns
        - true if audio capture is supported, false otherwise
        """

class InputSoundFile:
    """
    Provide read access to sound files.

    This class decodes audio samples from a sound file.

    It is used internally by higher-level classes such as sf::SoundBuffer and sf::Music, but can also be useful if you want to process or analyze audio files without playing them, or if you want to implement your own version of sf::Music with more specific features.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.

        Construct an input sound file that is not associated with a file to read.
        """

    @overload
    def __init__(self, filename: str) -> None:
        """
        Construct a sound file from the disk for reading.

        The supported audio formats are: WAV (PCM only), OGG/Vorbis, FLAC, MP3. The supported sample sizes for FLAC and WAV are 8, 16, 24 and 32 bit.

        Because of minimp3_ex limitation, for MP3 files with big (>16kb) APEv2 tag, it may not be properly removed, tag data will be treated as MP3 data and there is a low chance of garbage decoded at the end of file. See also: https://github.com/lieff/minimp3

        Parameters
        - filename	Path of the sound file to load

        Exceptions
        - sf::Exception	if opening the file was unsuccessful
        """

    @overload
    def __init__(self, data: bytes, sizeInBytes: int) -> None:
        """
        Construct a sound file in memory for reading.

        The supported audio formats are: WAV (PCM only), OGG/Vorbis, FLAC. The supported sample sizes for FLAC and WAV are 8, 16, 24 and 32 bit.

        Parameters
        - data	Pointer to the file data in memory
        - sizeInBytes	Size of the data to load, in bytes

        Exceptions
        - sf::Exception	if opening the file was unsuccessful
        """

    @overload
    def __init__(self, stream: sfSystem.InputStream) -> None:
        """
        Construct a sound file from a custom stream for reading.

        The supported audio formats are: WAV (PCM only), OGG/Vorbis, FLAC. The supported sample sizes for FLAC and WAV are 8, 16, 24 and 32 bit.

        Parameters
        - stream	Source stream to read from

        Exceptions
        - sf::Exception	if opening the file was unsuccessful
        """

    def open_from_file(self, filename: str) -> bool:
        """
        Open a sound file from the disk for reading.

        The supported audio formats are: WAV (PCM only), OGG/Vorbis, FLAC, MP3. The supported sample sizes for FLAC and WAV are 8, 16, 24 and 32 bit.

        Because of minimp3_ex limitation, for MP3 files with big (>16kb) APEv2 tag, it may not be properly removed, tag data will be treated as MP3 data and there is a low chance of garbage decoded at the end of file. See also: https://github.com/lieff/minimp3

        Parameters
        - filename	Path of the sound file to load

        Returns
        - true if the file was successfully opened
        """

    def open_from_memory(self, data: bytes) -> bool:
        """
        Open a sound file in memory for reading.

        The supported audio formats are: WAV (PCM only), OGG/Vorbis, FLAC. The supported sample sizes for FLAC and WAV are 8, 16, 24 and 32 bit.

        Parameters
        - data	Pointer to the file data in memory
        - sizeInBytes	Size of the data to load, in bytes

        Returns
        - true if the file was successfully opened
        """

    def open_from_stream(self, stream: sfSystem.InputStream) -> bool:
        """
        Open a sound file from a custom stream for reading.

        The supported audio formats are: WAV (PCM only), OGG/Vorbis, FLAC. The supported sample sizes for FLAC and WAV are 8, 16, 24 and 32 bit.

        Parameters
        - stream	Source stream to read from

        Returns
        - true if the file was successfully opened
        """

    def get_sample_count(self) -> int:
        """
        Get the total number of audio samples in the file.

        Returns
        - Number of samples
        """

    def get_channel_count(self) -> int:
        """
        Get the number of channels used by the sound.

        Returns
        - Number of channels (1 = mono, 2 = stereo)
        """

    def get_sample_rate(self) -> int:
        """
        Get the number of channels used by the sound.

        Returns
        - Number of channels (1 = mono, 2 = stereo)
        """

    def get_channel_map(self) -> List[SoundChannel]:
        """
        Get the map of position in sample frame to sound channel.

        This is used to map a sample in the sample stream to a position during spatialization.

        Returns
        - Map of position in sample frame to sound channel
        """

    def get_duration(self) -> sfSystem.Time:
        """
        Get the total duration of the sound file.

        This function is provided for convenience, the duration is deduced from the other sound file attributes.

        Returns
        - Duration of the sound file
        """

    def get_time_offset(self) -> sfSystem.Time:
        """
        Get the read offset of the file in time.

        Returns
        - Time position
        """

    def get_sample_offset(self) -> int:
        """
        Get the total number of audio samples in the file.

        Returns
        - Number of samples
        """

    @overload
    def seek(self, timeOffset: sfSystem.Time) -> None:
        """
        Change the current read position to the given time offset.

        Using a time offset is handy but imprecise. If you need an accurate result, consider using the overload which takes a sample offset.

        If the given time exceeds to total duration, this function jumps to the end of the sound file.

        Parameters
        timeOffset	Time to jump to, relative to the beginning
        """

    @overload
    def seek(self, sample_offset: int) -> None:
        """
        Change the current read position to the given sample offset.

        This function takes a sample offset to provide maximum precision. If you need to jump to a given time, use the other overload.

        The sample offset takes the channels into account. If you have a time offset instead, you can easily find the corresponding sample offset with the following formula: timeInSeconds * sampleRate * channelCount If the given offset exceeds to total number of samples, this function jumps to the end of the sound file.

        Parameters
        - sampleOffset	Index of the sample to jump to, relative to the beginning
        """

    def read(self, samples: int, maxCount: int) -> int:
        """
        Read audio samples from the open file.

        Parameters
        - samples	Pointer to the sample array to fill
        - maxCount	Maximum number of samples to read

        Returns
        - Number of samples actually read (may be less than maxCount)
        """

    def close(self) -> None:
        """
        Close the current file.
        """

class OutputSoundFile:
    """
    Provide write access to sound files.

    This class encodes audio samples to a sound file.

    It is used internally by higher-level classes such as sf::SoundBuffer, but can also be useful if you want to create audio files from custom data sources, like generated audio samples.
    """

    def __init__(self, filename: str, sampleRate: int, channelCount: int, channelMap: List[SoundChannel]) -> None:
        """
        Construct the sound file from the disk for writing.

        The supported audio formats are: WAV, OGG/Vorbis, FLAC.

        Parameters
        - filename	Path of the sound file to write
        - sampleRate	Sample rate of the sound
        - channelCount	Number of channels in the sound
        - channelMap	Map of position in sample frame to sound channel

        Exceptions
        - sf::Exception	if the file could not be opened successfully
        """

    def open_from_file(self, filename: str, sampleRate: int, channelCount: int, channelMap: List[SoundChannel]) -> bool:
        """
        Open the sound file from the disk for writing.

        The supported audio formats are: WAV, OGG/Vorbis, FLAC.

        Parameters
        - filename	Path of the sound file to write
        - sampleRate	Sample rate of the sound
        - channelCount	Number of channels in the sound
        - channelMap	Map of position in sample frame to sound channel

        Returns
        - true if the file was successfully opened
        """

    def write(self, samples: bytes, count: int) -> None:
        """
        Write audio samples to the file.

        Parameters
        - samples	Pointer to the sample array to write
        - count	Number of samples to write
        """

    def close(self) -> None:
        """
        Close the current file.
        """
