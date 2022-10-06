#!/usr/bin/env python

import enum
import time

class Status(enum.Enum):
    
    SUCCESS = 1
    RUNNNIG = 2
    FAILURE = 3

class Node:
    
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.active_node = 0        
    
    def activate(self):
        pass
        

class Root(Node):
    
    def activate(self):
        if len(self.nodes) == 0:
            print(self.name + " has no child nodes")
        else:
            self.result = self.nodes[self.active_node].activate()
            if self.result == Status.SUCCESS:
                if self.active_node < len(self.nodes) - 1:
                    self.active_node += 1
                    self.activate()
                else:
                    self.active_node = 0
            elif self.result == Status.RUNNNIG:
                pass
            elif self.result == Status.FAILURE:
                print(self.nodes[self.active_node].name + " has failed")
        

class Sequence(Node):
    
    def activate(self):
        if len(self.nodes) == 0:
            print(self.name + "has no child nodes")
        else:
            self.result = self.nodes[self.active_node].activate()
            if self.result == Status.SUCCESS:
                if self.active_node < len(self.nodes) - 1:
                    self.active_node += 1
                    self.activate()
                else:
                    self.active_node = 0
                return Status.SUCCESS
            elif self.result == Status.RUNNNIG:
                return Status.RUNNNIG
            elif self.result == Status.FAILURE:
                print(self.nodes[active_node].name + " has failed")
                return Status.SUCCESS
        return Status.FAILURE

class Action(Node):
    
    def activate(self):
        print(self.name)
        return Status.SUCCESS

def display_tree(root):
    print(root.name)
    iterate(root, 1)
        
def iterate(node, level):
    for i in node.nodes:
        print(level * "  " + i.name)
        if len(i.nodes) > 0:
            iterate(i, level + 1)

root = Root("root")

sequence = Sequence("sequence")
sequence2 = Sequence("sequence2")

action = Action("Hello")
action2 = Action("I like")
action3 = Action("behavior trees")
action4 = Action("a lot")

root.nodes.append(sequence)
root.nodes.append(sequence2)

sequence.nodes.append(action)
sequence.nodes.append(action2)

sequence2.nodes.append(action3)
sequence2.nodes.append(action4)

display_tree(root)
print("------------------")

while True:
    root.activate()
    time.sleep(1)

    