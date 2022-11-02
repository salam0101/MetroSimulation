import sys
from PyQt5.QtWidgets import QApplication
from ApplicationFacade import ApplicationFacade
from views.components.ui.mainwindow import mainWindow
from views.components.ui.ticketwindow import TicketWindow
from views.components.ui.login import LoginWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = mainWindow()
    ticketWindow = TicketWindow()
    loginWindow = LoginWidget()
    facade = ApplicationFacade.getInstance()
    facade.startup([loginWindow, ticketWindow, mainWindow])
    exit(app.exec_())
