import { createServer } from "node:http";

const test_server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello Sanjiv ES6");
}).listen(8080);

console.log("This is running");
