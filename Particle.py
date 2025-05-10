import bisect
from typing import Dict, List, Optional
from .sfGraphics import *
from .sfSystem import *

class Particle(Sprite):
    """
    Particle class, inherits from Sprite.

    It's a basic particle class. You can inherit from it to create your own particle class.
    """

    def __init__(self, texture: Texture, velocity: Vector2f, duration: Optional[Time], rectangle: IntRect = None):
        """
        Particle constructor.

        Parameters:
        - texture: Source texture.
        - velocity: Particle velocity, which is a vector of type Vector2f. Particle will corresponding pixels per second.
        - duration: Particle duration, which is a time of type Time. If duration is None, particle will not expire.
        - rectangle: Source rectangle.
        """

        self.velocity = velocity
        self.duration = duration
        self.render_state = RenderStates.default()
        self.render_state.texture = texture
        self._is_expired = False

        if rectangle is not None:
            super().__init__(texture, rectangle)
        else:
            super().__init__(texture)

    def update(self, delta_time: Time):
        """
        Update particle.

        Particle will move according to velocity.

        Parameters:
        - deltaTime: Time elapsed since last update.
        """

        if self.is_expired():
            return

        distance: Vector2f = self.velocity * delta_time.as_seconds()
        self.move(distance)
        if self.duration is not None:
            if self.duration > delta_time:
                self.duration -= delta_time
            else:
                self.duration = Time.Zero()
                self._is_expired = True

    def is_expired(self) -> bool:
        """
        Check if particle is expired.

        Returns:
        - True if particle is expired, False otherwise.
        """

        return self._is_expired

    def set_expired(self, expired: bool):
        """
        Set particle expired.

        Parameters:
        - expired: True if particle is expired, False otherwise.
        """

        self._is_expired = expired

    def is_collide(self, other: Sprite) -> bool:
        """
        Check if particle is collide with other sprite.

        Parameters:
        - other: Other sprite.

        Returns:
        - True if particle is collide with other sprite, False otherwise.
        """

        return (self.get_global_bounds().find_intersection(other.get_global_bounds()) is not None)

    def on_collide(self):
        """
        Called when particle is collide with other sprite.

        You can override this method to implement your own behaviour.
        """


class ParticleMgr:
    """
    Particle system class.

    It could manage all particles' behaviour.
    """

    def __init__(self):
        """
        Particle system constructor.
        """
        self._particles: Dict[int, Dict[Texture, List[Particle]]] = {}
        self._z_list = []
        self._particles_to_z: Dict[Particle, int] = {}

    def add_particle(self, particle: Particle, z: int = 0):
        """
        Add a particle to the particle system.

        Parameters:
        - particle: Particle to add.
        - z: Layer of the particle.
        """

        if particle in self._particles_to_z:
            raise ValueError('Particle already exists.')

        if z not in self._particles:
            self._particles[z] = {}
            bisect.insort(self._z_list, z)

        texture = particle.get_texture()
        if texture not in self._particles[z]:
            self._particles[z][texture] = []

        self._particles[z][texture].append(particle)
        self._particles_to_z[particle] = z

    def remove_particle(self, particle: Particle):
        """
        Remove a particle from the particle system.

        Parameters:
        - particle: Particle to remove.
        """

        if particle not in self._particles_to_z:
            raise ValueError('Particle not found.')

        texture = particle.get_texture()

        z = self._particles_to_z[particle]
        self._particles[z][texture].remove(particle)
        self._particles_to_z.pop(particle)

        if len(self._particles[z][texture]) == 0:
            self._particles[z].pop(texture)

        if len(self._particles[z]) == 0:
            self._particles.pop(z)
            self._z_list.remove(z)

    def clear(self):
        """
        Clear all particles.
        """

        self._particles.clear()
        self._z_list.clear()
        self._particles_to_z.clear()

    def get_z_list(self) -> List[int]:
        """
        Get all layers.

        Returns:
        - List of all layers.
        """

        return self._z_list.copy()

    def update(self, delta_time: Time):
        """
        Update all particles.

        Parameters:
        - deltaTime: Time elapsed since last update.
        """

        for particles_ in self._particles.copy().values():
            for particle_list in particles_.copy().values():
                for particle in particle_list:
                    particle.update(delta_time)
                    if particle.is_expired():
                        self.remove_particle(particle)

    def display(self, target: RenderTarget, z: int = None):
        """
        Draw all particles.

        Parameters:
        - target: Render target.
        - states: Render states.
        """
        if z is None:
            z_list = self.get_z_list()
        else:
            z_list = [z]

        for z_ in z_list:
            for particle_list in self._particles[z_].values():
                for particle in particle_list:
                    target.draw(particle, particle.render_state)
