import os
try:
    import cv2
except ImportError:
    try:
        import os, sys
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import cv2
    except ImportError:
        raise ImportError("Could not import cv2")

from typing import List
from . import sfSystem
from . import sfGraphics

class Video:
    def __init__(self, video_path: str, window_size: sfSystem.Vector2u):
        self.cap = cv2.VideoCapture(video_path)
        self.cap.set(cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY)
        self.window_size = window_size

        if not self.cap.isOpened():
            raise ValueError("Error opening video file")

        self.time_elapsed = 0
        self.target_frame_index = 0
        self._image: sfGraphics.Texture = None
        self._sprite: sfGraphics.Sprite = None

        self._frames: List[bytes] = []
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)

        self._image: sfGraphics.Texture = None
        self.sprite: sfGraphics.Sprite = None
        self.finished = False

    def _get_frame(self, delta_time: float) -> sfGraphics.Sprite:
        self.target_frame_index = int(self.time_elapsed * self.fps)

        if self.target_frame_index >= self.total_frames:
            return None

        bytes_data = self._frames[self.target_frame_index]
        self._image = sfGraphics.Texture()
        self._image.load_from_memory(bytes_data)
        size = self._image.get_size()
        self._sprite = sfGraphics.Sprite(self._image)
        self._sprite.set_scale(sfSystem.Vector2f(float(self.window_size.x) / size.x, float(self.window_size.y) / size.y))
        self.time_elapsed += delta_time
        return self._sprite

    def precache_frames(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (self.window_size.x, self.window_size.y))
            encode_params = [cv2.IMWRITE_PNG_COMPRESSION, 1]
            _, buffer = cv2.imencode('.jpg', frame, encode_params)
            fbytes = buffer.tobytes()
            self._frames.append(fbytes)

    def update(self, delta_time: float):
        if self.finished:
            return
        if len(self._frames) == 0:
            self.precache_frames()

        sprite = self._get_frame(delta_time)
        if sprite is not None:
            self.sprite = sprite
        else:
            self.finished = True

    def display(self, target: sfGraphics.RenderTarget):
        if self.sprite is not None:
            target.draw(self.sprite)

    def interrupt(self):
        self.finished = True

    def __del__(self):
        self.cap.release()

class VideoMgr:
    def __init__(self):
        self._videos: List[Video] = []

    def add_video(self, video: Video):
        video.precache_frames()
        self._videos.append(video)

    def remove_video(self, video: Video):
        self._videos.remove(video)

    def clear(self):
        self._videos.clear()

    def update(self, delta_time: float):
        for video in self._videos:
            video.update(delta_time)

    def display(self, target: sfGraphics.RenderTarget):
        for video in self._videos:
            video.display(target)
