#!/usr/bin/node
const firstArg = Number(process.argv[2]);
const secondArg = Number(process.argv[3]);
if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN');
} else {
  console.log(add(firstArg, secondArg));
}

function add (a, b) {
  return a + b;
}
