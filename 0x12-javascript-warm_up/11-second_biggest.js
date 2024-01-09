#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 3) {
  console.log(0);
} else {
  let firstBiggest = -Infinity;
  let secondBiggest = -Infinity;

  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);

    if (num > firstBiggest) {
      secondBiggest = firstBiggest;
      firstBiggest = num;
    } else if (num > secondBiggest && num !== firstBiggest) {
      secondBiggest = num;
    }
  }

  console.log(secondBiggest);
}
