#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const list_num = list.map(num => parseInt(num, 10));
  list_num.sort((a, b) => b - a);
  console.log(list_num[1]);
}
