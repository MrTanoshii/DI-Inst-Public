## Concepts to cover on Friday

### Project 1

#### Features

- JavaScript
  - Ternary Operator
  - &&
  - ||
  - Chaining
- NodeJS
- Databases
- Promises
- API (dev & call)

##### Ternary Operator

```js
const isValid = true;
const someState = {};

if (isValid) {
  console.log("Valid");
  saveToDatabase(someState);
} else {
  console.log("Invalid");
  invalidAnswerAndPrompt("Invalid Message Here");
}

isValid ? console.log("Valid") : console.log("Invalid");
```

#### Description

A simple website that downloads website favicons and stores them in a PostgreSQL db.
Provides an API endpoint to return the favicons.
API limits return to 10 favicons per page.
[Bonus] If the requested favicon is not available/stored, download it, store it and return it.

### Project 2

#### Features

- API (call)
- JSON
- ReactRouter
- Redux
- Material UI

#### Description

Display the favicons in a React app in pages of 10/25.
Have the ability to provide comments to a favicon entry.
Have the ability to delete a favicon entry.

### Project 3

#### Features

- Deploy projects

#### Description

Deploy the projects.
Potential hosts: Render/Amazon/Vercel/Heroku

### Project 4

#### Features

- Node
- Mongodb
- D3 https://www.npmjs.com/package/d3
- TailwindCSS

#### Description

A simple turn-based game where students are studying at a school.
A student has a starting energy and studiesProgress.
Activities drain student energyy and improve/worsen studies progress.
Students that reach 0 energy sleep for 4 turns.
Students that reach 100 studies progress graduate. (graduate means special icon and no more activities)
The database holds the students and their stats.
The database holds activities.
Use https://observablehq.com/@d3/radial-stacked-bar-chart to display the popularity of different activities.
