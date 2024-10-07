class Expected_Nc_Variable:
    def __init__(self, name,  units=None, min=None, max=None, size=None):
        self.name = name  # A string representing the name
        self.units = units  # A string representing the units
        self.min = min  # A float representing the min value
        self.max = max  # A float representing the max value
        self.size = size  # An int representing the size of the dimension

