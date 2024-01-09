#!/usr/bin/node
const { argv } = require('node:process');

let numElem = 0;
while (argv[numElem] !== undefined) {
  numElem++;
}

if (numElem < 3) {
  console.log('No Argument');
} else {
  console.log(argv[2]);
}
