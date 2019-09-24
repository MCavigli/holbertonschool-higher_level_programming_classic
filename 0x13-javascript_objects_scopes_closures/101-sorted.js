#!/usr/bin/node

const myDict = require('./101-data').dict;
const newDict = {};
for (const k in myDict) {
  if (myDict[k] in newDict) {
    newDict[myDict[k]].push(k);
  } else {
    newDict[myDict[k]] = [k];
  }
}
console.log(myDict);
console.log(newDict);
