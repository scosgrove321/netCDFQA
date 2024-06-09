class Variable:
    def __init__(self, name, dtype, units, long_name, standard_name, dimensions):
        self.name = name  # A string representing the name
        self.dtype = dtype  # A string representing the data type
        self.units = units  # A string representing the units
        self.long_name = long_name  # A string representing the long name
        self.standard_name = standard_name  # A string representing the standard name
        self.dimensions = dimensions  # A tuple representing the dimensions


class DimensionVariable(Variable):
    def __init__(self, name, dtype, units, long_name, standard_name, dimensions, axis):
        super().__init__(name, dtype, units, long_name, standard_name, dimensions)
        self.axis = axis  # A string representing the axis

class ExtraVariable(Variable):
    def __init__(self, name, dtype, units, long_name, standard_name, dimensions, fill_value, missing_value):
        super().__init__(name, dtype, units, long_name, standard_name, dimensions)
        self.fill_value = fill_value  # A string representing the fill value
        self.missing_value = missing_value  # A string representing the missing value