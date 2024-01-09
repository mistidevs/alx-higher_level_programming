#!/usr/bin/node
const { argv } = require('node:process');
const sentence = String(argv[2]) + ' is ' + String(argv[3]);
console.log(sentence);
