#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const newArray = [];
  let i = 2;
  let j = 0;
  for (; i < len; i++) {
    newArray[j] = parseInt(process.argv[i]);
    j++;
  }
  newArray.sort();
  const arrayLen = newArray.length;
  console.log(newArray[arrayLen - 2]);
}
