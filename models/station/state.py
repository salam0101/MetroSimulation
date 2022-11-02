import abc

from models.station.common import *
class State:
    pass


class Traffic(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name
        self.state = None

    @abc.abstractmethod
    def ChangeState(self):
        """

        :return:
        """

    def getState(self):
        return self.state

    def setState(self, state: State):
        self.state = state


class State(metaclass=abc.ABCMeta):
    def __init__(self, type):
        self.type = type

    @abc.abstractmethod
    def ChangeState(self, traffic: Traffic):
        pass


class RunningState(State):

    def __init__(self, name):
        super().__init__(name)

    def ChangeState(self, traffic: Traffic):
        traffic.setState(OpenningState(OPEN))


class OpenningState(State):

    def __init__(self, name):
        super().__init__(name)

    def ChangeState(self, traffic: Traffic):
        traffic.setState(CloseingState(CLOSE))


class CloseingState(State):

    def __init__(self, name):
        super().__init__(name)

    def ChangeState(self, traffic: Traffic):
        traffic.setState(RunningState(RUN))






