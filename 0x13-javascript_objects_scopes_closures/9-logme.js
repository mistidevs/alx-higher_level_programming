#!/usr/bin/node
let callCount = 0;

exports.logMe = function (item) {
  callCount++;
  console.log(`${callCount - 1}: ${item}`);
};
