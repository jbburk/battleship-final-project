class Point:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def update_coordinates(self,new_coord):
        x = self._x + new_coord.get_x()
        y = self._y + new_coord.get_y()
        return Point(x, y)

    def return_coordinates(self):
        return Point(self.get_x(),self.get_y())

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def equals(self,other_coord):
        return self._x == other_coord.get_x() and self._y == other_coord.get_y()

