#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.sort((a, b) => a - b);
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
};
