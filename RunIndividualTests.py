from CheckLatAndLong import check_nc_lat_long
from CheckTime import check_nc_time
import os

def run_lat_long_tests(file_paths):
    results = []
    for file_path in file_paths:
        result = check_nc_lat_long(file_path)
        results.append((file_path, result))
    return results

def run_time_tests(file_paths):
    results = []
    for file_path in file_paths:
        result = check_nc_time(file_path)
        results.append((file_path, result))
    return results

def write_results_to_file(results, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for file_path, result in results:
            output_file.write(f"{file_path}:\n")
            output_file.write("  Check Passed\n" if result.success else "  Check Failed\n")
            for message in result.messages:
                output_file.write(f"    - {message}\n")

def main():
    # List of file paths to check
    lat_long_file_paths = [
        'TestDataGeneration/TestDataStorage/test_correct_data.nc',
        'TestDataGeneration/TestDataStorage/test_fail_min_lat.nc',
        'TestDataGeneration/TestDataStorage/test_fail_max_lat.nc',
        'TestDataGeneration/TestDataStorage/test_fail_min_lon.nc',
        'TestDataGeneration/TestDataStorage/test_fail_max_lon.nc',
        'TestDataGeneration/TestDataStorage/test_fail_multiple_lat.nc',
        'TestDataGeneration/TestDataStorage/test_fail_multiple_lon.nc',
        'TestDataGeneration/TestDataStorage/test_fail_spacing_lat.nc',
        'TestDataGeneration/TestDataStorage/test_fail_spacing_lon.nc',
        'TestDataGeneration/TestDataStorage/test_pass_lat_long.nc'
    ]

    time_file_paths = [
        'TestDataGeneration/TestDataStorage/test_correct_data.nc',
        'TestDataGeneration/TestDataStorage/test_fail_missing_time_dim.nc',
        'TestDataGeneration/TestDataStorage/test_fail_missing_time_var.nc',
        'TestDataGeneration/TestDataStorage/test_fail_wrong_length.nc',
        'TestDataGeneration/TestDataStorage/test_fail_wrong_spacing.nc',
        'TestDataGeneration/TestDataStorage/test_fail_wrong_values.nc',
        'TestDataGeneration/TestDataStorage/test_pass_time.nc'
    ]

    # Run tests for latitude and longitude files
    lat_long_results = run_lat_long_tests(lat_long_file_paths)
    lat_long_output_file_path = 'TestDataGeneration/lat_long_test_results.txt'
    write_results_to_file(lat_long_results, lat_long_output_file_path)
    print(f"Latitude and Longitude test results written to {lat_long_output_file_path}")

    # Run tests for time files
    time_results = run_time_tests(time_file_paths)
    time_output_file_path = 'TestDataGeneration/time_test_results.txt'
    write_results_to_file(time_results, time_output_file_path)
    print(f"Time test results written to {time_output_file_path}")

if __name__ == "__main__":
    main()