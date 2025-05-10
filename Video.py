have_require = True
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from moviepy import VideoFileClip, AudioFileClip
    import numpy as np
except ImportError:
    have_require = False

import time
import threading
from . import sfSystem
from . import sfGraphics

class Video:
    def __init__(self, video_path: str, window: sfGraphics.RenderWindow):
        if not have_require:
            print("moviepy not found. Video playback will not be available.")
            return

        self._clip = VideoFileClip(video_path)
        self._window = window

        self._texture: sfGraphics.Texture = None
        self._sprite: sfGraphics.Sprite = None
        self._frame_gen = self._clip.iter_frames(fps=30, dtype='uint8')
        self._frame_duration = 1.0 / 24

        self._audio = self._clip.audio

        self._clock = sfSystem.Clock()

    def _play_audio(self):
        if self._audio is not None:
            self._audio.audiopreview()

    def play(self):
        audio_thread = threading.Thread(target=self._play_audio)
        audio_thread.start()
        for frame in self._frame_gen:
            if not self._window.is_open():
                break
            while True:
                event = self._window.poll_event()
                if event is None:
                    break
                if event.isClosed():
                    self._window.close()
                    break

            h, w, _ = frame.shape
            if self._texture is None:
                self._texture = sfGraphics.Texture(sfSystem.Vector2u(w, h))
                self._sprite = sfGraphics.Sprite(self._texture)
            rgba = np.dstack((frame, np.full((h, w), 255, dtype='uint8')))
            self._texture.update(rgba)
            scale = min(self._window.get_size().x / self._texture.get_size().x, self._window.get_size().y / self._texture.get_size().y)
            self._sprite.set_scale(sfSystem.Vector2f(scale, scale))
            self._sprite.set_position(sfSystem.Vector2f((self._window.get_size().x - self._texture.get_size().x * scale) / 2, (self._window.get_size().y - self._texture.get_size().y * scale) / 2))
            self._window.clear(sfGraphics.Color.transparent())
            self._window.draw(self._sprite)
            self._window.display()

            elapsed = self._clock.get_elapsed_time().as_seconds()
            to_sleep = self._frame_duration - elapsed
            if to_sleep > 0:
                time.sleep(to_sleep)
            print(to_sleep)
            self._clock.restart()
        audio_thread.join()
