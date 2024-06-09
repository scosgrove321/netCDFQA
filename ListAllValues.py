import netCDF4 as nc
from CheckDimensionMetadata import check_dimension_metadata
from CheckVariableMetadata import check_variable_metadata
from Variable import DimensionVariable
def list_all_values(nc_file):
    # Open the NetCDF file
    dataset = nc.Dataset(nc_file, mode='r')

    # Print dimensions
    print("Dimensions:")
    for dim_name, dim in dataset.dimensions.items():
        print(f"    Dimension name: {dim_name},  Length: {len(dim)}")
        match dim_name:
            case "time":
                check_dimension_metadata(dim_name, len(dim), "time", 240)
            case "lat":
                check_dimension_metadata(dim_name, len(dim), "lat", 180)
            case "lon":
                check_dimension_metadata(dim_name, len(dim), "lon", 360)


    # Print variable metadata
    print("Variable metadata:")
    for var_name, var in dataset.variables.items():
        print(f"    {var_name} ({var.dimensions}): {var.dtype}")
        check_variable_metadata(var)

    lat = dataset.variables['lat'][:]
    lon = dataset.variables['lon'][:]
    time = dataset.variables['time'][:]
    numItrs = 0
    print("Variable values:")
    for lat_idx, latitude in enumerate(lat):
        for lon_idx, longitude in enumerate(lon):
            for t_idx, t in enumerate(time):
                print(f"    lat: {latitude},  lon: {longitude}, time: {t}")

                numItrs += 1
                if numItrs >= 3:
                    return


    # Close the dataset
    dataset.close()




# Example usage
file_path = 'C:/Python/netCDFQA/RealData/v2023.nc'
list_all_values(file_path)
