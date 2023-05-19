class cars {
  constructor(engine, brand, make, colour) {
    // Get all cars engines and their horsepower
    // Filter and get the actual horsepower
    // let engineHorsepower = value
    let engineHorsepower;
    this.horsepower = engineHorsepower;
    this.brand = brand;
    this.make = make;
    this.colour = colour;

    this.drive();
  }

  drive() {
    console.log(`Vroom vroom ${this.brand}`);
  }
}

class coupe extends cars {
  constructor(engine, brand, make, colour, isFrontWheelDrive) {
    // Parent class properties
    super(engine, brand, make, colour);

    // Class specific properties
    this.isFrontWheelDrive = isFrontWheelDrive;
  }
}

class suv {}

let audi = new cars("something", "Audi", "Q5", "Grey");
let nissan = new cars("sklsjdkg", "Nissan", "Skyline", "Yellow");
let camaro = new coupe("sdfsdgs", "Chevrolet", "Camaro", "Black", true);

console.log(audi, nissan, camaro);
