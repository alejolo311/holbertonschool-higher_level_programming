#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const list = JSON.parse(body);
    console.log(list.reduce((ret, el) => {
      if (el.completed) {
        if (ret[el.userId]) {
          ret[el.userId]++;
        } else {
          ret[el.userId] = 1;
        }
      }
      return ret;
    }, {}));
  }
});
