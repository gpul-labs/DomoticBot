import __init__
__init__.nodes.getNode("NodeClimatization").setTemp(5)
__init__.nodes.initialize()

while True:
   __init__.nodes.update()
