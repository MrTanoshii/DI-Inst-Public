// // Regular function
// function funcName1(param1, param2, var3, var4) {
//   // something here
//   const result = var3 + var4;
// }

// // Arrow function
// const funcName2 = (greetingMorning, goodbye) => {
//   // something here
//   console.log();
// };

// // Calling functions
// funcName1("Vincent", "Blessing", 5, 10);
// funcName2("Guten Tag", "Sayounara");

function scopeFunc() {
  let hello = "hello";
  if (true) {
    let hello = "goodbye";
    console.log(hello);
  }
  console.log(hello);
  let greeting = "Test greeting";

  return greeting;
}

const result = scopeFunc();
console.log(result);
