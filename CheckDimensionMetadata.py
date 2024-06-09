def check_dimension_metadata(dim_name, dim_length, expected_name, expected_length):
    if dim_name != expected_name and dim_name.lower() == expected_name.lower():
        print(f"Incorrect casing for {expected_name} dimension. Expected: {expected_name}, Actual: {dim_name}")
    if dim_length < expected_length:
        print(f"Incorrect length for {expected_name} dimension. Expected: {expected_length}, Actual: {dim_length}")

