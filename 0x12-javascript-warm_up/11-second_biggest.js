#!/usr/bin/node
if (process.argv.length < 3) {
  console.log(0);
} else {
  let firstBiggest = -Infinity;
  let secondBiggest = -Infinity;

  for (let i = 2; i < process.argv.length; i++) {
    const num = parseInt(process.argv[i]);

    if (num > firstBiggest) {
      secondBiggest = firstBiggest;
      firstBiggest = num;
    } else if (num > secondBiggest && num !== firstBiggest) {
      secondBiggest = num;
    }
  }
  console.log(secondBiggest);
}
