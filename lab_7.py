
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        """"""

    def move(self,x ,y):
        self.x = x
        self.y = y
        print(self.x,self.y)

    def Xx(self):
        return self.x

    def Yy(self):
        return self.y


    def dist(self, point):
        print(((self.x - point.Xx()) ** 2 + (self.y - point.Yy()) ** 2 ) ** 0.5)

point1 = Point(2, 2)
point2 = Point(4, 3)

point1.dist(point2)







