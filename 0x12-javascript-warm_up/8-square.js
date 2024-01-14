#!/usr/bin/node
const char = 'X';
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += char;
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
