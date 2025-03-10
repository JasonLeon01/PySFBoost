import bisect
from typing import Dict, List, Optional
from . import sfGraphics, sfSystem

class Particle(sfGraphics.Sprite):
    """
    Particle class, inherits from sfGraphics.Sprite.

    It's a basic particle class. You can inherit from it to create your own particle class.
    """

    def __init__(self, texture: sfGraphics.Texture, velocity: sfSystem.Vector2f, duration: Optional[sfSystem.Time], rectangle: sfGraphics.IntRect = None):
        """
        Particle constructor.

        Parameters:
        - texture: Source texture.
        - velocity: Particle velocity, which is a vector of type sfSystem.Vector2f. Particle will corresponding pixels per second.
        - duration: Particle duration, which is a time of type sfSystem.Time. If duration is None, particle will not expire.
        - rectangle: Source rectangle.
        """

        self.velocity = velocity
        self.duration = duration
        self.render_state = sfGraphics.RenderStates.default()
        self.render_state.texture = texture
        self._is_expired = False

        if rectangle is not None:
            super().__init__(texture, rectangle)
        else:
            super().__init__(texture)

    def update(self, delta_time: sfSystem.Time):
        """
        Update particle.

        Particle will move according to velocity.

        Parameters:
        - deltaTime: Time elapsed since last update.
        """

        if self.is_expired():
            return

        distance: sfSystem.Vector2f = self.velocity * delta_time.as_seconds()
        self.move(distance)
        if self.duration is not None:
            if self.duration > delta_time:
                self.duration -= delta_time
            else:
                self.duration = sfSystem.Time.Zero()
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

    def is_collide(self, other: sfGraphics.Sprite) -> bool:
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

    _particles: Dict[int, Dict[sfGraphics.Texture, List[Particle]]] = {}
    _z_list = []
    _particles_to_z: Dict[Particle, int] = {}

    @staticmethod
    def add_particle(particle: Particle, z: int = 0):
        """
        Add a particle to the particle system.

        Parameters:
        - particle: Particle to add.
        - z: Layer of the particle.
        """

        if particle in ParticleMgr._particles_to_z:
            raise ValueError('Particle already exists.')

        if z not in ParticleMgr._particles:
            ParticleMgr._particles[z] = {}
            bisect.insort(ParticleMgr._z_list, z)

        texture = particle.get_texture()
        if texture not in ParticleMgr._particles[z]:
            ParticleMgr._particles[z][texture] = []

        ParticleMgr._particles[z][texture].append(particle)
        ParticleMgr._particles_to_z[particle] = z

    @staticmethod
    def remove_particle(particle: Particle):
        """
        Remove a particle from the particle system.

        Parameters:
        - particle: Particle to remove.
        """

        if particle not in ParticleMgr._particles_to_z:
            raise ValueError('Particle not found.')

        texture = particle.get_texture()

        z = ParticleMgr._particles_to_z[particle]
        ParticleMgr._particles[z][texture].remove(particle)
        ParticleMgr._particles_to_z.pop(particle)

        if len(ParticleMgr._particles[z][texture]) == 0:
            ParticleMgr._particles[z].pop(texture)

        if len(ParticleMgr._particles[z]) == 0:
            ParticleMgr._particles.pop(z)
            ParticleMgr._z_list.remove(z)

    @staticmethod
    def clear():
        """
        Clear all particles.
        """

        ParticleMgr._particles.clear()
        ParticleMgr._z_list.clear()
        ParticleMgr._particles_to_z.clear()

    @staticmethod
    def get_z_list() -> List[int]:
        """
        Get all layers.

        Returns:
        - List of all layers.
        """

        return ParticleMgr._z_list.copy()

    @staticmethod
    def update(delta_time: sfSystem.Time):
        """
        Update all particles.

        Parameters:
        - deltaTime: Time elapsed since last update.
        """

        for particles_ in ParticleMgr._particles.copy().values():
            for particle_list in particles_.copy().values():
                for particle in particle_list:
                    particle.update(delta_time)
                    if particle.is_expired():
                        ParticleMgr.remove_particle(particle)

    @staticmethod
    def display(target: sfGraphics.RenderTarget, z: int = None):
        """
        Draw all particles.

        Parameters:
        - target: Render target.
        - states: Render states.
        """
        if z is None:
            z_list = ParticleMgr.get_z_list()
        else:
            z_list = [z]

        for z_ in z_list:
            for particle_list in ParticleMgr._particles[z_].values():
                for particle in particle_list:
                    target.draw(particle, particle.render_state)
