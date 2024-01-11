#!/usr/bin/node
const Square_0 = require('./5-square');
module.exports = class Square extends Square_0 {
  charPrint (c) {
    let row;
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      row = '';
      for (let j = 0; j < this.height; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
