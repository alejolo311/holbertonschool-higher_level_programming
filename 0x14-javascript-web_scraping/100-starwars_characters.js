#!/usr/bin/node

const request = require('request');

request(`http://swapi-api.hbtn.io//api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
