const namesList = [
  "Vincent",
  "Blessing",
  "Nilesh",
  "Dhivyesh",
  "Abeenesh",
  "Jatin",
];

// Method 1, for loop
// for (let i = 0; i < namesList.length; i++) {
//   console.log("Good morning " + namesList[i]);
// }

// Method 2, while loop
// let i = 0;
// while (i < namesList.length) {
//   console.log("Good morning " + namesList[i]);
//   i++;
// }

// Method 3, foreach loop
// namesList.forEach((el) => {
//   console.log("Good morning " + el);
// });

// Method 4, for in loop
// for (const i in namesList) {
//   console.log("Good morning " + namesList[i]);
// }

namesList.forEach((ele) => {
  console.log("Hello world " + ele);
});
