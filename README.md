# Developers Institute Public Repo

## Table of Contents

- [Mauritius Python 95 - Full Time - January 2023](/MRU_PY%2395_FT_JAN_2023/)
  - [Week 4 - Python and Web Programming](/MRU_PY%2395_FT_JAN_2023/week_4/)
    - [Day 1 - Starting with Python](/MRU_PY%2395_FT_JAN_2023/week_4/day_1/)
    - [Day 2 - List, iterating and formatting data ](/MRU_PY%2395_FT_JAN_2023/week_4/day_2/)
    - [Day 3 - Dictionaries](/MRU_PY%2395_FT_JAN_2023/week_4/day_3/)
    - [Day 4 - Functions](/MRU_PY%2395_FT_JAN_2023/week_4/day_4/)
- [Mauritius JavaScript 96 - Part Time - January 2023](/MRU_JS%2396_PT_JAN_2023/)
- [Mauritius Javascript 106 - Full Time - April 2023](/MRU_JS%23106_FT_APR_2023/)

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
