import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)
    
    def reflect_x(point1):
        x = point1.getX()
        newy = point1.getY() * -1
        newpoint = Point(x, newy)
        return newpoint
    
    def slope_from_origin(self):
        if self.getX() == 0:
            return None
        else:
            slope = self.getY() / self.getX()
            return slope

    def slope_intersect(self, point2):    
        ydiff = point2.getY() - self.getY()
        xdiff = point2.getX() - self.getX()
        if xdiff == 0:
            return None
        else:
            slope = ydiff / xdiff
            intersect = point2.getY() - (slope * point2.getX())
            coordinates = (slope, intersect)
            return coordinates



class Rectangle:
    """ Rectangle class for defining the size of a rectangle"""
    
    def __init__(self, initP , initW, initH):
        """ create a rectangle with lowerleft coordinates, width, and height"""
        self.x = initP.getX()
        self.y = initP.getY()
        self.w = initW
        self.h = initH
        
    def getWidth(self):
        return self.w
    
    def getHeight(self):
        return self.h
    
    def __str__(self):
        lowerLeft = "(" + str(self.x) + "," + str(self.y) + ")"
        return "Lower Left Coordinates" + lowerLeft + "\n Width:" + str(self.w) + "\n Height:" + str(self.h)
    
    def area(self):
        a = self.getHeight() * self.getWidth()
        return a
    
    def perimeter(self):
        prm = (self.getHeight() * 2) + (self.getWidth() * 2)
        return prm
    
    def transpose(self):
        neww = self.getWidth()
        newh = self.getHeight()
        self.h = newh
        self.w = neww
        
    def contains(self, point):
        rightbound = self.x + self.w
        upperbound = self.y + self.h
        if point.getX() < rightbound and point.getX() > self.x:
            if point.getY() < upperbound and point.getY() > self.y:
                return True
            else:
                return False
        else:
            return False
        
    def diagonal(self):
        c = (self.w ** 2 + self.h **2) ** 0.5
        return c
    
    def collision(self, rectangle2):
        """Detects a collison between two rectangles by checking that no corner contacts another rectangle"""
        rect2PointA = Point(rectangle2.x, rectangle2.y)
        rect2PointB = Point(rectangle2.x, rectangle2.y + rectangle2.getHeight())
        rect2PointC = Point(rectangle2.x + rectangle2.getWidth(), rectangle2.y)
        rect2PointD = Point(rectangle2.x + rectangle2.getWidth(), rectangle2.y + rectangle2.getHeight())
        allpoints = [rect2PointA, rect2PointB, rect2PointC, rect2PointD]
        for each in allpoints:
            if self.contains(each) == True:
                return True
            else:
                return False
        
        
        
r = Rectangle(Point(0,0), 10, 5)
r2 = Rectangle(Point(9,6), 10, 5)
print(r.collision(r2))
