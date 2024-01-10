#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
