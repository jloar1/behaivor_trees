#!/usr/bin/env python

import enum

class Status(enum.Enum):
    
    SUCCESS = 1
    RUNNING = 2
    FAILURE = 3

class Node:       
    
    def __init__(self, name):
        self.name = name
    
    def activate():
        return Status.SUCCESS
        

class Root(Node):
    
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.running_node = 0
    
    def activate(self):
        if self.running_node != 0:
            for i in range(0, self.running_node):
                if hasattr(self.nodes[i], 'condition') and hasattr(self.nodes[i], 'priority'):
                    if self.nodes[i].priority == True and self.nodes[i].condition == True:
                        abort(self.nodes[self.running_node])
                        self.running_node = i
        
        for i in range(self.running_node, len(self.nodes)):
            self.status = self.nodes[i].activate()
            if self.status == Status.RUNNING:
                self.running_node = i
                return self.status
            elif self.status == Status.FAILURE:
                self.running_node = 0
                return self.status
            
        self.running_node = 0
        return Status.SUCCESS
        

class Sequence(Node):
    
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.running_node = 0
    
    def activate(self):
        for i in range(self.running_node, len(self.nodes)):
            self.status = self.nodes[i].activate()
            if self.status == Status.RUNNING:
                self.running_node = i
                return self.status
            elif self.status == Status.FAILURE:
                self.running_node = 0
                return self.status
            
        self.running_node = 0
        return Status.SUCCESS
            

class Selector(Node):
    
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.running_node = 0
    
    def activate(self):
        for i in range(self.running_node, len(self.nodes)):
            self.status = self.nodes[i].activate()
            if self.status == Status.RUNNING:
                self.running_node = i
                return self.status
            elif self.status == Status.SUCCESS:
                self.running_node = 0
                return self.status
            
        self.running_node = 0
        return Status.FAILURE

class Condition(Node):
    
    def __init__(self, name, default_condition = True, priority = False):
        self.name = name
        self.priority = priority
        self.condition = default_condition
        self.nodes = [] # conditions should only have one child
    
    def activate(self):
        if self.condition == True:
            self.status = self.nodes[0].activate()
            return self.status
        else:
            return Status.SUCCESS

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
        if hasattr(i, 'nodes') and len(i.nodes) > 0:
            iterate(i, level + 1)

def abort(node):
    if hasattr(node, 'running_node') and hasattr(node, 'nodes') and len(node.nodes) > 0:
        abort(node.nodes[running_node])
        node.running_node = 0

# --------------------------------------------------------------------------------
    