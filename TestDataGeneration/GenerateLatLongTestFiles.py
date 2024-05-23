import os
import netCDF4 as nc
import numpy as np

# Inject specific issues into the data
def inject_issue(lat_values, lon_values, times, data_dict, issue_type):
    if issue_type == 'min_lat':
        lat_values[0] -= 1
    elif issue_type == 'max_lat':
        lat_values[-1] += 1
    elif issue_type == 'min_lon':
        lon_values[0] -= 1
    elif issue_type == 'max_lon':
        lon_values[-1] += 1
    elif issue_type == 'multiple_lat':
        lat_values = np.clip(lat_values, -89.5, 89.5)
        lat_values[1] = lat_values[0]
    elif issue_type == 'multiple_lon':
        lon_values[1] = lon_values[0]
    elif issue_type == 'spacing_lat':
        lat_values = np.arange(-89, 91, 2) + np.random.uniform(-0.5, 0.5, size=len(np.arange(-89, 91, 2)))
    elif issue_type == 'spacing_lon':
        lon_values = np.arange(-179, 181, 2) + np.random.uniform(-0.5, 0.5, size=len(np.arange(-179, 181, 2)))

    # Update data_dict to match new dimensions
    new_data_dict = {}
    for key, attrs in data_dict.items():
        new_data_dict[key] = {
            'long_name': attrs['long_name'],
            'standard_name': attrs['standard_name'],
            'units': attrs['units'],
            'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')
        }

    return lat_values, lon_values, times, new_data_dict


# Function to create a NetCDF file with the specified variables and their attributes
def create_nc_file(file_path, lat_values, lon_values, times, data_dict):
    with nc.Dataset(file_path, 'w', format='NETCDF4') as dataset:
        # Create dimensions
        dataset.createDimension('lat', len(lat_values))
        dataset.createDimension('lon', len(lon_values))
        dataset.createDimension('time', len(times))

        # Create variables and set attributes
        lat = dataset.createVariable('lat', 'f4', ('lat',))
        lat.units = 'degrees_north'
        lat.axis = 'Y'
        lat.long_name = 'latitude'
        lat.standard_name = 'latitude'

        lon = dataset.createVariable('lon', 'f4', ('lon',))
        lon.units = 'degrees_east'
        lon.axis = 'X'
        lon.long_name = 'longitude'
        lon.standard_name = 'longitude'

        time = dataset.createVariable('time', 'i4', ('time',))
        time.bounds = 'time_bnds'
        time.units = 'seconds since 2000-01-01'
        time.axis = 'T'
        time.long_name = 'time'
        time.standard_name = 'time'

        def create_variable(name, long_name, standard_name, units, dataset, fill_value):
            var = dataset.createVariable(name, 'f4', ('time', 'lat', 'lon'), fill_value=fill_value)
            var.long_name = long_name
            var.standard_name = standard_name
            var.units = units
            var.missing_value = fill_value
            return var

        fill_value = 1e+20
        variables = {}
        for key, attrs in data_dict.items():
            variables[key] = create_variable(key, attrs['long_name'], attrs['standard_name'], attrs['units'], dataset,
                                             fill_value)

        # Add data to variables
        lat[:] = lat_values
        lon[:] = lon_values
        time[:] = times
        for key, data in data_dict.items():
            variables[key][:, :, :] = data['values']


# Define latitudes, longitudes, and times
lat_values = np.arange(-89.5, 90.5, 1)
lon_values = np.arange(-179.5, 180.5, 1)
times = np.arange(240)

# Generate random data for the new climatic variables
data_dict = {
    'dco2': {'long_name': 'delta pCO2', 'standard_name': 'dpCO2', 'units': 'muatm',
             'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'atm_co2': {'long_name': 'atm pCO2 marine surface level', 'standard_name': 'aCO2', 'units': 'muatm',
                'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'sol': {'long_name': 'CO2 solubility', 'standard_name': 'sol', 'units': 'mol/m3/muatm',
            'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'seaice': {'long_name': 'seaice fraction', 'standard_name': 'seaice', 'units': '%',
               'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'kw': {'long_name': 'kinetic gas transfer coefficient', 'standard_name': 'kw', 'units': 'm/yr',
           'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'spco2_raw': {'long_name': 'sea surface pCO2', 'standard_name': 'pCO2', 'units': 'muatm',
                  'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'spco2_smoothed': {'long_name': 'sea surface pCO2 smoothed', 'standard_name': 'pCO2 smoothed', 'units': 'muatm',
                       'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'fgco2_raw': {'long_name': 'CO2 flux', 'standard_name': 'CO2 flux', 'units': 'mol/m2/yr',
                  'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')},
    'fgco2_smoothed': {'long_name': 'CO2 flux smoothed', 'standard_name': 'CO2 flux smoothed', 'units': 'mol/m2/yr',
                       'values': np.random.rand(len(times), len(lat_values), len(lon_values)).astype('float32')}
}

# List of issues to introduce
issue_types = [
    'min_lat',
    'max_lat',
    'min_lon',
    'max_lon',
    'multiple_lat',
    'multiple_lon',
    'spacing_lat',
    'spacing_lon'
]

# Create NetCDF files with issues
for issue_type in issue_types:
    file_name = f'TestDataStorage/test_fail_{issue_type}.nc'
    lat_values_copy = lat_values.copy()
    lon_values_copy = lon_values.copy()
    injected_values = inject_issue(lat_values_copy, lon_values_copy, times, data_dict.copy(), issue_type)
    create_nc_file(file_name, *injected_values)

# Create a NetCDF file without any issues (to pass the test)
create_nc_file('TestDataStorage/test_pass_lat_long.nc', lat_values, lon_values, times, data_dict)
