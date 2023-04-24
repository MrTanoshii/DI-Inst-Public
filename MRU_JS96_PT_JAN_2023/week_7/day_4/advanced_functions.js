// currying
const testfn = (x) => (y) => (z) => {};

// compose
const testfn2 = (fnX, fnY) => (z) => fnX(fnY(z));
