import numpy as np
from Variable import DimensionVariable, ExtraVariable
def check_variable_metadata( var):
    expected_var = getExpectedVar(var)
    if expected_var is None:
            return
    if var.name != expected_var.name and var.name.lower() == expected_var.name.lower():
        print(f"Incorrect casing for {expected_var.name} variable. Expected: {expected_var.name}, Actual: {var.name}")
    if tuple(sorted(var.dimensions)) != tuple(sorted(expected_var.dimensions)):
        print(f"Incorrect dimension for {expected_var.name} variable. Expected: {expected_var.dimensions}, Actual: {var.dimensions}")
    if np.dtype(var.dtype).itemsize < np.dtype(expected_var.dtype).itemsize:
        print(f"Incorrect precision for {expected_var.name} variable. Expected at least {np.dtype(expected_var.dtype).itemsize} bits of precision, actual: {np.dtype(var.dtype).itemsize}")

    if isinstance(expected_var, DimensionVariable):
        check_dimension_variable_attibutes(var)
    if isinstance(expected_var, ExtraVariable):
        check_other_variables(var)

def check_dimension_variable_attibutes(var):
    print(f"    Checking: dimension variable {var.name} attributes")

def check_other_variables(var):
    print(f"    Checking: extra variable {var.name} attributes")

def getExpectedVar(var):
    match var.name.lower():
        case "time":
            return DimensionVariable( name='time', dimensions=('time',), units='seconds since 1970-01-01 00:00:00',
                                      long_name='time', standard_name='time', dtype= 'int32', axis='T')
        case "lat":
            return DimensionVariable( name='lat', dimensions=('lat',), units='degrees_north',
                                      long_name='latitude', standard_name='latitude', dtype='float32',
                                      axis='Y')
        case "lon":
            return DimensionVariable( name='lon', dimensions=('lon',), units='degrees_east',
                                      long_name='longitude', standard_name='longitude', dtype='float32',
                                      axis='X')
        case "dco2":
            return ExtraVariable( name='dco2', dimensions=('time', 'lat', 'lon'), units='muatm',
                                 long_name='delta pCO2', standard_name='dpCO2', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "atm_co2":
            return ExtraVariable(name='atm_co2', dimensions=('time', 'lat', 'lon'), units='muatm',
                                 long_name='atm pCO2 marine surface level', standard_name='aCO2', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "sol":
            return ExtraVariable(name='sol', dimensions=('time', 'lat', 'lon'), units='mol/m3/muatm',
                                 long_name='CO2 solubility', standard_name='sol', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "seaice":
            return ExtraVariable(name='dco2', dimensions=('time', 'lat', 'lon'), units='%',
                                 long_name='seaice fraction', standard_name='seaice', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "kw":
            return ExtraVariable(name='kw', dimensions=('time', 'lat', 'lon'), units='m/yr',
                                 long_name='kinetic gas transfer coefficient', standard_name='kw', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "spco2_raw":
            return ExtraVariable(name='spco2_raw', dimensions=('time', 'lat', 'lon'), units='muatm',
                                 long_name='sea surface pCO2', standard_name='pCO2', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "spco2_smoothed":
            return ExtraVariable(name='dco2', dimensions=('time', 'lat', 'lon'), units='muatm',
                                 long_name='CO2 flux', standard_name='CO2 flux', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "fgco2_raw":
            return ExtraVariable(name='fgco2_raw', dimensions=('time', 'lat', 'lon'), units='mol/m2/yr',
                                 long_name='CO2 flux', standard_name='CO2 flux', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)
        case "fgco2_smoothed":
            return ExtraVariable(name='fgco2_smoothed', dimensions=('time', 'lat', 'lon'), units='mol/m2/yr',
                                 long_name='CO2 flux smoothed', standard_name='CO2 flux smoothed', dtype='float32',
                                 fill_value=1e+20, missing_value=1e+20)

        case _:
            print(f"    Extra variable found: {var.name}")