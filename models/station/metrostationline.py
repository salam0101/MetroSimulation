from typing import List
from models.station.common import *
from models.station.state import *
class Station:
    all_stations = {}

    def __init__(self, name: str, position, lines: List['Line'] = None):
        if lines is None:
            lines = []
        self.name = name
        self.position = position
        self.lines = []
        for line in lines:
            self.add_line(line)

    def add_line(self, line: 'Line'):
        if line not in self.lines:
            self.lines.append(line)
        line.add_station(self)

    def rescale(self, initial_minX, initial_minY, initial_maxX, initial_maxY, final_minX, final_minY, final_maxX,
                final_maxY, inplace=True):
        X, Y = self.position
        new_x = (X - initial_minX) * (final_maxX - final_minX) / (
                initial_maxX - initial_minX) + final_minX
        new_y = (Y - initial_minY) * (final_maxY - final_minY) / (
                initial_maxY - initial_minY) + final_minY
        if inplace:
            self.position = (new_x, new_y)

        else:
            return self.__class__(name=self.name, position=(new_x, new_y), lines=self.lines)




class Line:
    all_lines = {}

    def __init__(self, lineNum, stations=None):
        self.lineNum = lineNum
        if stations is None:
            stations = []
        self.stations = stations

        self.color = COLORS[self.lineNum]

    def add_station(self, station: Station):
        if station not in self.stations:
            self.stations.append(station)

    def __repr__(self):
        return f"Line(Number: {self.lineNum},station_name: {[station.name for station in self.stations]},num={len(self.stations)}"
def find_bounding_rect(all_stations: List[Station]):
    min_x = all_stations[0].position[0]
    min_y = all_stations[0].position[1]
    max_x = all_stations[0].position[0]
    max_y = all_stations[0].position[1]
    for station in all_stations:
        pos = station.position
        min_x = min(min_x, pos[0])
        min_y = min(min_y, pos[1])
        max_x = max(max_x, pos[0])
        max_y = max(max_y, pos[1])
    return min_x, min_y, max_x, max_y

class Metro(Traffic):
    def __init__(self, line, name: str):
        super().__init__(name)
        self.time = 0
        self.line = line
        self.stateType = RUN
        self.At = 0
        self.next = self.At + 1
        self.step = 1
        self.MaxStep = 100
        self.StartStation = line.stations[self.At]
        self.EndStation = line.stations[-1]
        self.pos = self.StartStation.position
        self.stations_queue = line.stations.copy()
        self.direction = getDirection(self.line.stations[self.At].position, self.line.stations[self.next].position)
        self.speed = 0.5
        self.goback = False
        self.state = CloseingState(CLOSE)

    def Direction(self):
        if self.next == len(self.line.stations):
            dir = getDirection(self.line.stations[self.At - 1].position, self.line.stations[self.next - 1].position)
            # self.next=self.At
            # self.At-=1
            self.goback = True
            return dir
        elif self.next == -1:
            self.pos = self.StartStation.position
            self.At = 0
            self.next = self.At + 1
            dir = getDirection(self.line.stations[self.At].position, self.line.stations[self.next].position)
            self.goback = False
            return dir
        else:
            try:
                dir = getDirection(self.line.stations[self.At].position, self.line.stations[self.next].position)
            except:
                print("dd")
        return dir

    def move(self):
        if (self.step / self.MaxStep) == 0.1:
            self.ChangeState()
        if (self.step / self.MaxStep) == 0.9:
            self.ChangeState()

        if self.step == self.MaxStep:
            self.ChangeState()
            if self.goback is False:
                self.At += 1
                self.next += 1
            else:
                self.At -= 1
                self.next = self.At - 1
            self.pos = self.line.stations[self.At].position
            self.step = 1
        else:
            if self.next == -1 or self.next == len(self.line.stations):
                if self.goback is False:
                    self.At += 1
                    self.next += 1
                else:
                    self.At -= 1
                    self.next = self.At - 1
                self.pos = self.line.stations[self.At].position
                self.step = 1
            else:
                self.pos = (
                    (self.line.stations[self.At].position[0] * (self.MaxStep - self.step) +
                     self.line.stations[self.next].position[
                         0] * self.step) / self.MaxStep,
                    (self.line.stations[self.At].position[1] * (self.MaxStep - self.step) +
                     self.line.stations[self.next].position[
                         1] * self.step) / self.MaxStep)
                self.step += 1

    def rescale(self, initial_minX, initial_minY, initial_maxX, initial_maxY, final_minX, final_minY, final_maxX,
                final_maxY, inplace=True):
        X, Y = self.pos
        new_x = (X - initial_minX) * (final_maxX - final_minX) / (
                initial_maxX - initial_minX) + final_minX
        new_y = (Y - initial_minY) * (final_maxY - final_minY) / (
                initial_maxY - initial_minY) + final_minY
        if inplace:
            self.pos = (new_x, new_y)

        else:
            return self.__class__(name=self.name, line=self.line)

    def ChangeState(self):
        self.state.ChangeState(self)

