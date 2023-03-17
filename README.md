# Developers Institute Public Repo

For the class of Jan 2023 (MRU)

## Table of Contents

- [Week 4 - Python and Web Programming](/week_4/)
  - [Day 1 - Starting with Python](/week_4/day_1/)
  - [Day 2 - List, iterating and formatting data ](/week_4/day_2/)
  - [Day 3 - Dictionaries](/week_4/day_3/)
  - [Day 4 - Functions](/week_4/day_4/)

## How to create a new django project

```shell
# Create a virtual environment called "venv"
py -m venv venv

# Activate the virtual environment
./venv/Scripts/activate

# Install dependencies
pip install django

# If you have a requirements.txt you can also use
# pip install -r requirements.txt

# Make a new django project
django-admin startproject <my_project_name>

# Change your terminal directory to the project directory
cd <my_project_name>

# Make a new django app inside the django project
django-admin startapp <my_app_name>

# Run the django server
py manage.py runserver [port_number (default is 8000)]

# Deactivate the virtual environment
deactivate
```
