
from frameworck.patterns.mediator import Mediator
from ApplicationFacade import ApplicationFacade
from models.LoginProxy import LoginProxy
class LoginMediator(Mediator):
    NAME = 'LoginMediator'

    def __init__(self, name, viewComponent):

        super().__init__(name, viewComponent)
        self.button = viewComponent.button
        self.nameEdit = viewComponent.nameEdit
        self.passwdEdit = viewComponent.passwdEdit
        self.button.clicked.connect(self.Login)



    def listNotificationInterests(self):
        lis = [ApplicationFacade.LOGIN]
        return lis
    def Login(self):
        name=self.nameEdit.text()
        passwd=self.passwdEdit.text()
        proxy=self.facade.retrieveProxy(LoginProxy.NAME)
        if proxy.isLoginSuccess(name,passwd):
            self.sendNotification(ApplicationFacade.DISPLAY,self.viewComponent)


    def handleNotification(self, notification):
        self.viewComponent.show()
