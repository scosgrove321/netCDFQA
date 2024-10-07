from ExpectedNcVariable import Expected_Nc_Variable

def check_variable(var):
    expected_var = getExpectedVar(var)
    if expected_var is None:
        # Unknown variable
        print(f"Unknown variable found: {var.name}")
        return
    if not hasattr(var, 'units') and getattr(expected_var, 'units') is not None:
        print(f"Variable '{var.name}' was expected to have an attribute named 'units' but it was not found.")
        return
    if hasattr(var, 'units') and getattr(var, 'units') is None:
        print(f"Variable '{var.name}' found an attribute named 'units' but it did not have a value.")
        return
    if getattr(expected_var, 'units') is not None and not getattr(var, 'units').lower() == getattr(expected_var, 'units').lower():
        print(f"Variable '{var.name}' was expected to have units '{expected_var.units}' but '{getattr(var, 'units')}' was found instead.")
        return
    min_value = var[:].min()
    if getattr(expected_var, 'min') is not None and min_value < getattr(expected_var, 'min'):
        expected_min = getattr(expected_var, 'min')
        print(f"Variable '{var.name}' has a minimum value of '{min_value}', which is below the expected minimum of '{expected_min}'.")
        values_below_min = var[:] < expected_min
        print(f"    There are {values_below_min.sum()} instances below the expected minimum of '{expected_min}'.")
    max_value = var[:].max()
    if getattr(expected_var, 'max') is not None and max_value > getattr(expected_var, 'max'):
        expected_max = getattr(expected_var, 'max')
        print(f"Variable '{var.name}' has a maximum value of '{max_value}', which is below the expected minimum of '{expected_max}'.")
        values_above_max = var[:] > expected_max
        print(f"    There are {values_above_max.sum()} instances above the expected maximum of '{expected_max}'.")
    if getattr(expected_var, 'size') is not None:
        expected_size = getattr(expected_var, 'size')
        if expected_size != getattr(var, 'size'):
            print(f"Variable '{var.name}' has a size of '{getattr(var, 'size')}', which is different the expected size of '{expected_size}'.")

def getExpectedVar(var):
    #   Only add attributes that are mandatory
    match var.name.lower():
        case "time":
            return Expected_Nc_Variable(name='time', min=396)
        case "lat":
            return Expected_Nc_Variable(name='lat', min=-89.5, max=89.5, size=180)
        case "lon":
            return Expected_Nc_Variable(name='lon', min=0.5, max=359.5, size=360)
        case "region":
            return Expected_Nc_Variable(name='region', size=4)
        case "fgco2_reg":
            return Expected_Nc_Variable(name='fgco2_reg', units='pgc/yr', min=-1, max=4)
        case "fgco2":
            return Expected_Nc_Variable(name='fgco2', units='molc/m2/s', min=-1e-6, max=1e-6)
        case "sfco2":
            return Expected_Nc_Variable(name='sfco2', units='uatm', min=200, max=500)
        case "area":
            return Expected_Nc_Variable(name='area', units='m2')
        case "area_reg":
            return Expected_Nc_Variable(name='area', units='m2')
        case "mask_sfc":
            return Expected_Nc_Variable(name='mask_sfc', units='frac')
        case "kw":
            return Expected_Nc_Variable(name='kw', units='cm/hr', min=0, max=50)
        case "fco2atm":
            return Expected_Nc_Variable(name='fco2atm', units='μatm')
        case "tos":
            return Expected_Nc_Variable(name='tos', units='degC', min=-2, max=40)
        case "fice":
            return Expected_Nc_Variable(name='fice', units='frac', min=-0.01, max=1.01)
        case "alpha":
            return Expected_Nc_Variable(name='alpha', units='mol/m3/uatm', min=4e-5, max=4.7e-5)
