
from frameworck.patterns.mediator import Mediator
from ApplicationFacade import ApplicationFacade
from models.StationProxy import StationProxy
class MainWindowMediator(Mediator):
    NAME = 'FormMediator'

    def __init__(self, name, viewComponent):

        super().__init__(name, viewComponent)
        self.timer=viewComponent.timer
        self.label = viewComponent.label
        self.ticketBtn = viewComponent.ticketBtn
        self.ticketBtn.triggered.connect(self.BuyTicket)
        # 定义菜单open打开图片
        self.Dotimer=None



    def BuyTicket(self):
        proxy=self.facade.retrieveProxy(StationProxy.NAME)
        stationName= proxy.getAllStationName()
        self.sendNotification(ApplicationFacade.BUYTICKET,stationName)
    def listNotificationInterests(self):
        lis = [ApplicationFacade.DISPLAY,ApplicationFacade.UPDATE,ApplicationFacade.SELECTED]
        return lis

    def handleNotification(self, notification):
        name=notification.getName()
        if ApplicationFacade.DISPLAY==name:
            proxy=self.facade.retrieveProxy(StationProxy.NAME)
            self.Dotimer=proxy.update_label
            self.timer.timeout.connect(self.Dotimer)
            self.viewComponent.show()
            login=notification.getBody()
            login.close()
            self.timer.start(50)
        elif ApplicationFacade.UPDATE==name:
             pix=notification.getBody()
             self.label.setPixmap(pix)

        elif ApplicationFacade.SELECTED==name:
            proxy = self.facade.retrieveProxy(StationProxy.NAME)
            src,dst=notification.getBody()[0],notification.getBody()[1]
            if proxy.FindRoad(src,dst):
                self.sendNotification(ApplicationFacade.SUCCESS)
            else:
                self.sendNotification(ApplicationFacade.FAIL)


