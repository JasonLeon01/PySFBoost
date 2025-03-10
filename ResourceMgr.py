from typing import Dict, List, Union
from . import sfGraphics
from . import sfAudio

class TextureMgr:
    """
    Texture manager class.

    It could manage all textures.
    """

    _textures: Dict[str, sfGraphics.Texture] = {}

    @staticmethod
    def get_texture(path: str) -> sfGraphics.Texture:
        """
        Get texture from path.

        Parameters:
        - path: Path of texture.

        Returns:
        - The texture from path.
        """

        if path not in TextureMgr._textures:
            TextureMgr._textures[path] = sfGraphics.Texture()
            if not TextureMgr._textures[path].load_from_file(path):
                raise ValueError(f'Failed to load texture from {path}.')

        return TextureMgr._textures[path]

    @staticmethod
    def has_texture(path: str) -> bool:
        """
        Check if texture is loaded.

        Parameters:
        - path: Path of texture.

        Returns:
        - True if texture is loaded, False otherwise.
        """

        return path in TextureMgr._textures

    @staticmethod
    def release_texture(path: str):
        """
        Release texture from path.

        Parameters:
        - path: Path of texture.
        """

        if path in TextureMgr._textures:
            TextureMgr._textures.pop(path)
        else:
            raise ValueError(f'Failed to release texture from {path}.')

    @staticmethod
    def clear():
        """
        Clear all textures.
        """

        TextureMgr._textures.clear()

    @staticmethod
    def block(filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/blocks folder.

        Parameters:
        - filename: Name of texture.
        """

        return TextureMgr.get_texture(f'assets/blocks/{filename}')

    @staticmethod
    def character(filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/characters folder.

        Parameters:
        - filename: Name of texture.
        """

        return TextureMgr.get_texture(f'assets/characters/{filename}')

    @staticmethod
    def system(filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/system folder.

        Parameters:
        - filename: Name of texture.
        """

        return TextureMgr.get_texture(f'assets/system/{filename}')

    @staticmethod
    def tilesets(filename: str) -> sfGraphics.Texture:
        """
        It will return a texture from assets/tilesets folder.

        Parameters:
        - filename: Name of texture.
        """

        return TextureMgr.get_texture(f'assets/tilesets/{filename}')

    @staticmethod
    def release_block(filename: str):
        """
        Release texture from assets/blocks folder.

        Parameters:
        - filename: Name of texture.
        """

        TextureMgr.release_texture(f'assets/blocks/{filename}')

    @staticmethod
    def release_character(filename: str):
        """
        Release texture from assets/characters folder.

        Parameters:
        - filename: Name of texture.
        """

        TextureMgr.release_texture(f'assets/characters/{filename}')

    @staticmethod
    def release_system(filename: str):
        """
        Release texture from assets/system folder.

        Parameters:
        - filename: Name of texture.
        """

        TextureMgr.release_texture(f'assets/system/{filename}')

    @staticmethod
    def release_tilesets(filename: str):
        """
        Release texture from assets/tilesets folder.

        Parameters:
        - filename: Name of texture.
        """

        TextureMgr.release_texture(f'assets/tilesets/{filename}')


class FontMgr:
    """
    Font manager class.

    It could manage all fonts.
    """

    _fonts: Dict[str, sfGraphics.Font] = {}

    @staticmethod
    def get_font(filename: str) -> sfGraphics.Font:
        """
        Get font from name.

        Parameters:
        - filename: File name of font.

        Returns:
        - The font from path.
        """

        if filename not in FontMgr._fonts:
            FontMgr._fonts[filename] = sfGraphics.Font()
            if not FontMgr._fonts[filename].open_from_file(f'assets/fonts/{filename}'):
                raise ValueError(f'Failed to load font from {filename}.')

        return FontMgr._fonts[filename]

    @staticmethod
    def has_font(filename: str) -> bool:
        """
        Check if font is loaded.

        Parameters:
        - filename: File name of font.

        Returns:
        - True if font is loaded, False otherwise.
        """

        return filename in FontMgr._fonts

    @staticmethod
    def release_font(filename: str):
        """
        Release font from name.

        Parameters:
        - filename: File name of font.
        """

        if filename in FontMgr._fonts:
            FontMgr._fonts.pop(filename)
        else:
            raise ValueError(f'Fail to release font from {filename}.')

    @staticmethod
    def clear():
        """
        Clear all fonts.
        """

        FontMgr._fonts.clear()

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

    @staticmethod
    def get_music(name: str) -> sfAudio.Music:
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

        return AudioMgr._music

    @staticmethod
    def get_sound(name: str) -> sfAudio.SoundBuffer:
        """
        Get sound from name.

        Parameters:
        - name: Name of sound.

        Returns:
        - The sound from path.
        """

        if name not in AudioMgr._sounds_cache:
            AudioMgr._sounds_cache[name] = sfAudio.SoundBuffer()
            if not AudioMgr._sounds_cache[name].load_from_file(f'assets/sounds/{name}'):
                raise ValueError(f'Fail to load sound from {name}.')

        return AudioMgr._sounds_cache[name]

    @staticmethod
    def get_voice(name: str) -> sfAudio.SoundBuffer:
        """
        Get voice from name.

        Parameters:
        - name: Name of voice.

        Returns:
        - The voice from path.
        """

        if name not in AudioMgr._voices_cache:
            AudioMgr._voices_cache[name] = sfAudio.SoundBuffer()
            if not AudioMgr._voices_cache[name].load_from_file(f'assets/voices/{name}'):
                raise ValueError(f'Fail to load voice from {name}.')

        return AudioMgr._voices_cache[name]

    @staticmethod
    def release_music(keyword: str):
        """
        Release music from name.
        """

        if keyword in AudioMgr._music:
            AudioMgr._music[keyword].stop()
            AudioMgr._music.pop(keyword)
        else:
            raise ValueError(f'Fail to release music from {keyword}.')


    @staticmethod
    def release_sound(name: str):
        """
        Release sound from name.

        Parameters:
        - name: Name of sound.
        """

        if name in AudioMgr._sounds_cache:
            AudioMgr._sounds_cache[name].stop()
            AudioMgr._sounds_cache.pop(name)
        else:
            raise ValueError(f'Fail to release sound from {name}.')

    @staticmethod
    def release_voice(name: str):
        """
        Release voice from name.

        Parameters:
        - name: Name of voice.
        """

        if name in AudioMgr._voices_cache:
            AudioMgr._voices_cache[name].stop()
            AudioMgr._voices_cache.pop(name)
        else:
            raise ValueError(f'Fail to release voice from {name}.')

    @staticmethod
    def play_music(keyword: str, para: Union[str, sfAudio.Music]):
        """
        Play music from name or music.

        Parameters:
        - keyword: Keyword of music, such as 'bgm' or 'bgs'.
        - para: Name of music or music object.
        """

        if isinstance(para, str):
            music = AudioMgr.get_music(para)
        elif isinstance(para, sfAudio.Music):
            music = para
        else:
            raise ValueError('Music not found.')

        if keyword in AudioMgr._music:
            AudioMgr._music[keyword].stop()

        AudioMgr._music[keyword] = music

        AudioMgr._music[keyword].play()

    @staticmethod
    def play_sound(para: Union[str, sfAudio.SoundBuffer]):
        """
        Play sound from name or sound buffer.

        Parameters:
        - para: Name of sound or sound buffer.
        """

        sound: sfAudio.Sound = None

        if isinstance(para, str):
            sound = sfAudio.Sound(AudioMgr.get_sound(para))
        elif isinstance(para, sfAudio.SoundBuffer):
            sound = sfAudio.Sound(para)

        if sound is None:
            raise ValueError('Sound not found.')

        AudioMgr._sound_list.append(sound)
        sound.play()

    @staticmethod
    def play_voice(para: Union[str, sfAudio.SoundBuffer]):
        """
        Play voice from name or sound buffer.

        Parameters:
        - para: Name of voice or sound buffer.
        """

        voice: sfAudio.Sound = None

        if isinstance(para, str):
            voice = sfAudio.Sound(AudioMgr.get_voice(para))
        elif isinstance(para, sfAudio.SoundBuffer):
            voice = sfAudio.Sound(para)

        if voice is None:
            raise ValueError('Voice not found.')

        AudioMgr._voice_list.append(voice)
        voice.play()

    @staticmethod
    def update():
        """
        Update all audios.
        """

        for sound in AudioMgr._sound_list[:]:
            if sound.get_status() == sfAudio.Sound.Status.Stopped:
                AudioMgr._sound_list.remove(sound)
        for voice in AudioMgr._voice_list[:]:
            if voice.get_status() == sfAudio.Sound.Status.Stopped:
                AudioMgr._voice_list.remove(voice)

    @staticmethod
    def clear():
        """
        Clear all audios.
        """

        for value in AudioMgr._sounds_cache.values():
            value.stop()
        AudioMgr._sounds_cache.clear()
        for value in AudioMgr._voices_cache.values():
            value.stop()
        AudioMgr._voices_cache.clear()
        for value in AudioMgr._music.values():
            value.stop()
        AudioMgr._music.clear()
        AudioMgr._sound_list.clear()
        AudioMgr._voice_list.clear()
