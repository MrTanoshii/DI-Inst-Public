# Teams

| Team Name                | Teammate  | Ideas    |
| ------------------------ | --------- | -------- |
| KTSM                     | Khavind   | Jarvis   |
|                          | Tushil    |          |
|                          | Shabneez  |          |
|                          | Martine   |          |
|                          |           |          |
| Fruit Ninja              | Jacob     |          |
|                          | Yushi     |          |
|                          | Soubhug   |          |
|                          |           |          |
| Link The Megatron Clowns | Sebastien |          |
|                          | Ra'ees    |          |
|                          | Alexis    | News API |
|                          | David     |          |
|                          |           |          |
|                          | Cynthia   |          |

# Ideas

## Team KTSM

### Jarvis

A conversational agent

#### Technology

- Python
- Database
- (Optional) Machine Learning

#### Features

- Understand different Natural languages (English, French)
- Similar in function to ChatGPT but of course not inclusive of all functions
- Conversation
- (Optional)

## Team Link The Clowns

### News API

#### Technology

- Database
- Python
- API
- Website (HTML, CSS, JS)

#### Features

- Download news from API, save to DB
- Push news to twitter
- Display news on website
- Statistics: scan the news, keep a list of most used keywords
- Use matplotlib to generate a few interesting graphics (at least 4)
- Have a dark theme and a light theme
- Constraint: Use Tailwindcss or SASS
- Constraint: The website needs a unified look/feel

### Data Manager / File Merger

#### Technology

- Web app

## Team Fruit Ninja

Potential frameworks: Pygame, Ren'Py, Arcade?

### Snake / Memory game

#### Technology

- Web (HTML, CSS, JS)
- Python
- (Optional) OOP

#### Features (Memory game)

-

#### Features (Snake game)

-

## Team

## From Vincent

### Pokemon shop (Database and API oriented)

Make an item shop in Python using data from https://pokeapi.co/docs/v2#items-section

1. Have the ability to sync/download the data from the api into a local database (Postgres, Mysql, Sqlite, etc)
2. Provide the user with funds
3. Allow them to make purchases
4. Keep a list of purchased items
5. (Optional) Use matplotlib to display a pie chart of funds (used/unused)
6. (Optional) Use matplotlib to display a pie chart of purchased broken down in categories https://pokeapi.co/docs/v2#item-categories

### Celebrity database (OOP)

1. Retrieve information from https://api-ninjas.com/api/celebrity
2. Save info to a DB
3. Make a `Celebrity` class
   1. Have the following class methods `get_name()`, `get_networth()`, `get_gender()`, `get_nationality()`, `get_occupation()`
   2. Also have the following class methods to display information about a list of celebrities `get_total_networth()`, `display_statistics()`
   3. `get_total_networth()` will add all the celebrity networths and display them onscreen
   4. `display_statistics()` will use matplotlib to create graphics (e.g. total networth by gender/nationality pie chart, nationality pie chart) & generate a Markdown file (`.md`) to display the information (See https://www.markdownguide.org/basic-syntax/#images-1 for images)
4. (Optional\_ Make classes related to jobs (e.g. `Singer`, `Actor`, `Polician`) which inherit the `Celebrity` class and have at least 1 method in them that is unique to their relevant jobs

### Predict which year the average temperature of X country will be above 40 deg C (Machine learning)

https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data

1. Use matplotlib to graph the model data
2. Graph model
3. Graph the prediction
4. With all labels/legends/titles/blahblah
