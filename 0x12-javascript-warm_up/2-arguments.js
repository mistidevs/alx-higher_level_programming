#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 3) {
  console.log('No Argument');
} else if (argv.length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
