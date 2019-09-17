#!/usr/bin/node

const x = process.argv[2];
let i = 0;
if (i < x && x >= 0) {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else if (x < 0) {
} else {
  console.log('Missing number of occurrences');
}
