class Taxicab:
    """
    Represents a point on the Cartesian plane that can calculate the distance
    between itself and another point
    """
    def __init__(self, x_coord, y_coord, odometer):
        """Creates a Point object with the specified number of coordinates"""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def get_odom(self):
        return self._odometer

    def distance_to(self, other_point):
        """returns the distance to the other point"""
        x_diff = self._x_coord - other_point.get_x_coord()
        y_diff = self._y_coord - other_point.get_y_coord()
        result = (x_diff ** 2 + y_diff ** 2) ** 0.5
        return result

point_1 = Taxicab(0,4)
point_2 = Taxicab(3,0)
print(point_1.distance_to(point_2))