import bisect
from typing import Dict, List, Tuple, Union
from . import sfSystem, sfGraphics, sfAudio

class Event:
    """
    Animation events, including the appearance and duration of images and the playing of audio.
    """

    def __init__(self, event: Union[sfAudio.Sound, sfGraphics.Sprite, str], duration: sfSystem.Time):
        """
        Constructor.

        Parameters:
        - event: Event, which can be a sound or a sprite.
        - duration: Duration of the event.
        """

        self.event = event
        self.duration = duration
        self._is_expired = False

    def update(self, delta_time: sfSystem.Time):
        """
        Update event.

        Parameters:
        - deltaTime: Time elapsed since last update.
        """

        if self.is_expired():
            return

        if isinstance(self.event, sfAudio.Sound):
            if self.event.get_status() == sfAudio.Sound.Status.Stopped:
                self.set_expired(True)
            return

        if self.duration > delta_time:
            self.duration -= delta_time
        else:
            self.duration = sfSystem.Time.Zero()
            self.set_expired(True)

    def display(self, target: sfGraphics.RenderTarget):
        """
        Draw event.

        Parameters:
        - target: Render target.
        """

        if isinstance(self.event, sfGraphics.Sprite):
            target.draw(self.event)

    def is_expired(self) -> bool:
        """
        Check if event is expired.

        Returns:
        - True if event is expired, False otherwise.
        """

        return self._is_expired

    def set_expired(self, expired: bool):
        """
        Set event expired.

        Parameters:
        - expired: True if event is expired, False otherwise.
        """

        self._is_expired = expired

    def start(self, position: sfSystem.Vector3f):
        """
        Start event.
        """

        if isinstance(self.event, sfAudio.Sound):
            self.event.play()
            self.event.set_position(position)
        elif isinstance(self.event, sfGraphics.Sprite):
            texture_rect = self.event.get_texture_rect()
            self.event.set_origin(sfSystem.Vector2f(texture_rect.size.x / 2, texture_rect.size.y / 2))
            self.event.move(sfSystem.Vector2f(position.x, position.y))

class Animation:
    """
    Animation type, which is the data of a single animation.

    Animation has a timeline, and each event is executed on the timeline.
    """

    def __init__(self, animation_len: sfSystem.Time, animation_events: List[Tuple[Event, sfSystem.Time]]):
        """
        Constructor for the Animation class.

        Parameters:
        - animation_len: The total length of the animation in seconds.
        - animation_events: A list of tuples, where each tuple contains an Event object and the time at which the event should start.
        """

        self.animation_len = animation_len
        self.animation_events = animation_events
        self.position = sfSystem.Vector3f(0, 0, 0)

        self._animation_time = sfSystem.Time.Zero()
        self._is_expired = False
        self._executing_events: List[Event] = []

    def update(self, delta_time: sfSystem.Time):
        """
        Update the animation based on the elapsed time.

        Parameters:
        - delta_time: The time elapsed since the last update.
        """

        if self.is_expired():
            return

        for event_pair in self.animation_events:
            event, event_time = event_pair
            if event in self._executing_events:
                if not event.is_expired():
                    event.update(delta_time)
                continue
            if self._animation_time >= event_time:
                self._executing_events.append(event)
                event.start(self.position)

        self._animation_time += delta_time
        if self._animation_time >= self.animation_len:
            self.set_expired(True)
            return

    def display(self, target: sfGraphics.RenderTarget):
        """
        Draw all non-expired events in the current animation on the specified render target.

        Parameters:
        - target: The render target where the events will be drawn.
        """

        for event in self._executing_events:
            if not event.is_expired():
                event.display(target)

    def is_expired(self) -> bool:
        """
        Check if animation is expired.

        Returns:
        - True if animation is expired, False otherwise.
        """

        return self._is_expired

    def set_expired(self, expired: bool):
        """
        Set animation expired.

        Parameters:
        - expired: True if animation is expired, False otherwise.
        """

        self._is_expired = expired

class AnimationMgr:
    """
    Animation manager, which is used to manage animations.

    Animation manager is used to manage animations, and can be used to add, remove, clear, and display animations.
    """

    def __init__(self):
        """
        Default constructor for the AnimationMgr class.
        """
        self._animations: Dict[int, List[Animation]] = {}
        self._z_list: List[int] = []
        self._animation_to_z: Dict[Animation, int] = {}

    def add_animation(self, animation: Animation, z: int = 0):
        """
        Add an animation to the manager at the specified z - index.

        Parameters:
        - animation: The Animation object to be added.
        - z: The z - index at which the animation will be placed. Defaults to 0.

        Raises:
        - ValueError: If the animation already exists in the manager.
        """

        if animation in self._animation_to_z:
            raise ValueError('Animation already exists')

        if z not in self._animations:
            self._animations[z] = []
            bisect.insort(self._z_list, z)

        self._animations[z].append(animation)
        self._animation_to_z[animation] = z

    def remove_animation(self, animation: Animation):
        """
        Remove an animation from the manager.

        Parameters:
        - animation: The Animation object to be removed.

        Raises:
        - ValueError: If the animation does not exist in the manager.
        """

        if animation not in self._animation_to_z:
            raise ValueError('Animation does not exist')

        z = self._animation_to_z[animation]
        self._animations[z].remove(animation)
        self._animation_to_z.pop(animation)

        if len(self._animations[z]) == 0:
            self._animations.pop(z)
            self._z_list.remove(z)

    def clear(self):
        """
        Clear all animations and associated data from the manager.
        This method resets the manager to its initial state by clearing all stored animations,
        the list of z - indices, and the mapping between animations and their z - indices.
        """

        self._animations.clear()
        self._z_list.clear()
        self._animation_to_z.clear()

    def get_z_list(self) -> List[int]:
        """
        Retrieve a copy of the sorted list of z - indices used by the AnimationMgr.

        This method returns a copy of the internal list of z - indices,
        ensuring that the original list remains unmodified when the caller manipulates the returned list.

        Returns:
        - List[int]: A copy of the sorted list of z - indices.
        """

        return self._z_list.copy()

    def update(self, delta_time: sfSystem.Time):
        """
        Update all animations managed by the AnimationMgr and remove expired animations.

        Parameters:
        - delta_time: The time elapsed since the last update.
        """

        for animations in self._animations.copy().values():
            for animation in animations[:]:
                animation.update(delta_time)
                if animation.is_expired():
                    self.remove_animation(animation)

    def display(self, target: sfGraphics.RenderTarget, z: int = None):
        """
        Draw all animations managed by the AnimationMgr on the specified render target.
        If a z - index is provided, only animations at that z - index will be drawn;
        otherwise, animations at all z - indices will be drawn.

        Parameters:
        - target: The render target where the animations will be drawn.
        - z: The z - index of the animations to be drawn. If None, all z - indices will be considered. Defaults to None.
        """

        if z is None:
            z_list = self.get_z_list()
        else:
            z_list = [z]

        for z_ in z_list:
            for animation in self._animations[z_]:
                animation.display(target)
