#!/usr/bin/node

const request = require('request');

request(`http://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    order(characters, 0);
  }
});

function order (characters, i) {
  if (i === characters.length) { return; }
  request(characters[i], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      order(characters, i + 1);
    }
  });
}
