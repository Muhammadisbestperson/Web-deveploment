from turtle import*
# turtle is used to draw things + today we are going to draw a funny face
class Face:
    # the necessary function
    def __init__(self,xpos,ypos):
        self.size=90
        self.coord=(xpos,ypos)
        #circle function
    def setSize(self,radius):
        self.size=radius
        # for drawing
    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutline()
#defining go home function
    def goHome(self):
        penup()
        goto(self.coord)

        setheading(0)

    def drawOutline (self):
        penup()
        forward(self.size)
        left(90)           
        pendown()
        circle(self.size)
        self.goHome()
f1 = Face(0,0)           
f1.draw()

showturtle()
done()