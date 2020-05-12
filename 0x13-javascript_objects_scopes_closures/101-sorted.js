#!/usr/bin/node

const { dict } = require('./101-data');

console.log(Object.entries(dict).reduce((newDict, element) => {
  if (newDict[element[1]] === undefined) {
    newDict[element[1]] = [element[0]];
  } else {
    newDict[element[1]].push(element[0]);
  }
  return newDict;
}, {}));
