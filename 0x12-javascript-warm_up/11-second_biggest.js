#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const listnum = list.map(num => parseInt(num, 10));
  listnum.sort((a, b) => b - a);
  console.log(listnum[1]);
}
