import os
from typing import Dict, List, Union

from . import sfSystem
from . import sfGraphics
from . import sfAudio

class TextureMgr:
    """
    Texture manager class.

    It could manage all textures.
    """

    _textures: Dict[str, sfGraphics.Texture] = {}
    _ref_pak: Dict[str, Dict[str, bytes]] = {}

    @classmethod
    def get_texture(cls, path: str) -> sfGraphics.Texture:
        """
        Get texture from path.

        Parameters:
        - path: Path of texture.

        Returns:
        - The texture from path.
        """

        if os.path.exists(path):
            if path not in cls._textures:
                cls._textures[path] = sfGraphics.Texture()
                if not cls._textures[path].load_from_file(path):
                    raise ValueError(f'Failed to load texture from {path}.')
        else:
            path_parts = path.split('/')
            if len(path_parts) < 2:
                raise ValueError(f'Failed to load texture from {path}.')
            key = path_parts[1:]
            if len(key) < 2:
                raise ValueError(f'Failed to load texture from {path}.')
            ref = cls._ref_pak
            level = 0
            while level < len(key):
                if key[level] in ref:
                    ref = ref[key[level]]
                    level += 1
                else:
                    raise ValueError(f'Failed to load texture from {path}.')
                    break
            if isinstance(ref, bytes):
                texture = sfGraphics.Texture()
                if not texture.load_from_memory(ref):
                    raise ValueError(f'Failed to load texture from {path}.')
                cls._textures[path] = texture

        return cls._textures[path]

    @classmethod
    def add_pak_ref(cls, pak: Dict[str, Dict[str, bytes]]):
        """
        Add a pak reference to the manager.

        Parameters:
        - pak: The pak reference.
        """

        cls._ref_pak = pak

    @classmethod
    def has_texture(cls, path: str) -> bool:
        """
        Check if texture is loaded.

        Parameters:
        - path: Path of texture.

        Returns:
        - True if texture is loaded, False otherwise.
        """

        return path in cls._textures

    @classmethod
    def release_texture(cls, path: str):
        """
        Release texture from path.

        Parameters:
        - path: Path of texture.
        """

        if path in cls._textures:
            cls._textures.pop(path)
        else:
            raise ValueError(f'Failed to release texture from {path}.')

    @classmethod
    def clear(cls):
        """
        Clear all textures.
        """

        cls._textures.clear()

    @classmethod
    def block(cls, filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/blocks folder.

        Parameters:
        - filename: Name of texture.
        """

        return cls.get_texture(f'assets/blocks/{filename}')

    @classmethod
    def character(cls, filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/characters folder.

        Parameters:
        - filename: Name of texture.
        """

        return cls.get_texture(f'assets/characters/{filename}')

    @classmethod
    def system(cls, filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/system folder.

        Parameters:
        - filename: Name of texture.
        """

        return cls.get_texture(f'assets/system/{filename}')

    @classmethod
    def tilesets(cls, filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/tilesets folder.

        Parameters:
        - filename: Name of texture.
        """

        return cls.get_texture(f'assets/tilesets/{filename}')

    @classmethod
    def release_block(cls, filename: str):
        """
        Release texture from assets/blocks folder.

        Parameters:
        - filename: Name of texture.
        """

        cls.release_texture(f'assets/blocks/{filename}')

    @classmethod
    def release_character(cls, filename: str):
        """
        Release texture from assets/characters folder.

        Parameters:
        - filename: Name of texture.
        """

        cls.release_texture(f'assets/characters/{filename}')

    @classmethod
    def release_system(cls, filename: str):
        """
        Release texture from assets/system folder.

        Parameters:
        - filename: Name of texture.
        """

        cls.release_texture(f'assets/system/{filename}')

    @classmethod
    def release_tilesets(cls, filename: str):
        """
        Release texture from assets/tilesets folder.

        Parameters:
        - filename: Name of texture.
        """

        cls.release_texture(f'assets/tilesets/{filename}')


class FontMgr:
    """
    Font manager class.

    It could manage all fonts.
    """

    _fonts: Dict[str, sfGraphics.Font] = {}
    _font_filenames: Dict[str, str] = {}

    @classmethod
    def get_font_from_file(cls, filename: str) -> sfGraphics.Font:
        """
        Get font from name.

        Parameters:
        - filename: File name of font.

        Returns:
        - The font from path.
        """

        if filename not in cls._font_filenames:
            font = sfGraphics.Font()
            if not font.open_from_file(f'assets/fonts/{filename}'):
                raise ValueError(f'Failed to load font from {filename}.')
            cls._fonts[font.get_info().family] = font
            cls._font_filenames[filename] = font.get_info().family

        return cls._fonts[cls._font_filenames[filename]]

    @classmethod
    def get_font(cls, name: str) -> sfGraphics.Font:
        """
        Get font from name.
        Parameters:
        - name: File name of font.
        Returns:
        - The font from path.
        """

        if name not in cls._fonts:
            raise ValueError(f'Fail to get font from {name}.')

        return cls._fonts[name]

    @classmethod
    def has_font(cls, name: str) -> bool:
        """
        Check if font is loaded.

        Parameters:
        - name: File name of font.

        Returns:
        - True if font is loaded, False otherwise.
        """

        return name in cls._fonts

    @classmethod
    def release_font(cls, name: str):
        """
        Release font from name.

        Parameters:
        - name: File name of font.
        """

        if name in cls._fonts:
            cls._fonts.pop(name)
        else:
            raise ValueError(f'Fail to release font from {name}.')

    @classmethod
    def clear(cls):
        """
        Clear all fonts.
        """

        cls._fonts.clear()

class AudioMgr:
    """
    sfAudio manager class.

    It could manage all audios.
    """
    class _SoundExt(sfAudio.Sound):
        def __init__(self, buffer):
            super().__init__(buffer)
            self.started = False
        def play(self):
            self.started = True
            super().play()


    _sounds_cache: Dict[str, sfAudio.SoundBuffer] = {}
    _voice: Union[sfAudio.SoundBuffer, sfAudio.Sound] = None

    _music: Dict[str, sfAudio.Music] = {}
    _sound_list: List[_SoundExt] = []

    _sound_pool: Dict[sfAudio.SoundBuffer, List[sfAudio.Sound]] = {}

    @classmethod
    def get_music(cls, name: str) -> sfAudio.Music:
        """
        Get music from name.

        Parameters:
        - name: Name of music.

        Returns:
        - The music from path.
        """

        music = sfAudio.Music()
        if not music.open_from_file(f'assets/musics/{name}'):
            raise ValueError(f'Fail to load music from {name}.')

        return music

    @classmethod
    def get_sound(cls, name: str) -> sfAudio.SoundBuffer:
        """
        Get sound from name.

        Parameters:
        - name: Name of sound.

        Returns:
        - The sound from path.
        """

        if name not in cls._sounds_cache:
            cls._sounds_cache[name] = sfAudio.SoundBuffer()
            if not cls._sounds_cache[name].load_from_file(f'assets/sounds/{name}'):
                raise ValueError(f'Fail to load sound from {name}.')

        return cls._sounds_cache[name]

    @classmethod
    def get_voice(cls, name: str) -> sfAudio.SoundBuffer:
        """
        Get voice from name.

        Parameters:
        - name: Name of voice.

        Returns:
        - The voice from path.
        """

        sb: sfAudio.SoundBuffer = None
        if name not in cls._voices_cache:
            sb = sfAudio.SoundBuffer()
            if not sb.load_from_file(f'assets/voices/{name}'):
                raise ValueError(f'Fail to load voice from {name}.')

        return sb

    @classmethod
    def release_music(cls, keyword: str):
        """
        Release music from name.
        """

        if keyword in cls._music:
            cls._music[keyword].stop()
            cls._music.pop(keyword)
        else:
            raise ValueError(f'Fail to release music from {keyword}.')


    @classmethod
    def release_sound(cls, name: str):
        """
        Release sound from name.

        Parameters:
        - name: Name of sound.
        """

        if name in cls._sounds_cache:
            cls._sounds_cache[name].stop()
            cls._sounds_cache.pop(name)
        else:
            raise ValueError(f'Fail to release sound from {name}.')

    @classmethod
    def play_music(cls, keyword: str, para: Union[str, sfAudio.Music]):
        """
        Play music from name or music.

        Parameters:
        - keyword: Keyword of music, such as 'bgm' or 'bgs'.
        - para: Name of music or music object.
        """

        music = para
        if isinstance(para, str):
            music = cls.get_music(para)

        if keyword in cls._music:
            cls._music[keyword].stop()

        cls._music[keyword] = music

        cls._music[keyword].play()

    @classmethod
    def play_sound(cls, para: Union[str, sfAudio.SoundBuffer]):
        """
        Play sound from name or sound buffer.

        Parameters:
        - para: Name of sound or sound buffer.
        """

        sound: AudioMgr._SoundExt = None

        sound_buffer = para
        if isinstance(para, str):
            sound_buffer = cls.get_sound(para)

        if sound_buffer in cls._sound_pool:
            if len(cls._sound_pool[sound_buffer]) > 0:
                sound = cls._sound_pool[sound_buffer].pop()

        if sound is None:
            sound = cls._SoundExt(sound_buffer)

        cls._sound_list.append(sound)

    @classmethod
    def play_voice(cls, para: Union[str, sfAudio.SoundBuffer]):
        """
        Play voice from name or sound buffer.

        Parameters:
        - para: Name of voice or sound buffer.
        """

        sound_buffer = para
        if isinstance(para, str):
            sound_buffer = cls.get_voice(para)

        cls._voice = (sound_buffer, cls._SoundExt(sound_buffer))

    @classmethod
    def update(cls):
        """
        Update all audios.
        """

        for sound in cls._sound_list[:]:
            if not sound.started:
                sound.play()
                continue
            if sound.get_status() == sfAudio.Sound.Status.Stopped:
                if not sound.get_buffer() in cls._sound_pool:
                    cls._sound_pool[sound.get_buffer()] = []
                sound.started = False
                cls._sound_pool[sound.get_buffer()].append(sound)
                cls._sound_list.remove(sound)
        if cls._voice is not None:
            if not cls._voice.started:
                cls._voice.play()
                return
            if cls._voice.get_status() == sfAudio.Sound.Status.Stopped:
                cls._voice = None
                return

    @classmethod
    def clear(cls):
        """
        Clear all audios.
        """

        for value in cls._sound_list:
            value.stop()
        cls._sound_list.clear()
        cls._sounds_cache.clear()
        for value in cls._music.values():
            value.stop()
        cls._music.clear()
