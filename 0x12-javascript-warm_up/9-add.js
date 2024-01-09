#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

const firstNum = parseInt(argv[2]);
const secondNum = parseInt(argv[3]);
const sum = add(firstNum, secondNum);

console.log(sum);
