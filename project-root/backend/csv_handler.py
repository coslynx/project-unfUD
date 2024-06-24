import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

def merge_csv_files(group_info_file, hostel_info_file):
    group_info = read_csv(group_info_file)
    hostel_info = read_csv(hostel_info_file)
    return pd.merge(group_info, hostel_info, on='ID')

def allocate_rooms(merged_data):
    # Logic for room allocation based on specific criteria
    # Group members with the same ID stay together
    # Boys and girls stay in their respective hostels
    # Ensure room capacity is not exceeded

    return allocated_rooms_data

def generate_allocation_details_csv(allocated_data, output_file):
    allocated_data.to_csv(output_file, index=False)