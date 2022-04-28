# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/26/2022
# Description: Asks user to provide five numbers and then provides the total units the taxi moved.
#

class Taxicab():
    """Asks user to provide five numbers and then provides the total units the taxi moved."""

    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.odometer = 0

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_odometer(self):
        return self.odometer

    def move_x(self, units):
        self.x_coord += units
        # add the absolute distance to odometer
        self.odometer += abs(units)
    def move_y(self, units):
        self.y_coord += units
        # add the absolute distance to odometer
        self.odometer += abs(units)


