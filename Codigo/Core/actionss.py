class PenDownCommand:
    def __init__(self):
        pass
    def draw(self,turtle):
        turtle.pendown()
    def __str__(self):
        return '{"command":"PenDown"}'
class PyList:
    def __init__(self):
        self.items = []

    def append(self,item):
        self.items = self.items + [item]

    def removeLast(self):
        self.items.clear()

    def __iter__(self):
        for c in self.items:
            yield c

class GoToCommand:
    def __init__(self,x,y,width=1,color="black"):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
    
    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)
    def __str__(self):
        return '{"command": "GoTo","x": %s,"y": %s,"width": %s,"color": "%s" }' % (self.x, self.y, self.width, self.color)
    
class CircleCommand:
    def __init__(self,radius, width=1,color="black"):
        self.radius = radius
        self.width = width
        self.color = color
    
    def draw(self,turtle):  
        turtle.width(self.width)
        turtle.pencolor(self.color) 
        turtle.circle(self.radius)
        
    def __str__(self):
        return '{"command" : "Circle","radius": %s,"width": %s,"color": "%s" }' % (self.radius,self.width,self.color)
    
class BeginFillCommand:
    def __init__(self,color):
        self.color = color
    
    def draw(self,turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()
    def __str__(self):
        return '{"command":"BeginF","color": "%s"}' % self.color
    
class EndFillCommand:
    def __init__(self):
        pass
    def draw(self,turtle):
        turtle.end_fill()
    def  __str__(self):
        return '{"command":"EndFill"}'

class PenUpCommand:
    def __init__(self):
        pass
    def draw(self,turtle):
        turtle.penup()
    def __str__(self):
        
        return '{"command": "PenUp"}'