#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  fs.writeFile(process.argv[4], data, (err) => {
    if (err) throw err;
  });
});

fs.readFile(process.argv[3], 'utf-8', (err, data) => {
  if (err) throw err;
  fs.appendFile(process.argv[4], data, (err) => {
    if (err) throw err;
  });
});
