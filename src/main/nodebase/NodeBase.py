import bmp180

class NodeBase:
    def __init__(self):

    def getName(self):
        return "This is the node base"

    def initNode(self):

    def update(self):


class NodePresence(NodeBase):
    def __init__(self):
        self.presenceSensor = pir()

    def setHandler(self, handler):
        self.handler = handler



class NodeDoorbell(NodeBase):
    def __init__(self):

    def setHadler(self, handler)
        self.handler = handler


class NodeClimatization(NodeBase):
    def __init__(self):
        self.bmp180 = bmp180()
        #self.hotterActuator = switch()
        #self.coolerActuator = switch()

    def setTemp(self, temperature, thresold):
        self.temperature = temperature
        self.thresold = thresold
        #READ THE SENSOR
        #ACTUATE OVER THE HOTTER OR THE COOLER IF THE TEMPERATURE IS INCORRECT

    def getTemp(self):
        return bmp180.temp()


class NodeDoorlock:
    def __init__(self):

    def getStatus(self):

    def setStatus(self, status):

