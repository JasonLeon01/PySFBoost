have_require = True
from .sfSystem import *
from .sfGraphics import *
from .Time import *

try:
    import cv2
    import ffmpeg
    import numpy as np
    import sounddevice as sd
except ImportError:
    have_require = False

class Video:
    def __init__(self, video_path: str, window: RenderWindow):
        if not have_require:
            print("Require not found. Video playback will not be available.")
            return

        self.cap = cv2.VideoCapture(video_path)
        self.cap.set(cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY)

        out, _ = (
            ffmpeg.input(video_path)
            .output("-", format="f32le", acodec="pcm_f32le", ac=2, ar=44100)
            .run(capture_stdout=True, quiet=True)
        )

        self._audio_array = np.frombuffer(out, dtype=np.float32).reshape(-1, 2)

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
        sd.play(self._audio_array)
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

    def __del__(self):
        self.cap.release()

