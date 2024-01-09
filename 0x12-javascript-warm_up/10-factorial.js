#!/usr/bin/node
const { argv } = require('node:process');

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = parseInt(argv[2]);
const result = factorial(num);

console.log(result);
