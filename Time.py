from .sfSystem import *

class TimeMgr:
    """
    Time manager class.

    You can get the current time, delta time, ... from this class.
    """

    _clock = Clock()
    _last_elapsed_time = Time.Zero()
    _delta_time = Time.Zero()

    @staticmethod
    def init():
        """
        Initialize the time manager.
        """

        TimeMgr._clock.start()
        TimeMgr.update()

    @staticmethod
    def get_current_time() -> Time:
        """
        Get the current time.

        Returns:
        - Current time.
        """

        return TimeMgr._last_elapsed_time

    @staticmethod
    def get_delta_time() -> Time:
        """
        Get the delta time.

        Returns:
        - Delta time.
        """

        return Time.FromSeconds(TimeMgr._delta_time)

    @staticmethod
    def update():
        """
        Update the time manager.
        """

        last_time = TimeMgr._last_elapsed_time
        current_time = TimeMgr._clock.get_elapsed_time()
        TimeMgr._last_elapsed_time = current_time
        TimeMgr._delta_time = current_time - last_time
