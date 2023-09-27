#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes(id)) {
        count++;
      }
    });
  });
  console.log(count);
});
