import netCDF4 as nc
from TestResult import TestResult
import numpy as np


def check_nc_time(file_path: str) -> TestResult:
    messages = []
    success = True

    try:
        dataset = nc.Dataset(file_path, 'r')
    except Exception as e:
        return TestResult(False, [f"Failed to open file: {e}"])

    def get_variable_info(var, index):
        try:
            value = var[index]
            return value
        except:
            return 'N/A'

    # Check for 'time' dimension
    if 'time' not in dataset.dimensions:
        messages.append("Missing 'time' dimension.")
        success = False
    else:
        time_dim = dataset.dimensions['time']
        if len(time_dim) < 240:
            messages.append(f"'time' dimension length is {len(time_dim)}, which is less than the expected minimum of 240.")
            success = False

    # Check for 'time' variable
    if 'time' not in dataset.variables:
        messages.append("Missing 'time' variable.")
        success = False
    else:
        time_var = dataset.variables['time']
        time_values = time_var[:]

        # Check length
        if len(time_values) < 240:
            messages.append(f"'time' variable length is {len(time_values)}, which is less than the expected minimum of 240.")
            success = False

        # Check values
        expected_values = np.arange(1, len(time_values) + 1)
        first_incorrect_value = None
        for i, value in enumerate(time_values):
            if value != expected_values[i]:
                first_incorrect_value = value
                time_index = i
                break

        if first_incorrect_value is not None:
            expected_value = expected_values[time_index]

            lat_var = dataset.variables['lat'] if 'lat' in dataset.variables else None
            lon_var = dataset.variables['lon'] if 'lon' in dataset.variables else None

            lat_value = get_variable_info(lat_var, 0) if lat_var is not None else 'N/A'
            lon_value = get_variable_info(lon_var, 0) if lon_var is not None else 'N/A'

            time_value = get_variable_info(time_var, time_index) if time_var is not None else 'N/A'
            lat_variable_info = get_variable_info(lat_var, 0) if lat_var is not None else 'N/A'
            lon_variable_info = get_variable_info(lon_var, 0) if lon_var is not None else 'N/A'

            messages.append(
                f"First incorrect value in 'time' variable: {first_incorrect_value}. Expected value: {expected_value}. "
                f"Dimension info: {{Time: {time_value}, Lat: {lat_value}, Lon: {lon_value}}}. "
                f"Variable info at location: {{Time: {time_value}, Lat: {lat_variable_info}, Lon: {lon_variable_info}}}."
            )
            success = False

        # Check spacing
        spacing = np.diff(time_values)
        incorrect_spacing_idx = np.where(spacing != 1.0)[0]
        if len(incorrect_spacing_idx) > 0:
            first_incorrect_spacing = spacing[incorrect_spacing_idx[0]]
            time_index = incorrect_spacing_idx[0]

            lat_var = dataset.variables['lat'] if 'lat' in dataset.variables else None
            lon_var = dataset.variables['lon'] if 'lon' in dataset.variables else None

            lat_value = get_variable_info(lat_var, 0) if lat_var is not None else 'N/A'
            lon_value = get_variable_info(lon_var, 0) if lon_var is not None else 'N/A'

            time_value = get_variable_info(time_var, time_index) if time_var is not None else 'N/A'
            lat_variable_info = get_variable_info(lat_var, 0) if lat_var is not None else 'N/A'
            lon_variable_info = get_variable_info(lon_var, 0) if lon_var is not None else 'N/A'

            messages.append(
                f"Incorrect spacing between 'time' variable values. First incorrect spacing: {first_incorrect_spacing}. "
                f"Dimension info: {{Time: {time_value}, Lat: {lat_value}, Lon: {lon_value}}}. "
                f"Variable info at location: {{Time: {time_value}, Lat: {lat_variable_info}, Lon: {lon_variable_info}}}."
            )
            success = False

    dataset.close()

    if success:
        return TestResult(True)
    else:
        return TestResult(False, messages)
