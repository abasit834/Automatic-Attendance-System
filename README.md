# Automatic Attendance System using OpenCV, LBPH, and MySQL

## Project Overview

The Automatic Attendance System utilizes OpenCV for facial recognition and the Local Binary Patterns Histograms (LBPH) algorithm to mark attendance automatically. This project aims to streamline the process of taking attendance in various settings such as schools, colleges, and offices, providing a more efficient and accurate solution compared to traditional methods.

## Features

- **Face Detection**: Detects faces in real-time using a camera.
- **Face Recognition**: Identifies individuals using the LBPH algorithm.
- **Attendance Logging**: Automatically marks attendance and logs it into a MySQL database.
- **User Management**: Add, update, and delete user data.
- **Reporting**: Generate attendance reports.
- **Modules**:
  - Student Details
  - Face Detector
  - Attendance
  - Help Desk
  - Train Data
  - Photos
  - Developer Information
  - Exit

## Requirements

### Hardware

- A computer with a webcam or an external camera.

### Software

- Python 3.x
- OpenCV
- NumPy
- Pandas
- MySQL
- Tkinter (for GUI)
- mysql-connector-python

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abasit834/Automatic-Attendance-System
    cd automatic-attendance-system
    ```

2. **Install the required packages**:
    ```bash
    pip install opencv-python opencv-contrib-python numpy pandas mysql-connector-python
    ```

3. **Setup the MySQL database**:
    - Install MySQL and create a database named `attendance_system`.
    - Run the following SQL script to create necessary tables:
      ```sql
      CREATE DATABASE attendance_system;

      USE attendance_system;

      CREATE TABLE users (
          id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          face_data BLOB NOT NULL
      );

      CREATE TABLE attendance (
          id INT AUTO_INCREMENT PRIMARY KEY,
          user_id INT,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
          FOREIGN KEY (user_id) REFERENCES users(id)
      );
      ```

4. **Configure the database connection**:
    - Update the `config.py` file with your MySQL database credentials:
      ```python
      MYSQL_HOST = 'localhost'
      MYSQL_USER = 'yourusername'
      MYSQL_PASSWORD = 'yourpassword'
      MYSQL_DB = 'attendance_system'
      ```

## Usage

1. **Run the main application**:
    ```bash
    python main.py
    ```

2. **Adding Users**:
    - Navigate to the user management section in the application.
    - Enter the required details and capture the face using the camera.

3. **Marking Attendance**:
    - The system will automatically detect faces and mark attendance when users appear in front of the camera.

4. **Generating Reports**:
    - Navigate to the reports section and select the desired date range to generate attendance reports.

## Project Structure

automatic-attendance-system/
│
├── data/
│ ├── faces/ # Directory to store face images
│ └── attendance.db # SQLite database file
│
├── src/
│ ├── face_recognition.py # Face recognition logic using LBPH
│ ├── camera.py # Camera handling logic
│ ├── database.py # Database interaction logic
│ ├── gui.py # GUI handling logic using Tkinter
│ └── utils.py # Utility functions
│
├── config.py # Database configuration file
├── setup_database.py # Script to setup the initial database
├── main.py # Main script to run the application
├── requirements.txt # List of required packages
└── README.md # Project documentation

## Contributing

We welcome contributions from the community. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenCV for providing powerful computer vision tools.
- The community for their invaluable feedback and contributions.

