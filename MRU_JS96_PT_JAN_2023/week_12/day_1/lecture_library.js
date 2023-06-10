// Function, arrow function
// Sum(x, y)
// Return the addition of x and y

const Sum = (x, y) => x + y;

function Substract(x, y) {
  return x - y;
}

module.exports = {
  Sum,
  Sub: Substract,
};
