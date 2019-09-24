#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const path = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < path.length; i++) {
    for (let j = 0; j < path[i].characters.length; j++) {
      if (path[i].characters[j] === 'https://swapi.co/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
