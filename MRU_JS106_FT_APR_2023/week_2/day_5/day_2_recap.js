const morningGreeting = "Good morning";
const eveningGreeting = "Good evening";
let isMorning = true;

if (isMorning) {
  console.log(morningGreeting);
} else if (!isMorning) {
  console.log(eveningGreeting);
} else {
  console.warn("Neither true nor false");
}

if (isMorning) {
  console.log(morningGreeting);
} else {
  console.log(eveningGreeting);
}

// Ternary operator, conditional
console.log(isMorning ? morningGreeting : eveningGreeting);
