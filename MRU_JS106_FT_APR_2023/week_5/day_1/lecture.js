// console.log(document.forms);

// console.log(document.forms.fLogin.username);
// console.log(document.forms.fLogin.elements.username);
// console.log(document.forms[0]);

// console.log(
//   document.forms.fLogin.elements.lLogin.elements.password_check.elements
//     .password
// );

// console.log(fLogin.username);
// console.log(fLogin.password_check.elements.password.form);

// // Console log the value of username
// // every time a change in input happens
// // Using addeventlistener
// let nameEl = fLogin.username;
// // console.warn(name);
// nameEl.addEventListener("input", () => {
//   console.log(nameEl.value);
// });

// // Console log value of checkbox
// // every time the submit btn is pressed
// let checkboxEl = fLogin.remember;
// let submitEl = fLogin.submit;

// console.debug(submitEl);
// submitEl.addEventListener("click", (e) => {
//   console.log(checkboxEl.checked);
//   e.preventDefault();
// });

// let paymentEl = fLogin.paymentOpt;
// paymentEl.addEventListener("input", () => {
//   //   console.log(fLogin.paymentOpt.options);

//   let selected = Array.from(fLogin.paymentOpt.options)
//     .filter((option) => option.selected)
//     .map((option) => option.value);

//   console.log(selected);

//   //   paymentEl.selectedIndex = 2;
//   paymentEl.value = "amex";
// });

// let venmoOpt = new Option("Venmo", "venmo", false, false);
// let juiceOpt = new Option("Juice", "juice", false, false);

// console.log(venmoOpt, juiceOpt);

// document.forms[0].paymentOpt.appendChild(venmoOpt);
// document.forms[0].paymentOpt.appendChild(juiceOpt);

// // <option value="visa">Visa</option>;
// let blinkOpt = document.createElement("option");
// blinkOpt.setAttribute("value", "blink");
// blinkOpt.innerText = "Blink";
// console.log(blinkOpt);
// document.forms[0].paymentOpt.appendChild(blinkOpt);

// let emailEl = fLogin.email;
// console.log(emailEl);

// emailEl.addEventListener("input", () => {
//   emailEl.value = emailEl.value.trim();
//   let result = emailEl.value.replace(/ /g, "");
//   emailEl.value = result;

//   if (emailEl.validity.typeMismatch) {
//     emailEl.setCustomValidity("I am expecting an e-mail address!");
//     console.log("Email is invalid");
//   } else {
//     emailEl.setCustomValidity("");
//     console.log("Email is valid");
//   }

//   emailEl.reportValidity(); // Missing from example
// });

let mauritianFruits = {
  fruits: [
    "dragonfruit",
    "starfruit",
    "lychee",
    "longan",
    "mango",
    "coconut",
    "papaya",
  ],
};

// let jsonText = JSON.stringify(mauritianFruits);
// let kitsoz = msgBox.message;
// kitsoz.value = jsonText;
// console.log(kitsoz);

// // {"fruits":["dragonfruit","starfruit","lychee","longan","mango","coconut","papaya"]}

// let zafer = msgBox.toObj;
// zafer.addEventListener("click", () => {
//   let jsonObj = JSON.parse(kitsoz.value);
//   console.log(jsonObj);
// });

let mauritianFruitsClone = JSON.parse(JSON.stringify(mauritianFruits));

mauritianFruitsClone.abracadabra = "test";
console.log(mauritianFruits, mauritianFruitsClone);

console.warn(JSON.stringify(100));

try {
  var pokemon = "Pichu";
  throw new Error("Pichu is not a pokemon");
  console.log("sdklufdjlgdf");
  console.log("sdklufdjlgdf");
  console.log("sdklufdjlgdf");
  console.log("sdklufdjlgdf");
} catch (e) {
  console.error("PICHU BROKE");
  console.error(e.name);
  console.error(e.message);
  console.error(e.stack);
} finally {
  console.log(pokemon);
}
