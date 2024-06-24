# Project Overview
- Develop a web application for digitalizing the hospitality process in group accommodations.
- Users can upload two CSV files to allocate rooms efficiently in hostels while adhering to specific criteria.

# Features
1. CSV File 1 (Group Information)
- Contains group details like ID, number of members, and gender.
- Various scenarios under the same ID: different group sizes and gender compositions.

2. CSV File 2 (Hostel Information)
- Includes hostel room details like name, room number, capacity, and gender accommodation.
- Specify rooms for boys and girls in different hostels.

3. Frontend Requirements
- User-friendly interface to upload both CSV files.
- Algorithm for room allocation based on specific criteria:
  - Group members with the same ID stay together.
  - Boys and girls stay in their respective hostels.
  - Ensure room capacity is not exceeded.

4. Output
- Display of allocated rooms with group members in each room.
- Downloadable CSV file with allocation details for reference.

# Enhancements
- Include a feature to optimize room allocation for maximum space utilization.
- Implement a visual representation of room allocation for better understanding.
- Add a feature to handle any conflicts or exceptions in the allocation process.

# Submission Requirements
- Complete project submission with source code.
- Brief documentation explaining logic and usage.
- Instructions for running the application smoothly.
- Create a public repository on Github and submit the link for evaluation.

# Programming Languages
- Backend: Python
- Frontend: HTML, CSS, JavaScript

# APIs
- Flask: To create the backend server and handle HTTP requests.
- Pandas: For data manipulation and CSV file handling in Python

# Packages/Libraries (latest versions)
- Flask (1.1.2)
- Pandas (1.1.3)
- Bootstrap (4.5.2)
- jQuery (3.5.1)
- Plotly (4.12.0)

# Rationale for Technical Choices
- Python: Widely used for data processing tasks like CSV handling.
- Flask: Lightweight and easy to set up for creating web applications.
- Pandas: Efficient for data manipulation, perfect for working with CSV files.
- Bootstrap: Ensures a responsive and visually appealing frontend design.
- jQuery: Simplifies DOM manipulation and event handling in the frontend.
- Plotly: Provides interactive visualizations for better user experience.

# Project Structure
- Backend: Python scripts to handle CSV file uploads, room allocation logic, and API endpoints.
- Frontend: HTML templates with Bootstrap for UI, JavaScript for client-side logic, and Plotly for visualizations.
- Integration: Flask API endpoints to communicate between backend and frontend for data processing and allocation.