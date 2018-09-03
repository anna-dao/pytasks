# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class Switch:
    def __init__(self, unit_name=None, mac_address=None, ip_address=None, login=None, password=None):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    def print_info(self):
        print('_______________________________________________________________________________________________________')
        print('Unit Name: ', self._unit_name)
        print('Mac Address: ', self._mac_address)
        print('Ip Address: ', self._ip_address)
        print('Login: ', self._login)
        print('Password: ', self._password)
        print('______________________________________________________________________________________________________')

    @property
    def unit_name(self):
        return self._unit_name
    @unit_name.setter
    def unit_name(self, unit_name):
        self._unit_name = unit_name
    @unit_name.getter
    def unit_name(self):
        return self._unit_name

    @property
    def mac_address(self):
        return self._mac_address
    @mac_address.setter
    def mac_address(self, mac_address):
        self._mac_address = mac_address
    @mac_address.getter
    def mac_address(self):
        return self._mac_address

    @property
    def ip_address(self):
        return self._ip_address
    @ip_address.setter
    def ip_address(self, ip_address):
        self._ip_address = ip_address
    @ip_address.getter
    def ip_address(self):
        return self._ip_address

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, login):
        self._login = login
    @login.getter
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password
    @password.getter
    def password(self):
        return self._password

first_switch = Switch('CA18DET', 'None', '6.1625.199.130.127', 'login', 'qwerty')
first_switch.print_info()
first_switch.password = 'password'
first_switch.print_info()

