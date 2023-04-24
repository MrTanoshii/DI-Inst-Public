// Primitive types
var testStr = "Hello Dev Inst";
let test2Str = "Hello Dev Inst";
let testNum = 123;
let testBool = true; // True of False

// Non-primitive type
// Type: object
let testObj = {
  objName: "Test Object",
  objGreeting: "Hello Dev Inst",
  objNum: 50,
  objBool: false,
};

// Pass by values
let copyTestNum = testNum; // This makes an exact copy/clone
console.log(`testNum = ${testNum} | copyTestNum = ${copyTestNum}`);
testNum = 5; // The copy/clone is not affected
console.log(`testNum = ${testNum} | copyTestNum = ${copyTestNum}`);

let copyTestStr = testStr; // This makes an exact copy/clone
console.log(`testStr = ${testStr} | copyTestStr = ${copyTestStr}`);
testStr = "Goodbye Dev Inst"; // The copy/clone is not affected
console.log(`testStr = ${testStr} | copyTestStr = ${copyTestStr}`);

// Pass by reference
let copyTestObj = testObj; // This refers to the same object
console.log(
  `testObj.objName = ${testObj.objName} | copyTestObj.objName = ${copyTestObj.objName}`
);
testObj.objName = "DI Object"; // The copy/clone is affected
// testObj.objNum = 6;
console.log(
  `testObj.objName = ${testObj.objName} | copyTestObj.objName = ${copyTestObj.objName}`
);

// Pass by reference example
const printCopyVar = (variable) => {
  // Make a copy/clone of the object
  //   let copyVar = Object.assign({}, variable); // METHOD 1
  //   let copyVar = structuredClone(variable); // METHOD 2
  // let copyVar = { ...variable }; // METHOD 3
  let copyVar = JSON.parse(JSON.stringify(variable)); // METHOD 4
  copyVar.objName = "Cloned Object"; // The original is not affected
  console.log(copyVar);
};

printCopyVar(testObj);
console.log(testObj);

// Pass by value example
const printVar = (variable) => {
  let copyVar = variable;
  copyVar = 1000; // The original is not affected because primitives are copied/cloned by default
  console.log(copyVar);
};

printVar(testNum);
console.log(testNum);
