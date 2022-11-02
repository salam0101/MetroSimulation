from frameworck.patterns.facade import Facade


class ApplicationFacade(Facade):
    LOGIN='login'
    STARTUP = 'startup'
    DISPLAY='display'
    UPDATE='update'
    BUYTICKET='buyTicket'
    SELECTED='selected'
    SUCCESS="success"
    FAIL='fail'

    @staticmethod
    def getInstance():
        return ApplicationFacade()

    def startup(self, args):
        from controllers.StartupCommand import StartUpCommand
        self.registerCommand(self.STARTUP,StartUpCommand)
        self.sendNotification(ApplicationFacade.STARTUP,args)


