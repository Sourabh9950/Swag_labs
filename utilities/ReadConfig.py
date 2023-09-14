import configparser

config = configparser.RawConfigParser()
filepath = "C:\\Users\\LENOVO\\PycharmProjects\\pythonProject_swaglabs\\Configuration\\config.ini"
config.read(filepath)



class Readconfig:
    @staticmethod
    def GetUsername():
        username = config.get('common data','username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data', 'password')
        return password

