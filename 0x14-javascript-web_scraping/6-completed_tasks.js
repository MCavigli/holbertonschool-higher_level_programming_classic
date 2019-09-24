#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = {};

  for (let i = 0; i < JSON.parse(body).length; i++) {
    const user = JSON.parse(body)[i].userId;
    const com = JSON.parse(body)[i].completed;
    if (isNaN(dict[user]) && com) {
      dict[user] = 1;
    } else if (com) {
      dict[user] += 1;
    }
  }
  console.log(dict);
});
