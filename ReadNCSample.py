import netCDF4 as nc

def read_dimensions(nc_file):
    dimensions = {}
    with nc.Dataset(nc_file, 'r') as dataset:
        for dim_name, dim_obj in dataset.dimensions.items():
            dimensions[dim_name] = {
                'size': len(dim_obj),
                'values': dim_obj[:]
            }
    return dimensions

# Path to the NetCDF file
nc_file_path = "TestDataGeneration/TestDataStorage/test_pass.nc"

# Read dimensions and their values
dimensions_info = read_dimensions(nc_file_path)

# Print dimension information
for dim_name, dim_info in dimensions_info.items():
    print(f"Dimension: {dim_name}")
    print(f"Size: {dim_info['size']}")
    print(f"Values: {dim_info['values']}\n")