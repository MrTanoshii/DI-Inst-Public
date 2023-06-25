// If my score is 80+, I get a "Well done"
// If my score is 79 - 60, I get a "Solid effort"
// Else I get a "Whatever"

const grade = 7;

// Basic if-else
if (grade >= 80) {
  console.log("Well done");
  // } else if (grade < 80 && grade >= 60) {
} else if (grade >= 60) {
  console.log("Solid effort");
} else {
  console.log("Whatever");
}

// Ternary
// statement ? if true : if false

grade >= 80
  ? console.log("Well done")
  : grade >= 60
  ? console.log("Solid effort")
  : console.log("Whatever");

const isPet = true;
const isCat = false;
const isDog = false;

// That animal is my pet/stray and it is a dog/cat

let outputStr = "That animal is ";
if (isPet) outputStr += "my pet";
else outputStr += "stray";
outputStr += " and it is a ";
if (isCat) outputStr += "cat";
else if (isDog) outputStr += "dog";

console.log(outputStr);

if (isPet && isCat) {
  console.log("That animal is my pet and it is a cat");
} else if (isPet && isDog) {
  console.log("That animal is my pet and it is a dog");
} else if (!isPet && isCat) {
  console.log("That animal is stray and it is a cat");
} else if (!isPet && isDog) {
  console.log("That animal is stray and it is a dog");
}

outputStr = "That animal is ";
if (isPet && (isDog || isCat)) {
  outputStr += "my pet";
  outputStr += " and it is a ";
  if (isCat) outputStr += "cat";
  else if (isDog) outputStr += "dog";
} else {
  outputStr += "stray";
  outputStr += " and it is a ";
  if (isCat) outputStr += "cat";
  else if (isDog) outputStr += "dog";
}
console.log(outputStr);

console.log(
  `That animal is ${isPet ? "my pet" : "stray"} and it is a ${
    isCat ? "cat" : isDog ? "dog" : "undefined"
  }`
);

// optional chaining

const student = {
  firstName: "Nilesh",
  email: "Nilesh@email.email",
  favorite: {
    food: "Pizza",
    car: "Toyota Rav4",
  },
};

console.log(student);
console.log(student?.email);
console.log(student?.preferred?.pet);
