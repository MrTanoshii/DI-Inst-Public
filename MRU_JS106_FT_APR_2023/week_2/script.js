// console.log("Hello, this is another script");
// console.error("ERROR THIS IS AN ERROR");

// let _hello = "hello";
// console.log(_hello);

// // console.log(vincent);
// let vincent;
// console.log(vincent);
// vincent = 100;
// vincent = null;
// console.warn(vincent);

// let longString =
//   "hey guys this is a super long \
// long long long string";
// console.log({
//   "Long String": longString,
//   "String length": longString.length,
//   "Position of 'hey'": longString.indexOf("hey"),
//   "Position of 'long'": [...longString.matchAll("long")],
//   "String between longs": longString.substring(25, 40),
//   "Upper case": longString.toLocaleUpperCase(),
//   "Other upper case": longString.toUpperCase(),
//   "Lower case": longString
//     .toUpperCase()
//     .toLowerCase()
//     .substring(0, 20)
//     .toUpperCase()
//     .toLowerCase(),
//   Replace: longString.replaceAll("long", "short"),
//   "Concat example": longString.concat(_hello, _hello, _hello),
//   Trimmed: longString.trim(),
//   "char at": longString.charAt(1),
//   "char unicode": longString.charCodeAt(1),
// });

//   "hey guys this is a super long" +
// "long long long string";

// var addressNumber = 5;
// let addressStreet = "Menagerie St";
// let country = "Papua New Guinea";

// console.log(addressNumber);
// console.warn(addressStreet);
// console.debug(country);
// console.error(addressNumber, addressStreet, country);

// var globalAddress = addressNumber + " | " + addressStreet + " | " + country;
// console.log(globalAddress);

// let addressNumberStr = addressNumber.toString();
// console.debug(addressNumberStr.concat(addressStreet, country));

// console.warn(addressNumberStr);

// 000 - 0
// 001 - 1
// 010 - 2
// 011 - 3

// // Signed Int3

// 100 - -0
// 101 - -1
// 110 - -2
// 111 - -3

// // Unsigned Int3

// 100 - 4
// 101 - 5
// 110 - 6
// 111 - 7

// console.log(100 / 25);
// console.log(100 ** 25);
// console.log(isNaN("Jatin"));
// console.log(isNaN("678213"));
// console.log(isNaN(678213));
// console.log(NaN === NaN);
// console.log(isNaN(true));
// console.log(isNaN(null));
// console.log(isNaN(1));

// console.log(isNaN(1) && isNaN("dsfsd"));
// console.log(isNaN(1) || isNaN("dsfsd"));

// console.warn(isNaN(0(5435435)));

// let birthYear = 1900;
// var futureYear = 2300;
// console.log("I will be " + (futureYear - birthYear) + " in " + futureYear);
// console.log(Boolean(10 > 9));
// console.log(Boolean(10 >= 10));
// console.log(Boolean(10 < 10));
// console.log(Boolean(100 == 10));
// console.log(Boolean(100 != 10));

// console.log(109 % 10);

// let x = 10;

// let alphaArray = ["a", "b", "c", "d", "e", "f", "g"];

// let aALength = alphaArray.length;

// console.log(alphaArray[x % aALength]);

// // alphaArray[10 % 7]
// // 10 - 7 = 3
// // Remainder = 3

// console.warn(typeof "safkdsjlfds");
// console.warn(typeof 12321);
// console.warn(typeof ["fsdfdsf", "safkdsjlfds"]);

// let colors = [
//   "blue",
//   "yellow",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
//   "green",
// ];
// console.log(colors);
// colors[40] = "yellow";
// console.log(colors);

// let array1D = ["1"];
// let array2D = [[["11"], ["12"]]];
// let array3D = [
//   [
//     [["111"], ["112"]],
//     [["121"], ["122"]],
//   ],
// ];

// console.log(array1D[0]);
// console.error(array2D);
// console.log(array2D[0][1]);
// console.log(array3D[0][1][1]);

// let newArray = [];
// console.log(newArray);

// newArray.push("1");
// newArray.push("2");
// newArray.push("3");
// newArray.unshift("0");
// newArray.shift();

// console.warn(newArray.splice(0, 2, 100, 200, 300));
// console.log(newArray.slice(3, 4));

// // splice(5, 2); // From the index 5, remove 2 elements
// // slice(5, 2); // From the index 5 to the index 2, remove elements (Error)

// console.log(newArray);
// console.log(newArray.pop());
// console.log(newArray.pop());
// console.log(newArray.pop());

// console.log(newArray.join("-------------------"));

// let reallyBigNumber = [21321312, 3213213213, 21321321321, 21321321];
// console.log("Really big number: " + reallyBigNumber.join(","));

let pets = ["cat", "dog", "fish", "rabbit", "cow"];
console.log(pets[1]);
pets.push("horse");
console.log(pets);
pets.splice(3, 1);
console.warn(pets);

// alert("sdkfnhkdshfndkshl");
// let age = prompt("How old are you?", 20);
// console.log(age);
// confirm("test");
