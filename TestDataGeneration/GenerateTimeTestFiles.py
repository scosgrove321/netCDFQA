import os
import netCDF4 as nc
import numpy as np

# Ensure the output directory exists
output_dir = 'TestDataStorage'
os.makedirs(output_dir, exist_ok=True)


def create_test_nc_file(file_path, time_values, create_time_var=True):
    with nc.Dataset(file_path, 'w', format='NETCDF4') as dataset:
        # Create the latitude dimension and variable
        dataset.createDimension('lat', 180)
        lat_var = dataset.createVariable('lat', 'f4', ('lat',))
        lat_var.units = 'degrees_north'
        lat_var.long_name = 'latitude'
        lat_var.standard_name = 'latitude'
        lat_var.axis = 'Y'
        lat_var[:] = np.arange(-89.5, 90, 1)

        # Create the longitude dimension and variable
        dataset.createDimension('lon', 360)
        lon_var = dataset.createVariable('lon', 'f4', ('lon',))
        lon_var.units = 'degrees_east'
        lon_var.long_name = 'longitude'
        lon_var.standard_name = 'longitude'
        lon_var.axis = 'X'
        lon_var[:] = np.arange(-179.5, 180, 1)

        # Create the time dimension
        if time_values is not None:
            dataset.createDimension('time', len(time_values))

        if create_time_var and time_values is not None:
            # Create the time variable
            time_var = dataset.createVariable('time', 'i4', ('time',))
            time_var.units = 'seconds since 2000-01-01'
            time_var.long_name = 'time'
            time_var.standard_name = 'time'
            time_var.axis = 'T'

            # Assign the time values
            time_var[:] = time_values


# Define different scenarios for the 'time' variable
test_cases = {
    'test_pass_time.nc': (np.arange(1, 241), True),
    'test_fail_missing_time_dim.nc': (None, True),  # Missing time dimension
    'test_fail_missing_time_var.nc': (np.arange(1, 241), False),  # Missing time variable
    'test_fail_wrong_length.nc': (np.arange(1, 239), True),  # Length different than 240
    'test_fail_wrong_values.nc': (np.arange(2, 242), True),  # Values not starting from 1
    'test_fail_wrong_spacing.nc': (np.arange(1, 241, 0.5)[:240], True)  # Incorrect spacing
}

for file_name, (time_values, create_time_var) in test_cases.items():
    file_path = os.path.join(output_dir, file_name)

    if time_values is None:
        # Special case for missing time dimension
        with nc.Dataset(file_path, 'w', format='NETCDF4') as dataset:
            # Create a dummy dimension to avoid empty file errors
            dataset.createDimension('lat', 1)
    else:
        create_test_nc_file(file_path, time_values, create_time_var)

print(f"Test files generated in {output_dir}")
