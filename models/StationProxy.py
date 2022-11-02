from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from models.station.metrostationline import *
from models.station.metronet import *
from frameworck.patterns.proxy import Proxy
from models.station.common import *
from ApplicationFacade import ApplicationFacade
class StationProxy(Proxy):
    NAME = 'StationProxy'

    def __init__(self, name):
        super().__init__(name, [])
        self.TrainImagemap = {UP: Image.open('views/components/ui/metroImage/up.png').resize((40, 40)),
                              DOWN: Image.open('views/components/ui/metroImage/down.png').resize((40, 40)),
                              LEFT: Image.open('views/components/ui/metroImage/left.png').resize((40, 40)),
                              RIGHT: Image.open('views/components/ui/metroImage/right.png').resize((40, 40)),
                              RIGHTDOWN: Image.open('views/components/ui/metroImage/downright.png').resize((40, 40)),
                              LEFTUP: Image.open('views/components/ui/metroImage/upleft.png').resize((40, 40)),
                              DOWNLEFT: Image.open('views/components/ui/metroImage/downleft.png').resize((40, 40)),
                              UPRIGHT: Image.open('views/components/ui/metroImage/upright.png').resize((40, 40)),
                              }
        self.map = Image.open('views/components/resources/image/img.jpg').resize((40, 40)).convert("RGBA")
        self.Myfont = ImageFont.truetype('views/components/resources/image/micro.ttf', 15)
        self.Myfont2 = ImageFont.truetype('views/components/resources/image/micro.ttf', 20)
        self.Myfont3 = ImageFont.truetype('views/components/resources/image/micro.ttf', 50)
        self.all_metro = []
        self.init()
    def init(self):
        for line_number, station_name, station_position in metronet:
            if line_number not in Line.all_lines:
                current_line = Line(line_number)
                Line.all_lines.update({line_number: current_line})
            else:
                current_line = Line.all_lines[line_number]
            if station_name in Station.all_stations:
                Station.all_stations[station_name].add_line(current_line)
            else:
                Station.all_stations.update(
                    {station_name: Station(station_name, station_position, lines=[current_line])})

        minX, minY, maxX, maxY = find_bounding_rect(list(Station.all_stations.values()))

        for _, station in Station.all_stations.items():
            station.rescale(0, 0, maxX + 100, maxY + 100, 0, 0, 1000, 1000)
            # station.rescale(0, 0, 1200, 1200, 0, 0, 1000,1000)
        for line_number, name in metro:
            new_metro = Metro(Line.all_lines[line_number], name)
            self.all_metro.append(new_metro)
    def getAllStationName(self):
        return Station.all_stations.keys()
    def FindRoad(self, src, dst):
        if src == dst:
            return False
        return True
    def getImage(self):
        img = Image.new('RGB', (1000, 1000), 'white')
        draw = ImageDraw.Draw(img)
        draw.text(tuple((400, 15)), text="地铁运营系统", font=self.Myfont3, fill="green")
        for station in Station.all_stations.values():
            x, y = int(station.position[0]), int(station.position[1])
            img.paste(self.map, tuple((x - 20, y - 20)))
        for line_number in Line.all_lines:
            if line_number == 0:
                continue
            xy = [tuple(station.position) for station in Line.all_lines[line_number].stations]
            color = COLORS[line_number]
            draw.line(xy, fill=color, width=3)
        i = 1
        for station in Station.all_stations.values():
            x, y = int(station.position[0]), int(station.position[1])
            draw.text(tuple((x - 10 + 4, y - pow(-1, i) * (10 + 10))), text=station.name, fill='black',
                      font=self.Myfont)
            i += 1
        for mtrp in self.all_metro:
            x, y = int(mtrp.pos[0]), int(mtrp.pos[1])
            img.paste(self.TrainImagemap[mtrp.Direction()], tuple((x - 20, y - 28)))
            text = state_str[mtrp.state.type]
            draw.text(tuple((x - 20 - 10, y - 28 - 30)), text=text, fill='red', font=self.Myfont2)

        return img

    def update_label(self):
        for train in self.all_metro:
            train.move()
        img = self.getImage()
        data = img.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, img.size[0], img.size[1], QtGui.QImage.Format.Format_RGBA8888)
        pix = QtGui.QPixmap.fromImage(qim)
        self.sendNotification(ApplicationFacade.UPDATE,pix)
    def onRemove(self):

        pass

    def onRegister(self):
        print("on register")

    def show_message(self,parent,message):
        QMessageBox.information(parent, "标题", message,
                                QMessageBox.Yes)