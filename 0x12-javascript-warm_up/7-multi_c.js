#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (!isNaN(myNum)) {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
