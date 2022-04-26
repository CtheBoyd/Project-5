class Taxicab():
    """"""

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


cab = Taxicab(5,-8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.odometer) # will print 8 3+4+1 = 8