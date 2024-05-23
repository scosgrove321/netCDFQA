import netCDF4 as nc
import numpy as np


# Replace 'example.nc' with the path to your NetCDF file
file_path = 'TestDataGeneration/TestDataStorage/test_correct_data.nc'
ojk

# Open the NetCDF file
dataset = nc.Dataset(file_path, mode='r')

# Print global attributes
print("Global Attributes:")
for attr in dataset.ncattrs():
    print(f"{attr}: {dataset.getncattr(attr)}")

# Print dimensions
print("\nDimensions:")
for dim_name, dim in dataset.dimensions.items():
    print(f"{dim_name}: {len(dim)}")

# Print variables and their attributes
print("\nVariables:")
for var_name, var in dataset.variables.items():
    print(f"{var_name} ({var.dimensions}): {var.dtype}")
    for attr in var.ncattrs():
        print(f"  {attr}: {var.getncattr(attr)}")

# Close the dataset
dataset.close()

