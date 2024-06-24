import pandas as pd

def allocate_rooms(group_info_file, hostel_info_file):
    group_info = pd.read_csv(group_info_file)
    hostel_info = pd.read_csv(hostel_info_file)

    allocated_rooms = {}

    for index, group_row in group_info.iterrows():
        group_id = group_row['ID']
        group_size = group_row['Number of Members']
        group_gender = group_row['Gender']

        filtered_hostel_info = hostel_info[(hostel_info['Gender Accommodation'] == group_gender) & (hostel_info['Capacity'] >= group_size)]

        for _, hostel_row in filtered_hostel_info.iterrows():
            hostel_name = hostel_row['Name']
            room_number = hostel_row['Room Number']

            if hostel_name not in allocated_rooms:
                allocated_rooms[hostel_name] = {}

            if room_number not in allocated_rooms[hostel_name]:
                allocated_rooms[hostel_name][room_number] = []

            if len(allocated_rooms[hostel_name][room_number]) + group_size <= hostel_row['Capacity']:
                allocated_rooms[hostel_name][room_number].append(group_id)
                break

    return allocated_rooms, group_info, hostel_info

# Call the function with the file paths
allocated_rooms, group_info, hostel_info = allocate_rooms('data/group_info.csv', 'data/hostel_info.csv')