/**
 * Author: Tsen Chee Vincent LEUNG YIN KO
 * Email: sdlkjslkjglksjglkjsdg
 * Date Created: 2023/05/08
 * Last Modified: 2023/05/08
 * Version: 0.0.1
 * Filename: lecture.js
 * Company:
 * Description:
 */

// let x = 10;
// function autoexecute() {
//   let x = 1;
// }
// console.log(x);

// function doSomething() {
//   console.log(x); //undefined
//   var x = 1;
//   console.log("x: ", x); //x: 1
// }
// doSomething();

// function doSomething() {
//   console.log(x);
//   let x = 1;
// }
// doSomething();

// function doSomething() {
//   var x = 1;
//   var x = 2;
//   console.log("x: ", x); //x: 2
// }
// doSomething();

// function doSomething() {
//   let x = 1;
//   console.log(x);
//   let x = 2;
//   console.log(x);
// }
// doSomething();

// const num = 8;
// const num = 10;

// console.log(num);

// {
//   console.log("Hello this is a block");
// }

// let y = 1;
// {
//   let x = 2;
//   console.log("x : ", x); //x: 2
//   y = 10;
// }
// console.log("y : ", y); //x: 1

// var x = 1;
// {
//   var x = 2;
//   console.log("x : ", x); //x: 2
//   x = 10;
// }
// console.log("x : ", x); //x: 1

// function checkAge(age) {
//   var message;
//   if (age < 18) {
//     message = "Sorry, you're too young.";
//   } else {
//     message = "Yay! You're old enough!";
//   }

//   return message;
// }

// console.log(checkAge(16));
// console.log(message);
// console.log(sdfkshdkfjsdkjfhksdjfkjsdhfjksdhflkhsdlfsd);

// function numbers() {
//   for (let i = 0; i < 5; i += 1) {
//     console.log("Inner: " + i);
//   }
//   console.log("Outer: " + i);
// }
// numbers();

// function multiply(a, b = 100) {
//   // print the value of a and b to the console
//   console.log("a: " + a);
//   console.log("b: " + b);

//   return a * b;
// }

// console.log(multiply(5, 2));
// //expected output: 10

// console.log(multiply(5));
// //expected output: 5

// function getFee(isMember) {
//   // if (isMember) {
//   //   return "$2.00";
//   // } else {
//   //   return "$10.00";
//   // }

//   return isMember ? "$2.00" : "$10.00";
// }

// console.log(getFee(true));
// // expected output: "$2.00"

// console.log(getFee(false));
// // expected output: "$10.00"

// console.log(getFee(1));
// // expected output: "$2.00"
// // because Boolean(1) is true

// function checkYear(year) {
//   // if (year > 2000) {
//   //   console.log("You are in the 21st century");
//   // } else {
//   //   console.log("You live in the Middle Age");
//   // }
//   year > 2000
//     ? console.log("You are in the 21st century")
//     : {console.log("You live in the Middle Age")console.log("You live in the Middle Age")console.log("You live in the Middle Age")};
// }

// checkYear(1);

// /**
//  * Calculate the result of an operation on two values.
//  *
//  * @param {Number} x Value 1.
//  * @param {Number} y Value 2.
//  * @param {String} op Operator to apply.
//  * @return {Number|null} The result if the operator is valid. null if operator invalid.
//  *
//  * Example: calculator(10, 20 "-") will return 10 - 20, i.e. -10
//  *
//  */
// const calculator = (x, y, op) => {
//   let result;

//   op == "+"
//     ? (result = x + y)
//     : op == "-"
//     ? (result = x - y)
//     : op == "*"
//     ? (result = x * y)
//     : op == "/"
//     ? (result = x / y)
//     : (result = null);

//   return result;
// };

// console.log(calculator(10, 20, "2349832498"));

// let greeting = "Hello world";
// console.log(
//   greeting +
//     ", \
// \
// \
// \
// \
// this is a string"
// );
// console.log(`${greeting},

// this is a string`);

// let x = 10;
// let y = 50;
// console.log("The result is: " + (x + y));
// console.log(`The result is: ${x + y}`);

// const show = (x, y) => x + y;
// console.log(show(10, 20));

// const testFunc = () => {
//   let xString = "default";
//   console.log("The string is: " + xString);
// };
// testFunc("tessdgfdgdft", "tessdgfdgdft", 234972359832);

// const testFunc = function (x) {
//   return x;
// };

// console.log(testFunc(100));

// const arrowFunc = (x) => x;
// console.log(arrowFunc(500));

// const myArray = [2, 3, 4, 5, 6];

// // //1st example with arrow function
// // myArray.forEach((number, index) => {
// //   console.log("number: ", number); // logs each element of the array
// //   console.log("index: ", index); // logs each index of the array
// // });

// // myArray.forEach((vaskdhfksdf, uyuytuy) => {
// //   // console.log("number: ", number); // logs each element of the array
// //   console.log("value: ", vaskdhfksdf); // logs each index of the array
// // });

// //2nd example with arrow function
// myArray.forEach((number, i, arr) => {
//   arr[i] = arr[i] * 2;
// });

// console.log(myArray);
// // //output : [ 4, 6, 8, 10, 12 ]

// // //2nd example with function expression
// myArray.forEach(function (number, i, arr) {
//   arr[i] = number * 2;
// });

// console.log(myArray);
// // //output : [ 4, 6, 8, 10, 12 ]

// const numbers = [10, 11, 12, 15, 20];

// // numbers.forEach((number) => {
// //   if (number % 2 == 0) {
// //     // EVEN
// //     console.log(number);
// //   } else {
// //     // OOD
// //   }
// // });

// // numbers.forEach((x) => (x % 2 == 0 ? console.log(x) /*Even*/ : null /* Odd*/));

// console.log(
//   numbers.some((el) => {
//     return result == 10;
//   })
// );

// let containsTen = false;
// for (let i = 0; i < numbers.length; i++) {
//   if (numbers[i] == 10) {
//     containsTen = true;
//     break;
//   }
// }
// console.log(containsTen);

// const words = ["hwow", "sdgdsghey", "hbye"];

// // Check if any word starts with the letter 'h'
// console.log(words.some((value) => value[0] === "h"));

// // Check if all word starts with the letter 'h'
// console.log(words.every((value) => value[0] === "h"));
