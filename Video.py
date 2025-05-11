have_require = True
from .sfSystem import *
from .sfGraphics import *
from .sfAudio import *
from .Time import *

try:
    import cv2
    import ffmpeg
    import numpy as np
except ImportError:
    have_require = False

class Video:
    def __init__(self, video_path: str, window: RenderWindow):
        if not have_require:
            print("Require not found. Video playback will not be available.")
            return

        self.cap = cv2.VideoCapture(video_path)
        self.cap.set(cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY)

        sr, ch = self._get_audio_info(video_path)

        out, _ = (
            ffmpeg
            .input(video_path)
            .output('pipe:', format='wav', acodec='pcm_s16le', ac=ch, ar=sr)
            .run(capture_stdout=True, capture_stderr=True)
        )

        audio = np.frombuffer(out, np.int16).tobytes()
        self._sb = SoundBuffer()
        self._sb.load_from_memory(audio)
        self._sound = Sound(self._sb)

        self._window = window

        if not self.cap.isOpened():
            raise ValueError("Error opening video file")

        self.time_elapsed = 0
        self.target_frame_index = 0
        self._image: Texture = None
        self._sprite: Sprite = None

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        self._image: Texture = None
        self._sprite: Sprite = None
        self.finished = False

    def _get_audio_info(self, path):
        probe = ffmpeg.probe(path)
        audio_streams = [s for s in probe['streams'] if s['codec_type'] == 'audio']
        if not audio_streams:
            raise ValueError("No audio stream found")

        audio_stream = audio_streams[0]
        sample_rate = int(audio_stream['sample_rate'])
        channels = int(audio_stream['channels'])
        return sample_rate, channels

    def _get_frame(self) -> None:
        if not have_require:
            self._sprite = None
            return

        ret, frame = self.cap.read()
        if not ret:
            self._sprite = None
            return

        frame_data = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        if self._image is None:
            h, w, _ = frame_data.shape
            self._image = Texture(Vector2u(w, h))
            self._sprite = Sprite(self._image)
            scale = min(float(self._window.get_size().x) / w, float(self._window.get_size().y) / h)
            self._sprite.set_scale(Vector2f(scale, scale))
            self._sprite.set_origin((self._image.get_size() / 2).to_float())
            self._sprite.set_position((self._window.get_size() / 2).to_float())
        self._image.update(frame_data)

    def _update(self, delta_time: float):
        self.time_elapsed += delta_time
        expected_frame = int(self.time_elapsed * self.fps)
        if expected_frame > self.target_frame_index or (expected_frame == 0 and self._sprite is None):
            self.target_frame_index = expected_frame
            self._get_frame()
        if self._sprite is None:
            self.finished = True

    def play(self):
        self._sound.play()
        while self._window.is_open():
            while True:
                event = self._window.poll_event()
                if event is None:
                    break
                if event.isClosed():
                    self._window.close()
                    break
            TimeMgr.update()
            delta_time = TimeMgr.get_delta_time().as_seconds()
            print(1/delta_time)
            self._window.clear(Color.transparent())
            self._update(delta_time)
            if self._sprite is not None:
                self._window.draw(self._sprite)
            self._window.display()
            if self.finished:
                break
        self._sound.stop()

    def __del__(self):
        self.cap.release()

