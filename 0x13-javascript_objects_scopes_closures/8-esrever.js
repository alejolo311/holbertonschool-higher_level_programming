#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (element of list) {
    newList.unshift(element);
  }
  return newList;
};
