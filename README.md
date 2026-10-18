# Habit Tracker

A simple desktop application for tracking daily habits, built with Python, CustomTkinter, and SQLite.

## Features

- Add and delete habits
- Track daily progress for the last 7 days
- Mark habits as completed using checkboxes
- Track consecutive days with a habit streak counter
- View daily completion statistics
- Save habits and progress in a local SQLite database
- Dark theme with a green accent color

## Technologies Used

- **Python** — application logic
- **CustomTkinter** — graphical user interface
- **SQLite** — local database
- **datetime** — date calculations and streak tracking
- **os** — database file path management

## Requirements

- Python 3.10 or newer
- CustomTkinter

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Open the project folder:

   ```bash
   cd habit-tracker
   ```

3. Install the required dependency:

   ```bash
   pip install customtkinter
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## How to Use

1. Launch the application.
2. Enter the name of a habit, such as "Read for 20 minutes".
3. Click **Add** to create the habit.
4. Check the boxes for the days when you complete the habit.
5. Monitor your current streak and daily completion statistics.
6. Delete a habit when you no longer need to track it.

## Data Storage

The application uses SQLite to store habits and their completion history locally. Your progress remains saved between sessions.

## Project Structure

```text
habit-tracker/
├── main.py
├── habit_tracker.db
├── requirements.txt
└── README.md
```

The database file is created automatically when the application runs.

## License

This project is available for personal and educational use.
