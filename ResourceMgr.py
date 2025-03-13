from typing import Dict, List, Union
from . import sfGraphics
from . import sfAudio

class TextureMgr:
    """
    Texture manager class.

    It could manage all textures.
    """

    _textures: Dict[str, sfGraphics.Texture] = {}

    @classmethod
    def get_texture(cls, path: str) -> sfGraphics.Texture:
        """
        Get texture from path.

        Parameters:
        - path: Path of texture.

        Returns:
        - The texture from path.
        """

        if path not in cls._textures:
            cls._textures[path] = sfGraphics.Texture()
            if not cls._textures[path].load_from_file(path):
                raise ValueError(f'Failed to load texture from {path}.')

        return cls._textures[path]

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

    @classmethod
    def get_font(cls, filename: str) -> sfGraphics.Font:
        """
        Get font from name.

        Parameters:
        - filename: File name of font.

        Returns:
        - The font from path.
        """

        if filename not in cls._fonts:
            cls._fonts[filename] = sfGraphics.Font()
            if not cls._fonts[filename].open_from_file(f'assets/fonts/{filename}'):
                raise ValueError(f'Failed to load font from {filename}.')

        return cls._fonts[filename]

    @classmethod
    def has_font(cls, filename: str) -> bool:
        """
        Check if font is loaded.

        Parameters:
        - filename: File name of font.

        Returns:
        - True if font is loaded, False otherwise.
        """

        return filename in cls._fonts

    @classmethod
    def release_font(cls, filename: str):
        """
        Release font from name.

        Parameters:
        - filename: File name of font.
        """

        if filename in cls._fonts:
            cls._fonts.pop(filename)
        else:
            raise ValueError(f'Fail to release font from {filename}.')

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

    _sounds_cache: Dict[str, sfAudio.SoundBuffer] = {}
    _voices_cache: Dict[str, sfAudio.SoundBuffer] = {}

    _music: Dict[str, sfAudio.Music] = {}
    _sound_list: List[sfAudio.Sound] = []
    _voice_list: List[sfAudio.Sound] = []

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

        return cls._music

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

        if name not in cls._voices_cache:
            cls._voices_cache[name] = sfAudio.SoundBuffer()
            if not cls._voices_cache[name].load_from_file(f'assets/voices/{name}'):
                raise ValueError(f'Fail to load voice from {name}.')

        return cls._voices_cache[name]

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
    def release_voice(cls, name: str):
        """
        Release voice from name.

        Parameters:
        - name: Name of voice.
        """

        if name in cls._voices_cache:
            cls._voices_cache[name].stop()
            cls._voices_cache.pop(name)
        else:
            raise ValueError(f'Fail to release voice from {name}.')

    @classmethod
    def play_music(cls, keyword: str, para: Union[str, sfAudio.Music]):
        """
        Play music from name or music.

        Parameters:
        - keyword: Keyword of music, such as 'bgm' or 'bgs'.
        - para: Name of music or music object.
        """

        if isinstance(para, str):
            music = cls.get_music(para)
        elif isinstance(para, sfAudio.Music):
            music = para
        else:
            raise ValueError('Music not found.')

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

        sound: sfAudio.Sound = None

        if isinstance(para, str):
            sound = sfAudio.Sound(cls.get_sound(para))
        elif isinstance(para, sfAudio.SoundBuffer):
            sound = sfAudio.Sound(para)

        if sound is None:
            raise ValueError('Sound not found.')

        cls._sound_list.append(sound)
        sound.play()

    @classmethod
    def play_voice(cls, para: Union[str, sfAudio.SoundBuffer]):
        """
        Play voice from name or sound buffer.

        Parameters:
        - para: Name of voice or sound buffer.
        """

        voice: sfAudio.Sound = None

        if isinstance(para, str):
            voice = sfAudio.Sound(cls.get_voice(para))
        elif isinstance(para, sfAudio.SoundBuffer):
            voice = sfAudio.Sound(para)

        if voice is None:
            raise ValueError('Voice not found.')

        cls._voice_list.append(voice)
        voice.play()

    @classmethod
    def update(cls):
        """
        Update all audios.
        """

        for sound in cls._sound_list[:]:
            if sound.get_status() == sfAudio.Sound.Status.Stopped:
                cls._sound_list.remove(sound)
        for voice in cls._voice_list[:]:
            if voice.get_status() == sfAudio.Sound.Status.Stopped:
                cls._voice_list.remove(voice)

    @classmethod
    def clear(cls):
        """
        Clear all audios.
        """

        for value in cls._sounds_cache.values():
            value.stop()
        cls._sounds_cache.clear()
        for value in cls._voices_cache.values():
            value.stop()
        cls._voices_cache.clear()
        for value in cls._music.values():
            value.stop()
        cls._music.clear()
        cls._sound_list.clear()
        cls._voice_list.clear()
