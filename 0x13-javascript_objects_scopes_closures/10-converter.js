#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (base < 2 || base > 36) {
      return 'Invalid base';
    }

    const digits = [];
    const sign = number < 0 ? -1 : 1;
    number = Math.abs(number);

    while (number > 0) {
      digits.push(number % base);
      number = Math.floor(number / base);
    }

    if (sign === -1) {
      digits.push('-');
    }

    return digits.reverse().map(digit => digit >= 10 ? String.fromCharCode(digit - 10 + 65) : digit).join('');
  };
};
