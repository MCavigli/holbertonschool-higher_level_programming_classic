#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});
