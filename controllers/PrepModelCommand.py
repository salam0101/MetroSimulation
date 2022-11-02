# -*- coding: utf-8 -*-

from frameworck.patterns.command import SimpleCommand

from ApplicationFacade import ApplicationFacade
from models.StationProxy import StationProxy
from models.LoginProxy import LoginProxy
class PrepModelCommand(SimpleCommand):
    """
    Prepare the Model.
    """

    def execute(self, notification):
        self.facade.registerProxy(StationProxy(StationProxy.NAME))
        self.facade.registerProxy(LoginProxy(LoginProxy.NAME))






