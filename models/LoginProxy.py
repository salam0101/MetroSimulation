
from frameworck.patterns.proxy import Proxy


class LoginProxy(Proxy):
    NAME = 'LoginProxy'

    def __init__(self, name):
        super().__init__(name, [])

    def onRemove(self):

        pass

    def onRegister(self):
        pass

    def isLoginSuccess(self,name,passwd):
        print(name,passwd)
        return True
