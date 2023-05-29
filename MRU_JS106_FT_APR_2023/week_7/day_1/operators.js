function addOperator(x, y) {
  return x + y;
}

let divideOperator = (x, y) => {
  return x / y;
};

module.exports = {
  sumof2: addOperator,
  divide2num: divideOperator,
};
