# Automated-Backup
A lightweight Python automation script that performs daily backups of a specified directory, organizing backups by date. Designed to run on Linux systems (tested on Pop!_OS) and ideal for protecting project folders with minimal setup.

The script uses Python’s schedule library to trigger backups at a fixed time each day and shutil.copytree() to create a full directory snapshot. Each backup is stored in a date-named folder, ensuring clean versioned backups without overwriting previous days.

[+] Features
- Automatic daily backups at a scheduled time
- Date-based backup folders (YYYY-MM-DD)
- Preserves original directory structure
- Linux-friendly (Pop!_OS tested)
- Lightweight and easy to modify

[+] Tech Stack
- Python 3
- schedule
- shutil
- datetime

[+] Use Case
- Perfect for developers who want a simple, no-nonsense local backup solution for projects, configs, or important folders—especially useful during active development.

[+] How to run
- pip install schedule
- python backup.py 
