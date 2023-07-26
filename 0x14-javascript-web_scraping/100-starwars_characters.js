#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const film = JSON.parse(response.body);
  film.characters.forEach(characterUrl => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
      }
      const character = JSON.parse(response.body);
      console.log(character.name);
    });
  });
});
