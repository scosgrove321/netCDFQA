import netCDF4 as nc
import numpy as np
from TestResult import TestResult

def open_dataset(file_path):
    try:
        return nc.Dataset(file_path, mode='r')
    except Exception as e:
        raise Exception(f"An error occurred while opening the dataset: {str(e)}")

def read_lat_variables(dataset):
    try:
        latitudes = dataset.variables['lat'][:]
        return latitudes
    except KeyError:
        raise KeyError("Latitude variable not found in the dataset.")
    except Exception as e:
        raise Exception(f"An error occurred while reading latitude variables: {str(e)}")

def read_lon_variables(dataset):
    try:
        longitudes = dataset.variables['lon'][:]
        return  longitudes
    except KeyError:
        raise KeyError("Longitude variable not found in the dataset.")
    except Exception as e:
        raise Exception(f"An error occurred while reading longitude variables: {str(e)}")

def calculate_min_max(latitudes, longitudes):
    min_lat = latitudes.min()
    max_lat = latitudes.max()
    min_lon = longitudes.min()
    max_lon = longitudes.max()
    return min_lat, max_lat, min_lon, max_lon

def find_unique_counts(latitudes, longitudes):
    unique_lats, counts_lats = np.unique(latitudes, return_counts=True)
    unique_lons, counts_lons = np.unique(longitudes, return_counts=True)
    return unique_lats, counts_lats, unique_lons, counts_lons

def check_multiple_counts(unique_lats, counts_lats, unique_lons, counts_lons):
    lat_multiple_counts = {lat: count for lat, count in zip(unique_lats, counts_lats) if count > 1}
    lon_multiple_counts = {lon: count for lon, count in zip(unique_lons, counts_lons) if count > 1}
    return lat_multiple_counts, lon_multiple_counts

def check_spacing(latitudes, longitudes):
    lat_spacing = np.diff(latitudes)
    lon_spacing = np.diff(longitudes)

    # Find indices of non-conforming spacings
    lat_indices = np.where(lat_spacing != 1)[0]
    lon_indices = np.where(lon_spacing != 1)[0]

    # Retrieve corresponding values for latitude
    lat_spacing_error = latitudes[1:][lat_indices]  # First incorrect latitude

    # Retrieve corresponding values for longitude
    lon_spacing_error = longitudes[1:][lon_indices]  # First incorrect longitude

    return lat_spacing_error, lon_spacing_error

def check_expected_ranges(min_lat, max_lat, min_lon, max_lon):
    expected_min_lat = -89.5
    expected_max_lat = 89.5
    expected_min_lon = -179.5
    expected_max_lon = 179.5
    messages = []
    if min_lat != expected_min_lat:
        messages.append(f"Latitude minimum value differs from expected range. Expected Min: {expected_min_lat}, Actual Min: {min_lat}")
    if max_lat != expected_max_lat:
        messages.append(f"Latitude maximum value differs from expected range. Expected Max: {expected_max_lat}, Actual Max: {max_lat}")
    if min_lon != expected_min_lon:
        messages.append(f"Longitude minimum value differs from expected range. Expected Min: {expected_min_lon}, Actual Min: {min_lon}")
    if max_lon != expected_max_lon:
        messages.append(f"Longitude maximum value differs from expected range. Expected Max: {expected_max_lon}, Actual Max: {max_lon}")
    return messages

def check_unique_counts(lat_multiple_counts, lon_multiple_counts):
    messages = []
    if lat_multiple_counts:
        lat_error = "\n".join([f"Latitude: {lat}, Count: {count}" for lat, count in lat_multiple_counts.items()])
        messages.append(f"Latitude values that appear more than once:\n{lat_error}")
    if lon_multiple_counts:
        lon_error = "\n".join([f"Longitude: {lon}, Count: {count}" for lon, count in lon_multiple_counts.items()])
        messages.append(f"Longitude values that appear more than once:\n{lon_error}")
    return messages

def check_spacing_errors(lat_spacing_error, lon_spacing_error):
    messages = []
    if len(lat_spacing_error) > 0:
        lat_spacing_error_message = f"Latitudes are not spaced by 1 degree. First offending value: {lat_spacing_error[0]}"
        messages.append(lat_spacing_error_message)
    if len(lon_spacing_error) > 0:
        lon_spacing_error_message = f"Longitudes are not spaced by 1 degree. First offending value: {lon_spacing_error[0]}"
        messages.append(lon_spacing_error_message)
    return messages

def close_dataset(dataset):
    dataset.close()

def check_nc_lat_long(file_path):
    messages = []
    try:
        dataset = open_dataset(file_path)
        latitudes = read_lat_variables(dataset)
        longitudes = read_lon_variables(dataset)
        min_lat, max_lat, min_lon, max_lon = calculate_min_max(latitudes, longitudes)
        unique_lats, counts_lats, unique_lons, counts_lons = find_unique_counts(latitudes, longitudes)
        lat_multiple_counts, lon_multiple_counts = check_multiple_counts(unique_lats, counts_lats, unique_lons, counts_lons)
        lat_spacing_error, lon_spacing_error = check_spacing(latitudes, longitudes)

        # Check expected range
        messages.extend(check_expected_ranges(min_lat, max_lat, min_lon, max_lon))

        # Check for unique counts
        messages.extend(check_unique_counts(lat_multiple_counts, lon_multiple_counts))

        # Process spacing errors
        messages.extend(check_spacing_errors(lat_spacing_error, lon_spacing_error))

        close_dataset(dataset)
    except Exception as e:
        messages.append(f"An error occurred while checking the file: {str(e)}")

    if messages:
        return TestResult(False, messages)
    else:
        return TestResult(True)
