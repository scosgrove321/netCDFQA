Author: Stephen Cosgrove
Date: Oct 6, 2024
Description: 
    This script processes NetCDF files to perform quality assurance checks on variable names and values. 
    It specifically checks for expected dimensions, dimension size, expected variables, and min/max variable values.

Required Libraries:
    - netCDF4: For handling NetCDF files.
    - numpy: required by netCDF4.

Usage:
    Ensure that the required libraries are installed. 
    Example usage: py CheckNetCdf.py "C:/Python/input/testNC.nc"
    This program is free for non-commercial use. 

Contact:
    scosgrove321@gmail.com

QC Constraints:
    Dimensions:
        region      [Only check is that the dimension exists]
        time        [size >= 396] 
        lat         [size = 180, min = -89.5, max = 89.5]
        lon         [size = 360, min = -89.5, max = 89.5]
    Variables:
        fgco2_reg   [units='pgc/yr', min=-1, max=4]
        fgco2       [units='molc/m2/s', min=-1e-6, max=1e-6]
        sfco2       [units='uatm', min=200, max=500]
        area        [units='m2']
        mask_sfc    [units='frac']
        area_reg    [units='m2']
        kw          [units='cm/hr', min=0, max=50]
        Fco2atm     [units='μatm']
        tos         [units='degC', min=-2, max=40]
        fice        [units='frac', min=-0.01, max=1.01]
        alpha       [units='mol/m3/uatm', min=4e-5, max=4.7e-5]
