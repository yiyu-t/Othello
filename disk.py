STROKE_COLOR = 0


class Disk:
    '''draw a disk'''
    def __init__(self, color, spacing, diamater, location, x, y):
        '''initiate a disk'''
        self.color = color
        self.SPACING = spacing
        self.DIAMATER = diamater
        self.LOCATION = location
        self.x = x
        self.y = y

    def display(self):
        '''display one disk'''
        stroke(STROKE_COLOR)
        fill(self.color)
        ellipse(self.x * self.SPACING + self.LOCATION,
                self.y * self.SPACING + self.LOCATION, self.DIAMATER,
                self.DIAMATER)

## possibly have a flip.