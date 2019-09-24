#!/usr/bin/node

const myList = require('./100-data').list;
const mapList = myList.map(function (num, index) {
  return num * index;
});
console.log(myList);
console.log(mapList);
