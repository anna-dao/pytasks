# Создать класс для представления информации о времени.
# Ваш класс должен иметь  возможности установки времени и изменения его отдельных полей (час, минута, секунда) с
# проверкой допустимости вводимых значений. В случае недопустимых значений полей выбрасываются исключения.
#  Создать методы изменения времени на заданное количество часов, минут и секунд.

class Time:
    def __init__(self, hour=0, min=0, sec=0):
        self._hour = hour
        self._min = min
        self._sec = sec

    def print_info(self):
        print('_______________________________________________________________________________________________________')
        print('Hour: ', self._hour)
        print('Minutes: ', self._min)
        print('Seconds: ', self._sec)
        print('_______________________________________________________________________________________________________')

    def change_time(self, hour=0, min=0, sec=0):
        self._hour += hour
        self._min += min
        self._sec += sec

    @property
    def hour(self):
        return self._hour
    @hour.setter
    def hour(self, hour):
        if hour > 24 or hour < 0:
            raise ValueError('Value of hour must be less than 24 and more than 0')
        else:
            self._hour = hour

    @property
    def min(self):
        return self._min
    @min.setter
    def min(self, min):
        if min > 60 or min < 0:
            raise ValueError('Value of min must be less than 60 and more than 0')
        else:
            self._min = min

    @property
    def sec(self):
        return self._sec
    @sec.setter
    def sec(self, sec):
        if sec > 60 or sec < 0:
            raise ValueError('Value of sec must be less than 60 and more than 0')
        else:
            self._sec = sec

firsthour = Time(12, 35, 47)
firsthour.print_info()
firsthour.change_time(5, 1, 6)
firsthour.print_info()