#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let count = 0;
  const data = JSON.parse(body);
  const results = data.results;
  for (let i = 0; i < results.length; i++) {
    const episode = results[i];
    const characters = episode.characters;
    for (let j = 0; j < characters.length; j++) {
      const character = characters[j];
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
