#!/usr/bin/node

exports.esrever = function (list) {
  list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
