let color = null;
let mousedown = false;

let body = document.getElementsByTagName("body")[0];
let color_blocks = document.querySelectorAll("#sidebar > *");

{
  /* <html>
  <head></head>

  <body>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
  </body>
</html>; */
}

for (let i = 0; i < 200; i++) {
  // create
  // add to dom
}

querySelector("div"); // Single object/element, first element
querySelectorAll("div"); // Array of objects/elements

let fill_blocks = document.querySelectorAll("#main > *");
let clear_button = document.getElementsByTagName("button")[0];

clear_button.addEventListener("click", function () {
  for (fill_block of fill_blocks) {
    fill_block.style.backgroundColor = "white";
  }
});

body.addEventListener("mousedown", function () {
  mousedown = true;
});

body.addEventListener("mouseup", function () {
  mousedown = false;
});

for (color_block of color_blocks) {
  color_block.addEventListener("click", function (event) {
    color = event.target.style.backgroundColor;
  });
}

for (fill_block of fill_blocks) {
  // Mouse down on a block
  fill_block.addEventListener("mousedown", function (event) {
    if (color != null) event.target.style.backgroundColor = color;
  });

  // Drag & paint
  fill_block.addEventListener("mouseover", function (event) {
    if (mousedown && color != null) event.target.style.backgroundColor = color;
  });
}

const petArray = [
  "dog",
  "cat",
  "fish",
  "monkey",
  "turtle",
  "dolphin",
  "shark",
  "orca",
  "hedgehog",
];
for (let x = 0; x < petArray.length; x++) {
  console.log(petArray[x]);
}

let username = "Vincent";
let password = "Supersecretpass";

if (fUsername == username && fPassword == password) {
  // SUCCESSFUL LOGIN
}

// var x;
// let y;
// const z;

// var PascalCase;
// var camelCase;
// var snake_case;
// var lowercase;
// var UPPERCASE;
