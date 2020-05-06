#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject._increment = () => {
  this.value += 1;
};

myObject._increment();
console.log(myObject);
myObject._increment();
console.log(myObject);
myObject._increment();
console.log(myObject);
