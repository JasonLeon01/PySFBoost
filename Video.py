try:
    import cv2
except ImportError:
    try:
        import os, sys
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import cv2
    except ImportError:
        raise ImportError("Could not import cv2")
from . import sfSystem
from . import sfGraphics

class Player:
    def __init__(self, video_path: str, window_size: sfSystem.Vector2u):
        self.cap = cv2.VideoCapture(video_path)
        self.window_size = window_size

        if not self.cap.isOpened():
            raise ValueError("Error opening video file")

        self.time_elapsed = 0
        self.target_frame_index = 0
        self._image: sfGraphics.Texture = None
        self._sprite: sfGraphics.Sprite = None

        self._frames = []
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self._preload_frames()

    def get_frame(self, delta_time: float) -> sfGraphics.Sprite:
        self.target_frame_index = int(self.time_elapsed * self.fps)

        if self.target_frame_index >= self.total_frames:
            return None

        self._image = self._frames[self.target_frame_index]
        size = self._image.get_size()
        self._sprite = sfGraphics.Sprite(self._image)
        self._sprite.set_scale(sfSystem.Vector2f(float(self.window_size.x) / size.x, float(self.window_size.y) / size.y))
        self.time_elapsed += delta_time
        return self._sprite

    def _preload_frames(self):
        now_frame_index = 0
        while True:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, now_frame_index)
            ret, frame = self.cap.read()
            if not ret or now_frame_index >= self.total_frames:
                break
            _, buffer = cv2.imencode('.png', frame)
            fbytes = buffer.tobytes()
            image = sfGraphics.Texture()
            image.load_from_memory(fbytes)
            self._frames.append(image)
            now_frame_index += 1

    def __del__(self):
        self.cap.release()