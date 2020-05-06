#!/usr/bin/node
const argument = process.argv[2];
if (isNaN(Number(argument))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(argument); i++) {
    let r = '';
    for (let j = 0; j < Number(argument); j++) {
      r += 'X';
    }
    console.log(r);
  }
}
