
from frameworck.patterns.mediator import Mediator
from ApplicationFacade import ApplicationFacade
from models.StationProxy import StationProxy
class TicketMediator(Mediator):
    NAME = 'TicketMediator'

    def __init__(self, name, viewComponent):

        super().__init__(name, viewComponent)
        self.buyBtn = viewComponent.buyBtn
        self.src = viewComponent.src
        self.dst = viewComponent.dst
        self.buyBtn.clicked.connect(self.BuyClicked)


    def BuyClicked(self):
        src=self.src.currentText()
        dst=self.dst.currentText()
        lis=[src,dst]
        self.sendNotification(ApplicationFacade.SELECTED,lis)

    def listNotificationInterests(self):
        lis = [ApplicationFacade.BUYTICKET,ApplicationFacade.SUCCESS,ApplicationFacade.FAIL]
        return lis

    def handleNotification(self, notification):
        if ApplicationFacade.BUYTICKET==notification.getName():
            self.viewComponent.show()
            self.dst.addItems(notification.getBody())
            self.src.addItems(notification.getBody())
        elif ApplicationFacade.SUCCESS==notification.getName():
            proxy = self.facade.retrieveProxy(StationProxy.NAME)
            proxy.show_message(self.viewComponent,"购票成功")
            self.viewComponent.close()
        elif ApplicationFacade.FAIL==notification.getName():
            proxy = self.facade.retrieveProxy(StationProxy.NAME)
            proxy.show_message(self.viewComponent,"购票失败")



