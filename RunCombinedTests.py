from CheckLatAndLong import check_nc_lat_long
from CheckTime import check_nc_time
import os

def run_combined_tests(file_paths):
    results = []
    for file_path in file_paths:
        lat_long_result = check_nc_lat_long(file_path)
        time_result = check_nc_time(file_path)
        results.append((file_path, lat_long_result, time_result))
    return results

def write_results_to_file(results, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for file_path, lat_long_result, time_result in results:
            output_file.write(f"{file_path}:\n")

            # Write latitude and longitude test results
            output_file.write("  Latitude and Longitude Check Passed\n" if lat_long_result.success else "  Latitude and Longitude Check Failed\n")
            for message in lat_long_result.messages:
                output_file.write(f"    - {message}\n")

            # Write time test results
            output_file.write("  Time Check Passed\n" if time_result.success else "  Time Check Failed\n")
            for message in time_result.messages:
                output_file.write(f"    - {message}\n")

def main():
    # List of file paths to check
    file_paths = [
        'TestDataGeneration/TestDataStorage/test_correct_data.nc'
    ]

    # Run combined tests
    combined_results = run_combined_tests(file_paths)

    # Write results to file
    output_file_path = 'TestDataGeneration/combined_test_results.txt'
    write_results_to_file(combined_results, output_file_path)
    print(f"Combined test results written to {output_file_path}")

if __name__ == "__main__":
    main()