# -*- coding: utf-8 -*-

from frameworck.patterns.command import SimpleCommand
from views.LoginMediator import LoginMediator
from  views.MainWindowMediator import MainWindowMediator
from ApplicationFacade import ApplicationFacade
from views.ticketMediator import TicketMediator

class PrepViewCommand(SimpleCommand):
    """
    Prepare the View.

    Get the view Components for the Mediators from the app,
    a reference to which was passed on the original startup notification.
    """

    def execute(self, notification):
        lis=notification.getBody()

        self.facade.registerMediator(LoginMediator(LoginMediator.NAME, lis[0]))
        self.facade.registerMediator(TicketMediator(TicketMediator.NAME,lis[1]))
        self.facade.registerMediator(MainWindowMediator(MainWindowMediator.NAME, lis[2]))
        self.facade.sendNotification(ApplicationFacade.LOGIN)



