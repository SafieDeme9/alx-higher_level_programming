#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const film = JSON.parse(response.body);
  for (const characterUrl of film.characters) {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
