#!/usr/bin/node

exports.esrever = function (list) {
  let rev = list.length - 1;
  const newList = [];
  for (let i = 0; i < list.length; i++) {
    newList[rev] = list[i];
    rev--;
  }
  return (newList);
};
