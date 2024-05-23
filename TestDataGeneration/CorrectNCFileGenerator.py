import netCDF4 as nc
import numpy as np

# Define the file path
file_path = 'TestDataStorage/test_correct_data.nc'

# Create the NetCDF file
with nc.Dataset(file_path, 'w', format='NETCDF4') as dataset:
    # Create dimensions
    dataset.createDimension('time', 500)
    dataset.createDimension('lat', 180)
    dataset.createDimension('lon', 360)

    # Create variables
    time_var = dataset.createVariable('time', 'i4', ('time',))
    lat_var = dataset.createVariable('lat', 'f4', ('lat',))
    lon_var = dataset.createVariable('lon', 'f4', ('lon',))

    dco2_var = dataset.createVariable('dco2', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    atm_co2_var = dataset.createVariable('atm_co2', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    sol_var = dataset.createVariable('sol', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    seaice_var = dataset.createVariable('seaice', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    kw_var = dataset.createVariable('kw', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    spco2_raw_var = dataset.createVariable('spco2_raw', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    spco2_smoothed_var = dataset.createVariable('spco2_smoothed', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    fgco2_raw_var = dataset.createVariable('fgco2_raw', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))
    fgco2_smoothed_var = dataset.createVariable('fgco2_smoothed', 'f4', ('time', 'lat', 'lon'), fill_value=np.float32(1e+20))

    # Assign attributes to the time variable
    time_var.units = 'seconds since 2000-01-01'
    time_var.axis = 'T'
    time_var.long_name = 'time'
    time_var.standard_name = 'time'

    # Assign attributes to the latitude variable
    lat_var.units = 'degrees_north'
    lat_var.axis = 'Y'
    lat_var.long_name = 'latitude'
    lat_var.standard_name = 'latitude'

    # Assign attributes to the longitude variable
    lon_var.units = 'degrees_east'
    lon_var.axis = 'X'
    lon_var.long_name = 'longitude'
    lon_var.standard_name = 'longitude'

    # Assign attributes to the other variables
    dco2_var.long_name = 'delta pCO2'
    dco2_var.standard_name = 'dpCO2'
    dco2_var.units = 'muatm'
    dco2_var.missing_value = np.float32(1e+20)

    atm_co2_var.long_name = 'atm pCO2 marine surface level'
    atm_co2_var.standard_name = 'aCO2'
    atm_co2_var.units = 'muatm'
    atm_co2_var.missing_value = np.float32(1e+20)

    sol_var.long_name = 'CO2 solubility'
    sol_var.standard_name = 'sol'
    sol_var.units = 'mol/m3/muatm'
    sol_var.missing_value = np.float32(1e+20)

    seaice_var.long_name = 'seaice fraction'
    seaice_var.standard_name = 'seaice'
    seaice_var.units = '%'
    seaice_var.missing_value = np.float32(1e+20)

    kw_var.long_name = 'kinetic gas transfer coefficient'
    kw_var.standard_name = 'kw'
    kw_var.units = 'm/yr'
    kw_var.missing_value = np.float32(1e+20)

    spco2_raw_var.long_name = 'sea surface pCO2'
    spco2_raw_var.standard_name = 'pCO2'
    spco2_raw_var.units = 'muatm'
    spco2_raw_var.missing_value = np.float32(1e+20)

    spco2_smoothed_var.long_name = 'sea surface pCO2 smoothed'
    spco2_smoothed_var.standard_name = 'pCO2 smoothed'
    spco2_smoothed_var.units = 'muatm'
    spco2_smoothed_var.missing_value = np.float32(1e+20)

    fgco2_raw_var.long_name = 'CO2 flux'
    fgco2_raw_var.standard_name = 'CO2 flux'
    fgco2_raw_var.units = 'mol/m2/yr'
    fgco2_raw_var.missing_value = np.float32(1e+20)

    fgco2_smoothed_var.long_name = 'CO2 flux smoothed'
    fgco2_smoothed_var.standard_name = 'CO2 flux smoothed'
    fgco2_smoothed_var.units = 'mol/m2/yr'
    fgco2_smoothed_var.missing_value = np.float32(1e+20)

    # Generate the latitude and longitude values
    lat_values = np.linspace(-89.5, 89.5, 180)
    lon_values = np.linspace(-179.5, 179.5, 360)

    # Assign values to the lat and lon variables
    lat_var[:] = lat_values
    lon_var[:] = lon_values

print(f"NetCDF file created at {file_path}")
