from frameworck.patterns.command import MacroCommand
from controllers.PrepViewCommand import PrepViewCommand
from controllers.PrepModelCommand import PrepModelCommand


class StartUpCommand(MacroCommand):
    def initializeMacroCommand(self):


        self.addSubCommand(PrepModelCommand)
        self.addSubCommand(PrepViewCommand)
