from . import sfSystem

class TimeMgr:
    """
    Time manager class.

    You can get the current time, delta time, ... from this class.
    """

    _clock = sfSystem.Clock()
    _last_elapsed_time = sfSystem.Time.Zero()
    _delta_time = sfSystem.Time.Zero()

    @staticmethod
    def init():
        """
        Initialize the time manager.
        """

        TimeMgr._clock.start()
        TimeMgr.update()

    @staticmethod
    def get_current_time() -> sfSystem.Time:
        """
        Get the current time.

        Returns:
        - Current time.
        """

        return TimeMgr._last_elapsed_time

    @staticmethod
    def get_delta_time() -> sfSystem.Time:
        """
        Get the delta time.

        Returns:
        - Delta time.
        """

        return sfSystem.Time.FromSeconds(TimeMgr._delta_time)

    @staticmethod
    def update():
        """
        Update the time manager.
        """

        last_time = TimeMgr._last_elapsed_time
        current_time = TimeMgr._clock.get_elapsed_time()
        TimeMgr._last_elapsed_time = current_time
        TimeMgr._delta_time = current_time - last_time
