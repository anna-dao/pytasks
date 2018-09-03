# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)

class IpAddress:
    def __init__(self, ip_address):
        self.ip_address_name = ip_address

    @staticmethod
    def print_ip_addresses(list_of_ipaddresses):
        print('IP-ADDRESSES:')
        for ip_address in list_of_ipaddresses:
            print('IP address: ', ip_address.ip_address_name, end='\n')
        print()

    @staticmethod
    def print_ip_addresses_fully(list_of_ipaddresses):
        dot = '.'
        print('FULL IP ADDRESSES: ')
        for ip_address in list_of_ipaddresses:
            ip_name = ip_address.ip_address_name
            ip_name_splitted = ip_name.split(dot)
            ip_name_reversed = ip_name_splitted[-1], ip_name_splitted[-2], ip_name_splitted[-3], ip_name_splitted[-4]
            ip_address_reversed_joined = dot.join(ip_name_reversed)
            print('IP address: ', ip_name, '===>', ip_address_reversed_joined, end='\n')
        print()

    @staticmethod
    def print_ip_addresses_wo_octets(list_of_ipaddresses):
        dot = '.'
        print('IP-ADDRESSES WITHOUT FIRST OCTETS:')
        for ip_address in list_of_ipaddresses:
            ip_name = ip_address.ip_address_name
            ip_name_splitted = ip_name.split(dot)
            ip_address_wo_octets = ip_name_splitted[1:]
            print('IP address: ', ip_name, '===>', dot.join(ip_address_wo_octets))
        print()

    @staticmethod
    def print_ip_addresses_w_last(list_of_ipaddresses):
        dot = '.'
        print('IP-ADDRESSES WITH LAST OCTET:')
        for ip_address in list_of_ipaddresses:
            ip_name = ip_address.ip_address_name
            ip_name_splitted = ip_name.split(dot)
            ip_address_w_last = ip_name_splitted[-1]
            print('IP address: ', ip_name, '===>', ip_address_w_last)
        print()


ip_adress1 = IpAddress('1.40.215.65')
ip_adress2 = IpAddress('5.9.158.755.7')
ip_adress3 = IpAddress('3.129.64.105')
ip_adress4 = IpAddress('4.10223.129.64.1032')
ip_adress5 = IpAddress('9.64.10123.129.6')
ip_adress6 = IpAddress('3.121.214.13423.12')
ip_adress7 = IpAddress('8.1723.31.239.172')
ip_adress8 = IpAddress('8.42.71.25412.13')
ip_adress9 = IpAddress('6.1625.199.130.127')
ip_adress10 = IpAddress('6.1.1295.196.6')
list_of_ipadresses = [ip_adress1, ip_adress2, ip_adress3, ip_adress4, ip_adress5, ip_adress6, ip_adress7, ip_adress8, ip_adress9,ip_adress10]

IpAddress.print_ip_addresses(list_of_ipadresses)
IpAddress.print_ip_addresses_fully(list_of_ipadresses)
IpAddress.print_ip_addresses_wo_octets(list_of_ipadresses)
IpAddress.print_ip_addresses_w_last(list_of_ipadresses)