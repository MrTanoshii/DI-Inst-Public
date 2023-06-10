const lib = require("./lecture_library.js");

console.log("Hello Previn");

let result = lib.Sum(10, 55);
console.debug(result);

result = lib.Sum(50, 250);
console.debug(result);

console.log(lib.Sub(100, 50));

// Module types
// -- Core
// -- Local
// -- External

// Common Modules - require()
// ES6 Modules - import

console.log("Hello Everyone");

// Core module `http` already available in NodeJS
const http = require("http");

// To note, the enduser does not see our script!
const server = http.createServer((req, res) => {
  console.log("Hello Ashley & Kovesh");
  res.statusCode = 200;
  res.write("<h1>Hello Malala</h1>");
  res.write(`The result of 50 + 250 is ${result}`);
  res.end();
});
server.listen(3000);

// NPM
// Node Package Manager
