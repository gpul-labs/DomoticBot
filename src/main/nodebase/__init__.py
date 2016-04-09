import DomoticNodes
import NodePresence
import NodeDoorbell
import NodeClimatization
import NodeDoorlock
import Buzzer

nodes = DomoticNodes.DomoticNodes()
nodes.addNode(NodePresence.NodePresence(23)) # gpio
nodes.addNode(NodeDoorbell.NodeDoorbell(17, 26, 1, 3000)) # gpio, gpioBuzzer, duration, frequency
nodes.addNode(NodeClimatization.NodeClimatization(22, 24)) # gpioCooler, gpioHeater
nodes.addNode(NodeDoorlock.NodeDoorlock(18))
