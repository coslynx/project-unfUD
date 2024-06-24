import os
from flask import Flask, request, jsonify
import pandas as pd
from csv_handler import read_csv, save_csv
from room_allocator import allocate_rooms

app = Flask(__name__)

@app.route('/upload_group_info', methods=['POST'])
def upload_group_info():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        group_info_df = read_csv(file)
        return jsonify({'message': 'Group information uploaded successfully'})

@app.route('/upload_hostel_info', methods=['POST'])
def upload_hostel_info():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        hostel_info_df = read_csv(file)
        return jsonify({'message': 'Hostel information uploaded successfully'})

@app.route('/allocate_rooms', methods=['GET'])
def allocate_rooms_endpoint():
    if 'group_info_df' not in globals() or 'hostel_info_df' not in globals():
        return jsonify({'error': 'Group info or hostel info not uploaded'})
    
    allocation_df = allocate_rooms(group_info_df, hostel_info_df)
    save_csv(allocation_df, 'allocation_details.csv')
    
    return jsonify({'message': 'Rooms allocated successfully'})

if __name__ == '__main__':
    app.run(debug=True)