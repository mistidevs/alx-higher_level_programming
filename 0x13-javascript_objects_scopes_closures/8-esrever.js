#!/usr/bin/node
exports.esrever = function (list) {
  const listRev = [];

  for (const element in list) {
    listRev.unshift(list[element]);
  }

  return listRev;
};
