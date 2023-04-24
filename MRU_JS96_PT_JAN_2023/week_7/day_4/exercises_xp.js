// Exercise 2

// METHOD 1: Arrow function declaration
const arrowFn = (x) => console.log(x); // Declaration of the function
arrowFn(5); // Invoking/Calling the function

// METHOD 2: Function declaration
function regularFn() {}

// METHOD 3: Arrow function expression
((x) => console.log(x))(10);

// Exercise 3

document.querySelector("#exercise3").innerHTML = "OMG GUYS THIS WORKS HAHA";

// Exercise 5

const makeJuice = () => {
  let ingredients = [];

  const addIngredients = (x, y, z) => {
    ingredients.push(x, y, z);
  };
  addIngredients("apple", "strawberry", "passionfruit");
  addIngredients("kiwi", "litchi", "mango");

  const displayJuice = () => {
    // console log or DOM manipulation to display the juice and its ingredients.
  };
};

makeJuice();
