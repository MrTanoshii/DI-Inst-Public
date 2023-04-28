// Get user input
const userInput = prompt("Please enter a few words");
console.log("Input: " + userInput);

// Turn into an array of words
const wordArray = userInput.split(",");
console.log(wordArray);

let i = 0;
let longestWordLength = 0;
// Loop to find the longest word length
while (i < wordArray.length) {
  if (longestWordLength < wordArray[i].length) {
    longestWordLength = wordArray[i].length;
  }
  i++;
}

// Log box top
let boxTop = "";
// Add stars to match the longest word
for (let j = 0; j < longestWordLength + 4; j++) {
  boxTop += "*";
}
console.log(boxTop);

// Loop through the array and log the word (the box content)
i = 0;
while (i < wordArray.length) {
  let outputString = "";

  outputString += "* ";
  outputString += wordArray[i].trim();

  // Add whitespaces to match the longest word
  for (let j = 0; j < longestWordLength - wordArray[i].length; j++) {
    outputString += " ";
  }

  outputString += " *";

  console.log(outputString);
  i++;
}

// Log box bottom
let boxBottom = "";
boxBottom += "**";
// Add stars to match the longest word
for (let j = 0; j < longestWordLength; j++) {
  boxBottom += "*";
}
boxBottom += "**";
console.log(boxBottom);
