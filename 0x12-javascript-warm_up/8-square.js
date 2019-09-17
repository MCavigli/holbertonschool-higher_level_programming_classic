#!/usr/bin/node

let r = 0;
let c = 0;
let newstr = '';
if (process.argv[2] >= 0) {
  const l = process.argv[2];
  for (r = 0; r < l; r++) {
    newstr += 'X';
  }
  for (c = 0; c < l; c++) {
    console.log(newstr);
  }
} else if (process.argv[2] < 0) {
} else {
  console.log('Missing size');
}
