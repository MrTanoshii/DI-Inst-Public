// // Family app | family-app.js
// // -- Class person | person.js
// // -- Class family | family.js
// // -- Class car | car.js
// // -- Class pet | pet.js
// // -- Class job | job.js
// // -- Class house | house.js
// // -- Class hobby | hobby.js
// // -- Class food | food.js

// console.log("This works");

// import { greeting } from "./hello.js";
// // let hello = require("./hello.js");

// // console.log(hello.greeting);
// // console.info(hello.myDate());

// // ES6 Module
// import { helloStudent, getCurrentDate, listGames } from "./hello.mjs";

// console.log(helloStudent);
// console.log(getCurrentDate());

// listGames(
//   "Nilesh",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper",
//   "Valorant",
//   "FIFA",
//   "Spongebob",
//   "Rocket League",
//   "Minesweeper"
// );

// let AbeeneshObj = {
//   test: "test",
//   hello: () => {
//     console.log(this.greeting);
//   },
//   greeting: "Aloha",
// };

// console.log(AbeeneshObj);

// let JatinObj = {
//   ...AbeeneshObj,
//   hello: () => {
//     console.log(this.greeting);
//   },
//   greeting: "Ni Hao",
// };

// console.log(JatinObj);

let http = require("http");
let fs = require("fs");

const test_server = http
  .createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/plain");
    res.end("Hello Blessing");
  })
  .listen(8080);
