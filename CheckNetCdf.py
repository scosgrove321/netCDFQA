import netCDF4 as nc
from CheckVariableMetadata import check_variable
import argparse

"""
Author: Stephen Cosgrove
Date: Oct 6, 2024
Description: 
    This script processes NetCDF files to perform quality assurance checks on variable names and values. 
    It specifically checks for expected dimensions, dimension size,  expected variables, and min/max variable values.

Required Libraries:
    - netCDF4: For handling NetCDF files.
    - numpy: For numerical operations and array handling.

Usage:
    Ensure that the required libraries are installed. 
    Example usage: py CheckNetCdf.py "D:/Python/input/testNC.nc"
    This program is free for non-commercial use. 

Contact:
    Stephen Cosgrove: scosgrove321@gmail.com

"""

def check_net_cdf(file_path):
    # Process the NetCDF file
    dataset = nc.Dataset(file_path, mode='r')

    expected_dimensions = ["time", "lat", "lon", "region"]
    expected_variables = ["time", "lat", "lon", "fgco2_reg", "fgco2", "sfco2", "area", "area_reg", "mask_sfc", "kw",
                          "fco2atm", "tos", "fice", "alpha"]

    # Print dimensions that should exist, but do not
    for dim_name in expected_dimensions:
        if dim_name not in dataset.dimensions:
            print(f"Could not find expected dimension: {dim_name}")

    # Check variables
    for var_name in expected_variables:
        if var_name not in dataset.variables:
            # Print variables that should exist, but do not
            print(f"Could not find expected variable: {var_name}")
            continue

        var = dataset.variables[var_name]
        # Additional checks
        check_variable(var)

    # Close the dataset
    dataset.close()

def is_valid_netcdf(file_path):
    try:
        dataset = nc.Dataset(file_path, mode='r')
        dataset.close()  # Close the dataset if it's valid
        return True
    except:
        print(f"File '{file_path}' could not be opened as a nc dataset.")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check NetCDF variable metadata.")
    parser.add_argument("file_path", help="Path to the NetCDF file.")
    args = parser.parse_args()

    if is_valid_netcdf(args.file_path):
        print(f"Checking file: {args.file_path}")
        check_net_cdf(args.file_path)
        print("Finished!")
