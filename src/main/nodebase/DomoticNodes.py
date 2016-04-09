#!/usr/bin/python

class DomoticNodes:

   def getNodeNames(self):
      nodeList = []
      for i in self.nodes:
         nodeList.append(i.getName())
      return nodeList

   def addNode(self, node):
      self.nodes.append(node)

   def delNode(self, name):
      for i in self.nodes:
         if i.getName() == name:
            self.nodes.remove(i)

   def getNode(self, name):
      for i in self.nodes:
         if i.getName() == name:
            return i 
      return None

   def initialize(self):
      for i in self.nodes:
         i.initialize()

   def update(self):
      for i in self.nodes:
         i.update()

   def __init__(self):
      self.nodes = []
