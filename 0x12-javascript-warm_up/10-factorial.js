#!/usr/bin/node
const argument = Number(process.argv[2]);
if (isNaN(argument)) {
  console.log(1);
} else {
  console.log(factorial(argument));
}
function factorial (number) {
  if (number <= 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
