#!/usr/bin/node

function factorial (a) {
  if (a > 0) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}

const a = parseInt(process.argv[2]);
const result = factorial(a);
console.log(result);
