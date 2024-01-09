#!/usr/bin/node

const { argv } = require('node:process');

const firstArg = argv[2]; // Skip the script name and first argument

const number = parseInt(firstArg);

if (!isNaN(number)) {
 console.log(`My number: ${number}`);
} else {
 console.log('Not a number');
}
