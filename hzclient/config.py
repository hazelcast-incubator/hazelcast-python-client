__author__ = 'jonathanbrodie'


class Config:
    def __init__(self):
        self._username=""
        self._password=""
        self._targethost="127.0.0.1"
        self._port=5701
        self.ssl=False
        #any other configurations that need to be used

    def set_username(self,username):
        self._username=username
    def set_password(self,password):
        self._password=password
    def get_username(self):
        return self._username
    def get_password(self):
        return self._password

    def sethost(self,host):
        self._targethost=host
    def setport(self,newport):
        self._port=newport
    def gethost(self):
        return self._targethost
    def getport(self):
        return self._port