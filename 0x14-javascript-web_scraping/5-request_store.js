#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = response.body;
  fs.writeFile(path, data, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
