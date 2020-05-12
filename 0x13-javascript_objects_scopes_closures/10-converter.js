#!/usr/bin/node

exports.converter = function (base) {
  const myconverter = num => num.toString(base);
  return myconverter;
};
