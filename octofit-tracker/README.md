# OctoFit Tracker

## Project Overview

The OctoFit Tracker is a fitness application designed to help users track their activities, manage teams, and receive personalized workout suggestions. The application includes features such as user authentication, activity logging, competitive leaderboards, and more.

## Project Structure

The project is organized into the following directories:

- **backend/**: Contains the server-side code and dependencies for the OctoFit Tracker application.
  - **venv/**: This directory contains the Python virtual environment for the OctoFit Tracker application. It includes all the necessary packages and dependencies isolated from the global Python environment.
  - **octofit_tracker/**: This directory will contain the main application code for the OctoFit Tracker backend. It will include Django models, views, and other components necessary for the application.
  - **requirements.txt**: This file lists the required Python packages for the OctoFit Tracker project. It includes specific versions of packages such as Django, djangorestframework, and others necessary for the application to function properly.

- **frontend/**: This directory is intended for the frontend part of the OctoFit Tracker application. It will contain the code and assets for the user interface.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd octofit-tracker
   ```

2. **Create a Python virtual environment**:
   ```
   python3 -m venv backend/venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```
     source backend/venv/bin/activate
     ```
   - On Windows:
     ```
     backend\venv\Scripts\activate
     ```

4. **Install the required packages**:
   ```
   pip install -r backend/requirements.txt
   ```

5. **Run the application**:
   - Follow the instructions in the backend directory to start the Django server and set up the database.

## Usage Guidelines

- Users can create profiles, log activities, and manage teams through the application interface.
- The competitive leaderboard allows users to track their progress against others.
- Personalized workout suggestions will be provided based on user activity and preferences.

## Contributing

Contributions to the OctoFit Tracker project are welcome! Please submit a pull request or open an issue for any suggestions or improvements.