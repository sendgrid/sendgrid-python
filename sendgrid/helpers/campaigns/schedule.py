from datetime import datetime, timedelta


class Schedule(object):
    """Get schedule-accepted Unix time stamp

    Python datetime.datetime or Unix timestamp are both accepted.
    If send_at is None, the value will be created with other inputs

    :param send_at: Unix timestamp
    :type send_at: int, datetime.datetime
    :param year: Scheduled year (current+)
    :type year: int
    :param month: Scheduled year [1..12]
    :type month: int
    :param day: Scheduled year [1..31]
    :type day: int
    :param hour: Scheduled hour [0..23]
    :type hour: int
    :param minute: Scheduled minute [0..59]
    :return: `send_at`=Unix timestamp dict
    :rtype: dict
    """
    def __init__(self, send_at=None, year=None, month=None,
                 day=None, hour=None, minute=None):

        def_dt = datetime.now() + timedelta(days=1)
        self._minute = 0
        self._hour = 0
        self._day = def_dt.day
        self._month = def_dt.month
        self._year = def_dt.year

        if send_at is not None:
            if isinstance(send_at, datetime):
                self._timestamp = self.convert_datetime(send_at)
            else:
                self._timestamp = int(send_at)
            self.parse_timestamp()

        if send_at is None:
            if year is not None:
                self._year = year
            if month is not None:
                self._month = month
            if day is not None:
                self._day = day
            if hour is not None:
                self._hour = hour
            if minute is not None:
                self._minute = minute
            self._timestamp = self.convert_datetime(
                datetime(self.year, self.month, self.day, self.hour, self.minute)
            )

    @staticmethod
    def convert_datetime(dt):
        """Converts a datetime to Unix time stamp

        :param dt: Datetime to parse
        :type dt: datetime.datetime
        :return: Unix timestamp
        :rtype: int
        """
        t_delta = dt - datetime(1970, 1, 1)
        return t_delta.seconds + t_delta.days * 86400

    def get(self):
        return {"send_at": self._timestamp}

    def parse_timestamp(self):
        """Parses the Schedule object's timestamp into year, month, etc.

        :return: Parsed datetime object
        :rtype: datetime.datetime
        """
        dt = datetime(1970, 1, 1) + timedelta(seconds=self._timestamp)
        self._year = dt.year
        self._month = dt.month
        self._day = dt.day
        self._hour = dt.hour
        self._minute = dt.minute
        return dt

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = int(value)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value
