#!/usr/bin/node
const argument = process.argv[2];
if (isNaN(argument, 10)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(argument); i++) {
    console.log('C is fun');
  }
}
