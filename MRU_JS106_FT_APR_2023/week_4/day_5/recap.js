// Class kitsoz, 3d object
class kitsoz {
  /* Constructor */
  //   constructor(length, height, width) {
  constructor(name, x, y, z) {
    this.name = name;
    this.length = x;
    this.height = y;
    this.width = z;
    this.calcVolume();
  }

  // logName will console debug the name
  logName() {
    console.debug(this.name);
  }

  calcVolume() {
    this.volume = this.length * this.height * this.width;
    return this.volume;
  }
}

// Subclass of kitsoz, square box has equilateral sides
class squareBox extends kitsoz {
  constructor(name, x) {
    super(name, x, x, x);

    // name == "hello"
    // then, I want name = "squareBox hello"

    // name == "jello"
    // then, I want name = "squareBox jello"

    this.name = "squareBox " + this.name;
  }

  getName() {
    return this.name;
  }

  setName(newName) {
    this.name = newName;
  }

  getLength() {
    if (this.length != this.width || this.width != this.height) {
      console.warn("The sides of this box are not equal!!!");
    }
    return this.length;
  }

  getHeight() {
    this.getLength();
    return this.height;
  }

  setLength(newLength) {
    this.length = newLength;
    this.height = newLength;
    this.width = newLength;
    this.calcVolume();
  }
}

{
  // console.log("Hello World");
  // let kitsoz1 = new kitsoz("kitsoz1", 10, 15, 20);
  // var kitsoz2 = new kitsoz("kitsoz2", 55, 75, 88);
  // const kitsoz3 = new kitsoz("kitsoz3", 100, 500, 1000);
  // console.log(kitsoz1, kitsoz2, kitsoz3);
  // kitsoz2.height = 200;
  // kitsoz3.name = "zafer3";
  // kitsoz3.name = "zafer31";
  // kitsoz3.name = "zafer32";
  // kitsoz3.name = "zafer33";
  // kitsoz3.name = "zafer34";
  // console.log(kitsoz1, kitsoz2, kitsoz3);
  // const xArr = [];
  // console.debug(xArr);
  // xArr.push(100);
  // xArr.push(200);
  // console.debug(xArr);
  // xArr[0] = 1000;
  // console.debug(xArr);
  // kitsoz1.logName();
  // kitsoz2.logName();
  // kitsoz3.logName();
  // console.debug(kitsoz3.volume);
  // kitsoz1.calcVolume();
  // kitsoz2.calcVolume();
  // kitsoz3.calcVolume();
  // console.debug(kitsoz3.volume);
  // console.log(kitsoz1, kitsoz2, kitsoz3);
  // console log the different available properties of kitsoz1
  /*
for (let key in kitsoz1) {
  console.error(key);
}*/
  // console.error(Object.keys(kitsoz1));
  // console.debug(Object.getOwnPropertyNames(kitsoz1));
}

const box1 = new squareBox("box1", 10);
let box2 = new squareBox("box2", 10);
console.debug(box1, box2);

// box1.name = "oldbox1";
// box2.name = "oldbox2";
// console.log(box1.getName(), box2.getName());

// box1.setName("oldbox1");
// box1.setName("oldbox2");
// console.log(box1.getName(), box2.getName());

// console.log(box1.getName(), box2.getName());
// console.log(box1.name, box2.name);

// box1.length = 1000;
// console.debug(box1, box2);
// console.error(box1.height, box1.getHeight());

// box1.setLength(50);
// console.debug(box1, box2);
// console.error(box1.height, box1.getHeight());

const address = {
  street: "3 Boutiques",
  number: "742",
  city: "Springfield",
  state: "NT",
  zip: "49007",
  cars: ["BMW", "Chevrolet"],
};

const addressCopied = { ...address };
console.log(address, addressCopied);
addressCopied.street = "test";
addressCopied.cars.push("Skoda");
console.log(address, addressCopied);

// let { street: s, city: c } = address;
// console.log(s);
// console.log(c); //Springfield

// s = "Quatre Bornes";
// console.log(s);
// console.warn(address);

// const { street, city } = address;
// console.log(street); //Evergreen Terrace
// console.log(city); //Springfield

// const student = {
//   name: "John Doe",
//   age: 16,
//   scores: {
//     maths: 74,
//     english: 63,
//     science: 85,
//     social_studies: 100,
//   },
// };

// // With Destructuring
// function displaySummary({
//   name,
//   scores: { maths = 0, english = 0, science = 0, chemistry = 0 },
// }) {
//   console.log("Hello, " + name);
//   console.log("Your Maths score is " + maths);
//   console.log("Your English score is " + english);
//   console.log("Your Science score is " + science);
//   console.log("Your Chemistry score is " + chemistry);
// }

// displaySummary(student);

// let obj = {
//   foo: 1,
//   bar: 2,
//   food: "dholl puri",
//   nestedObj: { name: "test", id: 5 },
// };
// let newObj = { ...obj, testvar: 3 };
// console.log(newObj); //{ foo: 1, bar: 2, testvar: 3 }

// function x() {}

// function y() {}

// let something;
// const xy = (y) => (x) => something;
