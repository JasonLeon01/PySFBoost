have_require = True
from io import BytesIO
from .sfSystem import *
from .sfGraphics import *
from .sfAudio import *
from .Time import *

try:
    import cv2
    import av
except ImportError as e:
    have_require = False

class Video:
    def __init__(self, video_path: str, window: RenderWindow):
        if not have_require:
            print("Require not found. Video playback will not be available.")
            return

        self.cap = cv2.VideoCapture(video_path)
        self.cap.set(cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY)

        try:
            audio_data, sample_rate, channels = self._extract_audio_with_av(video_path)
            self._sb = SoundBuffer()
            self._sb.load_from_memory(audio_data)
            self._sound = Sound(self._sb)
        except Exception as e:
            print(f"Failed to extract audio: {e}")
            self._sound = None

        self._window = window

        if not self.cap.isOpened():
            raise ValueError("Error opening video file")

        self.target_frame_index = 0
        self._image: Texture = None
        self._sprite: Sprite = None

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        self._image: Texture = None
        self._sprite: Sprite = None
        self.finished = False

    def _extract_audio_with_av(self, video_path):
        container = av.open(video_path)

        audio_stream = next((s for s in container.streams if s.type == 'audio'), None)
        if not audio_stream:
            raise ValueError("No audio stream found in the video")

        sample_rate = audio_stream.codec_context.sample_rate
        channels = audio_stream.codec_context.channels

        output = BytesIO()

        output_container = av.open(output, 'w', format='wav')

        output_stream = output_container.add_stream(
            codec_name='pcm_s16le',
            rate=sample_rate,
            options={'ac': str(channels)}
        )

        layout = 'mono' if channels == 1 else 'stereo'

        resampler = av.AudioResampler(
            format='s16',
            layout=layout,
            rate=sample_rate
        )

        for packet in container.demux(audio_stream):
            for frame in packet.decode():
                resampled_frames = resampler.resample(frame)
                for resampled_frame in resampled_frames:
                    for p in output_stream.encode(resampled_frame):
                        output_container.mux(p)

        for p in output_stream.encode(None):
            output_container.mux(p)

        output_container.close()

        wav_data = output.getvalue()
        output.close()

        return wav_data, sample_rate, channels

    def _get_frame(self) -> None:
        if not have_require:
            self._sprite = None
            return None

        ret, frame = self.cap.read()
        if not ret:
            self._sprite = None
            return None

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
        return self.cap.get(cv2.CAP_PROP_POS_FRAMES) - 1

    def _update(self):
        expected_frame = int(self._sound.get_playing_offset().as_seconds() * self.fps)
        while self.target_frame_index is not None and (expected_frame > self.target_frame_index or (expected_frame == 0 and self._sprite is None)):
            self.target_frame_index = self._get_frame()
        if self._sprite is None:
            self.finished = True

    def play(self):
        if not have_require:
            return
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
            self._window.clear(Color.transparent())
            self._update()
            if self._sprite is not None:
                self._window.draw(self._sprite)
            self._window.display()
            if self.finished:
                break
        self._sound.stop()

    def __del__(self):
        self.cap.release()
