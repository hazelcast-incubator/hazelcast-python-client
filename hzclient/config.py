__author__ = 'jonathanbrodie'


class Config:
    def __init__(self):
        self._username=""
        self._password=""
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