import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// let studentNames = [
//   "Abeenesh",
//   "Blessing",
//   "Dhivyesh",
//   "Jatin",
//   "Khavind",
//   "Nilesh",
//   "Tushil",
// ];

// console.log(studentNames);
// const [
//   studentOne,
//   studentTwo,
//   studentThree,
//   studentFour,
//   studentFive,
//   studentSix,
//   sutdentSeven,
// ] = studentNames;
// // studentNames[2] = "Vincent";
// // studentThree = "Vincent";
// console.log(studentThree, sutdentSeven);
// // studentNames[4] = "Nilesh";
// // studentNames[6] = "Sanjiv";
// // console.log(studentNames);

const family = {
  dad: "Tushil",
  mom: "Priyanka",
  daughter: "Claire",
  son: "MariClair",
  pet: "Nemo",
};
console.log(family);
var { dad, mom, daughter, pet } = family;
// family.dad = "Jatin";
dad = "Jatin";
// family.pet = "Pepper";
// pet = "Pepper";
console.log(dad, mom, daughter, pet);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
